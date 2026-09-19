---
title: Claude+JadxMCP
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - AI辅助逆向
tags:
  - AI
  - MCP
  - 逆向
---

## 1、安装jadx、jadx-mcp
科学上网下载对应的版本的jar包和zip，jar包用于jadx中导入插件，zip包用于建立连接，后边配置claude的时候使用
![](/images/Claude+JadxMCP/20260531183937.png)

![](/images/Claude+JadxMCP/20260531182109.png)

![](/images/Claude+JadxMCP/20260531182145.png)

![](/images/Claude+JadxMCP/20260531182159.png)

![](/images/Claude+JadxMCP/20260531182333.png)

![](/images/Claude+JadxMCP/20260531182401.png)

## 2、claude安装

## 3、claude配置mcp
在settings.json文件中配置mcpServers
![](/images/Claude+JadxMCP/20260531182633.png)

![](/images/Claude+JadxMCP/20260531185616.png)
我这里专门创建一个venv环境用于claude使用
![](/images/Claude+JadxMCP/20260531182933.png)

## 4、试运行、
需要注意可能部分环境依赖需要安装。我这里直接做了一个venv专门用于claude调用
让他自己去安装依赖就行
![](/images/Claude+JadxMCP/20260531184209.png)

![](/images/Claude+JadxMCP/20260531185702.png)
![](/images/Claude+JadxMCP/20260531185717.png)

## 5、配置skills
两种方式：1、settings.json中指定skills路径。2、创建skills目录，下面分别存放skills
第二种实现：
![](/images/Claude+JadxMCP/20260531191229.png)
