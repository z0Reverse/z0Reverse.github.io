# 我的安全笔记 · Hexo 博客

基于 **Hexo 7 + Reimu 主题** 的静态笔记博客，通过 GitHub Actions 自动部署到 GitHub Pages。

## 分类体系

`source/_posts/` 下的**文件夹结构与网页分类是一一对应的**，文件夹只影响本地整理，不影响文章 URL。

| 大类 | 当前子类 |
| ---- | ---- |
| WebSecurity | SQL注入、JS逆向、小程序、越权、中间件/FastJson、AI辅助安全 |
| JavaCodeSecurity | Java基础、JavaWeb安全基础、组件漏洞/FastJson、常见知识、项目实战、实战审计、常见环境 |
| AndroidReverse | Android基础、NDK开发、Frida逆向、加解密算法、网络协议逆向、恶意代码分析、环境问题、AI辅助逆向、文件存储与沙箱 |
| Tools | Android抓包 |

新增子类：直接在对应大类下建文件夹，文件 front-matter 里多加一行 `categories` 即可。

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

### 几条约定

- **文件夹随便建**：`_posts` 下的子文件夹只用于本地整理，URL 由 `permalink: :year/:month/:name/` 决定，和文件夹无关，移动文件不会导致老链接失效。
- **图片统一放 `source/images/`**：笔记里用站内绝对路径引用，例如 `![](/images/笔记名/xxx.png)`。Obsidian 中把附件目录设为 `images`、链接格式选 “Vault 绝对路径” 即可自动生成这种写法。
- **草稿放 `source/_drafts/`**：该目录不会被发布，适合先列大纲后期再补内容。
- **附件放 `source/attachments/`**：脚本、压缩包等可下载文件放这里，用 `/attachments/xxx.sh` 引用。

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
│   ├── _posts/            # ★ 所有笔记 Markdown（按四大类分文件夹）
│   │   ├── WebSecurity/
│   │   ├── JavaCodeSecurity/
│   │   ├── AndroidReverse/
│   │   └── Tools/
│   ├── _drafts/           # 草稿（不会被发布）
│   ├── images/            # ★ 笔记图片（按笔记名分目录）
│   ├── attachments/       # 可下载附件（脚本等）
│   ├── categories/        # 分类汇总页
│   ├── tags/              # 标签汇总页
│   └── about/             # 关于页
├── themes/reimu/          # 主题源码
├── .github/workflows/     # 自动部署工作流
└── nodejs/                # 本地免安装 Node.js（不提交）
```
