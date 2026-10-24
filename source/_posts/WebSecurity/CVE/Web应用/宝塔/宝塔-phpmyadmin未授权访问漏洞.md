---
title: "宝塔 phpmyadmin未授权访问漏洞"
date: 2026-10-16 09:10:40
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "宝塔"
tags:
  - "宝塔"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

【宝塔面板】紧急安全更新通知，Linux面板7.4.2版本/Windows面板6.8版本存在安全隐患，其他版本无此风险。已发布紧急更新，请所有使用此版本的用户务必升级到最新版，更新方法，登录面板直接升级更新即可，如更新出现问题，请登录宝塔论坛反馈或者联系客服反馈

## 漏洞影响

```
Linux正式版7.4.2
Linux测试版7.5.13
Windows正式版6.8
```

## 漏洞复现

访问 [**http://xxx.xxx.xxx.xxx:888/pma**](http://xxx.xxx.xxx.xxx:888/pma) 即可



![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091838946.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%AE%9D%E5%A1%94-phpmyadmin%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
