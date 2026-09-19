---
title: SpringBoot项目
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - 常见知识
tags:
  - 鉴权
  - SpringBoot
  - 框架
---

## 1、配置文件application.yml
配置文件一般会配置mysql等配置信息

```
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/hybrid_encryption?useSSL=false&serverTimezone=Asia/Shanghai&allowPublicKeyRetrieval=true&characterEncoding=utf8mb4
    driver-class-name: com.mysql.cj.jdbc.Driver
    username: root
    password: root
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: false
    database-platform: org.hibernate.dialect.MySQLDialect
  sql:
    init:
      mode: always
```

## 2、启动入口Application.java

## 3、打包部署
SpringBoot 部署服务器完整教程：分两种方式（内置 Tomcat / 外置 Tomcat）

### 1、Jar 包部署（内置 Tomcat，推荐）

#### 1、修改 pom.xml（无需改动，默认即可）
SpringBoot 父工程自带内置 tomcat 依赖，不用额外引入。

```
<!-- spring-boot-starter-web 自带内置Tomcat -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

#### 2. 打包项目

```bash
# 清理+打包
mvn clean package -Dmaven.test.skip=true

gradle clean build -x test
```

打包后在 `target/` 目录生成 `xxx.jar` 文件。

#### 3. 上传到服务器

工具：Xshell、FinalShell、宝塔、rz/sz、FTP

把 jar 上传到服务器任意目录，例如 `/home/project/demo.jar`

#### 4. 服务器运行（Linux 为例）

##### 临时启动（关闭终端程序就停止，测试用）

```
java -jar demo.jar
```

##### 后台常驻运行（生产推荐）

```bash
# 日志输出到log文件，后台运行
nohup java -jar demo.jar > app.log 2>&1 &
```

- `nohup`：脱离终端，关闭窗口不停止程序
- `&`：后台执行
- `> app.log 2>&1`：把控制台日志写入文件
**SpringBoot 默认端口 8080，服务器防火墙放开端口才能外部访问：**

```bash
# firewalld
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --reload

# 阿里云/腾讯云还要在安全组放行8080端口
```

### 2：War 包部署（外置独立 Tomcat，需要装 Tomcat）

#### 1. pom 修改配置
1）打包类型改为 war

```
<packaging>war</packaging>
```

2）排除内置 Tomcat

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <!-- 排除内置tomcat -->
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

3）添加 Servlet 依赖（Tomcat 提供容器，本地编译需要）

```
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <scope>provided</scope>
</dependency>
```

#### 2. 启动类改造

继承`SpringBootServletInitializer`，重写 configure 方法

```java
@SpringBootApplication
public class DemoApplication extends SpringBootServletInitializer {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder builder) {
        return builder.sources(DemoApplication.class);
    }
}
```

#### 3. 打包 war

```
mvn clean package -DskipTests
```

target 下生成 `xxx.war`

#### 4. 服务器安装、配置 Tomcat

1. 下载 Tomcat、解压，配置 JAVA_HOME 环境变量
2. 将 war 包放入 `tomcat/webapps/` 目录
3. 启动 Tomcat：`tomcat/bin/startup.sh`
4. 访问地址规则：`服务器IP:8080/项目名`

    - 若想直接 IP 访问不带项目名：把 war 改名为`ROOT.war`

## 4、项目框架结构
