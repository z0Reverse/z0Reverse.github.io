---
title: "JCG JHR-N835R 后台命令执行漏洞"
date: 2026-10-18 09:14:51
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "JCG-JHR-N835R"
tags:
  - "JCG-JHR-N835R"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

JCG JHR-N835R 后台存在命令执行，通过 ; 分割 ping 命令导致任意命令执行

## 漏洞影响

```
JCG JHR-N835R
```

## Shodan

```
JHR-N835R
```

## 漏洞复现

登录页面 admin admin登录

![image-20220209202626135](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202092026189.png)

在后台系统工具那使用 PING工具，使用 ; 命令执行绕过

![image-20220209202640541](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202092026647.png)

![image-20220209202702580](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202092027634.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/JCG-JHR-N835R-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
