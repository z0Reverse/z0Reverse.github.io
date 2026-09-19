---
title: XSS
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - JavaWeb安全基础
tags:
  - JavaWeb
  - 漏洞利用
---

使用request.setAttribute方法将请求到的数据未经过滤存储到request域中，然后在jsp页面里使用el表达式进行输出

示例代码
selvet.java

```java
@WebServlet("/demo")
public class xssServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doGet(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        response.setContentType("text/html");// 设置响应类型
        String content = request.getParameter("content");  //获取content传参数据
        request.setAttribute("content", content);  //content共享到request域
        request.getRequestDispatcher("/WEB-INF/pages/xss.jsp").forward(request, response);  //转发到xxs.jsp页面中

    }
}
```

jsp

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    ${requestScope.content}
</head>
<body>

</body>
</html>
```
