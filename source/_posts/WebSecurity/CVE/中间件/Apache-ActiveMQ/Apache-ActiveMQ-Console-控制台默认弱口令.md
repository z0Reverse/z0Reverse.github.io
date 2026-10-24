---
title: "Apache ActiveMQ Console 控制台默认弱口令"
date: 2026-10-14 09:02:51
categories:
  - WebSecurity
  - CVE
  - "中间件"
  - "Apache-ActiveMQ"
tags:
  - "Apache-ActiveMQ"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

Apache ActiveMQ Console 存在默认弱口令 admin:admin，进入控制台后可被进一步恶意利用

## 漏洞影响

```
Apache ActiveMQ
```

## 漏洞复现

Apache ActiveMQ 默认开启了 8186 控制台

访问目标: http://xxx.xxx.xxx.xxx:8161/admin

![6fdafa69-51e4-4215-aa0d-0c912e47ba6c](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/6fdafa69-51e4-4215-aa0d-0c912e47ba6c.png)

使用默认口令 admin:admin

![7dc4d568-31b4-494e-8c32-3a465830ff3c](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/7dc4d568-31b4-494e-8c32-3a465830ff3c.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/middleware/Apache-ActiveMQ-Console-%E6%8E%A7%E5%88%B6%E5%8F%B0%E9%BB%98%E8%AE%A4%E5%BC%B1%E5%8F%A3%E4%BB%A4.md)
