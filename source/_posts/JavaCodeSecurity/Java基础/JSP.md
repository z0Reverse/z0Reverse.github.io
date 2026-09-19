---
title: JSP
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

# 一、什么是 JSP
JSP 全称 Java Server Page，基于 Java 语言，是一种动态网页技术。

它使用JSP标签在 HTML 网页中插入 Java 代码。标签通常以 <% code %>显示。

JSP 本质是简化版的 Servlet，JSP 在编译后就变成Servlet。JVM 只能识别 Java 的类，是无法识别 JSP 代码的。所以WEB 服务器会将 JSP 编译成 JVM 能识别的 Java类。

JSP 跟 Servlet 区别：JSP 常用于动态页面显示，Servlet 常用于逻辑控制。在代码中常使用 JSP 做前端动态页面，在接收到用户输入后交给对应的 Servlet 进行处理。当然 JSP 也可以当做后端代码进行逻辑控制。

# 二、JSP 基础知识
 1、JSP 文件后缀名为 *.jsp
 2、JSP 代码需要写在指定的标签之中

```
 常用：
 <%
 out.println("hellpo JSP!");
 %>

 <jsp:scriptlet>
 代码片段
 </jsp:scriplet>

```

   3、JSP 生命周期：
   编译阶段 -> 初始化阶段 -> 执行阶段 -> 销毁阶段，此处多了一个编译阶段，是将 JSP 编译成 Servlet 的阶段。 而这个阶段也是有三个步骤的： 解析 JSP 文件 -> 将 JSP 文件转为 Servlet -> 编译 Servlet。
  4、JSP 指令：
  是用来设置 JSP 整个页面属性的。格式为：

```
<%@ directive attribute="value" %>

jsp三种指令
<%@ page %> 定义网页的依赖属性，比如脚本语言，erro页面，缓存需求等

<%@ include %> 包含其他文件

<%@ taglib %> 引入标签库的定义
```

  5、JSP的九大内置对象（隐式对象）
  这九个对象，可以不用声明直接使用。

```
out javax.Servlet.jsp.JspWriter 页面输出

request  javax.Servlet.http.HttpServletRequest 获得用户请求

response javax.Servlet.http.HttpServletResponse 服务器向客户端的回应信息

config javax.Servlet.ServletConfig  服务器配置，可以取得初始化参数

session  javax.Servlet.http.HttpSession 保存用户的信息

application javax.Servlet.ServletContext 所有用户的共享信息

page java.lang.Object 之当前页面转换后的servlet类的实例

pageContext javax.Servlet.jsp.PageContext JSP的页面容器

exception java.lang.Throwable 表示jsp页面发生的错五，在错误页面中才起作用
```bash

# 三、JSP程序编写

## 1.简单的jsp展示
创建新项目-maven项目，选择webapp进行加载
![](/images/JSP/20251211-30.png)

## 2.logindemo
login.jsp根据用户输入采用get方法跳转到dologin.jsp中进行执行。dologin通过jsp定义好的request来获取前面传递过来的数据，并根据判断输入是否满足在本页面中respose写入success或者fail
（需要注意jsp中的java代码并不会在前端显示）
login.jsp

```
<%--
  Created by IntelliJ IDEA.  User: z0Reverse  Date: 2025/5/26  Time: 20:38  To change this template use File | Settings | File Templates.--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <title>user to register page</title>
</head>
<br>
<hr><br>登陆页面<br>
<form action="do_login.jsp" method="get">
    <br>    <h1>Please input your message:</h1>
    Name:<input type="text" name="username"><br>
    Pswd:<input type="password" name="password"><br>
    <br><br><br>    <input type="submit">    <input type="reset"><br>
</form>

</body>
</html>
```

do_login.jsp

```
<%--
  Created by IntelliJ IDEA.  User: z0Reverse  Date: 2025/5/26  Time: 20:38  To change this template use File | Settings | File Templates.--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Server to do the register page!</title>
</head>
<body>
<%
  String username=request.getParameter("username");
  String passwd=request.getParameter("password");
%>
<%
  if(username.equals("admin") && passwd.equals("password")){
    response.getWriter().write("success login");
  }else {
    response.getWriter().write("login fail");
  }
%>
</body>
</html>
```bash

# 四、jsp木马
前些年是jsp木马鼎盛时期，目前基本采用springboot框架，该框架不引入jsp解析，需要引入特定的以来才行

jsp木马又叫做jsp webshell
常见的webshell工具：
	冰蝎：https://github.com/rebeyond/Behinder
	蚂蚁剑：https://github.com/AntSwordProject
	哥斯拉：https://github.com/BeichenDream/Godzilla

JSP大码：
https://github.com/theralfbrown/WebShell-2/tree/master/jsp
该shell木马可以实现在网页中进行一些危险操作，种类很多，在本地中演示
（找不到了，回头可以看一下）

#哥斯拉等工具进行shell连接
