---
title: Hash
date: 2026-09-20 02:16:38
categories:
  - AndroidReverse
  - 加解密算法
tags:
  - 加解密
  - 算法逆向
---

# MD5

```java
public static String hash(String data) {
    try {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashInBytes = md.digest(data.getBytes());

        // bytes to hex
        StringBuilder hash = new StringBuilder();
        for (byte b : hashInBytes) {
            hash.append(String.format("%02x", b));
        }

        return hash.toString();

    } catch (NoSuchAlgorithmException e) {
        e.printStackTrace();
        return null;
    }
}
```bash

# SHA256

```java
public static String hash(String data) {
    try {
        MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
        byte[] hashInBytes = sha256.digest(data.getBytes());

        // bytes to hex
        StringBuilder hash = new StringBuilder();
        for (byte b : hashInBytes) {
            hash.append(String.format("%02x", b));
        }

        return hash.toString();

    } catch (NoSuchAlgorithmException e) {
        e.printStackTrace();
        return null;
    }
}
```
