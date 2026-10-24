---
title: "泛微OA sysinterfacecodeEdit.jsp 任意文件上传漏洞"
date: 2026-10-17 09:12:46
categories:
  - WebSecurity
  - CVE
  - "OA"
  - "泛微OA"
tags:
  - "泛微OA"
  - "文件上传"
  - "未授权访问"
  - "漏洞复现"
---
## 漏洞描述

泛微OA sysinterface/codeEdit.jsp 页面任意文件上传导致可以上传恶意文件

## 漏洞版本

```
较老版本，目前无准确版本
```

## 漏洞复现

```
filename=******5308.java&filetype=javafilename为文件名称 为空时会自动创建一个
String fileid = "Ewv";<br>
    String readonly = "";<br>
    boolean isCreate = false;<br>
    if(StringHelper.isEmpty(fileName)) {<br>
     Date ndate = new Date();<br>
     SimpleDateFormat sf = new SimpleDateFormat("yyyyMMddHHmmss");<br>
     String datetime = sf.format(ndate);<br>
     fileid = fileid + datetime;<br>
     fileName= fileid + "." + filetype;<br>
     isCreate = true;<br>
    } else {<br>
        int pointIndex = fileName.indexOf(".");<br>
        if(pointIndex > -1) {<br>
            fileid = fileName.substring(0,pointIndex);<br>
        }}
```

![1](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091045304.png)

![2](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091045317.png)

![3](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091045310.png)

![4](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091045312.png)

![5](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/oa/images/202202091045316.png)



## 参考文章

[泛微OA未授权可导致GetShell](https://www.uedbox.com/post/15730/)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/oa/%E6%B3%9B%E5%BE%AEOA-sysinterfacecodeEdit.jsp-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E.md)
