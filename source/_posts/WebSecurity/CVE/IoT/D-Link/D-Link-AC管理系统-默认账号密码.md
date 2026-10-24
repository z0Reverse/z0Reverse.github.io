---
title: "D-Link AC管理系统 默认账号密码"
date: 2026-10-18 09:14:11
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "D-Link"
tags:
  - "D-Link"
  - "信息泄露"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

D-Link AC管理系统存在默认账号密码，可被获取敏感信息

## 漏洞影响

```
D-Link AC管理系统
```

## 网络测绘

```
"AC集中管理平台"  && body="D-Link路由器管理页"
```

## 漏洞复现

默认口令为 admin:admin

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162228466.png)

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162228570.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/D-Link-AC%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-%E9%BB%98%E8%AE%A4%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81.md)
