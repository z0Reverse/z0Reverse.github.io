---
title: "网御星云 web防护系统 信息泄露漏洞"
date: 2026-10-16 09:11:31
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "网御星云-web防护系统"
tags:
  - "网御星云-web防护系统"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

网御星云 web防护系统 存在信息泄露漏洞，通过访问特殊的Url获取部分敏感信息

## 漏洞影响

```
网御星云
```

## 网络测绘

```
title="网页防篡改系统"
```

## 漏洞复现

登录页面如下



![image-20220209200743358](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202092007654.png)



访问



```plain
http://xxx.xxx.xxx.xxx/API/
```



![image-20220209200809080](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202092008160.png)

部分 API请求 不需要登录即可访问获取信息，例如 **/user/list**



![image-20220209200829973](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202092008053.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%BD%91%E5%BE%A1%E6%98%9F%E4%BA%91-web%E9%98%B2%E6%8A%A4%E7%B3%BB%E7%BB%9F-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
