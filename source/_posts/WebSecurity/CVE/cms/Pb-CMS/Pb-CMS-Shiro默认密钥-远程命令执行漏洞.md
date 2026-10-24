---
title: "Pd-CMS Shiro默认密钥 远程命令执行漏洞"
date: 2026-10-12 09:00:53
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "Pb-CMS"
tags:
  - "Pb-CMS"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

Pd-CMS存在Shiro默认密钥，攻击者通过已知的密钥将会造成Shiro远程命令执行漏洞

## 漏洞影响

```
Pd-CMS
```

## 网络测绘

```
"pb-cms"
```

## 漏洞复现

主页面

![image-20220518155442570](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181554764.png)

默认密钥

```
3AvVhmFLUs0KTA3Kprsdag==
```

![image-20220518155454512](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181554589.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/Pb-CMS-Shiro%E9%BB%98%E8%AE%A4%E5%AF%86%E9%92%A5-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
