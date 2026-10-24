---
title: "默安 幻阵蜜罐未授权访问 RCE"
date: 2026-10-16 09:11:55
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "默安"
tags:
  - "默安"
  - "代码执行"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

默安 幻阵蜜罐存在部署页面未授权访问 ，可执行任意命令

## 漏洞影响

```
默安 幻阵蜜罐
```

## 漏洞复现

产品页面



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091842964.png)



安装页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091843119.png)



刷新并抓包



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091844386.png)



Drop掉 **/huanzhen/have_installed?**



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091844013.png)



进入页面



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091844519.png)

点击调试抓包

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091844068.png)



执行其他命令



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091844606.png)



点击一键诊断泄露 IP数据



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202091844354.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%BB%98%E5%AE%89-%E5%B9%BB%E9%98%B5%E8%9C%9C%E7%BD%90%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE-RCE.md)
