---
title: "西迪特 Wi-Fi Web管理 jumpto.php 后台命令执行漏洞"
date: 2026-10-18 09:16:51
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "西迪特"
tags:
  - "西迪特"
  - "命令执行"
  - "越权"
  - "漏洞复现"
---
## 漏洞描述

西迪特 Wi-Fi Web管理系统后台过滤不足导致远程命令执行漏洞

## 漏洞影响

```
西迪特 Wi-Fi Web管理
```

## 网络测绘

```
title=="Wi-Fi Web管理"
```

## 漏洞复现o

登录页面

![image-20220519183944313](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191841065.png)

通过越权漏洞获取权限，添加Cookie

```
Cookie: timestamp=0; cooLogin=1; cooUser=admin
```

进入后台后，诊断功能点存在命令拼接执行漏洞

![image-20220519184158173](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191841279.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E8%A5%BF%E8%BF%AA%E7%89%B9-Wi-Fi-Web%E7%AE%A1%E7%90%86-jumpto.php-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
