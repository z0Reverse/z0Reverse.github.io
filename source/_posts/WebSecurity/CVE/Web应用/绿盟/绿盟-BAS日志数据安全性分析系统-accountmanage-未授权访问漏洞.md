---
title: "绿盟 BAS日志数据安全性分析系统 accountmanage 未授权访问漏洞"
date: 2026-10-16 09:11:29
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "绿盟"
tags:
  - "绿盟"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

绿盟 BAS日志数据安全性分析系统存在未授权访问漏洞，通过漏洞可以添加任意账户登录平台获取敏感信息

## 漏洞影响

```
绿盟 BAS日志数据安全性分析系统
```

## 网络测绘

```
body="WebApi/encrypt/js-sha1/build/sha1.min.js"
```

## 漏洞复现

登录页面

![image-20220525145937586](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251459725.png)

未授权页面

```
/accountmanage/index
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251500626.png)

添加用户并登录

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251500966.png)

使用账户登录后台

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251500218.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%BB%BF%E7%9B%9F-BAS%E6%97%A5%E5%BF%97%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8%E6%80%A7%E5%88%86%E6%9E%90%E7%B3%BB%E7%BB%9F-accountmanage-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
