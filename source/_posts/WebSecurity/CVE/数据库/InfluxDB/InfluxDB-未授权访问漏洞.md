---
title: "InfluxDB 未授权访问漏洞"
date: 2026-10-15 09:06:02
categories:
  - WebSecurity
  - CVE
  - "数据库"
  - "InfluxDB"
tags:
  - "InfluxDB"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

influxdb是一款著名的时序数据库，其使用jwt作为鉴权方式。在用户开启了认证，但未设置参数`shared-secret`的情况下，jwt的认证密钥为空字符串，此时攻击者可以伪造任意用户身份在influxdb中执行SQL语句。

JWT，全称是JSON Web Token，是一种易于使用、无状态的鉴权方式。简单来说，就是Server端把JSON数据经过加密做成token，以授权给Client端。

参考链接：

- https://www.komodosec.com/post/when-all-else-fails-find-a-0-day
- https://docs.influxdata.com/influxdb/v1.7/administration/config/#http-endpoints-settings

## 环境搭建

执行如下命令启动influxdb 1.6.6：

```
docker-compose up -d
```

环境启动后，访问`http://your-ip:8086/debug/vars`即可查看一些服务信息，但此时执行SQL语句则会出现401错误：

![image-20220224131904529](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/database/images/202202241319614.png)

## 漏洞复现

借助https://jwt.io/来生成jwt token：

```
{
  "alg": "HS256",
  "typ": "JWT"
}
{
  "username": "admin",
  "exp": 1745680213
}
```

其中，`admin`是一个已经存在的用户，`exp`是一个时间戳，代表着这个token的过期时间，你需要设置为一个未来的时间戳，`secret`置空。

最终生成的token：

![image-20220224132837081](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/database/images/202202241328222.png)

发送带有这个jwt token的数据包，注意Content-Type设置为`application/x-www-form-urlencoded`。

可见SQL语句执行成功：

![image-20220224133310332](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/database/images/202202241333480.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/database/InfluxDB-%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E6%BC%8F%E6%B4%9E.md)
