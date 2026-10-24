---
title: "若依管理系统 Druid未授权访问"
date: 2026-10-16 09:11:32
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "若依管理系统"
tags:
  - "若依管理系统"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

若依管理系统使用了Druid 默认开启了匿名访问，导致未授权获取敏感信息

## 漏洞影响

```
若依管理系统
```

## 网络测绘

```
app="若依-管理系统"
```

## 漏洞复现

源码中看到 pom.xml 文件中查看到引用了 阿里Druid

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101956128.png)



从 issues 中发现了默认存在的未授权访问



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101957569.png)



Url为



```plain
http://xxx.xxx.xxx.xxx/prod-api/druid/index.html
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101957317.png)

## 

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E8%8B%A5%E4%BE%9D%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-Druid%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE.md)
