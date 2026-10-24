---
title: "用友 NC bsh.servlet.BshServlet 远程命令执行漏洞"
date: 2026-10-17 09:12:58
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "用友"
tags:
  - "用友"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

用友 NC bsh.servlet.BshServlet 存在远程命令执行漏洞，通过BeanShell 执行远程命令获取服务器权限

## 漏洞影响

```
用友 NC
```

## 网络测绘

```
icon_hash="1085941792"
```

## 漏洞复现

访问页面如下

![yongyou-4-1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/yongyou-4-1.png)

漏洞Url为

```plain
/servlet/~ic/bsh.servlet.BshServlet
```

![yongyou-4-2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/yongyou-4-2.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-NC-bsh.servlet.BshServlet-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
