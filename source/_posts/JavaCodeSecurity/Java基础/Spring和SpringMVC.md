---
title: Spring和SpringMVC
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

# Spring
一个Java开源框架接口，其核心框架是SpringFramework，在此基础上衍生的SpringBoot，SpringCloud，SpringData，SpringSecurity等

# SpringMVC
 SpringMVC是spring基础上的一个mvc框架，基于模型-视图-控制器模式进行javaweb的狂发
 基于spring功能上添加的web框架，想使用springmvc必须先以来
 spring

# MVC
一种框架模式
model
	处理数据逻辑部分
	也就是数据的映射，数据的增删改查。Bean，Dao等
view
	给用户展示的地方
controller
	魔图与数据之间的交互
	从视图获取数据，进行处理，并向模型发送数据。也可以从模型获取数据发送给视图

## springmvc核心框架
![](/images/Spring和SpringMVC/20251211-23.png)
Spring MVC 框架中， DispatcherServlet 、 HandlerMapping 和 HandlerAdapter 是三个重要的组件，它们各自承担不同的角色，协同工作以处理客户端的请求并调度相应的处理程序DispatcherServlet（调度器Servlet）：
	DispatcherServlet 是 Spring MVC 中的前端控制器（Front Controller），负责接收客户 端的所有请求并将其分派给适当的处理程序（Controller）。
	当客户端发送请求时， DispatcherServlet 接收请求，然后根据配置和规则找到合适的 HandlerMapping 来确定请求对应的处理程序。一旦找到处理程序， 交给该处理程序进行处理。它还负责处理异常、视图解析和其他与请求生命周期相关的任务。
HandlerMapping（处理程序映射）：
	HandlerMapping 负责将请求映射到相应的处理程序（Controller）。它确定了客户端请求 应该由哪个处理程序来处理。
	在 Spring MVC 中，可以有多个 HandlerMapping 实现，包括基于注解的映射、基于路径 的映射等。 HandlerMapping 将请求的 URL 映射到具体的控制器类和方法，以便 DispatcherServlet 可以将请求分发给正确的处理程序。
HandlerAdapter（处理程序适配器）
	HandlerAdapter 负责调用实际的处理程序（Controller）来处理请求，并将处理程序的执 行结果返回给 DispatcherServlet 。
	不同的处理程序可能有不同的接口， HandlerAdapter 的作用是适配各种不同类型的处理 程序，使得它们能够被 DispatcherServlet 统一调用。它将请求传递给处理程序，处理程序执行 后， HandlerAdapter 还负责处理返回的结果，如视图解析、数据绑定等。
 DispatcherServlet 充当总管， 负责找到处理程序，而 HandlerMapping HandlerAdapter 则负责调用实际的处理程序执行业务逻辑。这种设计使得 Spring MVC 具有灵活性，允许通过配置来适应不同的业务需求和处理程序类型。

（跟着凯涛学springmvc）

## spring项目

spring项目了解
某汽车租赁系统 mybatis+spring+mvc
1.看下pom中依赖是否加载完成
2.看代码，如果src下还存在xxx。java代表还没有编译好，编译好就会显示为class

#审计思路
1.pom中看版本是否存在cve
2.看web.xml配备的映射关系
![](/images/Spring和SpringMVC/20251211-24.png)
可以看到配置的serlvet策略，该框架是mvc框架，定义的规则url均走springmvc这个serlvet，根据这个servletname一年关涉到上面的springMvc并且知道了他的servletclass为servlet.DispatcherServlet，这个也即是springmvc框架的核心

3.resource下面的各种配置文件
resource/mapper下面一些配置文件：eg：mybatis的mapper.xml文件配置sql执行语句

4,正向审计
根据api dispatcherservlet经过处理后定位到具体的control实现，根据实现找到service层（一般是接口，找到及具体实现）对于方法的实现，再往下就是mapper--->dao层的数据操作
control定位到service
![](/images/Spring和SpringMVC/20251211-25.png)
跟进之后发现carservice的load方法啊是一个接口，继续跟进找到该方法的实现
![](/images/Spring和SpringMVC/20251211-29.png)

到了这里，该方法返回一个新的对象dataGridView对象，包括视图和数据，这里需要定位list数据
> 图片缺失：Pasted image 20251211012915.png （原文件未随笔记一起复制，请补充后删除本行提示）
继续根据mapper
到了CarMapper中的loadAllCar
![](/images/Spring和SpringMVC/20251211-28.png)
分析对应xml文件映射中loadAllCar的操作
![](/images/Spring和SpringMVC/20251211-27.png)
这个一般会设置的跟mapper名字一样的xml文件
具体去看代码部分
![](/images/Spring和SpringMVC/20251211-26.png)
可以看到实现的sql语句，然后进行判断是否存在sql诸如即可
