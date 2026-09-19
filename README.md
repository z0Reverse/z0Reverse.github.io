# 我的安全笔记 · Hexo 博客

基于 **Hexo 7 + Reimu 主题** 的静态笔记博客，通过 GitHub Actions 自动部署到 GitHub Pages。

## 分类体系

| 大类 | 说明 |
| ---- | ---- |
| WebSecurity | Web 安全漏洞、渗透测试、靶机通关 |
| JavaCodeSecurity | Java 代码审计、反序列化、组件漏洞 |
| AndroidReverse | 安卓逆向、Hook、脱壳与抓包 |
| Tools | 常用安全工具技巧（可加二级分类，如 Tools/BurpSuite） |

## 日常写笔记流程

1. 在 `source/_posts/` 下新建 Markdown 文件（或用命令 `npx hexo new "笔记标题"`）
2. 文件开头写好 front-matter：

```yaml
---
title: 笔记标题
date: 2026-09-20 10:00:00
categories:
  - WebSecurity   # 大类，子类继续往下写一行即可
tags:
  - SQL注入
---
```

3. 本地预览：`npx hexo server`，访问 http://localhost:4000
4. 发布：`git add . && git commit -m "新笔记" && git push`，GitHub Actions 自动构建发布

## 本地环境说明

本仓库自带免安装 Node.js（`nodejs/` 目录，已被 .gitignore 排除，不会推送到 GitHub）。
每次使用前在 PowerShell 中执行：

```powershell
$env:Path = "e:\AIForCode\githubweb\nodejs;$env:Path"
```

## 首次发布到 GitHub Pages

1. 在 GitHub 创建名为 `你的用户名.github.io` 的仓库
2. 仓库 Settings → Pages → Source 选择 **GitHub Actions**
3. 修改根目录 `_config.yml` 中的 `url` 为 `https://你的用户名.github.io`
4. 推送代码：

```powershell
git init -b main
git add .
git commit -m "init: hexo reimu blog"
git remote add origin https://github.com/你的用户名/你的用户名.github.io.git
git push -u origin main
```

推送后约 1-2 分钟，访问 `https://你的用户名.github.io` 即可看到网站。

## 目录结构

```
├── _config.yml            # 站点主配置（站名、URL、主题等）
├── _config.reimu.yml      # Reimu 主题配置（导航、分类卡片、侧边栏）
├── source/
│   ├── _posts/            # ★ 所有笔记 Markdown 都放这里
│   ├── categories/        # 分类汇总页
│   ├── tags/              # 标签汇总页
│   └── about/             # 关于页
├── themes/reimu/          # 主题源码
├── .github/workflows/     # 自动部署工作流
└── nodejs/                # 本地免安装 Node.js（不提交）
```
