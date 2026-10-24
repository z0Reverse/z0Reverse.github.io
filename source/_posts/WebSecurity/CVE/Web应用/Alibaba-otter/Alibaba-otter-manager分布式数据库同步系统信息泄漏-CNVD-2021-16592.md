---
title: "Alibaba otter manager分布式数据库同步系统信息泄漏 CNVD-2021-16592"
date: 2026-10-16 09:06:31
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Alibaba-otter"
tags:
  - "Alibaba-otter"
  - "信息泄露"
  - "弱口令"
  - "CNVD-2021-16592"
  - "漏洞复现"
---
## 漏洞描述

Alibaba otter manager分布式数据库同步系统是基于数据库增量日志解析，准实时同步到本机房或异地机房的mysql/oracle数据库，一个分布式数据库同步系统。阿里巴巴otter manager分布式数据库同步系统存在信息泄露漏洞，攻击者可利用漏洞获取zookper信息。

参考链接：

* https://www.cnvd.org.cn/flaw/show/CNVD-2021-16592
* https://forum.ywhack.com/thread-115309-1-8.html

## 网络测绘

```
title="Otter Manager"
```

## 漏洞复现

默认口令：`admin/admin`

进入后直接f12查看元素，修改password为text即可查看数据库等敏感信息密码。

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Alibaba-otter-manager%E5%88%86%E5%B8%83%E5%BC%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8C%E6%AD%A5%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F-CNVD-2021-16592.md)
