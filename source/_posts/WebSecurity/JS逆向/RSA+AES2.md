---
title: RSA+AES2
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - JS逆向
tags:
  - JS逆向
  - 加密算法
  - 前端安全
---

跟上个差不多，rsa+aes加密实现
rsa公钥硬编码，aes密钥、iv随机生成，rsa加密密钥、iv，aes加密数据
上次采用hook固定，多层代理到yakit是明文，但是那是一个body参数，对于多个且加密后参数改变的，目前可以利用ai直接给出接口明确的参数，手动去构建，转给mitproxy加密后转发

场景：全局加密
所有接口全部加密
![](/images/RSA+AES2/20260912214637.png)
直接ai分析加解密逻辑
![](/images/RSA+AES2/20260912214751.png)
让其给出mitproxy脚本，然后根据分析的明文接口数据进行构造
