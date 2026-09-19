---
title: SQL进阶
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - SQL注入
tags:
  - SQL注入
  - 注入
  - WAF绕过
---

## Cookie头注入
响应包中明显使用到cookie场景，可以考虑
![](/images/SQL进阶/20260914222507.png)

```
1' or 1=1 order by 8 #
执行SQL语句：SELECT * FROM users WHERE cookie='1' or 1=1 order by 8 #'<br />Unknown
column '8' in 'order clause'
```
