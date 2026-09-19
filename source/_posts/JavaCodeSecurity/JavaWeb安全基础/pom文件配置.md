---
title: pom文件配置
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - JavaWeb安全基础
tags:
  - JavaWeb
  - 漏洞利用
---

项目基本信息

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
	    <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.4.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.kalvin</groupId>
	<artifactId>kvf</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>kvf-admin</name>
	<packaging>jar</packaging>
	<description>Demo project for Spring Boot</description>
```

dependencies：直接声明的依赖项
dependencyManagement：集中管理依赖版本

properties：项目定义属性
	重点关注是否存在敏感信息硬编码
	不安全的配置参数

```
<properties> <java.version>1.8</java.version> <spring-boot.version>2.2.4.RELEASE</spring-boot.version> <!-- 其他组件版本定义 --> </properties>
```

profiles：属性定义

```
<profiles> <profile> <id>dev</id> <properties> <activeProfile>dev</activeProfile> </properties> <activation> <activeByDefault>true</activeByDefault> </activation> </profile> <!-- 其他环境配置 --> </profiles>
```

build和plugins：构建和打包配置
	代码混淆，加密插件
	远程部署插件的配置
	自定义插件可能存在的安全风险

```
<build> <plugins> <plugin> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-maven-plugin</artifactId> </plugin> <!-- 其他插件 --> </plugins> </build>
```
