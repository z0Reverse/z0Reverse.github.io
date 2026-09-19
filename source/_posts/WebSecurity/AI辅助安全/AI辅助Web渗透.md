---
title: AI辅助Web渗透
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - AI辅助安全
tags:
  - AI
  - MCP
  - 渗透测试
---

本文主要针对AI在Web渗透方面的使用分析，按照环境搭建、skills、效果三个方面

# 1、信息搜集：AI+Tscan无影
Tscan目前已经支持MCP能力，那么实现思路
1、配置好各个api或者校验身份的cookie

2、配置mcp到ai侧，这里使用codex

3、尝试调用mcp能力

# 2、AI渗透：AI+BurpSuit
目前已BurpSuit在202512的版本已经支持MCP能力，那么实现思路
1、下载最新并配置好支持mcp版本的burpsuit

2、extension中搜索mcp插件，下载

3、目前支持sse和stdio两种方式，但是stdio更稳定些，演示就按照stdio来
1、导出这个mcp的jar文件
2、ai侧配置这个mcp
3、试运行

# 3、AI+Yakit
Yakit目前支持实验功能-mcp能力

yakit启动mcp服务
![](/images/AI辅助Web渗透/20260912214220.png)
ai侧接入mcp
由于Yakit提供的是sse接入方式，只需要mcpserver配置对应端口即可
![](/images/AI辅助Web渗透/20260912214257.png)

试运行：
![](/images/AI辅助Web渗透/20260912214321.png)
