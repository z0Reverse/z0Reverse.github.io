---
title: "三汇SMG 网关管理软件 down.php 任意文件读取漏洞"
date: 2026-10-18 09:15:39
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "三汇SMG-网关管理软件"
tags:
  - "三汇SMG-网关管理软件"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

三汇SMG 网关管理软件 down.php文件中存在任意文件读取漏洞，攻击者通过漏洞可以下载服务器任意文

## 漏洞影响

```
三汇SMG 网关管理软件
```

## 网络测绘

```
body="text ml10 mr20" && title="网关管理软件"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202203180949105.png)

存在漏洞的页面为 **down.php**

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202203180949106.png)

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202203180949107.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E4%B8%89%E6%B1%87SMG-%E7%BD%91%E5%85%B3%E7%AE%A1%E7%90%86%E8%BD%AF%E4%BB%B6-down.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
