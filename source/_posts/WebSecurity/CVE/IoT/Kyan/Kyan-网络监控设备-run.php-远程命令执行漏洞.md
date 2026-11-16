---
title: "Kyan 网络监控设备 run.php 远程命令执行漏洞"
date: 2026-10-18 09:15:00
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Kyan"
tags:
  - "Kyan"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

Kyan 网络监控设备 run.php可在身份验证的情况下执行任意命令, 配合账号密码泄露漏洞，可以获取服务器权限，存在远程命令执行漏洞

## 漏洞影响

```
Kyan
```

## 网络测绘

```
title="platform - Login"
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140928343.png)

使用 Gobuster扫描文件

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140928616.png)

其中 run.php 文件内容为

```php
&lt;?php 
require_once 'functions.php';
require_once 'international.php';
session_start();
auth_check();
print_html_begin('run');
?&gt;
&lt;body link="#000000" vlink="#000000" alink="#000000" bgcolor="#FFFFFF"&gt;

&lt;form method="post"&gt;
&lt;table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" width="100%" id="AutoNumber1" height="25" bordercolor="#000000"&gt;
    &lt;tr&gt;
      &lt;td width="100%" height="25" bgcolor="#FCFEBA"&gt;
      &lt;p align="center"&gt;&lt;font face="Verdana" size="2"&gt; Shell Execute &lt;/font&gt;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;td width="100%" height="25" bgcolor="#FCFEBA"&gt;
            &lt;div align="center"&gt;
              &lt;textarea name="command" rows="2" cols="100" &gt;&lt;?php echo &#36;_POST['command']; ?&gt;
              &lt;/textarea&gt; 
        &lt;/div&gt;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;td width="100%" height="25" bgcolor="#FCFEBA"&gt;
        &lt;div align="center"&gt;
          &lt;input type="submit" value="Execute"&gt;
          &lt;/div&gt;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr&gt;
      &lt;td width="100%" height="25" bgcolor="#FCFEBA"&gt;
        &lt;div align="center"&gt;
          &lt;textarea name="textarea" cols="100" rows="50" readonly&gt;&lt;?php @$output = &#115;ystem(trim(&#36;_POST['command'])); ?&gt;
          &lt;/textarea&gt;
        &lt;/div&gt;&lt;/td&gt;
    &lt;/tr&gt;
&lt;/table&gt;
&lt;/form&gt;
&lt;/body&gt; 
&lt;?php
print_html_end(); 
?&gt;</code></pre>

</details>

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140928998.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Kyan-%E7%BD%91%E7%BB%9C%E7%9B%91%E6%8E%A7%E8%AE%BE%E5%A4%87-run.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
