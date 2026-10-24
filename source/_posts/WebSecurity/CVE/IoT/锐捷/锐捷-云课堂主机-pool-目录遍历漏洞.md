---
title: "锐捷 云课堂主机 pool 目录遍历漏洞"
date: 2026-10-18 09:17:07
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "锐捷"
tags:
  - "锐捷"
  - "目录遍历"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

锐捷云课堂主机存在目录遍历漏洞，通过访问get请求/pool/，即可读取目录.导致敏感信息泄露.

## 漏洞影响

```
锐捷云课堂
```

## 网络测绘

```
title="Ruijie" && "云课堂主机"
```

## 漏洞复现

访问 http://xxx.xxx.xxx.xxx/pool 造成目录遍历

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110919267.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%94%90%E6%8D%B7-%E4%BA%91%E8%AF%BE%E5%A0%82%E4%B8%BB%E6%9C%BA-pool-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
