---
title: "极致CMS 后台文件编辑插件 任意文件上传"
date: 2026-10-12 09:01:29
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "极致CMS"
tags:
  - "极致CMS"
  - "文件上传"
  - "漏洞复现"
---
## 漏洞描述

极致CMS后台中含有文件编辑插件，通过逻辑漏洞可任意修改文件

## 漏洞影响

```
极致CMS
```

## 网络测绘

```
icon_hash="1657387632"
```

## 漏洞复现

登陆后台查看插件处，有一个后台编辑的插件

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170920402.jpg)

安装之后设置密码并使用

- 如果已经设有密码，重新安装插件即可解决密码未知问题

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170920491.jpg)

修改为php代码

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170920842.jpg)

成功执行php代码的命令

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/%E6%9E%81%E8%87%B4CMS-%E5%90%8E%E5%8F%B0%E6%96%87%E4%BB%B6%E7%BC%96%E8%BE%91%E6%8F%92%E4%BB%B6-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0.md)
