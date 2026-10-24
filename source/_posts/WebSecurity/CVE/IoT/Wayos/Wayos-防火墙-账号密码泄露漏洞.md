---
title: "Wayos 防火墙 账号密码泄露漏洞"
date: 2026-10-18 09:15:27
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Wayos"
tags:
  - "Wayos"
  - "漏洞复现"
---
## 漏洞描述

Wayos 防火墙存在账号密码泄露漏洞，攻击者通过前端可以查看到密码的md5的加密字符，解密后可以登陆后台

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

F12 查看账号密码

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162239392.png)

解密Md5即可登录后台

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162239676.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Wayos-%E9%98%B2%E7%81%AB%E5%A2%99-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
