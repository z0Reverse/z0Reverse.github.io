---
title: "吉拉科技 LVS精益价值管理系统 Business 目录遍历漏洞"
date: 2026-10-16 09:10:25
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "吉拉科技-LVS精益价值管理系统-Business"
tags:
  - "吉拉科技-LVS精益价值管理系统-Business"
  - "目录遍历"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

杭州吉拉科技有限公司多个系统存在目录遍历漏洞，由于 /Business/ 访问控制不严，攻击者可利用该漏洞获取敏感信息。

## 漏洞影响

吉拉科技 LVS精益价值管理系统

## 网络测绘

```
"Supperd By 吉拉科技"
```

## 漏洞复现

登录页面

![image-20220525143613247](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251436458.png)

验证POC

```
/Business/
```

![image-20220525143712687](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251437757.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%90%89%E6%8B%89%E7%A7%91%E6%8A%80-LVS%E7%B2%BE%E7%9B%8A%E4%BB%B7%E5%80%BC%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-Business-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
