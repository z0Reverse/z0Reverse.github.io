---
title: "杭州法源软件 法律知识数据库系统 后台XSS漏洞"
date: 2026-10-16 09:10:50
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "杭州法源软件-法律知识数据库系统"
tags:
  - "杭州法源软件-法律知识数据库系统"
  - "XSS"
  - "漏洞复现"
---
## 漏洞描述

杭州法源软件开发有限公司开发的实践教学平台系统下的法律知识数据库系统登录后台用户名处存在通用XSS漏洞

## 漏洞影响

```
杭州法源软件 法律知识数据库系统
```

## 网络测绘

```
icon_hash="2018105215" || title="实践教学平台 - 杭州法源软件开发有限公司"
```

## 漏洞复现



登录后台后更改用户名，使用 td标签 闭合



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101857066.png)



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101857457.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%9D%AD%E5%B7%9E%E6%B3%95%E6%BA%90%E8%BD%AF%E4%BB%B6-%E6%B3%95%E5%BE%8B%E7%9F%A5%E8%AF%86%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F-%E5%90%8E%E5%8F%B0XSS%E6%BC%8F%E6%B4%9E.md)
