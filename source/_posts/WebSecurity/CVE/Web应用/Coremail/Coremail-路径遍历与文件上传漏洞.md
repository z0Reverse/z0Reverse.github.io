---
title: "Coremail 路径遍历与文件上传漏洞"
date: 2026-10-16 09:07:20
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Coremail"
tags:
  - "Coremail"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

监测到Coremail论客邮件系统存在路径遍历与文件上传漏洞，攻击者可利用/lunkr/cache/;/;/../../manager/html 设置参数X-Forwarded-For: 127.0.0.1.Coremail 的 nginx 配置文件中，未针对/lunkr/cache 路径向上解析的时候做 X-Forwarded-For 字段的限制，从而可以利用该接口实现配合利用 nginx 不解析，但 tomcat 解析的差异特性，实现绕过 tomcat manager 的本地 ip 限制。

## 漏洞复现

通过/lunkr/cache/;/;/../../manager/html进入Tomcat控制台，部署war包进行getshell。

![image-20221206101942381](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20221206101942381.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Coremail-%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E4%B8%8E%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
