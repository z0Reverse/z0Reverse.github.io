---
title: 分层思想和MVC
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - Java基础
tags:
  - Java
  - JavaWeb
  - 基础
---

# Java分层思想
主要层次
表现层（Presentation Layer）：
	主要负责与用户交互，处理用户界面和用户输入输出。在 Java 中， 通常由 Servlet、JSP、或者更现代的框架如 Spring MVC 负责、或者 Springboot 下的 Controller 层。
业务层（Business Layer）：
	业务层包含应用程序的业务逻辑，处理业务规则和数据处理。这一层通常 由 JavaBean、Service 等组成，负责执行具体的业务操作。
服务层（Service Layer）：
	服务层是业务层的一部分，提供业务逻辑的具体实现。在 Spring 框架中， 使用 @Service 注解来表示服务层。
持久层（Persistence Layer）：
	持久层负责数据的持久化，通常与数据库交互。在 Java 中，常见的持 久层技术包括 JDBC、Hibernate、MyBatis 等。
数据访问层（Data Access Layer）：
	这一层是持久层的一部分，负责封装数据访问细节，提供统一的 接口给业务层。通常由 DAO（Data Access Object）组成

# Java MVC 模式
MVC 即模型（Model） 、视图（View）、控制器（Controller）。
MVC（Model-View-Controller）是一种软件架构模式，用于设计和组织代码。它将一个应用程序分为三 个主要组件：模型（Model）、视图（View）和控制器（Controller）。每个组件有不同的责任，以实现 代码的分离和模块化，以便更容易维护和扩展应用程序。 通俗来说，各司其职高效完成任务。
模型（Model）
	模型是用于处理数据逻辑的部分。 所谓数据逻辑，也就是数据的映射以及对数据的增删改查，Bean、DAO（data access object，数据访 问对象）等都属于模型部分。
视图（View）
	视图负责数据与其它信息的显示，也就是给用户看到的页面。 html、JSP 等页面都可以作为视图。
控制器（controller）
	控制器是模型与视图之间的桥梁，控制着数据与用户的交互。 控制器通常负责从视图读取数据，处理用户输入，并向模型发送数据，也可以从模型中读取数据，再发 送给视图，由视图显示。
#RBAC项目
