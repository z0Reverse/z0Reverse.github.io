前端js采用aes密钥、iv随机生成（一般都有规则，不会纯随机），aes加密请求体，rsa公钥加密aes密钥，传输给后端
![](pic/Pasted%20image%2020260621062721.png)
![](pic/Pasted%20image%2020260621062734.png)
去分析encryptedBody
定位到login.js中，随机生成aes密钥以及iv，然后将body进行加密采用cbc模式，body格式
”username:password“格式
![](pic/Pasted%20image%2020260621062908.png)
打断点尝试
![](pic/Pasted%20image%2020260621063457.png)
思路：
1、注入aes加密前，让aeskey永远为我们固定的值。同时需要注入rsa加密aes密钥处
![](pic/Pasted%20image%2020260621064644.png)
```js
// ========== AES Key、IV 自定义固定值（自行替换） ==========
// AES-256 32字节 十六进制（64位hex）
const FIX_AES_KEY_HEX = "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff";
// IV 16字节 十六进制（32位hex）
const FIX_IV_HEX = "112233445566778899aabbccddeeff00";

// 缓存原始随机函数
let originalWordArrayRandom;

// 转换十六进制字符串为 WordArray
function hexToWordArray(hexStr) {
    return CryptoJS.enc.Hex.parse(hexStr);
}

// Hook CryptoJS.lib.WordArray.random
function hookCryptoRandom() {
    // 保存原生方法
    originalWordArrayRandom = CryptoJS.lib.WordArray.random;
    
    CryptoJS.lib.WordArray.random = function(size) {
        // 判断长度区分 AESKey(32) / IV(16)
        if (size === 32) {
            // 生成固定32字节AES密钥
            return hexToWordArray(FIX_AES_KEY_HEX);
        } else if (size === 16) {
            // 生成固定16字节IV
            return hexToWordArray(FIX_IV_HEX);
        } else {
            // 其他长度走原生随机
            return originalWordArrayRandom(size);
        }
    };
}

// 等待 CryptoJS 加载完成再 Hook
function waitCryptoJSAndHook() {
    if (window.CryptoJS && CryptoJS.lib && CryptoJS.lib.WordArray) {
        hookCryptoRandom();
        console.log("[Hook成功] CryptoJS.random 已劫持，固定AES Key/IV");
    } else {
        setTimeout(waitCryptoJSAndHook, 10);
    }
}
waitCryptoJSAndHook();
```

Hook成功，进行验证
这是hook成功后的数据，现在进行aes解密验证
```
x-key: okrkPcxIHub0EjiKmkjyCFw6R4G12IDBz1grLJlcZnOoCS0GMAZWXU4CrRYDSrxQ2PxqqHAbGcnbB1ZLKfXOhZzPLZgGWUMan6SUDe50ZhSnMGBAfYUfCJQLcyXmxvdqA7BVvtL+DpqhBSr3o/TnmXYu7Zgb8o8sK7kXn59GACU+4DOXzoSqhnErAOv0boBP0xzXiYFeEL2M+/0DMa+CRQSyv8s5V8dQVuQI+hqncCaw+NgkmRFPfTcrUqNq/p+z8AFWMFSxEc+AO5A9Y4YqacZkktju0l+IimCLdSUuV1dz9C653RJvwpeHEG49PW9zutVLMlQbENG9RSWQWrXjpw==
Accept: */*
Origin: http://121.37.229.118:8080
Referer: http://121.37.229.118:8080/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_49889d9149ea3475919030325b18afef=1764308241,1764685415

{"encryptedBody":"ESIzRFVmd4iZqrvM3e7/AKkLykgip5J2oyuHHe/VO3U="}
```
解密失败，再去看代码发现，加密的数据这里，吧iv拼接进去了（重点！！！如果iv没有特殊规则，随机生成，那么后端就必须拿到iv，否则解密肯定不成功。这里是吧iv放到加密后的数据中进行了拼接）
![](pic/Pasted%20image%2020260621070859.png)
所以解密脚本
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# ===================== 固定参数（必须与前端 Hook 一致） =====================
# AES-256 密钥（32 字节），十六进制字符串（64 个 hex 字符）
FIXED_AES_KEY_HEX = "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
# IV（16 字节），十六进制字符串（32 个 hex 字符）
FIXED_IV_HEX = "112233445566778899aabbccddeeff00"

# 将 hex 转为字节
KEY = bytes.fromhex(FIXED_AES_KEY_HEX)
IV = bytes.fromhex(FIXED_IV_HEX)


def decrypt_login_payload(encrypted_body_b64: str) -> str:
    """
    解密 /api/auth/login 请求中的 encryptedBody 字段

    :param encrypted_body_b64: 请求体中的 encryptedBody 值（Base64 字符串）
    :return: 明文字符串，格式 "username:password"
    """
    # 1. Base64 解码得到 IV(16) + 密文 的拼接字节
    combined = base64.b64decode(encrypted_body_b64)

    # 2. 拆分：前 16 字节为 IV，剩余为密文（这里直接用固定 IV，也可从数据中提取）
    # 从数据中提取 IV 仅供校验，实际解密用固定 IV
    iv_from_data = combined[:16]
    ciphertext = combined[16:]

    # （可选）校验 iv_from_data 是否等于固定 IV，若不相等则可能被篡改或密钥不匹配
    if iv_from_data != IV:
        print("[警告] 数据中的 IV 与固定 IV 不一致，仍使用固定 IV 继续解密")

    # 3. AES-CBC 解密
    cipher = AES.new(KEY, AES.MODE_CBC, IV)  # 使用固定 IV
    decrypted_padded = cipher.decrypt(ciphertext)

    # 4. 去除 PKCS7 填充
    try:
        decrypted = unpad(decrypted_padded, AES.block_size)
    except ValueError:
        # 如果填充不对，可能是密钥/IV错误，或数据损坏
        raise ValueError("解密失败，可能密钥/IV不正确或数据损坏")

    # 5. 转为 UTF-8 字符串
    return decrypted.decode('utf-8')


# ========================== 使用示例 ==========================
if __name__ == "__main__":
    # 示例：从浏览器的 Network 面板复制 encryptedBody 值
    sample = "ESIzRFVmd4iZqrvM3e7/AKkLykgip5J2oyuHHe/VO3U="
    try:
        plain = decrypt_login_payload(sample)
        print(f"解密成功: {plain}")
    except Exception as e:
        print(f"解密失败: {e}")

    # 如果是从完整请求体 JSON 中解析，可以这样：
    # with open('request.json', 'r') as f:
    #     data = json.load(f)
    #     encrypted_body = data['encryptedBody']
    #     print(decrypt_login_payload(encrypted_body))
```
验证
![](pic/Pasted%20image%2020260621071155.png)

接下来做自动脚本，实现前端hook，解密明文到bp，bp转发出去给服务端还是密文
**浏览器 → mitmproxy(解密) → Burp(看到明文/修改) → mitmproxy(加密) → 服务器**
思路：mitA脚本，监听8081端口并将数据进行解密，转给上游代理8080（burpsui）
burpsuit开启上游代理转给mitB脚本，B脚本再根据原始加密逻辑进行还原
mit命令
![](pic/Pasted%20image%2020260621082001.png)
![](pic/Pasted%20image%2020260621081829.png)
![](pic/Pasted%20image%2020260621082018.png)
mit脚本：
```python
# decrypt_proxy.py  
# 启动命令：mitmproxy -p 8081 --mode upstream:http://127.0.0.1:8080 -s decrypt_proxy.py  
import json  
import base64  
from Crypto.Cipher import AES  
from Crypto.Util.Padding import unpad  
from mitmproxy import http  
  
# ========== 固定 AES Key/IV 和最初保持一致 ==========FIX_AES_KEY_HEX = "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"  
FIX_IV_HEX = "112233445566778899aabbccddeeff00"  
KEY = bytes.fromhex(FIX_AES_KEY_HEX)  
IV = bytes.fromhex(FIX_IV_HEX)  
  
def decrypt_aes_cbc(encrypted_b64: str) -> str | None:  
    """原始解密逻辑：base64(IV+密文)，丢弃数据包内IV，使用固定IV解密"""  
    try:  
        combined = base64.b64decode(encrypted_b64)  
        ciphertext = combined[16:]  
        cipher = AES.new(KEY, AES.MODE_CBC, IV)  
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)  
        return decrypted.decode('utf-8')  
    except Exception as e:  
        print(f"[解密失败] {e}")  
        return None  
  
def request(flow: http.HTTPFlow) -> None:  
    print("\n===== 解密代理8081 收到请求 =====")  
    print(f"原始路径: {flow.request.path}, Method: {flow.request.method}")  
    print(f"原始请求体: {flow.request.text}")  
    # 打印当前携带的x-key，确认不会丢失  
    origin_xkey = flow.request.headers.get("x-key", "无")  
    print(f"当前携带x-key: {origin_xkey[:80]}...")  
  
    # 仅处理 POST + application/json    if flow.request.method != "POST":  
        print("跳过：非POST请求，原样放行")  
        return  
    content_type = flow.request.headers.get("Content-Type", "")  
    if "application/json" not in content_type:  
        print("跳过：非JSON请求，原样放行")  
        return  
  
    # 备份全部原始内容，异常时完整恢复（防止丢header/body）  
    origin_body = flow.request.text  
  
    try:  
        body = json.loads(flow.request.text)  
        encrypted_body = body.get("encryptedBody")  
        if not encrypted_body:  
            print("跳过：无encryptedBody字段，不修改请求，所有头完整保留")  
            return  
  
        # 执行解密  
        plain = decrypt_aes_cbc(encrypted_body)  
        if plain is None:  
            print("解密返回空，放弃修改请求体，原始流量透传")  
            return  
  
        print(f"解密明文：{plain}")  
        # 拆分账号密码，构造明文JSON  
        if ":" in plain:  
            username, password = plain.split(":", 1)  
            new_body = json.dumps({"username": username, "password": password}, separators=(',', ':'))  
        else:  
            new_body = plain  
  
        # 只替换请求体，【完全不碰任何请求头，不删除x-key！】  
        flow.request.text = new_body  
        print(f"已替换为明文请求体: {new_body}")  
        # 移除了之前 flow.request.headers.pop("x-key", None) 这行删除代码  
  
    except Exception as e:  
        print(f"解密处理异常，恢复原始完整请求: {repr(e)}")  
        # 异常恢复原始body，所有header（包含x-key）维持不变，不会丢失  
        flow.request.text = origin_body
```

mitB脚本
```python
# encrypt_proxy.py  
# 启动命令：mitmproxy -p 8082 -s encrypt_proxy.py  
import json  
import base64  
from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad  
from mitmproxy import http  
  
# ========== 固定 AES Key/IV 沿用原来配置 ==========FIX_AES_KEY_HEX = "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"  
FIX_IV_HEX = "112233445566778899aabbccddeeff00"  
KEY = bytes.fromhex(FIX_AES_KEY_HEX)  
IV = bytes.fromhex(FIX_IV_HEX)  
  
def encrypt_aes_cbc(plaintext: str) -> str:  
    """沿用原始逻辑：固定IV，返回 Base64(IV + Ciphertext)"""    cipher = AES.new(KEY, AES.MODE_CBC, IV)  
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))  
    combined = IV + ciphertext  
    return base64.b64encode(combined).decode('utf-8')  
  
def request(flow: http.HTTPFlow) -> None:  
    print("\n===== 加密代理8082 收到明文请求 =====")  
    print(f"原始Body: {flow.request.text}")  
    x_key_val = flow.request.headers.get("x-key", "")  
    print(f"透传原始x-key: {x_key_val[:60]}...")  
  
    # 只处理 POST + application/json    if flow.request.method != "POST":  
        print("跳过：非POST")  
        return  
    content_type = flow.request.headers.get("Content-Type", "")  
    if "application/json" not in content_type:  
        print("跳过：非JSON请求")  
        return  
  
    # 备份原始内容，异常时恢复，防止400  
    orig_body = flow.request.text  
  
    try:  
        body = json.loads(flow.request.text)  
        username = body.get("username")  
        password = body.get("password")  
        if username is None or password is None:  
            print("跳过：无username/password，不加密，原样转发")  
            return  
  
        # 拼接明文 username:password        plain = f"{username}:{password}"  
        encrypted_body = encrypt_aes_cbc(plain)  
        print(f"生成encryptedBody: {encrypted_body}")  
  
        # 构造加密请求体  
        new_body = json.dumps({"encryptedBody": encrypted_body}, separators=(',', ':'))  
        flow.request.text = new_body  
  
        # x-key 不做任何修改，直接透传，不新增、不删除、不RSA加密  
        # 删掉手动设置Content-Length（关键修复400）  
        print(f"替换后加密请求体: {new_body}")  
  
    except Exception as e:  
        print(f"加密处理异常，恢复原始明文包: {repr(e)}")  
        # 出错还原原始body，不发送非法加密数据包  
        flow.request.text = orig_body
```