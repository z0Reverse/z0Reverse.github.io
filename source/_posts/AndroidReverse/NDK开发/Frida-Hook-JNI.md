---
title: Frida Hook JNI 实战
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - NDK开发
tags:
  - NDK
  - JNI
  - Native
---

# System.loadlibrary函数追踪
Android源码：https://cs.android.com/android/platform/superproject/+/android-latest-release:art/libnativeloader/native_loader.cpp;l=294?q=OpenNativeLibrary&sq=&ss=android

System.loadlibrary用于加载so文件，也是相当于java跟c通讯的开始。分析这个其实也就是so文件的加载
跟踪system.loadbrary整个流程调用链：Java → ART → Linker → 回调
**这里分析下android16的**
`System.loadLibrary()` 的加载机制是一个从 Java 层到 Native 层的完整调用过程。其核心调用链清晰地展示了 `.so` 文件是如何被查找并最终加载到内存中的。
整个过程可以概括为以下几个关键步骤：
1. **Java 层入口**：`System.loadLibrary()` 被调用。
2. **库名转换与路径查找**：将库的简短名称（如 "mylib"）转换为标准文件名（如 `libmylib.so`），并根据 ClassLoader 的配置在指定路径下查找其绝对路径。
3. **JNI 桥接**：通过 JNI 调用进入 Native 层。
4. **Native 层加载**：在 C++ 层执行最终的动态链接器函数 (`dlopen`) 来加载库文件。

### 🧬 详细调用链分析

#### 1. Java 层：`System.loadLibrary()`

一切的起点是 Java 代码中的 `System.loadLibrary("mylib")`。这个方法会委托给 `Runtime.loadLibrary0` 进行处理。

```java
1// java/lang/System.java
2public static void loadLibrary(String libname) {
3    Runtime.getRuntime().loadLibrary0(Reflection.getCallerClass(), libname);
4}
```

#### 2. Java 层：`Runtime.loadLibrary0()`

```java
1// java/lang/Runtime.java
2private synchronized void loadLibrary0(ClassLoader loader, Class<?> callerClass, String libname) {
3    // 1. 检查库名是否合法（不能包含路径分隔符）
4    if (libname.indexOf((int) File.separatorChar) != -1) {
5        throw new UnsatisfiedLinkError("Directory separator should not appear in library name: " + libname);
6    }
7
8    String filename = null;
9    // 2. 尝试通过 ClassLoader 查找库的绝对路径
10    if (loader != null && !(loader instanceof BootClassLoader)) {
11        // ClassLoader.findLibrary 会遍历其内部维护的 nativeLibraryPathElements 来查找
12        filename = loader.findLibrary(libname);
13        if (filename == null) {
14            throw new UnsatisfiedLinkError(loader + " couldn't find \"" + System.mapLibraryName(libname) + "\"");
15        }
16    }
17
18    // 3. 如果 loader 为 null 或查找失败，则使用默认的系统库路径
19    if (filename == null) {
20        getLibPaths(); // 初始化系统库路径，如 /system/lib, /vendor/lib
21        filename = System.mapLibraryName(libname); // 将 "mylib" 转换为 "libmylib.so"
22    }
23
24    // 4. 调用 Native 方法，进入 C++ 层
25    String error = nativeLoad(filename, loader, callerClass);
26    if (error != null) {
27        throw new UnsatisfiedLinkError(error);
28    }
29}
```

#### 3. JNI 桥接：`Runtime_nativeLoad`

`nativeLoad` 是一个 `native` 方法，它在 C++ 层的实现是 `Runtime_nativeLoad`。这个函数充当了 Java 和 Native 世界之间的桥梁。

```c++
1// art/openjdkjvm/OpenjdkJvm.cc
2JNIEXPORT jstring JNICALL
3Runtime_nativeLoad(JNIEnv* env, jclass ignored, jstring javaFilename, jobject javaLoader, jclass caller) {
4    // 直接调用 JVM 的实现函数
5    return JVM_NativeLoad(env, javaFilename, javaLoader, caller);
6}
```

#### 4. C++ 层：`JVM_NativeLoad`

这个函数是 ART (Android Runtime) 的一部分，它负责协调库的加载过程，并最终将任务交给 `JavaVMExt::LoadNativeLibrary`。

```C++
1// art/openjdkjvm/OpenjdkJvm.cc
2JNIEXPORT jstring JVM_NativeLoad(JNIEnv* env, jstring javaFilename, jobject javaLoader, jclass caller) {
3    ScopedUtfChars filename(env, javaFilename); // 将 Java String 转换为 C++ String
4    if (filename.c_str() == nullptr) {
5        return nullptr;
6    }
7
8    std::string error_msg;
9    art::JavaVMExt* vm = art::Runtime::Current()->GetJavaVM();
10
11    // 调用 JavaVMExt 的 LoadNativeLibrary 方法
12    bool success = vm->LoadNativeLibrary(env,
13                                         filename.c_str(),
14                                         javaLoader,
15                                         caller,
16                                         &error_msg);
17    if (success) {
18        return nullptr; // 加载成功，返回 null
19    }
20    // 加载失败，返回错误信息
21    return env->NewStringUTF(error_msg.c_str());
22}
```

#### 5. C++ 层：`JavaVMExt::LoadNativeLibrary`

这是 Native 层加载的核心逻辑。它首先会检查该库是否已经被加载过，以避免重复加载。如果未加载，则调用 `android::OpenNativeLibrary` 来执行真正的加载操作。

```c++
1// art/runtime/jni/java_vm_ext.cc
2bool JavaVMExt::LoadNativeLibrary(JNIEnv* env,
3                                  const std::string& path,
4                                  jobject class_loader,
5                                  jclass caller_class,
6                                  std::string* error_msg) {
7    // ... (检查库是否已加载的逻辑) ...
8
9    // 真正调用底层动态链接器的地方
10    void* handle = android::OpenNativeLibrary(env,
11                                              runtime_->GetTargetSdkVersion(),
12                                              path.c_str(),
13                                              class_loader,
14                                              caller_location.c_str(),
15                                              library_path.get(),
16                                              &needs_native_bridge,
17                                              &nativeloader_error_msg);
18
19    if (handle == nullptr) {
20        *error_msg = nativeloader_error_msg;
21        return false;
22    }
23
24    // ... (创建 SharedLibrary 对象来管理已加载的库) ...
25    return true;
26}
```

#### 6. Native 层：`android::OpenNativeLibrary`

这个函数是 Android 对标准 `dlopen` 的封装。它处理了 Android 特有的命名空间（Namespace）隔离机制。从 Android 7.0 开始，为了增强安全性，系统引入了命名空间来限制应用对私有系统库的访问。

```
1// art/libnativeloader/native_loader.cpp
2void* OpenNativeLibrary(JNIEnv* env, int32_t target_sdk_version, const char* path,
3                        jobject class_loader, const char* caller_location,
4                        const char* library_path, bool* needs_native_bridge,
5                        char** error_msg) {
6    void* handle = nullptr;
7
8    // 根据 class_loader 和 Android 版本，决定使用哪种方式加载
9    // 对于大多数应用层加载，会直接调用 dlopen
10    // 在更高版本或特定场景下，会使用 android_dlopen_ext 来处理命名空间
11    handle = dlopen(path, RTLD_NOW);
12
13    if (handle == nullptr) {
14        *error_msg = strdup(dlerror());
15    }
16    return handle;
17}
```bash

![](/images/Frida-Hook-JNI/20260419211751.png)
最终，`dlopen` 函数（或其扩展版本 `android_dlopen_ext`）会负责读取 `.so` 文件（一个 ELF 格式的文件），将其映射到进程的内存空间，进行符号重定位，并执行库的初始化函数（如 `.init_array` 和 `JNI_OnLoad`），从而完成整个加载过程。

# 动态注册
动态注册的native函数，调用链与静态区别很大，包括代码编写也是

### 静动态注册的区别：
静态注册会在so中通过JNIExport和JNICall强指定，对应java和c中函数方法，在使用的时候进行被动查找
动态注册会在加载so的时候主动一次性的在jvm中建立java与native的映射关系，实现方面会通过自定义的函数名和JNIONload进行绑定。jnionload加载后通过jniregister将java中的方法与本地方法进行绑定

### 流程：

#### 一：注册阶段 - 建立映射关系

这个阶段的触发点是 SO 库被加载到内存后。
1. **`System.loadLibrary()` 触发加载**
    当 Java 层调用 `System.loadLibrary("mylib")` 时，会触发systemloadlibrary完整加载链，最终由系统的 Linker (`dlopen`) 将 `libmylib.so` 加载到进程内存中。

2. **Linker 调用 `JNI_OnLoad`**
    SO 库加载完成后，Linker 会检查该库是否导出了 `JNI_OnLoad` 这个特殊函数。如果存在，Linker 会立即调用它。这是动态注册发生的关键时机。

3. **在 `JNI_OnLoad` 中执行 `RegisterNatives`**
    开发者会在 `JNI_OnLoad` 函数中编写逻辑，调用 JNI 提供的 `RegisterNatives` 函数来完成注册。这个过程是手动的，需要明确指定 Java 类和对应的 Native 方法。
    代码示例：

```c++
    1// libmylib.cpp
    2#include <jni.h>
    3
    4// 1. 实现真正的 Native 函数
    5jint myNativeMethod(JNIEnv* env, jobject thiz) {
    6    return 42;
    7}
    8
    9// 2. 定义一个 JNINativeMethod 数组，建立映射关系
    10//    这个数组描述了 Java 方法名、签名和 C++ 函数指针的对应关系
    11static JNINativeMethod gMethods[] = {
    12    {"nativeMethod", "()I", (void*)myNativeMethod}
    13};
    14
    15// 3. 实现 JNI_OnLoad 函数
    16extern "C" JNIEXPORT jint JNICALL
    17JNI_OnLoad(JavaVM* vm, void* reserved) {
    18    JNIEnv* env;
    19    // 获取 JNIEnv 指针
    20    if (vm->GetEnv(reinterpret_cast<void**>(&env), JNI_VERSION_1_6) != JNI_OK) {
    21        return JNI_ERR;
    22    }
    23
    24    // 4. 找到要注册 Native 方法的 Java 类
    25    jclass clazz = env->FindClass("com/example/myapp/MainActivity");
    26    if (clazz == nullptr) {
    27        return JNI_ERR;
    28    }
    29
    30    // 5. 调用 RegisterNatives 完成注册
    31    //    参数分别是：Java类对象, 映射关系数组, 数组元素个数
    32    jint result = env->RegisterNatives(clazz, gMethods, 1);
    33    if (result != JNI_OK) {
    34        return JNI_ERR;
    35    }
    36
    37    return JNI_VERSION_1_6;
    38}
```java

4. **JVM 内部存储映射**
RegisterNatives函数被调用后，JVM 会在内部的一个数据结构（通常是一个哈希表）中，将 com.example.myapp.MainActivity类中的 nativeMethod方法与 C++ 中的 myNativeMethod 函数指针直接关联起来。后续调用时，JVM 就可以直接查表找到函数指针，无需再进行任何字符串匹配。
#### 二：调用阶段 - 直接执行

当注册完成后，从 Java 层调用 Native 方法的流程就变得非常高效。

1. **Java 层发起调用**
```java

    1// MainActivity.java
    2public class MainActivity extends AppCompatActivity {
    3    static {
    4        System.loadLibrary("mylib"); // 触发注册阶段
    5    }
    6
    7    public native int nativeMethod(); // 声明 Native 方法
    8
    9    @Override
    10    protected void onCreate(Bundle savedInstanceState) {
    11        super.onCreate(savedInstanceState);
    12        // 6. 调用 Native 方法
    13        int result = nativeMethod();
    14    }
    15}
```bash

2. **JVM 直接查找并跳转**
    JVM 在执行到 `nativeMethod()` 时，会直接在其内部的注册表中查找该方法对应的函数指针。由于在 `JNI_OnLoad` 阶段已经完成了注册，查找过程是一次高效的哈希表查询，找到后便直接跳转到 C++ 的 `myNativeMethod` 函数执行。

# Frida Hook JNI
通过hook dlopen,android_dlopen_ext判断所有加载的so文件
本质是为了拦截JNIEnv函数表从而实现对JNI自身的函数进行hook，可用于实现Native层JNI调用的链路追踪
https://juejin.cn/post/7430494800236888099

# Frida Hook JNI参数、调用栈、返回值
通过hook到指定函数后，hook他的参数、调用栈和返回值

```javascript
Interceptor.attach(targetFunc.address, {

            onEnter(args) {

                console.log(`[Hook] 进入函数: ${targetFunc.name}`);

                // 根据函数签名读取参数，例如 args[0], args[1]...

                //console.log("传入参数：",args[2].readCString())

                // 读取 JNI 参数的正确方式：必须在 Java.perform 里操作或者Java.vm.tryGetEnv().getStringUtfChars(args[2])--

                // -->这里是char *指针，需要进一步提取指针的内容,readCString

                Java.perform(function() {

                    try {

                        const env = args[0];

                        const jstr = args[2];

                        const inputStr = Java.fromJString(jstr);

                        console.log("传入参数 (转换后):", inputStr);

                    } catch(e) {

                        console.log("读取参数失败:", e);

                    }

                });

            },

            onLeave(retval) {

                console.log(`[Hook] 原始返回值指针: ${retval}`);

                // 修改返回值：分配新字符串并替换

                const newValue = Memory.allocUtf8String("helloworld");

                retval.replace(newValue);

                console.log("[Hook] 返回值已被篡改");

            }

        });
```bash

# Frida invoke JNI（主动调用）
主动调用某个函数。一般某些方法如果没有被用到，你想主动去调用就需要invoke他，可参考frida-labs中某一关卡

```js
const funcPtr = Module.findExportByName(module.name, "Java_com_z0reverse_secondshell_MainActivity_md5");

    if (funcPtr) {

        // 6. 使用 NativeFunction 创建可调用的函数对象
        //这个地方对于pointer签名可以根据jadx中smail语法的来，快速填充
        // var adr = Module.findBaseAddress("libfrida0xa.so").add(0x18BB0)

        //针对地址不是ptr的还需要转换一次

        // var get_flag_ptr = new NativePointer(adr);nativefunction参数：地址，返回值，入参

        // const get_flag = new NativeFunction(get_flag_ptr, 'void', ['int', 'int']);

        const nativeFunc = new NativeFunction(funcPtr, 'pointer', ['pointer']);

        const input = Memory.allocUtf8String("主动调用测试数据");

        const result = nativeFunc(input);

        console.log(`[主动调用] 结果: ${result && result.readCString()}`);

    }
```
