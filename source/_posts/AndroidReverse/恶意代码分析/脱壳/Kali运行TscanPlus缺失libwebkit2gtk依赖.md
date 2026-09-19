---
title: Kali 运行 TscanPlus 缺失 libwebkit2gtk 依赖的解决过程
date: 2026-09-20 02:16:39
categories:
  - AndroidReverse
  - 恶意代码分析
tags:
  - 脱壳
  - 加固
  - 逆向
---

┌──(kali㉿kali)-[~/Desktop/web]
└─$ ./TscanPlus_Linux_Amd64
./TscanPlus_Linux_Amd64: error while loading shared libraries: libwebkit2gtk-4.0.so.37: cannot open shared object file: No such file or directory

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo apt install -y libwebkit2gtk-4.0-37
[sudo] password for kali:
Error: Unable to locate package libwebkit2gtk-4.0-37
Error: Couldn't find any package by glob 'libwebkit2gtk-4.0-37'

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo apt update
Get:1 http://mirrors.aliyun.com/kali kali-rolling InRelease [34.0 kB]
Get:2 http://mirrors.aliyun.com/kali kali-rolling/contrib Sources [84.0 kB]
Get:3 http://mirrors.aliyun.com/kali kali-rolling/main Sources [17.6 MB]
Get:4 http://mirrors.aliyun.com/kali kali-rolling/non-free Sources [119 kB]
Get:5 http://mirrors.aliyun.com/kali kali-rolling/main amd64 Packages [21.0 MB]
Hit:6 https://packages.microsoft.com/repos/code stable InRelease
Get:7 http://mirrors.aliyun.com/kali kali-rolling/main amd64 Contents (deb) [53.1 MB]
Hit:8 https://deb.nodesource.com/node_22.x nodistro InRelease
Get:9 http://mirrors.aliyun.com/kali kali-rolling/non-free amd64 Packages [189 kB]
Get:10 http://mirrors.aliyun.com/kali kali-rolling/non-free amd64 Contents (deb) [912 kB]
Get:11 http://mirrors.aliyun.com/kali kali-rolling/contrib amd64 Packages [120 kB]
Get:12 http://mirrors.aliyun.com/kali kali-rolling/contrib amd64 Contents (deb) [276 kB]
Fetched 11.9 MB in 21s (558 kB/s)
2240 packages can be upgraded. Run 'apt list --upgradable' to see them.

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo apt install -y libwebkit2gtk-4.0-37
Error: Unable to locate package libwebkit2gtk-4.0-37
Error: Couldn't find any package by glob 'libwebkit2gtk-4.0-37'

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo apt install -y libwebkit2gtk-4.1-0
The following packages were automatically installed and are no longer required:
  icu-devtools  libcrypt-dev  libgav1-1  libicu-dev
Use 'sudo apt autoremove' to remove them.

Upgrading:
  gir1.2-gstreamer-1.0  libavif16          libicu-dev                  libwebkit2gtk-4.1-0
  icu-devtools          libgstreamer1.0-0  libjavascriptcoregtk-4.1-0  libyuv0

Installing dependencies:
  libabsl20260107  libgav1-2  libicu78

Summary:
  Upgrading: 8, Installing: 3, Removing: 0, Not Upgrading: 2232
  Download size: 55.4 MB
  Space needed: 60.4 MB / 34.9 GB available

Get:1 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libgstreamer1.0-0 amd64 1.28.3-1 [1,466 kB]
Get:2 http://mirrors.aliyun.com/kali kali-rolling/main amd64 gir1.2-gstreamer-1.0 amd64 1.28.3-1 [119 kB]
Get:3 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libicu78 amd64 78.3-2 [10.0 MB]
Get:4 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libicu-dev amd64 78.3-2 [11.1 MB]
Get:5 http://mirrors.aliyun.com/kali kali-rolling/main amd64 icu-devtools amd64 78.3-2 [212 kB]
Get:6 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libabsl20260107 amd64 20260107.0-5 [549 kB]
Get:7 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libgav1-2 amd64 0.20.0-2+b1 [372 kB]
Get:8 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libyuv0 amd64 0.0.1922.20260106-1+b1 [175 kB]
Get:9 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libavif16 amd64 1.4.1-1+b1 [147 kB]
Get:10 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libwebkit2gtk-4.1-0 amd64 2.52.3-2 [23.7 MB]
Get:11 http://mirrors.aliyun.com/kali kali-rolling/main amd64 libjavascriptcoregtk-4.1-0 amd64 2.52.3-2 [7,522 kB]
Fetched 55.4 MB in 31s (1,812 kB/s)
(Reading database ... 422967 files and directories currently installed.)
Preparing to unpack .../00-libgstreamer1.0-0_1.28.3-1_amd64.deb ...
Unpacking libgstreamer1.0-0:amd64 (1.28.3-1) over (1.24.12-1) ...
Preparing to unpack .../01-gir1.2-gstreamer-1.0_1.28.3-1_amd64.deb ...
Unpacking gir1.2-gstreamer-1.0:amd64 (1.28.3-1) over (1.24.12-1) ...
Selecting previously unselected package libicu78:amd64.
Preparing to unpack .../02-libicu78_78.3-2_amd64.deb ...
Unpacking libicu78:amd64 (78.3-2) ...
dpkg: considering deconfiguration of libicu-dev:amd64, which would be broken by installation of icu-devtools ...
dpkg: yes, will deconfigure libicu-dev:amd64 (broken by icu-devtools)
Preparing to unpack .../03-icu-devtools_78.3-2_amd64.deb ...
De-configuring libicu-dev:amd64 (72.1-6), to allow installation of icu-devtools (78.3-2) ...
Unpacking icu-devtools (78.3-2) over (72.1-6) ...
Preparing to unpack .../04-libicu-dev_78.3-2_amd64.deb ...
Unpacking libicu-dev:amd64 (78.3-2) over (72.1-6) ...
Selecting previously unselected package libabsl20260107:amd64.
Preparing to unpack .../05-libabsl20260107_20260107.0-5_amd64.deb ...
Unpacking libabsl20260107:amd64 (20260107.0-5) ...
Selecting previously unselected package libgav1-2:amd64.
Preparing to unpack .../06-libgav1-2_0.20.0-2+b1_amd64.deb ...
Unpacking libgav1-2:amd64 (0.20.0-2+b1) ...
Preparing to unpack .../07-libyuv0_0.0.1922.20260106-1+b1_amd64.deb ...
Unpacking libyuv0:amd64 (0.0.1922.20260106-1+b1) over (0.0.1904.20250204-1) ...
Preparing to unpack .../08-libavif16_1.4.1-1+b1_amd64.deb ...
Unpacking libavif16:amd64 (1.4.1-1+b1) over (1.1.1-1) ...
Preparing to unpack .../09-libwebkit2gtk-4.1-0_2.52.3-2_amd64.deb ...
Unpacking libwebkit2gtk-4.1-0:amd64 (2.52.3-2) over (2.46.6-1) ...
Preparing to unpack .../10-libjavascriptcoregtk-4.1-0_2.52.3-2_amd64.deb ...
Unpacking libjavascriptcoregtk-4.1-0:amd64 (2.52.3-2) over (2.46.6-1) ...
Setting up libicu78:amd64 (78.3-2) ...
Setting up libjavascriptcoregtk-4.1-0:amd64 (2.52.3-2) ...
Setting up icu-devtools (78.3-2) ...
Setting up libabsl20260107:amd64 (20260107.0-5) ...
Setting up libyuv0:amd64 (0.0.1922.20260106-1+b1) ...
Setting up libicu-dev:amd64 (78.3-2) ...
Setting up libgstreamer1.0-0:amd64 (1.28.3-1) ...
Setcap worked! gst-ptp-helper is not suid!
Setting up gir1.2-gstreamer-1.0:amd64 (1.28.3-1) ...
Setting up libgav1-2:amd64 (0.20.0-2+b1) ...
Setting up libavif16:amd64 (1.4.1-1+b1) ...
Setting up libwebkit2gtk-4.1-0:amd64 (2.52.3-2) ...
Processing triggers for libc-bin (2.42-13) ...
Processing triggers for man-db (2.13.0-1) ...
Processing triggers for kali-menu (2025.1.1) ...

┌──(kali㉿kali)-[~/Desktop/web]
└─$ ./TscanPlus_Linux_Amd64
./TscanPlus_Linux_Amd64: error while loading shared libraries: libwebkit2gtk-4.0.so.37: cannot open shared object file: No such file or directory

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo ldconfig

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo ln -s /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.0.so.37

┌──(kali㉿kali)-[~/Desktop/web]
└─$ ./TscanPlus_Linux_Amd64
./TscanPlus_Linux_Amd64: error while loading shared libraries: libjavascriptcoregtk-4.0.so.18: cannot open shared object file: No such file or directory

┌──(kali㉿kali)-[~/Desktop/web]
└─$ sudo ln -s /usr/lib/x86_64-linux-gnu/libjavascriptcoregtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libjavascriptcoregtk-4.0.so.18

┌──(kali㉿kali)-[~/Desktop/web]
└─$ ./TscanPlus_Linux_Amd64
[08:03:33] [WARNING] config.db不存在，创建中...stat /home/kali/Desktop/web/config/config.db: no such file or directory /home/kali/Desktop/web/config/config.db /home/kali/Desktop/web/config /home/kali/Desktop/web/config
[08:03:33] [WARNING] config.db不存在，备份中...stat /home/kali/Desktop/web/config/config.db: no such file or directory
Config file backed up to /home/kali/Desktop/web/config/config_bak01.yaml
[08:03:35] [+] TscanPlus有效时间：2028.01.01
[08:03:35] [WARNING] Verify Key Error:文件License.lic不存在，以

个问题的原因很直接：**Kali Linux 的滚动更新机制已经把旧版本的库移除了**，所以系统提示找不到这个包。

Kali 是滚动发行版，软件包版本更新很快[](https://unix.stackexchange.com/questions/792032/installiing-libwebkit2gtk-4-0-37/792033#792033)。你需要的旧版 `libwebkit2gtk-4.0-37` 已经被新版 `libwebkit2gtk-4.1-0` 取代了，所以你直接搜索旧版包名当然找不到[](https://pkg.kali.org/pkg/webkit2gtk)[](https://pkg.kali.org/news/677053/webkit2gtk-2505-1-imported-into-kali-rolling/)。

好消息是，解决起来也很简单，主要推荐**方案一**。

### 方案一：安装新版库（推荐）

既然旧版找不到了，直接让系统安装新版库就行。新版是兼容的，能解决TscanPlus的依赖问题。

打开终端，执行下面的命令安装新版库：

bash

sudo apt update
sudo apt install -y libwebkit2gtk-4.1-0

### 方案二：给旧版库建立一个软链接

如果你出于某种原因必须使用旧版的 `libwebkit2gtk-4.0.so.37`，安装完新版库后，也可以通过创建一个“软链接”来满足程序的需求。

**操作步骤：**

1. **首先**，按照方案一安装 `libwebkit2gtk-4.1-0`。

2. 接着，执行下面的命令，创建一个从新版文件指向旧版文件名的链接：

    bash

    # 让系统能找到刚安装的新版库文件
    sudo ldconfig
    # 创建一个软链接，让程序找 libwebkit2gtk-4.0.so.37 时，被引导到新版的库文件上
    sudo ln -s /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.0.so.37

### 方案三：使用AppImage版本（备选）

如果上面的方法都遇到问题，还可以使用TscanPlus的AppImage格式。这种格式把依赖都打包好了，不用管系统的库文件。

你可以从TscanPlus的GitHub发布页下载 `TscanPlus_v*.*_Linux_x86_64.AppImage` 文件，然后直接运行。

---

**操作建议**：

最省事的做法就是直接用**方案一**，安装新版的 `libwebkit2gtk-4.1-0`。

bash

sudo apt install -y libwebkit2gtk-4.1-0

安装完成后，再次运行 `./TscanPlus_Linux_Amd64` 试试。如果还有报错，把新的错误信息发给我，我帮你再看看。

──(kali㉿kali)-[~/Desktop/web] └─$ ./TscanPlus_Linux_Amd64 ./TscanPlus_Linux_Amd64: error while loading shared libraries: libwebkit2gtk-4.0.so.37: cannot open shared object file: No such file or directory ┌──(kali㉿kali)-[~/Desktop/web] └─$ sudo ldconfig ┌──(kali㉿kali)-[~/Desktop/web] └─$ sudo ln -s /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.0.so.37 ┌──(kali㉿kali)-[~/Desktop/web] └─$ ./TscanPlus_Linux_Amd64 ./TscanPlus_Linux_Amd64: error while loading shared libraries: libjavascriptcoregtk-4.0.so.18: cannot open shared object file: No such file or directory

好的，现在又缺少另一个库了。继续用同样的方法创建软链接：

bash

# 创建 javascriptcoregtk 的软链接
sudo ln -s /usr/lib/x86_64-linux-gnu/libjavascriptcoregtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libjavascriptcoregtk-4.0.so.18

# 再次运行试试
./TscanPlus_Linux_Amd64

如果还有其他缺失的库，继续用这个模式补全即可。

---

### 一次性补全所有可能的依赖

为了避免一个一个地试，可以直接把所有可能需要的库都链接上：

bash

# 创建所有可能缺失的软链接
sudo ln -sf /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.0.so.37
sudo ln -sf /usr/lib/x86_64-linux-gnu/libjavascriptcoregtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libjavascriptcoregtk-4.0.so.18
sudo ln -sf /usr/lib/x86_64-linux-gnu/libsoup-3.0.so.0 /usr/lib/x86_64-linux-gnu/libsoup-2.4.so.1
sudo ln -sf /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.1.so.0 /usr/lib/x86_64-linux-gnu/libwebkit2gtk-4.0.so.37

# 更新库缓存
sudo ldconfig

# 运行
./TscanPlus_Linux_Amd64

---

### 如果还缺其他库

运行这个命令来查看具体缺什么：

bash

ldd ./TscanPlus_Linux_Amd64 | grep "not found"

把输出结果发给我，我帮你一次性把所有缺失的库都找出来并创建对应的软链接。
