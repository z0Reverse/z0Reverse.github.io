---
title: "云时空 社会化商业ERP系统 Shiro框架 远程命令执行漏洞"
date: 2026-10-16 09:10:13
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "云时空"
tags:
  - "云时空"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

云时空 社会化商业ERP为 Shiro框架 ，使用了默认的密钥导致了远程命令执行漏洞

## 漏洞影响

```
云时空 社会化商业ERP系统
```

## 网络测绘

```
title="云时空社会化商业ERP"
```

## 漏洞复现

登录页面

![image-20220525102459840](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251024908.png)

默认密钥为

```
kPH+bIxk5D2deZiIxcaaaA==
```

![image-20220525102542474](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251025549.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BA%91%E6%97%B6%E7%A9%BA-%E7%A4%BE%E4%BC%9A%E5%8C%96%E5%95%86%E4%B8%9AERP%E7%B3%BB%E7%BB%9F-Shiro%E6%A1%86%E6%9E%B6-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
