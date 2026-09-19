---
title: SpringBoot常见鉴权框架技术
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - 常见知识
tags:
  - 鉴权
  - SpringBoot
  - 框架
---

## 一、主流鉴权方案分类

### 1. 框架类（封装完整，企业首选）

1. **Spring Security**（Spring 官方，功能最全）

    - 支持：表单登录、Session、JWT、OAuth2、RBAC 权限、防 XSS/CSRF

2. **Apache Shiro**（轻量，老项目 / 小型后台）

    - 支持：登录认证、角色 / 权限、Session、记住我，上手简单

### 2. 自定义 Token 方案（前后端分离主流）

1. **Session 会话鉴权**（传统服务端渲染）
2. **JWT 无状态 Token 鉴权**（前后端分离、微服务最常用）
3. **Redis + 自定义 Token**（可主动失效、可控性强，替代 JWT 痛点）

### 3. 第三方标准协议

- OAuth2.0 / OpenID Connect（第三方登录：微信、支付宝、GitHub 登录）
- CAS 单点登录 SSO

---

# 二、每种机制完整代码示例

## 方案 1：Spring Security + Session 表单鉴权（传统后台）

### 1. pom 依赖

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependenc
```java

- `spring-boot-starter-web`：提供 Web 接口、Tomcat、HTTP 请求处理能力
- `spring-boot-starter-security`：引入 Spring 安全框架，内置认证、鉴权、防攻击全套能力

### 2. SecuritySessionConfig 配置类逐行拆解

```java
@Configuration
// 开启SpringSecurity自动配置，启用安全拦截链路
@EnableWebSecurity
public class SecuritySessionConfig {

    // Bean1：密码加密器
    @Bean
    public PasswordEncoder passwordEncoder() {
        // BCrypt强哈希加密，不可逆，生产必须使用，禁止明文存储密码
        return new BCryptPasswordEncoder();
    }
```java

执行顺序：项目启动时 Spring 容器扫描`@Configuration`，优先实例化`PasswordEncoder`，全局统一密码加密规则。

```java
    // Bean2：用户数据源（内存模拟用户，生产替换为数据库查询）
    @Bean
    public UserDetailsService userDetailsService(PasswordEncoder encoder) {
        // 创建管理员账号admin
        UserDetails admin = User.withUsername("admin")
                .password(encoder.encode("123456")) // 密码加密存储
                .roles("ADMIN") // 角色：管理员
                .authorities("sys:list","sys:add","sys:delete") // 细粒度接口权限
                .build();
        // 普通用户user
        UserDetails user = User.withUsername("user")
                .password(encoder.encode("123456"))
                .roles("USER")
                .authorities("sys:list")
                .build();
        // 内存用户管理器，存放所有登录账号
        return new InMemoryUserDetailsManager(admin, user);
    }
```java

执行流程：
1. 容器注入上面创建好的密码加密器
2. 把明文`123456`加密成密文，存入用户对象
3. 封装角色、权限，最后交给内存用户管理器
4. 用户登录时，Security 会调用这个 Bean 校验账号密码

```java
    // Bean3：核心安全过滤链，定义所有拦截、登录、权限规则
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                // 关闭CSRF防护：前后端分离/表单提交无Cookie时关闭；传统页面建议开启
                .csrf(csrf -> csrf.disable())
                // 1. 权限匹配规则
                .authorizeHttpRequests(auth -> auth
                        // 放行登录接口、静态资源，无需登录
                        .requestMatchers("/login","/css/**").permitAll()
                        // 访问/user/add接口，必须拥有sys:add权限
                        .requestMatchers("/user/add").hasAuthority("sys:add")
                        // 访问/user/delete接口，必须拥有ADMIN角色
                        .requestMatchers("/user/delete").hasRole("ADMIN")
                        // 剩下所有接口，必须登录认证后才能访问
                        .anyRequest().authenticated()
                )
                // 2. 表单登录配置
                .formLogin(form -> form
                        .loginProcessingUrl("/doLogin") // 前端提交登录表单的地址，Security内置接口，不用自己写Controller
                        .usernameParameter("username") // 表单账号参数名
                        .passwordParameter("password") // 表单密码参数名
                        .defaultSuccessUrl("/index",true) // 登录成功强制跳转到首页
                        .permitAll() // 登录页面所有人可访问
                )
                // 3. 退出登录配置
                .logout(logout -> logout.logoutUrl("/logout").permitAll());
        // 构建并返回过滤链，全局生效
        return http.build();
    }
}
```

### 3、请求完整执行链路（用户访问接口流程）

1. 浏览器发起请求 → 进入 Security 全局过滤器
2. 执行`authorizeHttpRequests`匹配路径：

    - 如果是`/login`：直接放行
    - 如果是`/user/add`：校验是否拥有`sys:add`权限，无权限返回 403
    - 其他接口：校验是否登录（Session 是否存在）

3. 未登录自动跳转到内置表单登录页
4. 前端提交账号密码到`/doLogin`：

    - Security 自动调用`UserDetailsService`查询用户
    - 使用`PasswordEncoder`比对加密密码
    - 校验成功，服务端创建 Session，返回 Set-Cookie 写入浏览器

5. 登录成功跳转`/index`，后续请求携带 Cookie，自动识别登录状态
6. 访问`/logout`：销毁 Session，退出登录

### 4、原理

登录成功后服务端生成 SessionID 存入 Cookie，每次请求携带 Cookie，服务端校验 Session 实现鉴权。

---

## 方案 2：Spring Security + JWT 无状态鉴权（前后端分离主流）

### 1. 依赖

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
<!-- JWT工具 -->
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-api</artifactId>
    <version>0.11.5</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-impl</artifactId>
    <version>0.11.5</version>
    <scope>runtime</scope>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt-jackson</artifactId>
    <version>0.11.5</version>
    <scope>runtime</scope>
</dependency>
```java

- api：核心 API 定义
- impl：底层实现包
- jackson：JSON 序列化，用于载荷解析

### 2. JWT 工具类

```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.stereotype.Component;
import javax.crypto.SecretKey;
import java.util.Base64;
import java.util.Date;

@Component
public class JwtUtil {
// 加密密钥，生产必须使用超长随机字符串，禁止硬编码明文
	private static final String SECRET = "abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890";
// 基于密钥生成加密对象，HS256对称加密
	private static final SecretKey KEY = Keys.hmacShaKeyFor(Base64.getEncoder().encode(SECRET.getBytes())); // Token有效期30分钟
	private static final long EXPIRE = 1000 * 60 * 30;
	// 方法1：根据用户名生成JWT字符串
	public String generateToken(String username) {
		Date now = new Date(); // 当前时间
		Date expireDate = new Date(now.getTime() + EXPIRE); // 过期时间
		return Jwts.builder() .setSubject(username) // 载荷：存储用户名（核心标识）
			.setIssuedAt(now) // 签发时间
			.setExpiration(expireDate) // 过期时间
			.signWith(KEY, SignatureAlgorithm.HS256) // 使用密钥加密签名，防止篡改
			.compact(); // 拼接成完整JWT字符串返回
	}
	// 方法2：解析Token，获取存储的用户名
	public String getUsername(String token) {
		Claims claims = Jwts.parserBuilder()
			.setSigningKey(KEY) // 使用同一个密钥解密校验签名
			.build()
			.parseClaimsJws(token) // 解析token，签名不一致直接抛异常
			.getBody(); // 获取载荷数据
		return claims.getSubject(); // 取出用户名
	}
	// 方法3：判断Token是否过期
	public boolean isExpire(String token) {
		Claims claims = Jwts.parserBuilder()
			.setSigningKey(KEY)
			.build()
			.parseClaimsJws(token)
			.getBody(); // 判断过期时间是否早于当前时间
		return claims.getExpiration().before(new Date());
	}
}
```java

### 3. JWT 拦截器（校验请求头 Token）
JwtAuthFilter 拦截器（OncePerRequestFilter：单次请求只执行一次）

```java
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;
import java.io.IOException;
@Component
public class JwtAuthFilter extends OncePerRequestFilter {
    @Autowired
    private JwtUtil jwtUtil; // 注入JWT工具
    @Autowired
    private UserDetailsService userDetailsService; // 注入用户查询服务

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        // 1. 从请求头获取Authorization字段
        String token = request.getHeader("Authorization");
        // 2. 判断是否携带Bearer格式token（前端规范 Bearer + 空格 + token）
        if(token != null && token.startsWith("Bearer ")){
            // 截取Bearer后面真实token字符串
            String jwt = token.substring(7);
            // 解析token拿到用户名
            String username = jwtUtil.getUsername(jwt);
            // 用户名不为空，且当前上下文无登录认证信息
            if(username != null && SecurityContextHolder.getContext().getAuthentication() == null){
                // 根据用户名查询用户、角色、权限
                UserDetails userDetails = userDetailsService.loadUserByUsername(username);
                // 校验token未过期
                if(!jwtUtil.isExpire(jwt)){
                    // 封装认证对象：用户名、密码(null)、权限集合
                    UsernamePasswordAuthenticationToken authToken = new UsernamePasswordAuthenticationToken(userDetails,null,userDetails.getAuthorities());
                    // 绑定请求详情
                    authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                    // 存入Security全局上下文，后续接口直接识别登录状态
                    SecurityContextHolder.getContext().setAuthentication(authToken);
                }
            }
        }
        // 放行，执行后续过滤器/Controller接口
        filterChain.doFilter(request,response);
    }
}
```java

所有请求进入 Controller**之前**执行，提前校验 Token，认证通过后写入 Security 上下文，后续接口`@PreAuthorize`权限注解可直接使用。

### 4. Security 配置适配 JWT

```java
@Configuration
@EnableWebSecurity
public class JwtSecurityConfig {
    @Autowired
    private JwtAuthFilter jwtAuthFilter; // 注入自定义JWT拦截器

    @Bean
    public PasswordEncoder passwordEncoder(){
        return new BCryptPasswordEncoder();
    }

    @Bean
    public UserDetailsService userDetailsService(PasswordEncoder encoder){
        UserDetails admin = User.withUsername("admin")
                .password(encoder.encode("123456"))
                .roles("ADMIN")
                .build();
        return new InMemoryUserDetailsManager(admin);
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception{
        http
                .csrf(csrf -> csrf.disable()) // 前后端分离无Cookie，关闭CSRF
                // 无状态模式：Security不创建Session，完全依赖Token鉴权
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .authorizeHttpRequests(auth -> auth
                        .requestMatchers("/api/login").permitAll() // 登录接口放行，不需要token
                        .anyRequest().authenticated() // 其余接口必须携带有效token
                )
                // 在用户名密码原生过滤器之前，执行我们自定义的JWT拦截器
                .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }
}
```java

### 5. 登录 Controller（发放 Token）

```java
@RestController
@RequestMapping("/api")
public class LoginController {
    @Autowired
    private AuthenticationManager authManager;// 认证管理器，校验账号密码
    @Autowired
    private JwtUtil jwtUtil;

    @PostMapping("/login")
    public Map<String,Object> login(@RequestParam String username,@RequestParam String password){
    // 封装账号密码，交给Security自动校验
        Authentication auth = authManager.authenticate(new UsernamePasswordAuthenticationToken(username,password));
        String token = jwtUtil.generateToken(username);
        return Map.of("code",200,"token",token);
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception{
        return config.getAuthenticationManager();
    }
}
```

### 6、使用方式

前端登录后拿到 token，后续请求头携带：`Authorization: Bearer xxx`

优点：无状态、适合分布式微服务；缺点：无法主动注销，过期前一直有效。

### 7、JWT 完整请求执行全流程

1. 前端调用`/api/login`传递账号密码
2. `AuthenticationManager`调用`UserDetailsService`校验账号密码
3. 校验通过，后端使用`JwtUtil`生成 token 返回前端
4. 前端存储 token，后续所有请求头携带：`Authorization: Bearer xxx`
5. 请求到达`JwtAuthFilter`拦截器：

    - 提取并解析 token，校验签名、过期时间
    - 合法则查询用户权限，写入 Security 上下文

6. 进入 Controller 接口，`@PreAuthorize("hasRole('ADMIN')")`可直接鉴权
7. 无 Session 存储，多台服务器分布式部署无需共享会话

### 8、JWT 缺陷说明
token 本身包含所有信息，服务端无存储，**无法主动注销**，只能等待过期。

## 方案 3：Shiro 权限鉴权（轻量框架）

### 1. pom 依赖

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring-boot-starter</artifactId>
    <version>1.12.0</version>
</dependency>
```java

### 2. Shiro 配置类

```java
import org.apache.shiro.authc.credential.HashedCredentialsMatcher;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.spring.web.ShiroFilterFactoryBean;
import org.apache.shiro.web.mgt.DefaultWebSecurityManager;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import java.util.LinkedHashMap;
import java.util.Map;

@Configuration
public class ShiroConfig {

    // 自定义Realm（账号校验、权限查询）
    @Bean
    public MyRealm myRealm(){
        MyRealm realm = new MyRealm();
        // 密码加密
        // 密码加密匹配器
        HashedCredentialsMatcher matcher = new HashedCredentialsMatcher();
        matcher.setHashAlgorithmName("bcrypt"); // 使用bcrypt加密比对密码
        realm.setCredentialsMatcher(matcher);
        return realm;
    }

    // 安全管理器
    @Bean
    public SecurityManager securityManager(MyRealm realm){
        DefaultWebSecurityManager manager = new DefaultWebSecurityManager();
        manager.setRealm(realm);
        return manager;
    }

    // 过滤器，配置拦截规则
    @Bean
    public ShiroFilterFactoryBean shiroFilter(SecurityManager manager){
        ShiroFilterFactoryBean filter = new ShiroFilterFactoryBean();
        filter.setSecurityManager(manager); // 绑定安全管理器
        filter.setLoginUrl("/login"); // 未登录跳转地址
        filter.setUnauthorizedUrl("/unauth"); // 登录但无权限跳转地址
        // 有序拦截规则（LinkedHashMap顺序从上到下匹配）
        Map<String,String> rule = new LinkedHashMap<>();
        rule.put("/login","anon"); // anon：匿名访问，无需登录
        rule.put("/user/add","perms[sys:add]"); // perms：需要指定权限
        rule.put("/user/**","authc"); // authc：必须登录认证
        rule.put("/**","authc"); // 其余全部需要登录
        filter.setFilterChainDefinitionMap(rule);
        return filter;
    }
}
```java

### 3. 自定义 Realm

```java
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.SimpleAuthenticationInfo;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

public class MyRealm extends AuthorizingRealm {
    // 授权：查询角色、权限
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {
        String username = principals.getPrimaryPrincipal().toString();
        SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();
        // 模拟数据库查询角色权限
        info.addRole("admin");
        info.addStringPermission("sys:list");
        info.addStringPermission("sys:add");
        return info;
    }

    // 认证：校验账号密码
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {
        String username = token.getPrincipal().toString();
        // 模拟数据库查询密码
        String password = "$2a$10$xxxx加密后的密码";
        return new SimpleAuthenticationInfo(username,password,getName());
    }
}
```java

### 4. 登录 Controller

```java
@RestController
public class ShiroLoginController {
    @PostMapping("/login")
    public String login(String username,String password){
        Subject subject = SecurityUtils.getSubject();
        UsernamePasswordToken token = new UsernamePasswordToken(username,password);
        try{
            subject.login(token);
            return "登录成功";
        }catch (Exception e){
            return "账号密码错误";
        }
    }

    @GetMapping("/logout")
    public String logout(){
        SecurityUtils.getSubject().logout();
        return "退出成功";
    }
}
```java

### 5、Shiro 完整执行流程

1. 请求进入`ShiroFilterFactoryBean`过滤器，匹配 URL 规则
2. 未登录接口跳转`/login`
3. 前端提交账号密码到 login 接口，创建`Subject`执行 login ()
4. 自动调用`MyRealm.doGetAuthenticationInfo`校验密码
5. 登录成功，Shiro 创建 Session 存储登录信息
6. 访问受限接口，触发`doGetAuthorizationInfo`加载权限校验
7. 调用 logout () 销毁会话，实现退出登录
---

## 方案 4：Redis 自定义 Token（可控注销，企业常用）

### 1、核心思路

1. 登录成功生成唯一 uuid 作为 token，存入 Redis `token:userId`，设置过期时间
2. 每次请求拦截器获取 Header 的 token，查询 Redis 是否存在
3. 退出登录直接删除 Redis 对应 key，实现主动失效（解决 JWT 无法注销痛点）

### 2、简易拦截器核心代码
执行时机：所有 Controller 执行前拦截，原生 SpringMVC 拦截器，不依赖 Security/Shiro 框架

```java
@Component
public class TokenInterceptor implements HandlerInterceptor {
    @Autowired
    private StringRedisTemplate redisTemplate;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String token = request.getHeader("token");
        if(token == null){
            response.getWriter().write("未登录");
            return false;
        }
        // 查询redis
        String userId = redisTemplate.opsForValue().get("token:"+token);
        if(userId == null){
            response.getWriter().write("token失效，请重新登录");
            return false;
        }
        // 续期
        redisTemplate.expire("token:"+token,30, TimeUnit.MINUTES);
        request.setAttribute("userId",userId);
        return true;
    }
}
```java

### 3、登录发放 Token

```java
@PostMapping("/login")
public Map<String,Object> login(String username,String password){
    // 校验账号密码
    if("admin".equals(username) && "123456".equals(password)){
        String token = UUID.randomUUID().toString().replace("-","");
        redisTemplate.opsForValue().set("token:"+token,"1",30,TimeUnit.MINUTES);
        return Map.of("code",200,"token",token);
    }
    return Map.of("code",500,"msg","账号错误");
}

// 退出登录
@PostMapping("/logout")
public String logout(HttpServletRequest request){
    String token = request.getHeader("token");
    redisTemplate.delete("token:"+token);
    return "退出成功";
}
```bash

### 4、Redis-Token 完整流程

1. 登录校验账号密码 → 生成 UUID token 存入 Redis
2. 前端携带 token 请求接口 → 拦截器查询 Redis
3. Redis 存在 key：续期，放行接口；不存在：拦截提示重新登录
4. 退出登录：删除 Redis 对应 key，token 立即失效，解决 JWT 无法注销痛点
5. 分布式多服务器共享 Redis，天然支持集群部署
---

# 三、各方案适用场景总结

| 鉴权方案                    | 适用场景                | 优缺点                       |
| ----------------------- | ------------------- | ------------------------- |
| Spring Security Session | 传统后台、服务端渲染页面        | 简单，依赖 Cookie；不适合分布式、前后端分离 |
| Spring Security JWT     | 前后端分离、微服务           | 无状态易分布式；无法主动注销            |
| Redis 自定义 Token         | 需要主动下线、多端登录控制       | 可控性强，支持注销；依赖 Redis        |
| Apache Shiro            | 小型单体后台、老项目改造        | 上手简单，轻量化；微服务生态适配差         |
| OAuth2.0                | 第三方登录（微信 / QQ/GitHu | 标准第三方授权，搭建复杂              |
- **SpringSecurity Session**

    请求 → Security 过滤器 → 匹配 URL 规则 → 校验 Cookie-Session → 放行 / 跳转登录页
- **SpringSecurity JWT**

    请求 → JwtAuthFilter 拦截器 → 解析 Header Token → 校验签名 & 过期 → 写入 Security 上下文 → 接口鉴权
- **Apache Shiro**

    请求 → Shiro 全局过滤器 → 匹配 URL 规则 → 校验 Session → 登录时调用 Realm 认证，访问权限接口调用 Realm 授权
- **Redis 自定义 Token**

    请求 → SpringMVC 拦截器 → 读取 Header Token → 查询 Redis 校验有效性 → 续期 / 拦截
