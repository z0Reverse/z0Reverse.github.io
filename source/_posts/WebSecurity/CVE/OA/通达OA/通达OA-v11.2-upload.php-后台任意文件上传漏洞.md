---
title: "通达OA v11.2 upload.php 后台任意文件上传漏洞"
date: 2026-10-17 09:13:30
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "通达OA"
tags:
  - "通达OA"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

通达OA v11.2后台存在文件上传漏洞，允许通过绕过黑名单的方法来上传恶意文件，导致服务器被攻击

## 漏洞影响

```
通达OA v11.2
```

## 环境搭建

[通达OA v11.2下载链接](https://cdndown.tongda2000.com/oa/2019/TDOA11.2.exe)

下载后按步骤安装即可

## 漏洞复现

该漏洞存在于后台，需要通过登录后才能进行使用

登录后点击 **菜单 -> 系统管理 -> 附件管理**

![image-20220209105402262](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091054355.png)

点击添加附录存储管理添加如下(存储目录为 webroot 目录，默认为 **D:/MYOA/webroot/**)

![image-20220209105417083](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091054194.png)

点击 **组织 -> 系统管理员 -> 上传附件**

![image-20220209105436655](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091054718.png)

抓包使用 windows 的绕过方法 **shell.php -> shell.php.**

![image-20220209105510484](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091055562.png)

2012 为目录

1717872192 为拼接的文件名

最后的shell名字为 1717872192.shell.php

![image-20220209105530593](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091055671.png)

访问木马文件

![image-20220209105545405](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091055475.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%80%9A%E8%BE%BEOA-v11.2-upload.php-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
