---
title: "NetMizer 日志管理系统 登录绕过漏洞"
date: 2026-10-18 09:15:08
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "NetMizer"
tags:
  - "NetMizer"
  - "漏洞复现"
---
## 漏洞描述

NetMizer 日志管理系统存在登录绕过漏洞，通过限制某个请求包的发送获取后台权限

## 漏洞影响

```
NetMizer 日志管理系统
```

## 网络测绘

```
title="NetMizer 日志管理系统"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162257795.png)

访问页面 main.html 并抓取请求包, 使用Burp Drop掉下面对请求包

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162257627.png)

Drop后停止抓包，成功进入后台

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162257550.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/NetMizer-%E6%97%A5%E5%BF%97%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-%E7%99%BB%E5%BD%95%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E.md)
