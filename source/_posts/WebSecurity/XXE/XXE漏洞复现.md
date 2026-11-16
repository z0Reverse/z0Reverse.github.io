---
title: "XXE漏洞复现"
date: 2026-10-25 01:04:48
categories:
  - "WebSecurity"
  - "XXE"
tags:
  - "XXE"
  - "XML外部实体注入"
  - "漏洞复现"
---


## 盲注外带

目标环境：

只有上传图片这里具备更改能力，其余无法修改，无法触发xml解析
![](images/Pasted%20image%2020261025010108.png)
尝试上传正常图片，看到具备解析图片能力
![](images/Pasted%20image%2020261025010448.png)
![](images/Pasted%20image%2020261025010509.png)
尝试进行上传操作并更改为上传svg触发xml解析
