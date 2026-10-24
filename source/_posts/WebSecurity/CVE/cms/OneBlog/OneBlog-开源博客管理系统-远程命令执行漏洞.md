---
title: "OneBlog 开源博客管理系统 远程命令执行漏洞"
date: 2026-10-12 09:00:46
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "OneBlog"
tags:
  - "OneBlog"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

由于使用含有漏洞版本的Apache Shiro和默认的密钥，导致OneBlog存在远程命令执行漏洞。

## 漏洞复现

shiro 默认密钥：

![image-20221206161928066](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/image-20221206161928066.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/OneBlog-%E5%BC%80%E6%BA%90%E5%8D%9A%E5%AE%A2%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
