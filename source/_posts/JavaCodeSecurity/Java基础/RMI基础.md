---
title: RMI基础
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

Remote Method Invocation远程方法调用
允许在不同的java虚拟机中进行通信
一组拥护开发分布式应用程序的api，使用java语言接口定义了远程对象，集合了java序列化和java远程方法协议
rmi以来的通信协议是jrmp，该协议主要用于查找和引用远程对象的协议，rmi对象是通过序列化方式进行传输的
RMI中的三个角色色
	服务端
	注册中心
	客户端
![](/images/RMI基础/20251211-2.png)存根/桩(Stub)：客户端侧的代理，每个远程对象都包含一个代理对象stub，当运行在本地 Java 虚拟机上 的程序调用运行在远程 Java 虚拟机上的对象方法时，它首先在本地创建该对象的代理对象 stub, 然后调 用代理对象上匹配的方法。
骨架(Skeleton)：服务端侧的代理，用于读取 stub 传递的方法参数，调用服务器方的实际对象方法， 并 接收方法执行后的返回值

RMI 代码编写步骤如下：
1. 创建远程接口及声明远程方法（SayHello.java）
2. 实现远程接口及远程方法（继承UnicastRemoteObject）(SayHelloImpl.java)
3. 启动 RMI 注册服务，并注册远程对象（RmiServer.java）
4. 客户端查找远程对象，并调用远程方法（RmiClient.java）
5. 执行程序：启动服务端RmiServer；运行客户端RmiClient进行调用

1.客户端需要也有服务端该类的接口的定义，但是具体该接口实现的方法是在服务端的，这既是分布式接口与实现分离
2.Calculator calculator = new CalculatorImpl();面向接口实现，这样的话更换实现类会比较方便，也可以面向实现CalculatorImpl calculator = new CalculatorImpl();

代码实现
SayHelloInterface

```java
package method1;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface SayHello extends Remote {
    public String sayHello(String name) throws RemoteException;
}
```

SayHelloImplments

```java
package method1;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class SayHelloImpl extends UnicastRemoteObject implements SayHello {
    public SayHelloImpl() throws RemoteException{
        super();
    }
    public String sayHello(String name) throws RemoteException {
        return "Hello " + name;
    }
}
```

CalculatorInterface

```java
package method2;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calcultor extends Remote {
    int add(int a, int b) throws RemoteException;
    int sub(int a, int b) throws RemoteException;
}
```

CalculatorImpl

```java
package method2;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class CalcutorImpl extends UnicastRemoteObject implements Calcultor {
    public CalcutorImpl()throws RemoteException{
        super();
    }

    public int add(int a, int b) throws RemoteException {
        return a+b;
    }
    public int sub(int a, int b) throws RemoteException {
        return a-b;
    }
}

```

RMIService

```java
package RMIService;

import method1.SayHello;
import method1.SayHelloImpl;
import method2.Calcultor;
import method2.CalcutorImpl;

import java.rmi.AlreadyBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RmiServer {
    public static void main(String[] args) throws RemoteException, AlreadyBoundException {
        System.out.println("RmiServer starting ing...");

        //创建远程对象SayHello
        SayHello sayHello = new SayHelloImpl();
        Registry registry = LocateRegistry.createRegistry(1099);
        registry.bind("sayhello",sayHello);
        System.out.println("SayHelloService is registered");

        //创建远程对象Cal

        // 创建服务实例
        Calcultor calculator = new CalcutorImpl();

        // 将服务绑定到注册表
        registry.rebind("calcutor", calculator);
        System.out.println("CalculatorService is registered");
    }
}
```

RMIClient

```java
package RMIClient;

import method1.SayHello;
import method2.Calcultor;

import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RmiClient {
    public static void main(String[] args) throws RemoteException, NotBoundException {
        Registry registry = LocateRegistry.getRegistry("localhost", 1099);
        SayHello sayHello=(SayHello) registry.lookup("sayhello");
        System.out.println("sayHello find");
        System.out.println(sayHello.sayHello("hacker"));

        Calcultor calcultor=(Calcultor) registry.lookup("calcutor");
        System.out.println("calcultor find");
        int sum=calcultor.add(1,2);
        System.out.println(sum);
        int sub=calcultor.sub(2,3);
        System.out.println(sub);

    }
}
```
