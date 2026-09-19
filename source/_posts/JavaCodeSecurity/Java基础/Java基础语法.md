---
title: Java基础语法
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

## 创建一个SpringWeb项目
![](/images/Java基础语法/20251211-41.png)
![](/images/Java基础语法/20251211-40.png)

# 一、基础

## 1.

## 2.修饰符
public：公开的，可以在任何地方访问
	类的实例能够在任何地方被创建和访问或者编写的library库希望可以被开发者使用
default：默认，类的可见性为包级别，只能在同一个包中被访问
protect：修饰符的类可以被同一包中的其他类以及该类的子类访问（子类在那个包中都可以）
private：尽可以被同一个类中的其它类访问，通常用于嵌套类或者内部实现细节

## 3.数据类型
基本数据类型和引用数据类型
基本数据类型
	整型
		byte，short，long，int
	浮点型
		float，double
	字符型
		char
	布尔型
		boolean

## 4.变量
变量必须先声明，并指定数据类型，命名要遵循驼峰命名法

## 5.基本运算
算术运算符
	+、-、*、/、%
关系运算符
	==、!=、<、>、<=、>=
逻辑运算符
	&&、||、！

## 6.顺序结构
按照顺序来的代码

## 7.选择结构
if-else
if
switch

## 8.循环结构

## 9.数组

## 10.函数方法

## 11.异常处理
Java中的异常处理机制通过try,catch,finally来进行捕获和处理异常
异常分为检查异常和非检查异常

```java
public class ExceptionHandling{
	public static void main(String args[]){
		try{
			int result=10/0;//会发生Arithmetic异常

		}cathch(ArithmeticException e){
			System.out.println("cannot divide by zero");
		}finally{
			System.out.println("FINALLY BLOCK always zhixing");
		}
	}
}
```bash

如果try中发生异常就会跳转到catch模块进行处理
而finally模块无论异常是否发生都会进行执行，通常用于确保资源的处理和释放工作

# 二、面向对象

## 1.类

## 2.对象
类可以用来创建对象，而对象就是类的实例
实例化一个对象，就是使用关键字new来调用类的构造方法并未该对象分配内存空间

## 3.继承
继承：允许一个子类继承另一个父类的属性和方法，子类可以继承父类的行为并且可以添加新的属性和方法来进行扩展

## 4.封装
封装是将对象的内部状态和实现细节隐藏起来，之对外提供访问接口。java中通过访问修饰符public或者private等进行封装

## 5.构造函数
构造函数是一种特殊的方法，与类同名，没有返回类型，在对象被创建时调用，用于初始化操作
如果没有显式的定义构造函数，编译器会默认生成一个无参数的构造函数，将类的实例变量初始化为默认值，如果该类继承自父类，会调用父类的无参数构造函数

### 继承中的构造函数
默认情况：
	如果父类（基类）有一个无参数的构造函数，子类（派生类）会自动继承这个无参数构造函数。
	如果子类没有显式定义构造函数，编译器会默认生成一个无参数构造函数，并在其中调用父类的无 参数构造函数。

```
class Animal { // 父类有一个无参数构造函数 }

class Dog extends Animal { // 子类没有显式定义构造函数，编译器默认生成一个无参数构造函数 }
```

父类有有参数构造函数：
	如果父类只提供了有参数的构造函数，子类需要显式定义构造函数，并通过类构造函数。此时 super() 方法是必须的。

```java
class Animal {
	public Animal(String name) { // 父类有一个有参数构造函数 }
}

class Dog extends Animal {
	public Dog(String name, String breed)
	{
		super(name);
	}
	// 调用父类的有参数构造函数 // 初始化子类特有的属性
}
```

 子类提供无参数构造函数：
	 如果父类没有提供无参数构造函数，但子类需要使用无参数构造函数，子类需要显式提供无参数构 造函数，并通过 super() 调用适当的父类构造函数。此时 super() 方法是必须的。

```java
class Animal
{
	public Animal(String name)
	{ 父类有一个有参数构造函数 }
}
class Dog extends Animal
{
	public Dog()
	{ super("DefaultName");} // 子类提供无参数构造函数，并在其中调用父类构造函数
}
```java

## 6.重载
函数重载

```java
public class Calculator {
    // 重载方法
    public int add(int a, int b) {
        return a + b;
    }
    public double add(double a, double b) {
        return a + b;
    }
    public String add(String a, String b) {
        return a + b;
    }
}
public static void main(String[] args) {
    Calculator myCalculator = new Calculator();
    System.out.println(myCalculator.add(2, 3));
    System.out.println(myCalculator.add(2.5, 3.5));
    System.out.println(myCalculator.add("Hello", " World"));
}

```

构造函数重载

```java
public class Person {
    private String name;
    private int age;
    // 构造函数重载
    public Person() {
        this.name = "Unknown";
        this.age = 0;
    }
    public Person(String name) {
        this.name = name;
        this.age = 0;
    }
    public Person(String name, int age) {
    this.name = name;
    this.age = age;
    }
}
```

## 7.其他
1 HashMap
HashMap 是 Java 中常用的集合类之一，用于存储Key-Value键值对的集合。它实现了存储键值对。Map 接口，用于 HashMap 的核心思想是通过散列算法将键映射到存储桶，提高查找效率。基本操作的时间  复杂度为 O(1)。然而，需要注意HashMap 不是线程安全的，如果在多线程环境中使用，可以考虑使用 ConcurrentHashMap 。

```java
package org.example.javademo.demos.web.Study;

import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("1", "1");
        map.put("2", "2");
        map.put("3", "3");
        map.put("4", "4");

        int oneValue= Integer.parseInt(map.get("1"));
        System.out.printf("oneValue=%d\n", oneValue);

        for (Map.Entry<String, String> entry : map.entrySet()) {
            String key = entry.getKey();
            String value = entry.getValue();
            System.out.printf("key=%s, value=%s\n", key, value);
        }
    }
}
```

2 StringBuilder
StringBuilder 是 java.lang 包中的一个类，用于在单线程环境下对字符串进行可变操作，避免了使用 String 类时的不断创建新字符串的开销。它提供了一系列方法用于修改字符串内容，是一个可变字符序列。

```java
package org.example.javademo.demos.web.Study;

public class StringBuilderExample {
    public static void main(String[] args) {
        StringBuilder str = new StringBuilder();
        str.append("Hello World");
        System.out.println(str.toString());
        str.append("!");
        str.append("!");
        str.append("!");
        str.append("!");
        System.out.println(str.toString());
        str.insert(5,"beautiful");
        System.out.println(str.toString());
        str.replace(15,20,"jinlulu");
        System.out.println(str.toString());
        System.out.println(str.length());
        str.delete(21,22);
        System.out.println(str.toString());
    }
}
```

3 StringBuffer
StringBuffer 与StringBuilder 类似，也是可变的字符序列。主要区别在于是安全的，因此在多线程环境中更适用。然而，由于同步的开销，

```

```

4 IO 流
输入输出流（IO流）是 Java 中用于处理输入和输出的机制。它分为字节流和字符流，以及输入流和输出流。常见的 IO 类有 FileInputStream 、  FileOutputStream 、 BufferedReader 、BufferedWriter 可以进行文件读取，网络操作，缓冲操作读取字节流，对象序列化等操作，也是比较重要的

5 Object
Object 类是 Java 中所有类的根类，每个类都是 Object 类的子类。它定义了一些基本的方法，如toString、equals 和 hashCode。在 Java 中，所有对象都可以被赋值给 Object 类型的变量。

toString() 方法
	用于返回对象的字符串表示。默认情况下，toString()返回类名后跟对象的哈希码。
equals(Object obj)  方法：
	用于比较两个对象是否相等。默认实现是比较对象的引用地址，但通常在子类中会被重写以根据业务逻辑判断对象是否相等。
hashCode()方法：
    返回对象的哈希码。哈希码用于在哈希表等数据结构中快速查找对象。
getClass() 方法：
	返回对象的运行时类，即对象所属的类。
notify()  、  notifyAll()  和  wait()  方法：
	用于线程间的协调和通信。这些方法通常与多线程编程有关，用于实现线程的等待和唤醒机制。
finalize()方法：
	在垃圾回收器清理对象之前调用。子类可以重写此方法以执行资源清理等操作
clone() 方法:
	创建并返回一个对象的副本。默认情况下，clone()方法执行的是浅拷贝，但可以在子类中重写以实现深拷贝。
