---
title: "泛微OA E-Office UserSelect 未授权访问漏洞"
date: 2026-10-17 09:12:34
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

泛微OA E-Office UserSelect接口存在未授权访问漏洞，通过漏洞攻击者可以获取敏感信息

## 漏洞影响

```
泛微OA E-Office
```

## 网络测绘

```
app="泛微-EOffice"
```

## 漏洞复现

登录页面

![image-20220520134445854](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201344907.png)

验证POC

```
/UserSelect/
```

![image-20220520140409297](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201404369.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Office-UserSelect-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
