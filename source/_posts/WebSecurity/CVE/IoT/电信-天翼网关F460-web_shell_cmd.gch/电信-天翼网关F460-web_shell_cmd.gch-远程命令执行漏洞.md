---
title: "电信 天翼网关F460 web_shell_cmd.gch 远程命令执行漏洞"
date: 2026-10-18 09:16:26
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "电信-天翼网关F460-web_shell_cmd.gch"
tags:
  - "电信-天翼网关F460-web_shell_cmd.gch"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

电信天翼网关F460 web_shell_cmd.gch文件存在命令调试界面，攻击者可以利用获取服务器权限

## 漏洞影响

```
电信天翼网关F460
```

## 网络测绘

```
title="F460"
```

## 漏洞复现

出现漏洞的文件为 web_shell_cmd.gch

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140925583.png)

直接输入命令就可以执行 **cat /etc/passwd**

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202140925693.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%94%B5%E4%BF%A1-%E5%A4%A9%E7%BF%BC%E7%BD%91%E5%85%B3F460-web_shell_cmd.gch-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
