---
title: "畅捷CRM 后台附件任意文件上传漏洞"
date: 2026-10-16 09:11:18
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "畅捷CRM"
tags:
  - "畅捷CRM"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

畅捷CRM 后台附件存在任意文件上传漏洞，通过解析漏洞可跳过后缀更改获取网站权限

## 漏洞影响

```
畅捷CRM
```

## 网络测绘

```
title="畅捷CRM"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101912910.png)



部分存在空密码 admin/空密码



登录后添加客户，并上传附件为PHP文件，其中文件名为



xxx.xxx.php格式，越过系统中的后缀更改



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101912584.png)



点击文件名跳转



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101912465.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%95%85%E6%8D%B7CRM-%E5%90%8E%E5%8F%B0%E9%99%84%E4%BB%B6%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
