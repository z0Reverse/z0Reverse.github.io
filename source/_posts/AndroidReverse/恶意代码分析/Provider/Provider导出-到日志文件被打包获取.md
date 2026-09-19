---
title: Provider导出 到日志文件被打包获取
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - 恶意代码分析
tags:
  - Provider
  - 组件安全
---

## 利用链：
任意App -> HLogSdkProvider.call -> ProcessBridgeProvider.call -> Dispatcher.m74904a -> HLogSdkServiceModule$Dispatcher.dispatch -> HLogSdkServiceModule.requestLogFile -> LogFileTransmitter.getGrantFileUri -> 权限授予并返回URI -> 攻击者成功读取文件。

## 代码分析：
发现存在Provider导出
![](/images/Provider导出-到日志文件被打包获取/20260419141049.png)
![](/images/Provider导出-到日志文件被打包获取/20260419141058.png)
继承于ProcessBridgeProvider。这个Provider里面只实现了自定义的call方法，其他方法并没有使用
![](/images/Provider导出-到日志文件被打包获取/20260419141106.png)
![](/images/Provider导出-到日志文件被打包获取/20260419141116.png)
分析call方法
![](/images/Provider导出-到日志文件被打包获取/20260419141125.png)
整个流程：从传递的bundle，设置其反序列化的类以及从bundle中提取目标类用于去做反射或者其他操作。然后匹配str是否满足dispatch。满足后跳转到后面的分支
![](/images/Provider导出-到日志文件被打包获取/20260419141135.png)
或者上下文和调用provider的包名，但是没有做判断。接着加载拦截器it2，其拦截器来园区c的CopyOnWriterArrayList，但是这个为空

也就是拦截器不起作用，可以直接跳过进入下一部
![](/images/Provider导出-到日志文件被打包获取/20260419141159.png)
直接去看这个方法：
创建一个buidler添加字符串“dispatch+str+targetClassName+str2+methid+i10
这里调用IDispatcher---调度器
![](/images/Provider导出-到日志文件被打包获取/20260419141211.png)
在打印完后直接使用调度器实例化一个对象，这个对象经过查看在HLogSdkServiceModule$Dispatcher初始化的时候会进行赋值，而这个str2其实是ProcessBrigeProvide中传递过来的targetClassName，这个值是可控的bundle中的
![](/images/Provider导出-到日志文件被打包获取/20260419141230.png)
![](/images/Provider导出-到日志文件被打包获取/20260419141241.png)
所以当我们篡改bundle中的targetClassName满足条件会进入判断分支，从而走到这里
![](/images/Provider导出-到日志文件被打包获取/20260419141246.png)
到这里后对i10进行判断，这个i10追溯上去也就是processbrigeprovider的里面从bundle提取的methodid
![](/images/Provider导出-到日志文件被打包获取/20260419141257.png)
可以根据代码看到i10=1或者objArr的长度为1，会有执行操作。
这里先去看i10=1，进入的HLogSdkServiceModule的requestLogFile方法
![](/images/Provider导出-到日志文件被打包获取/20260419141313.png)
最主要的是走到下面然后去执行LogFileTransmitter的getSalvageLogFileToTransmit方法
![](/images/Provider导出-到日志文件被打包获取/20260419141322.png)
![](/images/Provider导出-到日志文件被打包获取/20260419141336.png)
getSalvageLogFileToTransmit方法中，传递到granteKitUploadZipFils方法的时候，，有个参数是a类返回的值，去查看LogFileTransmitter类中静态内部类a
![](/images/Provider导出-到日志文件被打包获取/20260419141342.png)
可以看到当onZipOk的时候会生成文件的uri
![](/images/Provider导出-到日志文件被打包获取/20260419141354.png)
到这里其实也就可以啦。我们继续深入：

A类实现onzipok后，logFileGrantListener.onGrantSuc回调会去就到HLogSdkServiceModule的内部类 a 的 onGrantSuc
![](/images/Provider导出-到日志文件被打包获取/20260419141405.png)

## 攻击者实现：
