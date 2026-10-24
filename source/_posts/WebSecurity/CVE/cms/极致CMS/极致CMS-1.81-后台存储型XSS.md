---
title: "极致CMS 1.81 后台存储型XSS"
date: 2026-10-12 09:01:27
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "极致CMS"
tags:
  - "极致CMS"
  - "XSS"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

极致CMS后台中存在存储XSS，通过XSS漏洞，可能泄漏敏感信息

## 漏洞影响

```
极致CMS
```

## 网络测绘

```
icon_hash="1657387632"
```

## 漏洞复现

网站主页![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170914080.png)

登录管理员添加模块

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170915540.png)

注册用户

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170915958.png)

点击发布文章

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170915367.png)

在文章标题处插入xss payload

- `<details open ontoggle= confirm(document[`coo`+`kie`])>`

当管理员访问时XSS成功

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170915879.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/%E6%9E%81%E8%87%B4CMS-1.81-%E5%90%8E%E5%8F%B0%E5%AD%98%E5%82%A8%E5%9E%8BXSS.md)
