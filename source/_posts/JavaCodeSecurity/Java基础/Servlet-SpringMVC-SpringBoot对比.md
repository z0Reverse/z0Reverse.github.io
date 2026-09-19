---
title: Servlet SpringMVC SpringBoot对比
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

# Servlet

## 介绍
Servlet 是 JavaEE 规范中定义的 Web 组件标准，用于处理客户端请求并生成响应。它是运行在 Web 容器（如 Tomcat）中的 Java 类，通过实现 `javax.servlet.Servlet` 接口来处理 HTTP 请求。

## 作用：
- 接收浏览器请求（如 HTTP 请求），处理业务逻辑并返回响应（如 HTML、JSON 等）。
- 是早期 Java Web 开发的基础，所有 Java Web 框架（包括 SpringMVC）都基于 Servlet 规范实现。

## 代码
需要手动创建Servlet类并配置web.xml或者注解

```java
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

// 使用注解配置 Servlet，等价于在 web.xml 中配置
@WebServlet("/servlet")
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        // 1. 获取请求参数
        String name = req.getParameter("name");
        name = name == null ? "World" : name;

        // 2. 设置响应内容类型
        resp.setContentType("text/plain");
        resp.setCharacterEncoding("UTF-8");

        // 3. 返回响应
        resp.getWriter().write("Hello, " + name + "! (From Servlet)");
    }
}
```bash

## 运行方式
打包为war文件，部署到tomcat等servlet容器

# SpringMVC

## 介绍
SpringMVC 是 Spring 框架中处理 Web 层请求的模块，实现了 MVC 设计模式，替代传统 Servlet 开发。
**核心组件**：
- **DispatcherServlet**：中央控制器，接收所有请求并分发到对应处理器。
- **Controller**：处理请求并返回数据（如 `@Controller` 注解标注的类）。
- **ViewResolver**：将控制器返回的逻辑视图解析为物理视图（如 JSP、Thymeleaf 页面）。

## 代码
配置SpringMVC容器，创建Controller处理请求

```java
// 1. 配置 DispatcherServlet（web.xml 或 Java 配置）
// 以下是 Java 配置方式
public class WebAppInitializer implements WebApplicationInitializer {
    @Override
    public void onStartup(ServletContext servletContext) {
        AnnotationConfigWebApplicationContext context = new AnnotationConfigWebApplicationContext();
        context.register(WebConfig.class);

        DispatcherServlet dispatcherServlet = new DispatcherServlet(context);
        ServletRegistration.Dynamic registration = servletContext.addServlet("dispatcher", dispatcherServlet);
        registration.setLoadOnStartup(1);
        registration.addMapping("/");
    }
}

// 2. 配置 SpringMVC（WebConfig.java）
@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.example.controller")
public class WebConfig implements WebMvcConfigurer {
    // 视图解析器配置（如果需要返回页面）
    @Override
    public void configureViewResolvers(ViewResolverRegistry registry) {
        registry.jsp("/WEB-INF/views/", ".jsp");
    }
}

// 3. 创建 Controller 处理请求
@Controller
@RequestMapping("/springmvc")
public class HelloController {

    @GetMapping
    @ResponseBody  // 返回 JSON 或文本，而非视图
    public String sayHello(@RequestParam(required = false) String name) {
        name = name == null ? "World" : name;
        return "Hello, " + name + "! (From SpringMVC)";
    }
}
```bash

## 运行方式
打包为war，部署到Servlet容器

# SpringBoot

## 介绍
SpringBoot 是基于 Spring 的快速开发框架，通过 “约定大于配置” 的理念，自动配置项目依赖和环境，减少手动配置工作量。
**核心特性**：
- **自动配置**：根据依赖自动配置 Spring 容器（如添加 `spring-boot-starter-web` 自动配置 Web 环境）。
- **起步依赖（Starter）**：通过单一依赖引入整套功能（如 `spring-boot-starter-data-jpa` 包含 JPA 相关所有依赖）。
- **内嵌容器**：可直接打包为 jar 并内嵌 Tomcat、Jetty 等容器，无需手动部署到 Web 服务器

## 代码
使用SpringBoot自动配置，直接编写Controller

```java
// 1. 主应用类（自动扫描 @Controller、@Service 等组件）
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

// 2. 创建 Controller（无需额外配置）
@RestController  // 等价于 @Controller + @ResponseBody@RequestMapping("/springboot")
public class HelloController {

    @GetMapping
    public String sayHello(@RequestParam(required = false) String name) {
        name = name == null ? "World" : name;
        return "Hello, " + name + "! (From SpringBoot)";
    }
}
```bash

## 运行方式
添加Maven依赖
直接运行Application.main方法

# SpringCloud
SpringCloud 是基于 SpringBoot 的微服务框架集合，提供服务注册与发现、负载均衡、配置中心等组件，用于构建分布式系统。
**核心组件**：
- **Eureka/Consul/Nacos**：服务注册与发现，让微服务之间可互相访问。
- **Ribbon/Feign**：客户端负载均衡，实现服务调用的流量分配。
- **Hystrix/Sentinel**：服务熔断与限流，防止级联故障。
- **Config**：分布式配置中心，统一管理微服务配置。
SpringCloud 基于 SpringBoot 构建，需先掌握 SpringBoot 才能使用其功能。

# 关系及区分
![](/images/Servlet-SpringMVC-SpringBoot对比/20251211-1.png)
