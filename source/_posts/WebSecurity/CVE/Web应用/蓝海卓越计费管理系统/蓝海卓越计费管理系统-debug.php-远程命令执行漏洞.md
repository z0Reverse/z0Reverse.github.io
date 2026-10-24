---
title: "蓝海卓越计费管理系统 debug.php 远程命令执行漏洞"
date: 2026-10-16 09:11:34
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "蓝海卓越计费管理系统"
tags:
  - "蓝海卓越计费管理系统"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

蓝海卓越计费管理系统 debug.php 存在命令调试页面，导致攻击者可以远程命令执行

## 漏洞影响

```
蓝海卓越计费管理系统
```

## 网络测绘

```
title=="蓝海卓越计费管理系统"
```

## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101853490.png)



漏洞代码



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101853603.png)



访问 debug.php页面 远程调试命令执行



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101853251.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E8%93%9D%E6%B5%B7%E5%8D%93%E8%B6%8A%E8%AE%A1%E8%B4%B9%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-debug.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
