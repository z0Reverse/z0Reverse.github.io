---
title: "Apache Zeppelin 未授权任意命令执行漏洞"
date: 2026-10-16 09:06:40
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Apache-Zeppelin"
tags:
  - "Apache-Zeppelin"
  - "命令执行"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

Apache Zeppelin 存在未授权的用户访问命令执行接口，导致了任意用户都可以执行恶意命令获取服务器权限

## 漏洞影响

```
Apache Zeppelin
```

## 网络测绘

```
icon_hash="960250052"
```

## 漏洞复现

含有漏洞的页面如下

![image-20220209122046358](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091220423.png)



点击 创建一个匿名用户在用户页面执行命令即可

![image-20220209122110291](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091221386.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Apache-Zeppelin-%E6%9C%AA%E6%8E%88%E6%9D%83%E4%BB%BB%E6%84%8F%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
