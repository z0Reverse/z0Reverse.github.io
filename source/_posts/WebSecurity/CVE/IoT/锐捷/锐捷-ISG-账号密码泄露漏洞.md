---
title: "锐捷 ISG 账号密码泄露漏洞"
date: 2026-10-18 09:17:00
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "锐捷"
tags:
  - "锐捷"
  - "漏洞复现"
---
## 漏洞描述

锐捷ISG 存在账号密码泄露漏洞，通过查看前端，可以获取密码的md5值, 解密后获取后台权限

## 漏洞影响

```
锐捷ISG
```

## 网络测绘

```
title="RG-ISG"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110925459.png)

F12 查看到账号密码

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110925212.png)

解密md5 后登陆系统

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110925656.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%94%90%E6%8D%B7-ISG-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
