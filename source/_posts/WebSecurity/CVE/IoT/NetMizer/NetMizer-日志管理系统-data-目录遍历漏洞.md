---
title: "NetMizer 日志管理系统 data 目录遍历漏洞"
date: 2026-10-18 09:15:07
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "NetMizer"
tags:
  - "NetMizer"
  - "目录遍历"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

北京灵州网络技术有限公司NetMizer日志管理系统存在目录遍历漏洞，由于 /data 控制不严格，攻击者可利用该漏洞获取敏感信息。

## 漏洞影响

```
NetMizer 日志管理系统
```

## 网络测绘

```
title="NetMizer 日志管理系统"
```

## 漏洞复现

登录页面

![image-20220519175506872](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191757812.png)

验证POC

```
/data
```

![image-20220519175728991](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191757072.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/NetMizer-%E6%97%A5%E5%BF%97%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-data-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
