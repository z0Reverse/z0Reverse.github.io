---
title: Binder远程调用实现rce
date: 2026-09-20 02:16:39
categories:
  - AndroidReverse
  - 恶意代码分析
tags:
  - Service
  - Binder
  - IPC
---

## 简介：
Service有两种实现：一、本地intent进行通讯；二、远程通过Binder实现通讯，这个时候本地Service充当Binder的服务端，如果有跟客户端B的通讯，发起请求，此时他也会充当客户端（Binder的通讯是相互的）
远程Binder调用，需要实现：1、根据服务端的Binder，建立链接；2、根据服务端的Binder接受调度，进行构造数据；3、如果服务端也有对应的请求到客户端，客户端需要实现对应的接受Binder的处理机制
**Service的Binder远程双向通信**
![](/images/Binder远程调用实现rce/20260419141950.png)

## 利用链：
宿主绑定动态进程的Service，得到`PpsBinder`代理。
宿主调用`PpsBinder.transact(3, ...)`，将自己的`UuidManager` Binder传给动态进程。
动态进程保存该Binder代理，包装为`BinderUuidManager`。
宿主调用`PpsBinder.transact(1, loadRuntime)`。
动态进程收到后，调用`mUuidManager.getRuntime()` → 通过Binder代理调用宿主的`UuidManager.onTransact`。
宿主返回`InstalledApk`（APK路径）。
动态进程加载该APK。
![](/images/Binder远程调用实现rce/20260419142033.png)

## 漏洞分析：
![](/images/Binder远程调用实现rce/20260419142112.png)
Service组件导出，这里直接分析PluginProcessPPS
![](/images/Binder远程调用实现rce/20260419142117.png)Service一般启动有两种：
	1、 onStart、onStartCommond
	2、 远程的就是注册Binder服务，onBinder绑定返回
![](/images/Binder远程调用实现rce/20260419142134.png)

可以看到返回一个IBinder服务
![](/images/Binder远程调用实现rce/20260419142152.png)
通过定位IBinder服务的类，直接去看实现
可以看到PpsBinder实现onTract会根据传递的i10执行不同方法
![](/images/Binder远程调用实现rce/20260419142203.png)

这里以loadRuntime进行分析
parcel.enforceInterface(DESCRIPTOR);
这个起到校验作用，校验binder中客户端发来的数据是否是descriptor的。这个地方descriptor也就是**com.tencent.shadow.dynamic.host. PpsBinder**
然后获取binder中传递过来的字符串，跳转loadRuntime方法

![](/images/Binder远程调用实现rce/20260419142220.png)

简单分析发现需要走到try里面需要先走checkUuidManagerNotNull方法

![](/images/Binder远程调用实现rce/20260419142233.png)

Check方法会检测uuidmanager是否为空，根据其定义的类去看哪里有赋值
![](/images/Binder远程调用实现rce/20260419142237.png)

可以定位到serUuidManager中
![](/images/Binder远程调用实现rce/20260419142246.png)
![](/images/Binder远程调用实现rce/20260419142251.png)
且该方法刚好是onTract中case=3的是偶执行
![](/images/Binder远程调用实现rce/20260419142313.png)

所以考虑，客户端绑定服务后限制性case=3，在设置完uuid后在执行case=1
继续分析loadRuntime方法
InstalledApk对象实例化，是uuidManager的getRuntime方法，通过定位uuidManager的实现类，定位到BinderUuidManager类

![](/images/Binder远程调用实现rce/20260419142323.png)

![](/images/Binder远程调用实现rce/20260419142333.png)
其实这个类会在i10=3被设置uuid的时候就调用了，也从侧面说明先执行设置uuid才会进行下面的
![](/images/Binder远程调用实现rce/20260419142341.png)

这段代码实现：创建连个parcel用于传递数据。在parcelObtain中写入token用于binder身份校验，写入uuid。然后发起binder事务

```
checkException(parcelObtain2);

_// 6._ _读取响应：先读一个_ _int_ _标志，非_ _0_ _表示有_ _InstalledApk_ _对象，然后调用_ _CREATOR_ _从_ _Parcel_ _中重建对象_

return parcelObtain2.readInt() != 0 ? InstalledApk.CREATOR.createFromParcel(parcelObtain2) : null;
```

去看InstalldeApk类
![](/images/Binder远程调用实现rce/20260419142423.png)

对应的去看createFromParcel方法，然后再走到InstalledApk的重构方法中parcel类型数据的方法

![](/images/Binder远程调用实现rce/20260419142435.png)

也就是从parcel中获取apkFilePath、oDexPath、libraryPath、和一个整数

因为构造函数本身就是用来初始化对象的。它从 `Parcel` 中读取之前写入的字（`apkFilePath`, `oDexPath`, `libraryPath` 等），然后赋值给当前对象的成员变量。

在代理的 `getRuntime` 中，`CREATOR.createFromParcel(parcelObtain2)` 内部会调用这个构造函数，返回一个新的 `InstalledApk` 实例就到了InstalledApk runtime = **this**.mUuidManager.getRuntime(str);runtime就是这个实例，用于下面的初始化

![](/images/Binder远程调用实现rce/20260419142446.png)

然后去看DynamicRuntime类的这两个方法

先去判断runtimeClassloader中是否存在该apkfilepath的加载记录，有的话就不加载，然后根据加载的是否相同进行选择覆盖

![](/images/Binder远程调用实现rce/20260419142453.png)

没有的话直接
![](/images/Binder远程调用实现rce/20260419142503.png)

## 恶意实现：
