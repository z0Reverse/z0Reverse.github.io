---
title: Servlet 过滤器 拦截器 监听器
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

# 一、Serlvet
serlvet运行在web服务器或者应用服务器上的程序，作为来自web浏览器或者其他http客户端的请求跟http服务器上的数据库（或者应用程序）的中间层

## 生命周期
	init：初始化阶段
	service：服务阶段，主要用于处理来自客户端的请求
	doGet，doPost：处理阶段
	destory：销毁阶段

## 创建一个Serlvet项目

### 配置
1.双击启动 IDEA，点击 File -> Close Project，左侧选择 Create New Project（如果默认进入某个项目，需要退出，点击左上角 Maven 项目，选中 archetype-webapp ，点击Next，如下图所示
![](/images/Servlet-过滤器-拦截器-监听器/20251211-42.png)

2.在 pom.xml 中引入 servlet 依赖，写在 标签内，然后可以点击右上角 的按钮（也就是重新加载安装依赖），如下图所示：

```
<dependencies>
    <dependency>
	    <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.1.0</version>
    </dependency>
</dependencies>

```

3.配置tomcat
	tomcat下载好之后，选择当前文件配置-添加tomcat服务器-本地
![](/images/Servlet-过滤器-拦截器-监听器/20251211-43.png)
	在Server标签下配置应用服务器程序，去配置tomcat本地环境
	![](/images/Servlet-过滤器-拦截器-监听器/20251211-44.png)
	配置部署方式，点击Deployment标签，点击+按钮，选择war explorded方式；应用上下文设置即url根路径，一般/就行【这个地方创建工件是不同滴，两种形式】
	![](/images/Servlet-过滤器-拦截器-监听器/20251211-45.png)
	![](/images/Servlet-过滤器-拦截器-监听器/20251211-46.png)
	![](/images/Servlet-过滤器-拦截器-监听器/20251211-47.png)

	在配置的时候如果发现没有工件，点击 文件-项目结构-工件-点击添加选择web应用程序（看哪个有基于模块的，点击即可），一般代码编写后就会有，可以进行选择

### 编写代码Serlvet

#### FirstServlet代码

```java
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class FirstServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doGet(req, resp);
        //设置响应的内容形式
        resp.setContentType("text/html");
        //设置输出内容
        PrintWriter out = resp.getWriter();
        out.println("<h1>Hello World</h1>");
    }
}
```bash

#### 配置web.xml文件用于映射
映射匹配流程： /FirstServlet 路径绑定的 Servlet-name为FirstServlet ，而 class是FirstServlet ，最终访问 FirstServlet绑定的 /FirstServlet ，调用的类也就是 FirstServlet.class 。
![](/images/Servlet-过滤器-拦截器-监听器/20251211-48.png)

#### serlvet3之后的注释映射
可以通过@WebSerlvet("/xxx")进行映射
![](/images/Servlet-过滤器-拦截器-监听器/20251211-49.png)

### 运行
![](/images/Servlet-过滤器-拦截器-监听器/20251211-50.png)

# 二、过滤器，监听器
过滤器Filter：主要用于过滤字符编码，通常做一些统一的业务，采用javax.servlet.Filter接口实现。在代码中常用于防止xss，sql，文件上传等，在配置了filter之后可以统一过滤一些危险字符
监听器Listener：主要用于做一些初始化的内容，采用javax.servlet.ServletContextListener接口实现。同时存在监听器和过滤器，监听器在过滤器之前执行
拦截器Intrceptor：依赖web框架，在springmvc中依赖SpringMVC框架，属于面向切面变成的一种应用

过滤器，拦截器的区分：
	过滤器基于函数回调，拦截器基于java反射
	过滤器依赖Servlet容器，拦截器不依赖
	过滤器可以对几乎所有请求起作用，二拦截器只能对action请求有作用
	拦截器可以访问action上下文，值栈里面的对象；过滤器不能
	action的生命周期中，拦截器可以多次调用，过滤器只能在容器初始化的时候调用一次

## 过滤器代码实现

```java
package com.test.filter;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class FilterTest implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {

    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;
        //首先通过
        //String requestURI = request.getRequestURI();获取URL路径。然后对路径进行判断，
        //如果路径中包含
        ///FirstServlet ，则放行,否则跳转到根目录下
        String uri = request.getRequestURI();
        if(uri.contains("/FirstServlet")){
            filterChain.doFilter(request, response);
        }else {
            request.getRequestDispatcher("/").forward(request, response);
        }
    }

    @Override
    public void destroy() {

    }
}
```

根据代码逻辑：如果访问的api接口不是firstservlet的话，将会被重定向到根目录，就会访问到index.jsp页面，如果是firstservlet的话就是导航到fristservlet的输出
![](/images/Servlet-过滤器-拦截器-监听器/20251211-51.png)
