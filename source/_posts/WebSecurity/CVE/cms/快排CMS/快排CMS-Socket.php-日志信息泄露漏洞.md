---
title: "快排CMS Socket.php 日志信息泄露漏洞"
date: 2026-10-12 09:01:24
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "快排CMS"
tags:
  - "快排CMS"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

快排CMS 默认开启日志记录，由于日志名为时间作为文件名，造成管理员的Cookie泄露

## 漏洞影响

```
快排 CMS <= 1.2
```

## 环境搭建

https://gitee.com/qingzhanwang/kpcms

## 漏洞复现

文件 **thinkphp/library/think/log/driver/Socket.php**

这里默认开启日志写入

```plain
runtime/log/202104/06.log
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170921409.png)

其中可以看到泄露了管理员的Cookie信息和其他敏感信息

并且文件命名为 **年+月/日期.log**

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170921851.png)

这里关注后台的日志文件中的 admin.php页面的cookie就可以获得管理员权限

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/%E5%BF%AB%E6%8E%92CMS-Socket.php-%E6%97%A5%E5%BF%97%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
