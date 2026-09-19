---
title: SpringBoot和SpringCloud
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

# SpringBoot
简化spring应用搭建和开发流程
自动装配
	依赖管理： Spring Boot 通过 Maven 或 Gradle 等构建工具，引入了一系列默认的依赖项，以简化项目 的搭建。例如，通过添加 spring-boot-starter-web 依赖，你就能够使用Spring MVC来构建Web应 用。
	类路径扫描： Spring Boot会自动扫描项目中的特定包及其子包，寻找标有特殊注解的类，比如 @Controller 、 @Service 、 @Repository 等，然后将它们注册为Spring的组件。
	默认配置： Spring Boot 提供了大量的默认配置，当没有显式配置时，这些默认配置会自动应用。例如，如果项目中引入了数据库相关的依赖，Spring Boot 会根据类路径上的数据库驱动自动配置数据源。
	条件化装配： Spring Boot 引入了条件化装配的概念，根据类路径上的特定条件来决定是否启用某些配 置。这使得可以根据不同的环境或条件来自动装配不同的组件。
	Spring Boot Starter： Spring Boot 提供了一系列的 Starter 依赖，这些 Starter 提供了一组常用的依 赖项的整合，比如 spring-boot-starter-data-jpa 、 spring-boot-starter-security 等，它们能够一次性地引入一组相关的依赖和配置，简化了开发者的工作。
	自定义Starter： 除了 Spring Boot 提供的 Starter 之外，开发者也可以创建自己的 Starter，将一组相关的依赖和配置封装起来，使得它们能够在不同的项目中被重复使用。
	自动化配置类： Spring Boot通过自动化配置类来实现自动装配。这些配置类使用@Configuration 注解 标记，并且通常包含有 @ConditionalOn... 注解，用于指定生效的条件。
总体来说，Spring Boot通过一系列约定、默认配置、条件化装配等方式，实现了自动装配，使得开发者 能够更加方便地构建和配置项目

SpringBoot项目一般会存在一个以项目名+Application为名字的类，该类为整个springboot项目的入口
SpringBoot项目的Controller类中的注解
	@Controller 注解：标注该类为controller类，可以处理 http 请求。@Controller 一般要配合模版来使用。现在项目大多是前后端分离，后端处理请求，然后返回JSON格式数据即可，这样也就不需要模板了。
	@ResponseBody 注解：将该注解写在类的外面，表示这个类所有方法的返回的数据直接给浏览器。
	@RestController 相当于 @ResponseBody 加上 @Controller
	@RequestMapping 注解：配置 URL映射，可以作用于某个Controller类上，也可以作用于某Controller 类下的具体方法中，说白了就是URL中请求路径会直接映射到具体方法中执行代码逻辑。
	@RequestParam 注解：将请求参数绑定到你控制器的方法参数上（是springmvc中接收普通参数的注 解），常用于POST请求处理表单
	 @PathVariable 注解：接受请求URL路径中占位符的值，示例代码如下图所示：

```java
@Controller
@ResponseBody
@RequestMapping("/hello")
public class HelloController { @RequestMapping("/whoami/{name}/{sex}")
	public String hello(@PathVariable("name") String name, @PathVariable("sex") String sex){
	return "Hello" + name + sex;
	}
}
```bash

# SpringCloud
是一系列框架的有序集合。是一套基于 Spring Framework 的分布式系统开发工具，用于构建分布式应用程序中的各种模块化组件件。
它利用 Spring Boot 的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中 心、消息总线、负载均衡、断路器、数据监控等，都可以用 Spring Boot 的开发风格做到一键启动和部 署。
Spring Cloud 的诞生并不是为了解决微服务中的某一个问题，而是提供了一套解决微服务架构实施的综合性解决方案

微服务（英语：Microservices）是一种软件架构风格，它是以专注于单一责任与功能的小型功能区块 (Small Building Blocks) 为基础，利用模块化的方式组合出复杂的大型应用程序，各功能区块使用与语言 无关的API集相互通信。

ruoyi项目：https://gitee.com/y_project/RuoYi-Cloud
	每一个模块对应一个微服务，每个模块的实现又是类似于springboot的mvc模式实现
