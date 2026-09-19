---
title: 组件导出到webview外带token
date: 2026-09-20 02:16:39
categories:
  - AndroidReverse
  - 恶意代码分析
tags:
  - WebView
  - 组件安全
  - 漏洞利用
---

这个是因为组件加载webview后会将token等个人信息直接打包丢给加载的webview，而不是通过jsbridge反向外带android开放的接口
