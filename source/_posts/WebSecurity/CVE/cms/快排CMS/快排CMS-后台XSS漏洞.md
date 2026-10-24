---
title: "快排CMS 后台XSS漏洞"
date: 2026-10-12 09:01:25
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "快排CMS"
tags:
  - "快排CMS"
  - "XSS"
  - "漏洞复现"
---
## 漏洞描述

快排CMS 后台存在XSS漏洞，通过后台构造特殊语句可以造成访问网站的用户被XSS影响

## 漏洞影响

```
快排 CMS <= 1.2
```

## 环境搭建

https://gitee.com/qingzhanwang/kpcms

## 漏洞复现

漏洞出现在登录后台的网站编辑的位置，由于没有对输出的字符进行过滤，导致XSS

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170922990.png)

主页版权处嵌入XSS代码

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170922232.png)



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170923548.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/%E5%BF%AB%E6%8E%92CMS-%E5%90%8E%E5%8F%B0XSS%E6%BC%8F%E6%B4%9E.md)
