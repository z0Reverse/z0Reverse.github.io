---
title: SQL
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - JavaWeb安全基础
tags:
  - JavaWeb
  - 漏洞利用
---

# 执行SQL的几种方式：

## JDBC的java.sql.Statement执行SQL语句
	原生的方式执行语句，需要通过拼接来执行，拼接的语句没有做好过滤会导致sql注入

## JDBC的java.sql.PreparedStatement执行SQL语句
	预编译执行sql语句

## 使用MyBatis执行SQL语句
	java持久化框架，通过xml描述符或者注解方式把对象存储过程与sql语句关联，支持自定义sql语句
	MyBatis注解存储SQL语句

```java
package org.mybatis.example;
public interface BlogMapper{
	@Select("select * from Blog where id=#{id}")
	Blog selectBlog(int id);
}
```

	MyBatis映射存储SQL语句

```sql
<?XML version="1.0" encoding="UTF-8">
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="org.mybatis.example.BlogMapper">
	<select id="selectBlog" parameterType="int" resultType="Blog">
		select * from Blog where id=#{id}
	</select>
</mapper>
```java

定义主体测试代码mybatis.java

```java
public class mybatis{
	SqlSessionFactory sessionFactory=null;
	SqlSession sqlSession=null;
	{
		String resource="com/mybatis/mybatisConfig.xml";
		Reader reader=null;
		try{
			reader=Resources.getResourceAsReader(resource);

		}catch(IOException e){
			e.printStackTrace();
		}
		sessionFactory=new SqlSessionFactoryBuilder().buildedr(reader);
		sqlSession=sessionFactory.openSession(true);

	}
	public void testSelectUser(){
		String statement="com.mybatis.userMapper"+".getUser";
		User user=sqlSession.selectOne(statement,"2");
		System.out.println(user);
	}
	public static void main(String []args)throw IOExpection{
		new mybatisteset().etstSelectUser();
	}
}
```

定义SQL映射文件userMapper.xml

```sql
<?XML version="1.0" encoding="UTF-8">
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.mybatis.usrMapper">
	<select id="getUser" resultType="com.mybatis.sql.User">
		select * from users where id=#{id}
	</select>
</mapper>
```

定义Mybatis的mybatisConfig.xml配置文件

```
<?XML version="1.0" encoding="UTF-8">
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<configuration>
	<settings>
	<setting name="logImpl" value="STDOUT_LOGGING"/>
	</settings>
	<environments default="development">
		<environment id="development">
			<transactionManager type="JDBC">
			<dataSource type="POOLED">
				<property name="driver" value="com.mysql.cj.jdbc.Driver"/>
				<property name="url" value="jdbc:mysql://xxx.xxx.xxx.xxx:3306/test?serverTimezone=UTC"/>
				<property name="username" value="root"/>
				<property name="password" value="root"/>
			</dataSource>
		</enivornment>
	</enivornments>
	<mappers>
		<mapper resoutce="com/mybatis/userMpper.xml"/>
	</mappers>
</configuration>
```bash

在代码中，mybatistest.java通过String statement="com.mybatis.userMapper"+".getUser"调用了com.mybatis.sql.User,在userMapper.xml文件中映射执行的是select * from users where id=#{id}，通过测试代码User user=sqlSession.selectOne(statement,2)将id值设置为2，运行完输出id为2的值

# 常见的SQL注入

## sql语句参数直接动态拼接
主要适用于原生方式，没有进行预编译sql语句的时候，如果对传进来的参数校验不完善就会导致这种问题

## 预编译有误
虽然预编译可以防止很多问题，但是如果预编译的时候配置不完善也会导致问题

```
String username="user %' or '1'='1'#";
String id="2";
String sql="select * from user where id=?";
if(!CommonUtils.isEmptyStr(username))
{
	sql=sql+"and username like '%"+username+"%";
}
System.out.println(sql);
PreparedStatement paperdStatement=coon.prepareStatement(sql);
prepaerdStatement.setString(1,id);
rs=preparedStatement.executeQuery();
```sql

这样虽然对id进行了预编译，但是后面的sql采用拼接的方式，如果username拼接上没有做好校验仍然会导致sql注入
select * from user where id=1 and username like '%user%' or '1'='1'#

## order by注入
order by 注入：`order by` 子句用于对查询结果进行排序。在 SQL 语句中，如果 `order by` 后面的字段名是由用户输入动态生成，且没有进行严格的过滤，就可能存在注入风险。【因为orderby这里不能采用预编译，预编译导致将其作为字符串执行就并非作为字段。只能参数化排序值，不能参数化排序字段】攻击者可以通过构造恶意输入，修改 `order by` 子句的逻辑，获取敏感信息或执行恶意操作。

```java
String orderBy = request.getParameter("orderBy"); // 获取用户输入的排序字段
String sql = "SELECT * FROM users ORDER BY " + orderBy; // 拼接SQL语句
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```

恶意输入：如果用户输入 `id; DROP TABLE users; --`，则拼接后的 SQL 语句为 `SELECT * FROM users ORDER BY id; DROP TABLE users; --`，会导致 `users` 表被删除

## %和_模糊查询
  % 和_模糊查询：`%` 和 `_` 是 SQL 中用于模糊查询的通配符，`%` 匹配任意字符（包括 0 个或多个字符），`_` 匹配任意单个字符。在使用 `like` 语句进行模糊查询时，如果用户输入没有进行安全处理，可能会导致 SQL 注入。

```java
String keyword = request.getParameter("keyword"); // 获取用户输入的查询关键字
String sql = "SELECT * FROM products WHERE product_name LIKE '%" + keyword + "%'"; // 拼接SQL语句
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```sql

恶意输入：如果用户输入 `' OR 1=1 --`，则拼接后的 SQL 语句为 `SELECT * FROM products WHERE product_name LIKE '%' OR 1=1 -- %'`，会返回所有记录。

## MyBatis中的#{}和${}
#{}`：是预编译处理，MyBatis 会将 `#{}` 替换为 `?`，并通过预编译的方式执行 SQL 语句，有效防止 SQL 注入。
${}`：是字符串替换，MyBatis 会将 `${}` 直接替换为传入的值，存在 SQL 注入风险，除非能确保传入的值是安全的。

```xml
<!-- 使用#{} -->
<select id="getUserById" parameterType="int" resultType="User">
    SELECT * FROM users WHERE id = #{id}
</select>

<!-- 使用${} -->
<select id="getUserByName" parameterType="String" resultType="User">
    SELECT * FROM users WHERE name = '${name}'
</select>
```sql

使用 `#{}` 时，MyBatis 会将 `#{id}` 替换为 `?`，并通过预编译执行；使用 ${} 时，如果用户输入 `' OR 1=1 --`，则会导致 SQL 注入。

## MyBaits常见的SQL注入

### order by 查询：
与上述普通 SQL 的 `order by` 注入类似，在 MyBatis 中如果 `order by` 后面的字段名是由用户输入动态生成且未过滤，可能导致注入。

```xml
<select id="getUsersByOrder" parameterType="String" resultType="User">
    SELECT * FROM users ORDER BY ${orderBy}
</select>
```sql

恶意输入：如果 `orderBy` 参数传入 `id; DROP TABLE users; --`，会导致数据库表被删除。

### like 查询：
在 MyBatis 中使用 `like` 语句时，如果模糊查询的内容由用户输入且未处理，可能存在注入。

```xml
<select id="searchProducts" parameterType="String" resultType="Product">
    SELECT * FROM products WHERE product_name LIKE '%${keyword}%'
</select>
```sql

恶意输入：如果 `keyword` 参数传入 `' OR 1=1 --`，会返回所有产品记录。

还有一种是通配符被预先定义好，而不是在xml中配置
	不安全的

```java
String keyword = "test' OR '1'='1";
String likeValue = "%" + keyword + "%";

Map<String, Object> params = new HashMap<>();
params.put("likeValue", likeValue); //

Mapper XML
<select id="searchUsers" resultType="User">
SELECT * FROM users WHERE username LIKE #{likeValue}
</select>
```sql

安全的

```java
<select id="searchUsers" resultType="User">
SELECT * FROM users WHERE username LIKE CONCAT('%', #{value}, '%')
</select>
```sql

### in 参数：
如果 `in` 子句中的参数是由用户输入动态生成且未进行安全处理，可能导致 SQL 注入。

```xml
<select id="getUsersByIds" parameterType="String" resultType="User">
    SELECT * FROM users WHERE id IN (${ids})
</select>
```

恶意输入：如果 `ids` 参数传入 `1; DROP TABLE users; --`，会导致数据库表被删除。

Demo
