---
title: JNI 接口详解
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - NDK开发
tags:
  - NDK
  - JNI
  - Native
---

# 常见基础知识

## `extern "C"` 是干什么的？
**告诉 C++ 编译器：按照 C 语言的规则编译这段代码，不要做 C++ 的名字改编（name mangling）。**
1. Java 找本地方法时，是**按固定函数名**查找的（比如 `Java_com_example_MainActivity_test`）。
2. C++ 编译器会自动给函数改名（为了支持重载），Java 就找不到对应的 C 函数了。
3. 加了 `extern "C"`，函数名保持原样，Java 才能正确映射调用。
**JNI 代码写在.cpp 文件里，必须加 extern "C"，写在.c 文件里不用加。**

---

## 为什么 Java 方法没参数，C 函数却有 `JNIEnv*` 和 `jobject`？

这两个是**JNI 自动隐式传递**的固定参数，**不是你手动传的**，所有 Java 映射的本地方法都必须带。
**`JNIEnv* env`**
- 是**JNI 环境指针**，所有 JNI 操作都靠它。
- 作用：操作 Java 字符串、数组、创建对象、调用 Java 方法、抛出异常等。
- 你在 C/C++ 里操作 Java 数据，**必须用 env**。
 **`jobject thiz`**

- 代表**调用这个本地方法的 Java 对象本身**。
- 如果是 Java **static 方法**，这里类型是 `jclass`（代表类对象）。
- 作用：可以通过它调用 Java 层的方法、访问成员变量。

**这两个是 JNI 框架自动传入的，固定写在参数列表最前面。**

## Java ↔ JNI 类型对应表（完整版）

### 1. 基本数据类型

|Java 类型|JNI C 类型|描述|
|---|---|---|
|boolean|jboolean|无符号 8 位|
|byte|jbyte|有符号 8 位|
|char|jchar|无符号 16 位|
|short|jshort|有符号 16 位|
|int|jint|有符号 32 位|
|long|jlong|有符号 64 位|
|float|jfloat|32 位浮点数|
|double|jdouble|64 位浮点数|

### 2. 引用数据类型（对象 / 数组）

|Java 类型|JNI C 类型|
|---|---|
|java.lang.Object|jobject|
|java.lang.String|jstring|
|java.lang.Class|jclass|
|各类数组|对应数组类型|
|boolean[]|jbooleanArray|
|byte[]|jbyteArray|
|char[]|jcharArray|
|short[]|jshortArray|
|int[]|jintArray|
|long[]|jlongArray|
|float[]|jfloatArray|
|double[]|jdoubleArray|
|Object[]|jobjectArray|

---

## `NewStringUTF` 和 `GetStringUTFChars` 是干什么的？

这两个是**Java 字符串和 C 字符串互相转换**的核心函数。

### 1. `NewStringUTF`

**作用：把 C/C++ 的 UTF-8 字符串 → 转为 Java 的 String 对象。用于 C 层 返回字符串给 Java。

```
return (*env)->NewStringUTF(env, "Hello JNI");
```

### 2. `GetStringUTFChars`

**作用：把 Java 的 String 对象 → 转为 C/C++ 可读的 UTF-8 字符串。**

- 用于接收 Java 传过来的字符串,必须配套 `ReleaseStringUTFChars` 释放内存，否则泄漏！

```
// Java String → C字符串
    const char* str = (*env)->GetStringUTFChars(env, jstr, NULL);

    // 使用完必须释放！
    (*env)->ReleaseStringUTFChars(env, jstr, str);

```bash

# HookJNIEnv

从java层传递数据---jni--c：监听这个数据的流转过程：从java到c，c处理完后再从c返回到java
主要监听GetStringUTFChars和NewStringUTF

Java代码：

```java
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    binding = ActivityMainBinding.inflate(getLayoutInflater());
    setContentView(binding.getRoot());

    // Example of a call to a native method
    TextView tv = binding.sampleText;
    tv.setText(md5("Hello world"));
}
public native String md5(String str);
```

C代码

```c++
extern "C" JNIEXPORT
jstring JNICALL Java_com_z0reverse_secondshell_MainActivity_md5(JNIEnv *env, jobject thiz, jstring input) {
    if (input == nullptr) {
        return env->NewStringUTF("");
    }

    // Java String -> C++ 字符串
    const char *str = env->GetStringUTFChars(input, nullptr);
    uint8_t digest[16];
    md5String(str, digest);
    env->ReleaseStringUTFChars(input, str);

    // 转成 32 位小写 MD5 字符串
    char hex[33];
    for (int i = 0; i < 16; i++) {
        sprintf(hex + i * 2, "%02x", digest[i]);
    }
    hex[32] = '\0';

    return env->NewStringUTF(hex);
}
```javascript

JS进行hook trace

```js

function hook_libart() {

    var symbols = Module.enumerateSymbolsSync("libart.so");

    var addrGetStringUTFChars = null;

    var addrNewStringUTF = null;

    var addrFindClass = null;

    var addrGetMethodID = null;

    var addrGetStaticMethodID = null;

    var addrGetFieldID = null;

    var addrGetStaticFieldID = null;

    var addrRegisterNatives = null;

    var so_name = "lib";      //TODO 这里写需要过滤的so

    for (var i = 0; i < symbols.length; i++) {

        var symbol = symbols[i];

        if (symbol.name.indexOf("art") >= 0 &&

            symbol.name.indexOf("JNI") >= 0 &&

            symbol.name.indexOf("CheckJNI") < 0 &&

            symbol.name.indexOf("_ZN3art3JNIILb0") >= 0

        ) {

            if (symbol.name.indexOf("GetStringUTFChars") >= 0) {

                addrGetStringUTFChars = symbol.address;

                console.log("GetStringUTFChars is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("NewStringUTF") >= 0) {

                addrNewStringUTF = symbol.address;

                console.log("NewStringUTF is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("FindClass") >= 0) {

                addrFindClass = symbol.address;

                console.log("FindClass is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("GetMethodID") >= 0) {

                addrGetMethodID = symbol.address;

                console.log("GetMethodID is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("GetStaticMethodID") >= 0) {

                addrGetStaticMethodID = symbol.address;

                console.log("GetStaticMethodID is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("GetFieldID") >= 0) {

                addrGetFieldID = symbol.address;

                console.log("GetFieldID is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("GetStaticFieldID") >= 0) {

                addrGetStaticFieldID = symbol.address;

                console.log("GetStaticFieldID is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("RegisterNatives") >= 0) {

                addrRegisterNatives = symbol.address;

                console.log("RegisterNatives is at ", symbol.address, symbol.name);

            } else if (symbol.name.indexOf("CallStatic") >= 0) {

                console.log("CallStatic is at ", symbol.address, symbol.name);

                Interceptor.attach(symbol.address, {

                    onEnter: function (args) {

                        var module = Process.findModuleByAddress(this.returnAddress);

                        if (module != null && module.name.indexOf(so_name) == 0) {

                            var java_class = args[1];

                            var mid = args[2];

                            var class_name = Java.vm.tryGetEnv().getClassName(java_class);

                            if (class_name.indexOf("java.") == -1 && class_name.indexOf("android.") == -1) {

                                var method_name = prettyMethod(mid, 1);

                                console.log("<>CallStatic:", DebugSymbol.fromAddress(this.returnAddress), class_name, method_name);

                            }

                        }

                    },

                    onLeave: function (retval) { }

                });

            } else if (symbol.name.indexOf("CallNonvirtual") >= 0) {

                console.log("CallNonvirtual is at ", symbol.address, symbol.name);

                Interceptor.attach(symbol.address, {

                    onEnter: function (args) {

                        var module = Process.findModuleByAddress(this.returnAddress);

                        if (module != null && module.name.indexOf(so_name) == 0) {

                            var jobject = args[1];

                            var jclass = args[2];

                            var jmethodID = args[3];

                            var obj_class_name = Java.vm.tryGetEnv().getObjectClassName(jobject);

                            var class_name = Java.vm.tryGetEnv().getClassName(jclass);

                            if (class_name.indexOf("java.") == -1 && class_name.indexOf("android.") == -1) {

                                var method_name = prettyMethod(jmethodID, 1);

                                console.log("<>CallNonvirtual:", DebugSymbol.fromAddress(this.returnAddress), class_name, obj_class_name, method_name);

                            }

                        }

                    },

                    onLeave: function (retval) { }

                });

            } else if (symbol.name.indexOf("Call") >= 0 && symbol.name.indexOf("Method") >= 0) {

                console.log("Call<>Method is at ", symbol.address, symbol.name);

                Interceptor.attach(symbol.address, {

                    onEnter: function (args) {

                        var module = Process.findModuleByAddress(this.returnAddress);

                        if (module != null && module.name.indexOf(so_name) == 0) {

                            var java_class = args[1];

                            var mid = args[2];

                            var class_name = Java.vm.tryGetEnv().getObjectClassName(java_class);

                            if (class_name.indexOf("java.") == -1 && class_name.indexOf("android.") == -1) {

                                var method_name = prettyMethod(mid, 1);

                                console.log("<>Call<>Method:", DebugSymbol.fromAddress(this.returnAddress), class_name, method_name);

                            }

                        }

                    },

                    onLeave: function (retval) { }

                });

            }

        }

    }

    if (addrGetStringUTFChars != null) {

        Interceptor.attach(addrGetStringUTFChars, {

            onEnter: function (args) {

            },

            onLeave: function (retval) {

                if (retval != null) {

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var bytes = Memory.readCString(retval);

                        console.log("[GetStringUTFChars] result:" + bytes, DebugSymbol.fromAddress(this.returnAddress));

                    }

                }

            }

        });

    }

    if (addrNewStringUTF != null) {

        Interceptor.attach(addrNewStringUTF, {

            onEnter: function (args) {

                if (args[1] != null) {

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var string = Memory.readCString(args[1]);

                        console.log("[NewStringUTF] bytes:" + string, DebugSymbol.fromAddress(this.returnAddress));

                    }

                }

            },

            onLeave: function (retval) { }

        });

    }

    if (addrFindClass != null) {

        Interceptor.attach(addrFindClass, {

            onEnter: function (args) {

                if (args[1] != null) {

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var name = Memory.readCString(args[1]);

                        console.log("[FindClass] name:" + name, DebugSymbol.fromAddress(this.returnAddress));

                    }

                }

            },

            onLeave: function (retval) { }

        });

    }

    if (addrGetMethodID != null) {

        Interceptor.attach(addrGetMethodID, {

            onEnter: function (args) {

                if (args[2] != null) {

                    var clazz = args[1];

                    var class_name = Java.vm.tryGetEnv().getClassName(clazz);

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var name = Memory.readCString(args[2]);

                        if (args[3] != null) {

                            var sig = Memory.readCString(args[3]);

                            console.log("[GetMethodID] class_name:" + class_name + " name:" + name + ", sig:" + sig, DebugSymbol.fromAddress(this.returnAddress));

                        } else {

                            console.log("[GetMethodID] class_name:" + class_name + " name:" + name, DebugSymbol.fromAddress(this.returnAddress));

                        }

                    }

                }

            },

            onLeave: function (retval) { }

        });

    }

    if (addrGetStaticMethodID != null) {

        Interceptor.attach(addrGetStaticMethodID, {

            onEnter: function (args) {

                if (args[2] != null) {

                    var clazz = args[1];

                    var class_name = Java.vm.tryGetEnv().getClassName(clazz);

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var name = Memory.readCString(args[2]);

                        if (args[3] != null) {

                            var sig = Memory.readCString(args[3]);

                            console.log("[GetStaticMethodID] class_name:" + class_name + " name:" + name + ", sig:" + sig, DebugSymbol.fromAddress(this.returnAddress));

                        } else {

                            console.log("[GetStaticMethodID] class_name:" + class_name + " name:" + name, DebugSymbol.fromAddress(this.returnAddress));

                        }

                    }

                }

            },

            onLeave: function (retval) { }

        });

    }

    if (addrGetFieldID != null) {

        Interceptor.attach(addrGetFieldID, {

            onEnter: function (args) {

                if (args[2] != null) {

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var name = Memory.readCString(args[2]);

                        if (args[3] != null) {

                            var sig = Memory.readCString(args[3]);

                            console.log("[GetFieldID] name:" + name + ", sig:" + sig, DebugSymbol.fromAddress(this.returnAddress));

                        } else {

                            console.log("[GetFieldID] name:" + name, DebugSymbol.fromAddress(this.returnAddress));

                        }

                    }

                }

            },

            onLeave: function (retval) { }

        });

    }

    if (addrGetStaticFieldID != null) {

        Interceptor.attach(addrGetStaticFieldID, {

            onEnter: function (args) {

                if (args[2] != null) {

                    var module = Process.findModuleByAddress(this.returnAddress);

                    if (module != null && module.name.indexOf(so_name) == 0) {

                        var name = Memory.readCString(args[2]);

                        if (args[3] != null) {

                            var sig = Memory.readCString(args[3]);

                            console.log("[GetStaticFieldID] name:" + name + ", sig:" + sig, DebugSymbol.fromAddress(this.returnAddress));

                        } else {

                            console.log("[GetStaticFieldID] name:" + name, DebugSymbol.fromAddress(this.returnAddress));

                        }

                    }

                }

            },

            onLeave: function (retval) { }

        });

    }

    if (addrRegisterNatives != null) {

        Interceptor.attach(addrRegisterNatives, {

            onEnter: function (args) {

                console.log("[RegisterNatives] method_count:", args[3], DebugSymbol.fromAddress(this.returnAddress));

                var env = args[0];

                var java_class = args[1];

                var class_name = Java.vm.tryGetEnv().getClassName(java_class);

                var methods_ptr = ptr(args[2]);

                var method_count = parseInt(args[3]);

                for (var i = 0; i < method_count; i++) {

                    var name_ptr = Memory.readPointer(methods_ptr.add(i * Process.pointerSize * 3));

                    var sig_ptr = Memory.readPointer(methods_ptr.add(i * Process.pointerSize * 3 + Process.pointerSize));

                    var fnPtr_ptr = Memory.readPointer(methods_ptr.add(i * Process.pointerSize * 3 + Process.pointerSize * 2));

                    var name = Memory.readCString(name_ptr);

                    var sig = Memory.readCString(sig_ptr);

                    var find_module = Process.findModuleByAddress(fnPtr_ptr);

                    console.log("[RegisterNatives] java_class:", class_name, "name:", name, "sig:", sig, "fnPtr:", fnPtr_ptr, "module_name:", find_module.name, "module_base:", find_module.base, "offset:", ptr(fnPtr_ptr).sub(find_module.base));

                }

            },

            onLeave: function (retval) { }

        });

    }

}

setImmediate(hook_libart);
```

结果：

### 补充知识：
1、通过ps去找我们的应用的进程，再根据进程号通过cat /proc/pid/maps可以列举进程的libart.so，将so导出后通过nm命令可以列举所有符号=等效于frida的**Module.enumerateSymbolsSync("libart.so")**
2、使用Thread.backtrace()可以获取native层的调用栈信息

```
Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n')
```bash

- 实现原理：通过拦截函数调用并打印调用链，但准确性受JavaScript VM堆栈帧影响
- - 两种模式：
    - 模糊模式(Backtracer.FUZZY)：通过堆栈取证猜测返回地址，可能产生误报但适用于任意二进制
    - 精确模式(Backtracer.ACCURATE)：默认模式，依赖调试友好二进制或调试信息

# 自动hook JNIEnv：jnitracer源码
https://juejin.cn/post/7430494800236888099
