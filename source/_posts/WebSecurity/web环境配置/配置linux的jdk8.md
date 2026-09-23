部分漏洞强烈依赖jdk8，例如fastjson的反序列化。为了实现vps的java版本也为8，记录下
这里将linux的jdk8通过xftp上传到vps服务器
实现多版本java环境，优先考虑update-alternatives进行，可供选择版本切换
## 一、先把多个 JDK 解压放到统一目录

假设把所有 jdk 放在 `/usr/local/java/`

```
# 创建目录
mkdir -p /usr/local/java
# 上传或者wget下载jdk压缩包，解压
# 示例：
# jdk8
tar -zxvf jdk8u391-linux-x64.tar.gz -C /usr/local/java/
# jdk17
tar -zxvf jdk-17.0.10_linux-x64_bin.tar.gz -C /usr/local/java/
```

解压后目录类似：

```
/usr/local/java/jdk1.8.0_391
/usr/local/java/jdk-17.0.10
```
![](images/Pasted%20image%2020260922210453.png)
---

## 使用 update-alternatives
### 1. 注册多个 java、javac

```
# 添加 JDK8
sudo update-alternatives --install /usr/bin/java java /usr/local/java/jdk1.8.0_391/bin/java 100
sudo update-alternatives --install /usr/bin/javac javac /usr/local/java/jdk1.8.0_391/bin/javac 100
```

```
# 添加 JDK17
sudo update-alternatives --install /usr/bin/java java /usr/local/java/jdk-17.0.10/bin/java 200
sudo update-alternatives --install /usr/bin/javac javac /usr/local/java/jdk-17.0.10/bin/javac 200
```

> 末尾数字是优先级，数字大默认优先。

### 2. 切换版本

```
sudo update-alternatives --config java
sudo update-alternatives --config javac
```

执行后会列出所有 jdk，输入序号选择。
![](images/Pasted%20image%2020260922210723.png)
### 3. 验证

```
java -version
javac -version
```

> ⚠️ 注意：alternatives 只切换 `java/javac` 命令，**JAVA_HOME 环境变量不会自动跟着变**。 很多程序（maven、tomcat）依赖 `JAVA_HOME`，需要额外处理。