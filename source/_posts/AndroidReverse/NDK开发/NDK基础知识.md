---
title: NDK 基础知识
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - NDK开发
tags:
  - NDK
  - JNI
  - Native
---

Google提供两种开发方式：SDK、NDK
NDK用c语言编写，通过JNI实现c语言和java语言的胡同，更好的使用底层能力
![](/images/NDK基础知识/20260414221155.png)

## 常见配置及作用

### CMakeLists.txt

```cmake
# 1. 指定CMake最低版本（必须和AS中CMake版本匹配）
cmake_minimum_required(VERSION 3.22.1)
# 2. 项目名称（随便起，不影响最终SO库名）
project("myjnidemo")
# 3. 定义要编译的C/C++源文件
# 作用：告诉CMake，需要编译哪些.c/.cpp文件
# 格式：add_library(库名 编译类型 源文件路径)
add_library( # 生成的SO库名称 → 最终会生成 libnative-lib.so
	native-lib
	# 编译类型：SHARED=动态库(.so)，STATIC=静态库(.a)
	SHARED
	# 你的C代码文件（可以写多个，用空格分隔）
	native-lib.c )
# 4. 导入系统预编译库
# 作用：使用Android系统提供的原生库（如日志库、OpenSL ES等）
find_library(
	# 定义变量名，存储系统库路径
	log-lib
	# 要查找的系统库名称 → android.util.Log 对应的C层日志库
	log )
# 5. 链接库（最关键！）
# 作用：把 自定义库 + 系统库 链接在一起，否则调用系统API会报错
target_link_libraries(
# 要链接的目标库（就是第3步定义的native-lib）
	native-lib
	# 链接的系统库（第4步定义的log-lib）
	${log-lib} )
```

多个so对应多个cpp时候

```java
cmake_minimum_required(VERSION 3.22.1)
project("easymd5")
//libeasymd5.so
add_library(${CMAKE_PROJECT_NAME} SHARED

        md5github.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME}
        android
        log)
//libtest.so
add_library(test SHARED test.cpp)
target_link_libraries(test android log)
```

单个so对应多个cpp时候

```
cmake_minimum_required(VERSION 3.22.1)
project("easymd5")
//libeasymd5.so
add_library(${CMAKE_PROJECT_NAME} SHARED

        md5github.cpp test.cpp shell.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME}
        android
        log)

```

### so库中的c代码结构

```java
// 1. 必须引入的JNI头文件（核心！提供Java和C交互的所有类型/函数）
#include <jni.h>
// 2. 可选：引入Android日志库（用于C层打印日志，替代printf）
#include <android/log.h>
// 3. 日志宏定义（方便打印，TAG是日志标签）
#define LOG_TAG "MY_SO"
#define LOGD(...) __android_log_print(ANDROID_LOG_DEBUG, LOG_TAG, __VA_ARGS__)
#define LOGE(...) __android_log_print(ANDROID_LOG_ERROR, LOG_TAG, __VA_ARGS__)
// 4. JNI函数（Java能调用的C函数，必须遵守命名规则）
// 命名规则：Java_完整包名_类名_方法名 // 例：Java_com_example_myapp_MainActivity_stringFromJNI
//这个是静态注册函数
JNIEXPORT jstring JNICALL Java_com_example_myapp_MainActivity_stringFromJNI(JNIEnv *env, jobject thiz) {
	// 5. 业务逻辑代码：C语言实现的功能
	LOGD("C层代码执行成功");
	 // 6. 返回数据给Java：将C字符串转为Java字符串
	return (*env)->NewStringUTF(env, "Hello from C SO库!");
}
// 7. 自定义C函数（仅供C内部调用，Java无法直接访问）
int add(int a, int b) {
	 return a + b;
}

//8.动态注册函数
jsting native_getString(JNIEnv *env,jobject thisz){
	LOGD("动态注册")
	return (*env)->NewStringUTF(env,"hello dynamic register")
}
jint native_add(JNIEnv *env, jobject thiz, jint a, jint b) {
	LOGD("计算：%d + %d = %d", a, b, a + b);
	return a + b;
}
//将java方法和c函数进行手动绑定
//{ "Java方法名", "方法签名", (void*)对应的C函数 }
static const JNINativeMethod g_methods[]={
	{"getString","()Ljava/lang/String;",(void*)native_getString};
	{"add","(II)I",(void*)native_add},
};
jint JNI_OnLoad(JavaVM *vm,void *reserved){
	JNIEnv *env=Null;
	if ((*vm)->GetEnv(vm, (void**)&env, JNI_VERSION_1_6) != JNI_OK)
	{ return JNI_ERR; }
	// 2. 要注册的 Java 类全路径（非常重要）
	const char *className = "com/example/myapp/MainActivity";
	// 3. 找到类
	jclass clazz = (*env)->FindClass(env, className);
	if (clazz == NULL) { return JNI_ERR; }
	// 4. 执行注册
	//这里注册是拿着java的类clazz，c的方法，c方法的个数。每个在具体就是根据g_method提前定义好的格式去java中找指定方法将其绑定到c方法
	int methodCount = sizeof(g_methods) / sizeof(g_methods[0]);
	if ((*env)->RegisterNatives(env, clazz, g_methods, methodCount) != JNI_OK) { return JNI_ERR; }
	LOGD("JNI 动态注册成功！");
	// 返回JNI版本
	return JNI_VERSION_1_6;
}
```

### 添加适配的架构
Gradle(app)中

```
android{
	defaultConfig{
		ndk{
			abiFilters'arm64-v8a','x86_64'
		}
	}
}
```

### Java跟C参数对应的形式

| Java    | JNI      | 描述         |
| ------- | -------- | ---------- |
| boolean | jboolean | 无符号的char类型 |
|         |          |            |
|         |          |            |
|         |          |            |
|         |          |            |
|         |          |            |
|         |          |            |
|         |          |            |
|         |          |            |
