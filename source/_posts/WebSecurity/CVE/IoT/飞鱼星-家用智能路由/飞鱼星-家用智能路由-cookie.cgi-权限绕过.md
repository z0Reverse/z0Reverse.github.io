---
title: "飞鱼星 家用智能路由 cookie.cgi 权限绕过"
date: 2026-10-18 09:17:10
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "飞鱼星-家用智能路由"
tags:
  - "飞鱼星-家用智能路由"
  - "未授权访问"
  - "认证绕过"
  - "漏洞复现"
---
## 漏洞描述

飞鱼星 家用智能路由存在权限绕过，通过Drop特定的请求包访问未授权的管理员页面

## 漏洞影响

```
飞鱼星 家用智能路由
飞鱼星 企业级智能上网行为管理系统
```

## 网络测绘

```
title="飞鱼星家用智能路由"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162236515.png)

访问 index.html 时会请求 cookie.cgi

```plain
http://xxx.xxx.xxx.xxx/index.html
```

页面抓包 Drop掉 cookie.cgi

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162236102.png)

跳转后台获取了权限

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162236589.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%A3%9E%E9%B1%BC%E6%98%9F-%E5%AE%B6%E7%94%A8%E6%99%BA%E8%83%BD%E8%B7%AF%E7%94%B1-cookie.cgi-%E6%9D%83%E9%99%90%E7%BB%95%E8%BF%87.md)
