---
title: JNDI基础
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

JNDI:是一个JavaApi，允许Java应用程序与命名和目录服务进行交互。这些服务可以是本地的也可以是分布式的，可以基于各种协议【LDAP轻量级目录访问协议，DNS域名系统，NIS网络信息服务】

主要是为了统一不同命名和目录服务的访问方式，使得java应用程序能够以一种统一的方式来访问这些服务。可以访问的目录及服务包括：dns,rmi,ldap,corba

命名服务提供了将名称与对象关联映射的机制.在 Java 中，这些对象通常是网络资源、Java对象、文 件、服务等。命名服务允许开发人员使用简单的名称来访问这些对象，而不需要知道其底层的物理位置 或其他详细信息。例如，一个Web应用程序可能需要连接到一个数据库，而不需要知道数据库的确切位 置。通过命名服务，开发人员可以为数据库分配一个简单的名称，并在需要时通过该名称访问它
目录服务扩展了命名服务的概念，提供了一种更加结构化和查询友好的方式来组织和管理对象。目录服 务通常被用来存储和检索关于用户、组织、网络资源等信息的数据。与命名服务类似，目录服务也使用 名称来引用对象，但它们提供了更丰富的查询功能，使得可以根据各种属性进行搜索和过滤

JNDI的五个包
javax.naming
	命名服务的类和接口，定义了Context接口用于查找，绑定，接触绑定，重命名独以及创建和销毁子上下文的操作
	查找：lookup()
	绑定：list Bindings（）
	列表：list(),listBindings()
	InitialContext类
		构造方法
		InitialContext() 构建一个初始上下文。  
		InitialContext(boolean lazy) 构造一个初始上下文，并选择不初始化它。   InitialContext(Hashtable environment) 使用提供的环境构建初始上下文。
		常用方法：
		 bind(Name name, Object obj) 将名称绑定到对象。
		 list(String name) 枚举在命名上下文中绑定的名称以及绑定到它们的对象的类名。 lookup(String name) 检索命名对象。
		 rebind(String name, Object obj) 将名称绑定到对象，覆盖任何现有绑定。 unbind(String name) 取消绑定命名对象。
	Reference类
	构造方法：
	Reference(String className) 为类名为“className”的对象构造一个新的引用。   Reference(String className, RefAddr addr) 为类名为“className”的对象和地址构造一个新引用。  
	Reference(String className, RefAddr addr, String factory, String factoryLocation) 为类名为“className”的对象，对象工厂的类名和位置以及对象的地址构造一个新引用。   Reference(String className, String factory, String factoryLocation) 为类名为“className”的对象以及对象工厂的类名和位置构造一个新引用。
	常用方法：
	void add(int posn, RefAddr addr) 将地址添加到索引posn的地址列表中。  
	void add(RefAddr addr) 将地址添加到地址列表的末尾。  
	void clear() 从此引用中删除所有地址。  
	RefAddr get(int posn) 检索索引posn上的地址。  
	RefAddr get(String addrType) 检索地址类型为“addrType”的第一个地址。  
	Enumeration getAll() 检索本参考文献中地址的列举。  
	String getClassName() 检索引用引用的对象的类名。  
	String getFactoryClassLocation() 检索此引用引用的对象的工厂位置。  
	String getFactoryClassName() 检索此引用引用对象的工厂的类名。    
	Object remove(int posn) 从地址列表中删除索引posn上的地址。  
	 int size() 检索此引用中的地址数。  
	 String toString() 生成此引用的字符串表示形式
javax.naming.directory
	继承了 javax.naming，提供了除命名服务外访问目录服务的功能
javax.nameing.ldap
	继承了javax.naming，提供了访问 LDAP 的能力。
javax.naming.event
	包含了用于支持命名和目录服务中的事件通知的类和接口。
javax.naming,spi
	允许动态插入不同实现，为不同命名目录服务供应商的开发人员提供开发和实现的途径，以便应用程序 通过 JNDI 可以访问相关服务。

JNDI操作RMI
rmi相关服务不做变动，启动rmiserver
启动jndiservice

```java
package JNDIDemo;

import method1.SayHelloImpl;

import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.rmi.RemoteException;

public class JNDIServer {
    public static void main(String[] args) throws NamingException, RemoteException {
        InitialContext ic = new InitialContext();
        ic.rebind("rmi://127.0.0.1:1099/sayhello",new SayHelloImpl());
        System.out.println("jndi server started");
    }
}
```

启动jndiclient

```java
package JNDIDemo;

import method1.SayHello;

import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.rmi.RemoteException;

public class JNDIClient {
    public static void main(String[] args) throws RemoteException, NamingException {
        //IntialContext默认从上下文进行初始化
        InitialContext ic = new InitialContext();
        SayHello sayHello=(SayHello) ic.lookup("rmi://127.0.0.1/sayhello");
        System.out.println(sayHello.sayHello("Admin"));
    }
}
```

JNDI操作dns

```

```
