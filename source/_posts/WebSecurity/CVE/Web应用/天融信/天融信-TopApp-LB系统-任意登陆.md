---
title: "天融信 TopApp-LB系统 任意登陆"
date: 2026-10-16 09:10:34
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "天融信"
tags:
  - "天融信"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

天融信负载均衡TopApp-LB系统无需密码可直接登陆，查看敏感信息

## 漏洞影响

```
天融信负载均衡TopApp-LB
```

## 网络测绘

```
app="天融信-TopApp-LB-负载均衡系统"
```

## 漏洞复现

在登录页面中输入，账号:**任意账号**  密码:**;id**



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091919361.png)



成功登录



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091919022.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%A4%A9%E8%9E%8D%E4%BF%A1-TopApp-LB%E7%B3%BB%E7%BB%9F-%E4%BB%BB%E6%84%8F%E7%99%BB%E9%99%86.md)
