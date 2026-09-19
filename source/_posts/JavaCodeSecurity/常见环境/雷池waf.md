---
title: 雷池waf
date: 2026-09-20 02:16:39
categories:
  - JavaCodeSecurity
  - 常见环境
tags:
  - 环境搭建
  - WAF
---

## 1、安装Docker
华为云提供了自己的 Docker CE 镜像仓库，速度有保障：

```bash
# 1. 更新 apt 索引并安装依赖
apt-get update
apt-get install -y ca-certificates curl
# 2. 添加华为云 Docker 的 GPG 密钥和仓库
curl -fsSL https://repo.huaweicloud.com/docker-ce/linux/ubuntu/gpg | apt-key add -
echo "deb [arch=amd64] https://repo.huaweicloud.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
# 3. 安装 Docker
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io
# 4. 启动并验证
systemctl start docker
systemctl enable docker
docker version
```

## 2、配置镜像加速器

为了提高后续拉取雷池镜像的速度，配置华为云免费加速器：

1. 登录华为云控制台，进入 **容器镜像服务 SWR** → **镜像中心** → **镜像加速器**，复制您的专属加速器地址（类似 `https://<id>.mirror.swr.myhuaweicloud.com`）。

2. 创建 `/etc/docker/daemon.json`：

```
mkdir -p /etc/docker
    cat > /etc/docker/daemon.json <<EOF
    {
      "registry-mirrors": ["https://<你的加速器ID>.mirror.swr.myhuaweicloud.com"]
    }
    EOF
```

3. 重启 Docker：

```
systemctl daemon-reload
systemctl restart docker
```

## 3、 最后安装雷池 WAF

Docker 就绪后，直接执行官方一键安装命令（针对华为云，加上 `CDN=1` 参数）：

```
CDN=1 bash -c "$(curl -fsSLk https://waf-ce.chaitin.cn/release/latest/setup.sh)"
```

按提示注册管理员账号，然后访问 `https://你的服务器IP:9443` 即可。

## 4、常见问题

### 1、拉取镜像失败
解决：
1、使用 Docker Hub 官方镜像源（推荐）
雷池官方在 Docker Hub 上也有镜像，速度通常更稳定。你可以通过设置环境变量 `IMAGE_PREFIX` 来覆盖默认仓库地址。
**操作步骤**：
1. **退出当前安装**（如果还在运行，按 `Ctrl+C` 终止）。
2. **重新执行安装命令，并指定镜像前缀**：

```
IMAGE_PREFIX=docker.io/chaitin/safeline CDN=1 bash -c "$(curl -fsSLk https://waf-ce.chaitin.cn/release/latest/setup.sh)"
```

2、阿里云镜像

```
IMAGE_PREFIX=registry.cn-hangzhou.aliyuncs.com/chaitin/safeline CDN=1 bash -c "$(curl -fsSLk https://waf-ce.chaitin.cn/release/latest/setup.sh)"
```

3、考虑是出口的443端口没有开放

[INFO] Initial username：admin
[INFO] Initial password：MTgaSXFL
[INFO] Done
[SafeLine] 雷池 WAF 社区版安装成功，请访问以下地址访问控制台
[SafeLine] https://172.31.12.142:9443/
[SafeLine] https://172.17.0.1:9443/
[SafeLine] https://172.22.222.1:9443/

雷池waf是类似于映射的关系。真实的服务器在8080端口，在配置的时候就需要这样，当然对外暴露的也就是8088端口提供服务
![](/images/雷池waf/20260627002026.png)
