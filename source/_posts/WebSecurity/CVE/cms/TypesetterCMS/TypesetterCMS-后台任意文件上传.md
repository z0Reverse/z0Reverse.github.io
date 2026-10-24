---
title: "TypesetterCMS 后台任意文件上传"
date: 2026-10-12 09:01:01
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "TypesetterCMS"
tags:
  - "TypesetterCMS"
  - "命令执行"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

可以通过将.php放在.zip文件中并解压缩来绕过对.php文件的保护。一旦完成，就可以使用恶意的php文件（webshell）在计算机上执行命令

参考阅读：

- [Github 绕过文件上传限制导致命令执行](https://github.com/Typesetter/Typesetter/issues/674)

## 漏洞影响

```
Typesetter CMS 5-5.1
```

## 漏洞复现

按如下步骤复现

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170930270.gif)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/TypesetterCMS-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.md)
