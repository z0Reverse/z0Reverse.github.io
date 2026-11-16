---
title: "rConfig useradmin.inc.php 信息泄露漏洞"
date: 2026-10-18 09:15:36
categories:
  - WebSecurity
  - CVE
  - "IoT"
  - "rConfig"
tags:
  - "rConfig"
  - "信息泄露"
  - "漏洞复现"
---
## 漏洞描述

rConfig useradmin.inc.php 存在信息泄露漏洞，通过访问文件获取用户邮箱信息和登录名

## 漏洞影响

```
rConfig
```

## 网络测绘

```
app="rConfig"
<details>
<summary>POC 代码（点击展开 · 仅供学习，请勿用于非授权测试）</summary>

<pre><code class="language-text">
## 漏洞复现

出现漏洞的文件

```php
&lt;?php
/* Includes */
require_once("../classes/db2.class.php");
include_once('../classes/paginator.class.php');

/* Instantiate DB Class */
$db2 = new db2();

// get timezone for later
$db2-&gt;query("SELECT timeZone FROM settings");
$result = $db2-&gt;resultsetCols();
$timeZone = $result[0];
date_default_timezone_set($timeZone);

/* Get Row count from users where NOT deleted */
$db2-&gt;query('SELECT COUNT(*) AS total FROM users WHERE status = 1');
$row = $db2-&gt;resultsetCols();
$result["total"] = $row[0];
/* Instantiate Paginator Class */
$pages = new Paginator;
$pages-&gt;items_total = $result['total'];
$pages-&gt;mid_range = 7; // Number of pages to display. Must be odd and &gt; 3
$pages-&gt;paginate();
echo $pages-&gt;display_pages();
echo "&lt;span class=\"\"&gt;" . $pages-&gt;display_jump_menu() . $pages-&gt;display_items_per_page() . "&lt;/span&gt;";

/* GET all nodes records from DB */
$db2-&gt;query("SELECT id, username, userlevel, email, timestamp FROM users WHERE status = 1 $pages-&gt;limit");
$resultSelect = $db2-&gt;resultset();
// push rows to $itesm array
$items = array();
foreach ($resultSelect as $row) {
    array_push($items, $row);
}
/* Create Multidimensional array for use later */
$result["rows"] = $items;
$i = 0; # row counter  to enable alternate row coloring
?&gt;

&lt;table id="userAddTbl" class="tableSimple"&gt;
    &lt;thead&gt;
    &lt;th rowspan="2"&gt;&lt;input type="checkbox" disabled="disabled"/&gt;&lt;/th&gt;
    &lt;th rowspan="2"&gt;Username&lt;/th&gt;
    &lt;th rowspan="2"&gt;E-mail&lt;/th&gt;
    &lt;th rowspan="2"&gt;User Level&lt;/th&gt;
    &lt;th rowspan="2"&gt;Last Login&lt;/th&gt;
&lt;/thead&gt;
&lt;tbody&gt;
    &lt;?php
    foreach ($result['rows'] as $rows):
        $id = $rows['id'];
        /* This bit just updates the class='row' bit with an alternating 1 OR 0 for alternative row coloring */
        echo '&lt;tr class="row' . ($i++ % 2) . '"&gt;';
        ?&gt;
    &lt;td align="center"&gt;&lt;input type="checkbox" name="tablecheckbox" id="&lt;?php echo $id; ?&gt;"/&gt;&lt;/td&gt;
    &lt;td align="center"&gt;&lt;strong&gt;&lt;?php echo $rows['username'] ?&gt;&lt;/strong&gt;&lt;/td&gt;
    &lt;td align="center"&gt;&lt;?php echo $rows['email'] ?&gt;&lt;/td&gt;
    &lt;td align="center"&gt;
        &lt;?php
        // quick check if userlevel =9 user is admin else, user is a User
        if ($rows['userlevel'] == 9) {
            $userlevel = "Admin";
        } else {
            $userlevel = "User";
        }
        echo $userlevel;
        ?&gt;&lt;/td&gt;
    &lt;td align="center"&gt;
        &lt;?php
        // quick convert unix TimeStamp to normal times
        $lastLogin = date('H:i d-m-Y', $rows['timestamp']);
        echo $lastLogin;
        ?&gt;
    &lt;/td&gt;
    &lt;/tr&gt;
&lt;?php endforeach; ?&gt;
&lt;/tbody&gt;
&lt;/table&gt;

&lt;?php
echo $pages-&gt;display_pages();
echo "&lt;div class=\"spacer\"&gt;&lt;/div&gt;";
echo "&lt;p class=\"paginate\"&gt;Page: $pages-&gt;current_page of $pages-&gt;num_pages&lt;/p&gt;\n";</code></pre>

</details>

文件没有设定权限，任何人可以访问泄露信息

漏洞验证的Url为

```plain
/useradmin.inc.php
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/iot/images/202202162242982.png)

泄露用户信息

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/iot/rConfig-useradmin.inc.php-%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.md)
