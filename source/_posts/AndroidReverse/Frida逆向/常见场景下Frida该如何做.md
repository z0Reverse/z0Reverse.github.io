---
title: 常见场景下Frida该如何做
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - Frida逆向
tags:
  - Frida
  - Hook
  - 动态调试
---

Java层：
对于ACTIVITY
由于都会在内存中注册，所以去hook的时候关注是否被调用初始化
有初始化的
	对于其静态或动态注册的方法，直接Java.use
	对于变量，直接使用+value即可
未主动或被动调用的
	使用Java.choose直接调该ACTIVITY

对于类
有初始化的
	对于其静态或动态注册的方法，直接Java.use
	对于变量，直接使用+value即可
未主动或被动调用的
	使用使用Java.use先获取该类示例
	在进行new重新创建对象

SO层
	静态注册函数
		导出：
			直接Process.getModuleByName.enumerateExports,获取地址后Interceptor。attach
		不导出：
			不导出但是有被用到
				需要主动去调用，找到方法的开始---找偏移地址--偏移地址+基地址进行attach
			不导出未被用到
				需要找到地址后，使用NativeFunction进行主动调用，类似于new
		动态注册函数
			需要关注JNI_ONload和RegisterNative，这两个是动态函数注册的关键，一般去看Register就可以，其关联java层函数和native层函数的映射关系，根据这个找到地址再去hook就可以
