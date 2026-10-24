---
title: "Jupyter Notebook 未授权访问远程命令执行漏洞"
date: 2026-10-16 09:08:27
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Jupyter-Notebook"
tags:
  - "Jupyter-Notebook"
  - "命令执行"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。

如果管理员未为Jupyter Notebook配置密码，将导致未授权访问漏洞，游客可在其中创建一个console并执行任意Python代码和命令。

## 漏洞影响

```
Jupyter Notebook
```

## 网络测绘

```
app="Jupyter-Notebook" && body="Terminal"
```

## 环境搭建

Vulhub运行测试环境：

```
docker-compose up -d
```

运行后，访问`http://your-ip:8888`将看到Jupyter Notebook的Web管理界面，并没有要求填写密码。

![image-20220224195831711](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202241958784.png)

## 漏洞复现

访问目标, 点击new→Terminal即可创建一个控制台，可以直接执行任意命令：

![image-20220224195857801](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202241958870.png)

执行命令并反弹shell：

![image-20220224200055046](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202242000102.png)

监听2333端口，成功接收反弹shell：

![image-20220224200143472](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202242001536.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Jupyter-Notebook-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
