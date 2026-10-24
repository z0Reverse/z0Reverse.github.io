---
title: "锐捷 BCR商业无线云网关 后台命令执行漏洞"
date: 2026-10-18 09:16:54
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "锐捷"
tags:
  - "锐捷"
  - "命令执行"
  - "弱口令"
  - "漏洞复现"
---
## 漏洞描述

锐捷 BCR商业无线云网关 存在后台命令执行漏洞，攻击者通过默认口令可以登陆后台构造特殊的参数执行任意命令，获取服务器权限

## 漏洞影响

锐捷 BCR商业无线云网关

## 网络测绘

```
fid="N3IFMflkcmNQ2s4vuAhjzg=="
```

## 漏洞复现

登陆页面

![image-20230828150840869](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828150840869.png)

通过弱口令登陆后台 admin 拼接命令

![image-20230828150858507](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828150858507.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%94%90%E6%8D%B7-BCR%E5%95%86%E4%B8%9A%E6%97%A0%E7%BA%BF%E4%BA%91%E7%BD%91%E5%85%B3-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
