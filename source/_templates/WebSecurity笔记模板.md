---
title: WebSecurity 分类笔记模板（二级分类示例）
date: 2026-09-20 10:00:00
categories:
  - WebSecurity
  - SQL注入
tags:
  - 模板
  - Web安全
---

这是一篇 WebSecurity 分类的示例笔记，front-matter 中演示了**二级分类**写法：

```yaml
categories:
  - WebSecurity   # 大类
  - SQL注入       # 二级分类（可自行增加：越权 / 文件上传 / SSRF / 逻辑漏洞...）
```

## 分类与标签怎么选

- **分类**：这篇笔记"属于"哪条路径，一篇只写一条（大类 → 子类）
- **标签**：横跨多类的关键词，如 `提权` `ROOT` `复现` `CTF`，随便贴几个

## 常用记录结构

### 漏洞信息

| 项目 | 内容 |
| ---- | ---- |
| 漏洞类型 | SQL注入 / RCE / SSRF ... |
| 影响版本 | - |
| 复现环境 | - |

### 复现过程

```bash
# 命令和 payload 记录在这里
```

### 修复建议

- 补充修复方案
