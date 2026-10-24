---
title: "Hue 后台编辑器命令执行漏洞"
date: 2026-10-16 09:08:09
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Hue"
tags:
  - "Hue"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

Hue 后台编辑器存在命令执行漏洞，攻击者通过编辑上传  xxx.sh 文件即可达到命令执行的目的

## 漏洞影响

```
Hue 后台编辑器
```

## 网络测绘

```
title="Hue - 欢迎使用 Hue"
```

## 漏洞复现

登录页面如下

![hue-1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/hue-1.png)



上传并编辑文件为执行的命令

![hue-2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/hue-2.png)



按如下步骤点击即可执行想要执行的命令



![hue-3](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/hue-3.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Hue-%E5%90%8E%E5%8F%B0%E7%BC%96%E8%BE%91%E5%99%A8%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
