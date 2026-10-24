---
title: "OneBlog 小于v2.2.1 远程命令执行漏洞"
date: 2026-10-16 09:09:00
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "OneBlog"
tags:
  - "OneBlog"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

OneBlog 小于v2.2.1 由于使用含有漏洞版本的Apache Shiro和默认的密钥导致存在远程命令执行漏洞

## 漏洞影响

```
OneBlog <= v2.2.1
```

## 网络测绘

```
app="OneBlog开源博客后台管理系统"
```

## 漏洞复现

登陆页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101909905.png)



使用工具直接利用Apache Shiro漏洞即可



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101909954.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/OneBlog-%E5%B0%8F%E4%BA%8Ev2.2.1-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
