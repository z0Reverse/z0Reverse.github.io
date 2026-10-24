---
title: "Wayos 防火墙 后台命令执行漏洞"
date: 2026-10-18 09:15:26
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Wayos"
tags:
  - "Wayos"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

Wayos 防火墙 后台存在命令执行漏洞，通过命令注入可以执行远程命令

## 漏洞影响

```
Wayos 防火墙
```

## 网络测绘

```
body="Get_Verify_Info(hex_md5(user_string)."
```

## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162240644.png)

登录后台后 ping 模块命令执行

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162240143.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Wayos-%E9%98%B2%E7%81%AB%E5%A2%99-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
