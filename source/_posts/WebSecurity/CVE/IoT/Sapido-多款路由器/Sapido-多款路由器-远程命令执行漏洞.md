---
title: "Sapido 多款路由器 远程命令执行漏洞"
date: 2026-10-18 09:15:11
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Sapido-多款路由器"
tags:
  - "Sapido-多款路由器"
  - "命令执行"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

Sapido多款路由器在未授权的情况下，导致任意访问者可以以Root权限执行命令

## 漏洞影响

```
BR270n-v2.1.03
BRC76n-v2.1.03
GR297-v2.1.3
RB1732-v2.0.43
```

## 网络测绘

```
app="Sapido-路由器"
```

## 漏洞复现

固件中存在一个asp文件为 **syscmd.asp** 存在命令执行

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162237726.png)

访问目标：

```plain
http://xxx.xxx.xxx.xxx/syscmd.asp
http://xxx.xxx.xxx.xxx/syscmd.htm
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162237444.png)

直接输入就可以命令执行了

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Sapido-%E5%A4%9A%E6%AC%BE%E8%B7%AF%E7%94%B1%E5%99%A8-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
