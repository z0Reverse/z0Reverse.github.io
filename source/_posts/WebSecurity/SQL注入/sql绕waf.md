---
title: sql绕waf
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - SQL注入
tags:
  - SQL注入
  - 注入
  - WAF绕过
---

1、过滤空格

```
采用内敛注释
	/**/  /**!**/
采用换行符
	\n \t %00
加号代替

括号

子句嵌套

```

2、过滤union、select

```

```

3、过滤空格和注释

```

```

4、
