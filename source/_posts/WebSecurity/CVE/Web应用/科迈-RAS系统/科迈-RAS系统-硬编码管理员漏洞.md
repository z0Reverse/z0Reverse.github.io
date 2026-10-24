---
title: "科迈 RAS系统 硬编码管理员漏洞"
date: 2026-10-16 09:11:25
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "科迈-RAS系统"
tags:
  - "科迈-RAS系统"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

科迈 RAS系统 存在硬编码管理员漏洞，在内部自动创建了两个管理员账户，可被利用于登录

## 漏洞影响

```
科迈 RAS系统
```

## 网络测绘

```
app="科迈-RAS系统"
```

## 漏洞复现

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091840562.png)

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091840042.png)



可得知存在的账号密码为



```plain
user: RASCOM
pass: 1A2b3C4d56.

user: 1A2b3C4d56.
pass: 1A2b3C4d56.
```



当开启RDP即可使用该账号登陆

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%A7%91%E8%BF%88-RAS%E7%B3%BB%E7%BB%9F-%E7%A1%AC%E7%BC%96%E7%A0%81%E7%AE%A1%E7%90%86%E5%91%98%E6%BC%8F%E6%B4%9E.md)
