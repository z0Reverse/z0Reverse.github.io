---
title: FastJson总结
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - 中间件
tags:
  - FastJson
  - 反序列化
  - 中间件
---

## 序列化、反序列化介绍

## 原生反序列化和FastJson反序列化的不同

### 原生反序列化
JDK的原生反序列化，主要依赖java.io.Serializable，在定义User类的时候需要进行继承
![](/images/FastJson总结/20260726013842.png)
在这个时候，通常会写readObject回调，从而获取完整的User对象（非必须）
一般都是在这里产生的漏洞，因为在解析的时候Json.readObject会先去检查有没有重写readObject，有的话进行执行，没有的就默认的。所以如果User类重写了readObject方法，且方法中有危险行为，就会导致反序列化漏洞的产生
![](/images/FastJson总结/20260726013825.png)
当readObject方法存在危险行为，那么对于数据进行反序列化解析的时候
![](/images/FastJson总结/20260726014715.png)
![](/images/FastJson总结/20260726014735.png)
当然实际上开发自己写的readObject肯定是不会直接就在里面进行一些危险操作
**真正的攻击链条应该是这样的：**
服务端 Classpath 中存在某些第三方库（如 commons-collections）。 这些库中的某个类（如 Transformer）的 readObject() 方法存在可利用逻辑（可通过反射调用任意方法）。 攻击者序列化时，不是传 User 对象，而是传一个 由这些危险类组合而成的调用链（通过反射构造，将 Runtime.exec 挂在链条末端）。 服务端反序列化时，readObject() 层层嵌套调用，最终执行命令。 所以，User类在这里只是充当了一个“包裹”或“入口”，真正的恶意逻辑藏在它引用的其他类里。但是，触发时机和readObject()的调用机制是完全一样的。

### FastJson反序列化

## FastJson反序列化目前两个方向

### 1.2.83之前

### 1.2.83版本

## FastJson反序列化代码审计

### 1.2.83之前的版本xxxx

### 1.2.83版本

## FastJson反序列化历史版本梳理
