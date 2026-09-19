---
title: SQL注入常见类型
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - SQL注入
tags:
  - SQL注入
  - 注入
  - WAF绕过
---

整数型
字符串型

联合注入
布尔盲注
报错注入
二次注入
堆叠注入

MySQL
SQLServer
Oreal

# SQL注入常见类型及方法导论

![](/images/SQL注入常见类型/20260830235212.png)

## 联合注入
**MySQL UNION 操作符说明**
MySQL UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合，并去除重复的行。这句话的含义是指，我们可以在一条数据语句中，同时查询两个内容。
**比如：**
select * from users where username = '{输入内容}' union select xxxx;
**union select 使用要求：**
- UNION 操作符必须由两个或多个 SELECT 语句组成， **每个 SELECT 语句的列数和对应位置的数据类型必须相同**。
- 这里有一个要点就是，union select 后面列要和前面的列要一样。
这就会涉及到下一个步骤，就是如何判断前一个 select 有多少列--也就是orderby判断列数
![](/images/SQL注入常见类型/20260830224035.png)

```

```bash

# 主流数据库 SQL 注入差异总结

主流关系型数据库：**MySQL/MariaDB、SQL Server(MSSQL)、Oracle、PostgreSQL**

> 共同点：都支持 `UNION`、`AND/OR`、注释，都存在 SQL 注入风险；**注入的核心逻辑一致，但是函数、系统表、语法、报错、注释、限制完全不一样**。

> 前置：SQL 注入分为：**联合注入、报错注入、布尔盲注、时间盲注、堆叠查询**，不同数据库对这几类支持差异很大。

---

## 1. MySQL / MariaDB（MariaDB 是 MySQL 分支，语法几乎完全一致）

### 常用函数

- 版本：`version()`
- 当前数据库：`database()`
- 当前用户：`user()`
- 数据库名、表名、字段：`information_schema` 系统库
- 字符串拼接：`concat(a,b)`
- 延时：`sleep(5)`
- 报错函数：`updatexml()`、`extractvalue()`

### 注入特性

1. ✅支持 **UNION SELECT**，可以直接 `select 1,2` 不需要 from
2. ✅支持**堆叠查询**：`;` 分号结束后执行第二条 SQL（部分环境关闭）
3. ✅支持时间盲注：`sleep()`
4. ✅报错注入：updatexml、extractvalue 经典报错
5. 注释：`#`、`--` 、`/* */`
6. 字符编码：支持单引号；可使用 `0x十六进制` 代替字符串绕过引号过滤

### 坑

- 高版本 MySQL 8.0，`information_schema`部分权限受限；
- 部分配置关闭堆叠查询。

**联合注入示例**

```sql
union select 1,version(),database(),user()
```

---

## 2. SQL Server (MSSQL)

### 常用函数

- 版本：`@@version`
- 当前数据库：`db_name()`
- 当前用户：`user_name()`
- 系统视图：`sys.databases`、`sys.tables`、`sys.columns`
- 字符串拼接：`a+b`
- 延时：`waitfor delay '0:0:5'`
- 报错：floor 报错、rand 报错

### 注入特性

1. ✅支持 UNION SELECT
2. ✅**堆叠查询很强**：`;` 分号可以直接执行多条语句，支持执行存储过程，可提权
3. ✅时间盲注：`waitfor delay '0:0:5'`
4. ❌**不支持 # 注释**，只能用 `--` 、`/* */`
5. 类型校验严格：union 前后字段类型不匹配直接报错，不能随便用 null 填充

### 坑

- 没有 `sleep()`；
- 很多场景会过滤单引号；
- 可调用 xp_cmdshell 执行系统命令（需要开启配置）

**联合注入示例**

```sql
union select 1,@@version,db_name(),user_name()
```

---

## 3. Oracle

### 常用函数

- 版本：`select * from v$version`
- 当前用户：`user`
- 当前数据库：`user`（Oracle 是用户模式，没有数据库概念，一个用户对应一个 schema）
- 系统视图：`all_tables`、`all_columns`、`all_tab_columns`
- 字符串拼接：`a||b`
- 延时：`dbms_lock.sleep(5)`（需要权限）
- 报错：`utl_inaddr.get_host_name()` 报错注入

### 注入特性

1. ✅支持 UNION SELECT
2. ⚠️**强制必须有 from 子句！不能直接 select 1,2，必须加 from dual 伪表**
3. ❌**不支持堆叠查询！分号；不能执行多条 SQL**
4. ⚠️时间盲注 `dbms_lock.sleep()` 很多账号没有权限，很难用
5. 注释：`--` 、`/* */`，不支持`#`
6. 字段类型校验非常严格，union 的 null 也要匹配类型，容易 ORA 报错

> ORA‑00923：缺少 FROM 关键字，最常见踩坑

**联合注入示例**

```sql
union select 1,user from dual
```

---

## 4. PostgreSQL（PG）

### 常用函数

- 版本：`version()`
- 当前数据库：`current_database()`
- 当前用户：`current_user`
- 系统表：`information_schema.tables`
- 字符串拼接：`a||b`
- 延时：`pg_sleep(5)`

### 注入特性

1. ✅支持 UNION SELECT
2. ✅支持堆叠查询 `;`
3. ✅时间盲注 `pg_sleep()`
4. 注释：`--` 、`/* */`，不支持`#`
5. 支持`limit`，也支持`offset`；
6. 报错注入相对少，更多用布尔 / 时间盲注

**联合注入示例**

```sql
union select 1,version(),current_database(),current_user
```bash

---

# 四大数据库对比速查表

表格

|项目|MySQL/MariaDB|SQL Server|Oracle|PostgreSQL|||||
|---|---|---|---|---|---|---|---|---|
|UNION SELECT|✅，无需 from|✅，类型严格|✅，必须`from dual`|✅|||||
|堆叠查询 (;)|✅(可关闭)|✅，能力强|❌不支持|✅|||||
|时间盲注函数|`sleep(n)`|`waitfor delay '0:0:n'`|`dbms_lock.sleep(n)`(权限限制)|`pg_sleep(n)`|||||
|字符串拼接|`concat(a,b)`|`a+b`|`a||b`|`a||b`|
|系统元数据|`information_schema`|`sys.*`视图|`all_tables`视图|`information_schema`|||||
|注释符号|`# -- /* */`|`-- /* */`|`-- /* */`|`-- /* */`|||||
|报错注入|updatexml/extractvalue|floor/rand 报错|utl_inaddr|较少|||||

---

# 不同注入类型的数据库支持差异

## 1️⃣联合注入 UNION SELECT

全部支持，但：

- MySQL：随便 null 填充
- MSSQL：字段类型严格匹配
- Oracle：**必须 from dual，null 类型要匹配**
- PostgreSQL：列数一致即可

## 2️⃣报错注入

- MySQL：成熟，updatexml、extractvalue
- MSSQL：floor/rand 报错
- Oracle：utl_inaddr，很多环境权限不足用不了
- PostgreSQL：几乎没有成熟报错注入，优先盲注

## 3️⃣时间盲注

- MySQL：sleep () 简单好用
- MSSQL：waitfor delay
- Oracle：dbms_lock.sleep 经常无权限，很难利用
- PostgreSQL：pg_sleep()

## 4️⃣堆叠查询（分号；执行多条语句）

- ✅ MySQL、MSSQL、PostgreSQL
- ❌ Oracle：**不支持堆叠查询**，不能用`;`执行第二条语句

> MSSQL 堆叠查询可以调用存储过程，是高危点；Oracle 不能堆叠，所以无法直接执行多条 SQL。

## 5️⃣布尔盲注

全部数据库都支持，原理都是构造条件判断页面返回是否变化，只是函数不一样。

---

# 实战渗透小总结

1. **如果看到 `#` 注释有效，大概率是 MySQL/MariaDB**
2. 看到 `waitfor delay` 一定是 MSSQL
3. payload 必须写 `from dual` 基本就是 Oracle
4. 看到 `pg_sleep` 是 PostgreSQL

> 注意：现在 WAF、防火墙会拦截 union、select 等关键字；就算数据库语法支持，也可能被 WAF 拦截。

# 特性

## Mysql
MySQL 5.0 以上存在一个系统自带的数据库 `information_schema`。
`information_schema` 数据库里包含了这几张表： **schemata、tables、columns。** 这三张表依次分别存放着字段：(**schema_name**)、(**table_name、table_schema**)、(**table_schema、table_name、column_name**)

![information_schema 结构](http://hbc2.haobachang.com:27599/static/p9.png)
简单的理解一下就是数据库里的所有的表，字段，都会在这里保存一份。也就是说，我们可以直接通过这个数据库去查询到我们刚才查到的 mydb 里的表，以及表对应的字段。
所以union联合查询语句中
union select table_name from information_schema.tables where table_schema='mydb'就是查information_schema数据库的tables表中，table_schema为mydb的对应的tablename都有哪些
`group_concat`，是 MySQL 中用于将分组内多行数据连接成一个字符串的聚合函数
