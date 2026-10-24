---
title: "众望网络 微议管理系统 后台updatefile.html 任意文件上传漏洞"
date: 2026-10-16 09:10:21
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "众望网络-微议管理系统"
tags:
  - "众望网络-微议管理系统"
  - "文件上传"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

众望网络 微议管理系统 后台updatefile.html页面任意文件上传漏洞，攻击者通过漏洞可以上传恶意文件控制服务器

## 漏洞影响

```
众望网络 微议管理系统
```

## 网络测绘

```
"微议管理系统"
```

## 漏洞复现

登录页面

![image-20220525103602413](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251036461.png)

默认口令 amdin/admin, 服务器更新界面上传PHP文件

![image-20220525103740928](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251037014.png)

访问页面

```
/Updatefiles/文件名.php
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BC%97%E6%9C%9B%E7%BD%91%E7%BB%9C-%E5%BE%AE%E8%AE%AE%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-%E5%90%8E%E5%8F%B0updatefile.html-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
