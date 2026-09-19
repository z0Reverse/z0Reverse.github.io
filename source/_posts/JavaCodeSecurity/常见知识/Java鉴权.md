---
title: Java鉴权
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - 常见知识
tags:
  - 鉴权
  - SpringBoot
  - 框架
---

框架
SpringSecurity
原生
SpEl表达式
好的，下面我将把三种方式——**原生 Web 请求级鉴权**、**SpEL 注解（`@PreAuthorize`）**、**自定义注解**——从**权限数据准备**、**用户加载**、**鉴权配置**到**接口使用**，完整地串起来，给出可直接参考的代码实现。

---

## 1. 准备阶段：用户、角色、权限数据

为了演示，我们使用内存数据模拟。实际项目中可从数据库加载。

java

// 权限常量
public class Permissions {
    public static final String USER_QUERY = "user:query";
    public static final String USER_CREATE = "user:create";
    public static final String USER_DELETE = "user:delete";
    public static final String ORDER_QUERY = "order:query";
    public static final String ORDER_EDIT = "order:edit";
}
// 角色常量（角色会自动添加 ROLE_ 前缀）
public class Roles {
    public static final String ADMIN = "ADMIN";
    public static final String USER = "USER";
}

---

## 2. 加载用户权限：UserDetailsService

我们实现一个 `UserDetailsService`，为每个用户分配角色和权限。

java

import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import java.util.*;
@Service
public class CustomUserDetailsService implements UserDetailsService {
    // 模拟数据库存储用户信息（用户名 -> 密码、角色、权限）
    private final Map<String, UserInfo> userStore = new HashMap<>();
    public CustomUserDetailsService() {
        // 初始化用户：admin 拥有 ADMIN 角色和所有权限
        userStore.put("admin", new UserInfo("admin", "admin123",
                Set.of(Roles.ADMIN),
                Set.of(Permissions.USER_QUERY, Permissions.USER_CREATE, Permissions.USER_DELETE,
                       Permissions.ORDER_QUERY, Permissions.ORDER_EDIT)));
        // 普通用户 user，拥有 USER 角色和部分权限
        userStore.put("user", new UserInfo("user", "user123",
                Set.of(Roles.USER),
                Set.of(Permissions.USER_QUERY, Permissions.ORDER_QUERY)));
        // 只读用户 readOnly，拥有 USER 角色但只有查询权限
        userStore.put("readOnly", new UserInfo("readOnly", "read123",
                Set.of(Roles.USER),
                Set.of(Permissions.USER_QUERY)));
    }
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        UserInfo info = userStore.get(username);
        if (info == null) {
            throw new UsernameNotFoundException("用户不存在：" + username);
        }
        // 将角色和权限都转换为 GrantedAuthority
        Set<SimpleGrantedAuthority> authorities = new HashSet<>();
        // 角色：需要添加 ROLE_ 前缀（Spring Security 默认要求）
        for (String role : info.getRoles()) {
            authorities.add(new SimpleGrantedAuthority("ROLE_" + role));
        }
        // 权限：直接添加（无前缀）
        for (String perm : info.getPermissions()) {
            authorities.add(new SimpleGrantedAuthority(perm));
        }
        // 返回 UserDetails 对象（注意密码需加密，这里为了示例使用明文，实际会加密）
        return User.builder()
                .username(info.getUsername())
                .password("{noop}" + info.getPassword()) // {noop} 表示明文，实际应使用 BCrypt
                .authorities(authorities)
                .build();
    }
    // 内部类，存储用户信息
    static class UserInfo {
        private String username;
        private String password;
        private Set<String> roles;
        private Set<String> permissions;
        // 构造方法、getter 省略
    }
}

---

## 3. Web 请求级鉴权：原生 SecurityFilterChain 配置

这种方式通过 URL 模式直接限制访问，与注解无关。

java

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
@Configuration
@EnableWebSecurity
public class SecurityWebConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(authz -> authz
                // 1. 公共资源放行
                .requestMatchers("/public/**", "/login").permitAll()
                // 2. 基于角色的 URL 权限
                .requestMatchers("/admin/**").hasRole("ADMIN")   // 需要 ADMIN 角色
                .requestMatchers("/user/**").hasAnyRole("ADMIN", "USER")
                // 3. 基于具体权限的 URL 控制
                .requestMatchers("/api/orders/**").hasAuthority("order:query")
                .requestMatchers("/api/orders/edit/**").hasAuthority("order:edit")
                // 4. 其他所有请求需要认证
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")
                .permitAll()
            )
            .logout(logout -> logout.permitAll());
        return http.build();
    }
}

**特点**：

- 所有鉴权规则集中在 `SecurityFilterChain` 中，一目了然。

- 适用于简单、固定的权限控制场景。

- 缺点是权限变更需要重启应用（除非结合动态权限源）。

---

## 4. 方法级鉴权：使用 SpEL 表达式（@PreAuthorize）

首先开启方法级安全支持。

java

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
@Configuration
@EnableMethodSecurity(prePostEnabled = true)  // 启用 @PreAuthorize / @PostAuthorize
public class MethodSecurityConfig {
}

然后，我们创建一个自定义的权限校验 Bean，方便在 SpEL 中复用。

java

import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Component;
@Component("authz")  // 给 Bean 起名为 "authz"
public class AuthzService {
    // 检查当前用户是否拥有指定权限
    public boolean hasPermission(String permission) {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null) return false;
        // 检查 GrantedAuthority 列表中是否包含该权限（精确匹配）
        return auth.getAuthorities().stream()
                .anyMatch(g -> g.getAuthority().equals(permission));
    }
    // 检查用户是否拥有指定角色（注意角色名不带 ROLE_ 前缀）
    public boolean hasRole(String role) {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null) return false;
        return auth.getAuthorities().stream()
                .anyMatch(g -> g.getAuthority().equals("ROLE_" + role));
    }
}

现在，在 Controller 或 Service 中使用 `@PreAuthorize` 并调用 `authz` Bean。

java

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/api/users")
public class UserController {
    // 直接使用权限字符串
    @GetMapping("/query")
    @PreAuthorize("hasAuthority('user:query')")
    public String queryUsers() {
        return "User list";
    }
    // 组合多个条件
    @PostMapping("/create")
    @PreAuthorize("hasAuthority('user:create') and hasRole('ADMIN')")
    public String createUser() {
        return "User created";
    }
    // 调用自定义 Bean 的方法
    @DeleteMapping("/delete/{id}")
    @PreAuthorize("@authz.hasPermission('user:delete') and #id > 0")
    public String deleteUser(@PathVariable Long id) {
        return "User " + id + " deleted";
    }
    // 引用方法参数
    @PutMapping("/{id}")
    @PreAuthorize("#id == authentication.principal.id or hasRole('ADMIN')")
    public String updateUser(@PathVariable Long id, @RequestBody User user) {
        return "User updated";
    }
}

---

## 5. 自定义注解：封装 @PreAuthorize

为了简化重复的注解书写，我们可以创建自定义注解，将 SpEL 表达式封装起来。

### 5.1 创建自定义注解

java

import org.springframework.security.access.prepost.PreAuthorize;
import java.lang.annotation.*;
@Target({ElementType.METHOD, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
// ★ 核心：将 @PreAuthorize 作为元注解，并在其中引用我们自定义的 Bean
@PreAuthorize("@authz.hasPermission(#permission)")
public @interface RequirePermission {
    String permission();  // 注解属性，用于传递权限标识
}

如果需要支持角色，也可以创建类似的注解：

java

@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@PreAuthorize("@authz.hasRole(#role)")
public @interface RequireRole {
    String role();
}

### 5.2 使用自定义注解

java

@RestController
@RequestMapping("/api/orders")
public class OrderController {
    @GetMapping("/list")
    @RequirePermission(permission = "order:query")  // 替代 @PreAuthorize
    public String listOrders() {
        return "Order list";
    }
    @PostMapping("/edit")
    @RequirePermission(permission = "order:edit")
    public String editOrder() {
        return "Order edited";
    }
    @DeleteMapping("/{id}")
    @RequirePermission(permission = "order:delete")
    public String deleteOrder(@PathVariable Long id) {
        return "Order " + id + " deleted";
    }
}

如果还想同时检查角色，可以组合多个注解：

java

@RestController
@RequestMapping("/api/admin")
public class AdminController {
    @GetMapping("/dashboard")
    @RequireRole(role = "ADMIN")
    @RequirePermission(permission = "admin:dashboard")
    public String dashboard() {
        return "Admin dashboard";
    }
}

---

## 6. 三种方式的协同工作

在实际项目中，这三种方式常常**混合使用**：

- **Web 级** 用于拦截未认证请求，保护静态资源、登录页等。

- **方法级 `@PreAuthorize`** 用于业务方法细粒度控制，可结合自定义 Bean。

- **自定义注解** 用于统一权限表达，提高可读性和可维护性。

Spring Security 会依次检查：先经过过滤器链（Web级），再进入方法执行前的权限拦截（方法级）。两者都通过才算授权成功。

---

## 7. 总结对比

|特性|原生 Web 级配置|SpEL 注解（`@PreAuthorize`）|自定义注解|
|---|---|---|---|
|**配置位置**|`SecurityFilterChain`（集中）|各方法上（分散）|各方法上（分散）|
|**表达方式**|使用 `requestMatchers().hasRole()` 等|直接写 SpEL 表达式|自定义 Java 注解|
|**灵活性**|较低，适合固定路径规则|极高，可使用任意 SpEL 逻辑|中高，但受限于预定义表达式|
|**可维护性**|所有规则集中，便于审查|规则分散，但可复用 Bean|高度可读，语义清晰|
|**适用场景**|粗粒度资源保护（如 `/admin/**`）|细粒度业务方法权限校验|同一权限模型大量重复使用时|
|**审计重点**|检查 `permitAll` 路径和角色分配|检查 SpEL 表达式是否安全（如 `#id` 注入）|检查注解定义中的 SpEL 是否固定，防止绕过|

---

## 8. 审计建议

- **Web 级**：重点查看 `requestMatchers().permitAll()` 是否暴露了敏感接口；检查 `hasRole()` 是否与数据库角色一致。

- **SpEL 注解**：注意表达式是否引用了外部输入（如方法参数），防止权限绕过（例如 `#id == authentication.principal.id` 中若 `id` 为 `null` 可能异常）。

- **自定义注解**：确认注解内部的 SpEL 表达式固定，无动态拼接风险；确保自定义 Bean 的方法逻辑正确，避免被恶意调用。

以上就是三种实现方式的完整代码展示与总结。你可以根据项目实际需要灵活搭配使用。如果还有细节需要深入，欢迎继续提问！
