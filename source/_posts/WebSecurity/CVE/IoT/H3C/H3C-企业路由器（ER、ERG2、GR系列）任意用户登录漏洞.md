---
title: "H3C 企业路由器（ER、ERG2、GR系列）任意用户登录漏洞"
date: 2026-10-18 09:14:35
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "H3C"
tags:
  - "H3C"
  - "命令执行"
  - "目录遍历"
  - "漏洞复现"
---
## 漏洞描述

H3C企业路由器（ER、ERG2、GR系列）存在任意用户登录和命令执行漏洞，

## 漏洞复现

官方确认漏洞存在。

攻击者可通过访问 /userLogin.asp/../actionpolicy_status/../xxxx.cfg 接口，xxxx 为设备型号（比如设备型号为 ER5200G2，即访问 /userLogin.asp/../actionpolicy_status/../ER5200G2.cfg），绕过 COOKIE 验证，进行目录穿越，获取设备的明文配置文件。

配置中有明文的 Web 管理员账号 admin 密码，登录后台可通过开启 telnet 获取命令执行权限。

## 修复建议

1. 升级设备固件至最新版本：ERHMG2-MNW100-R1122 及之后版本、ERG2AW-MNW100-R1113 及之后版本、MiniGR1B0V100R014 及之后版本；
2. 关闭 H3C 设备 <远程 WEB 管理>和<远程 TELNET 管理> 功能；
3. 做好企业内外资产排查，将受影响的设备及时下线或转移至内网。

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/H3C-%E4%BC%81%E4%B8%9A%E8%B7%AF%E7%94%B1%E5%99%A8%EF%BC%88ER%E3%80%81ERG2%E3%80%81GR%E7%B3%BB%E5%88%97%EF%BC%89%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E.md)
