---
title: "Tenda W15E企业级路由器 RouterCfm.cfg 配置文件泄漏漏洞"
date: 2026-10-18 09:15:24
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "Tenda"
tags:
  - "Tenda"
  - "未授权访问"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

Tenda 企业级路由器 RouterCfm.cfg 配置文件可在未授权的情况下被读取，导致账号密码等敏感信息泄漏

## 漏洞影响

```
Tenda 企业级路由器
```

## 网络测绘

```
title=="Tenda | Login" && country="CN"
```

## 漏洞复现

登录页面

![image-20220519181331832](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191813876.png)

访问路径![image-20220519181508329](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191815422.png)

后台账号密码位于参数 `sys.userpass` base64解密后的字符

![image-20220519181456848](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191814923.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/Tenda-W15E%E4%BC%81%E4%B8%9A%E7%BA%A7%E8%B7%AF%E7%94%B1%E5%99%A8-RouterCfm.cfg-%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
