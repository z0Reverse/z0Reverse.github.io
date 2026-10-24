# -*- coding: utf-8 -*-
"""
将 Threekiii/Vulnerability-Wiki（PeiQi 文库）的漏洞文档整理导入到 Hexo 博客：
  源：docs-base/docs/<源分类>/xxx.md
  目标：source/_posts/WebSecurity/CVE/<一级分类>/<产品>/xxx.md
并补齐本项目约定的 front-matter（title / date / categories / tags），
相对图片链接统一改写为远端绝对地址（避免把 800+MB 图片拷进仓库）。
"""
import os
import re
import sys
import urllib.parse
from collections import OrderedDict

SRC_ROOT = r"e:/AIForCode/githubweb/_vulnwiki_tmp/docs-base/docs"
DST_ROOT = r"e:/AIForCode/githubweb/source/_posts/WebSecurity/CVE"

# 源分类 -> 本项目 CVE 下的一级分类
CAT_MAP = OrderedDict([
    ("cms",        "cms"),
    ("framework",  "三方组件"),
    ("middleware", "中间件"),
    ("database",   "数据库"),
    ("webapp",     "Web应用"),
    ("oa",         "OA"),
    ("iot",        "IoT"),
    ("cloud",      "云原生"),
    ("ai",         "AI"),
    ("os",         "操作系统"),
    ("language",   "编程语言"),
    ("others",     "其他"),
])

RAW_BASE = "https://raw.githubusercontent.com/Threekiii/Vulnerability-Wiki/master/docs-base/docs"
BLOB_BASE = "https://github.com/Threekiii/Vulnerability-Wiki/blob/master/docs-base/docs"

# ---------- 产品名提取 ----------

# 触发截断的“漏洞描述类”关键词（出现在 token 中即认为产品名到此为止）
STOP_PAT = re.compile(
    r"(漏洞|RCE|rce|命令执行|命令注入|代码执行|代码注入|反序列化|SQL注入|注入|任意文件|文件上传|文件读取|"
    r"文件下载|文件写入|文件删除|文件包含|SSRF|ssrf|XSS|xss|CSRF|未授权|认证绕过|鉴权绕过|权限绕过|"
    r"身份验证|身份|绕过|信息泄露|信息泄漏|泄露|泄漏|目录遍历|目录穿越|路径穿越|跨站|SSTI|XXE|拒绝服务|"
    r"提权|后门|硬编码|伪造|弱口令|越权|getshell|GetShell|表达式|溢出|逃逸|劫持|枚举|拒绝|沙箱|"
    r"列目录|变量覆盖|条件竞争|竞态|逻辑|解析|配置错误|CRLF|Cookie|cookie|读取|上传|下载|写入|删除|"
    r"执行|遍历|穿越|登录|越界|缓存|插件|模块|组件|接口|后台|前台|默认|口令)"
)
VERSION_PAT = re.compile(r"^[vV]?[0-9＜＜≤≥>=~]")
SYMBOL_PAT = re.compile(r"^[^\w]+$", re.UNICODE)
SHORT_PAT = re.compile(r"^[A-Za-z]{1,2}$|^[A-Za-z]\d+$")
ID_PAT = re.compile(r"^(CVE|CNVD|CNNVD|QVD|MS|EDB|S2|SPARK|NVD)[-_]?\d+", re.I)
EXT_PAT = re.compile(
    r"\.(php|asp|aspx|jsp|jspx|cgi|js|action|do|cfm|sh|py|class|inc|xml|json|log|cfg|svg|html|htm|ini|conf)$",
    re.I)
# 产品名里通常要去掉的“入口/端点”词
ENTRY_WORDS = {
    "api", "web", "console", "server", "dashboard", "manager", "admin", "ui", "cli",
    "service", "plugin", "images", "viewer", "client", "tools", "viewer", "portal",
    "controller", "config", "class", "index", "shell",
}

# 产品归并表：优先匹配完整名，其次前两段，其次首段
PRODUCT_ALIAS = {
    # ---- Apache 系 ----
    "apache-ofbiz": "Apache-OFBiz", "apache-struts": "Apache-Struts2",
    "apache-http": "Apache-HTTPd", "apache-tomcat8": "Apache-Tomcat",
    "tomcat8": "Apache-Tomcat", "tomcat": "Apache-Tomcat",
    "apache-skywalking": "Apache-SkyWalking",
    "apache-activemq-jolokia": "Apache-ActiveMQ", "apache-kafka-clients": "Apache-Kafka",
    "apache-commons": "Apache-Commons",
    "apache-log4j": "log4j", "apache-log4j2": "log4j",
    # ---- Java 容器 / 中间件 ----
    "weblogic": "Weblogic", "weblogic-xmldecoder": "Weblogic", "weblogic-ldap": "Weblogic",
    "weblogic-wls": "Weblogic", "weblogic-uddiexplorer": "Weblogic", "weblogic-t3": "Weblogic",
    "weblogic-local": "Weblogic",
    "jboss": "JBoss", "jboss-jmxinvokerservlet": "JBoss",
    "jenkins": "Jenkins", "jenkins-ci": "Jenkins", "jenkins-cli": "Jenkins",
    "jenkins-xstream": "Jenkins", "jenkins-checkscript": "Jenkins", "jenkins-script": "Jenkins",
    "jetty": "Jetty", "jetty-web": "Jetty", "jetty-通用": "Jetty",
    "geoserver": "GeoServer",
    "consul": "Consul",
    "saltstack": "SaltStack", "saltstack-minion": "SaltStack",
    "zabbix": "Zabbix", "zabbix-server": "Zabbix",
    "vmware": "VMware",
    "nginx": "Nginx",
    "uwsgi": "uWSGI",
    "goahead": "GoAhead", "goahead-server": "GoAhead",
    "next.js": "Next.js",
    # ---- 三方组件 / 框架 ----
    "fastjson": "Fastjson",
    "jackson": "Jackson", "jackson-databind": "Jackson",
    "xstream": "XStream",
    "spring": "Spring", "spring-framework": "Spring", "spring-cloud": "Spring",
    "spring-data": "Spring", "spring-security": "Spring", "spring-messaging": "Spring",
    "spring-webflow": "Spring", "spring-框架因": "Spring",
    "thinkphp": "ThinkPHP", "thinkphp5": "ThinkPHP",
    "django": "Django", "django-gis": "Django", "django-jsonfield": "Django",
    "django-querySet.order_by()": "Django", "django-debug": "Django", "django-trunc(kind)": "Django",
    "laravel": "Laravel", "laravel-.env": "Laravel", "laravel-filemanager插件": "Laravel",
    "laravel-ignition": "Laravel", "laravel-小于": "Laravel",
    "rails": "Ruby-On-Rails", "rails-accept": "Ruby-On-Rails", "rails-sprockets": "Ruby-On-Rails",
    "vite": "Vite", "vite-开发服务器": "Vite", "vite-开发服务器通过": "Vite",
    "flask": "Flask-Jinja2", "flask-jinja2": "Flask-Jinja2",
    # ---- CMS ----
    "wordpress": "WordPress", "wordpress-all": "WordPress", "wordpress-duplicator": "WordPress",
    "wordpress-elementor": "WordPress", "wordpress-file": "WordPress", "wordpress-redux": "WordPress",
    "wordpress-simple": "WordPress", "wordpress-superforms": "WordPress", "wordpress-wp_query": "WordPress",
    "wordpress-3dprint": "WordPress",
    "wordpress": "WordPress", "wordpress-3dprint": "WordPress",
    "drupal": "Drupal", "drupal-core": "Drupal", "drupal-drupalgeddon": "Drupal",
    "joomla": "Joomla", "joomla-application": "Joomla",
    "discuz": "Discuz", "discuz!x": "Discuz", "discuz!x3.4": "Discuz",
    "weiphp3.0": "WeiPHP", "weiphp5.0": "WeiPHP", "weiphp5.0-download_imgage": "WeiPHP",
    "pbootcms": "PbootCMS", "pbootcms-domain": "PbootCMS", "pbootcms-search": "PbootCMS",
    "cmseasy": "CmsEasy", "cmseasy-crossall_act.php": "CmsEasy",
    "cmseasy-language_admin.php": "CmsEasy", "cmseasy-update_admin.php": "CmsEasy",
    "opensns": "OpenSNS",
    "极致cms": "极致CMS", "极致cms-后台文件编辑插件": "极致CMS",
    "pbcms": "Pb-CMS",
    "doccms": "DocCMS", "doccms-keyword": "DocCMS",
    "pigcms": "PigCMS", "shopxo": "ShopXO", "shopxo-download": "ShopXO",
    "lifetray": "Liferay", "liferay-portal": "Liferay",
    "oneblog": "OneBlog", "oneblog-开源博客管理系统": "OneBlog",
    "yzmcms": "YzmCMS", "yzmcms-version": "YzmCMS",
    "74cms": "74CMS", "cms-made": "CMS-Made-Simple", "emlog": "emlog",
    "craftcms": "CraftCMS", "craft-cms": "CraftCMS",
    "发货100": "发货100", "原创先锋": "原创先锋",
    # ---- 数据库 ----
    "elasticsearch": "Elasticsearch", "elastic": "Elasticsearch",
    "mysql": "MySQL", "mysql-udf": "MySQL",
    "redis": "Redis", "redis-lua": "Redis", "redis-小于5.0.5": "Redis",
    "influxdb": "InfluxDB", "influxdb-jwt": "InfluxDB",
    "h2-database": "H2-Database", "h2-database-web-console": "H2-Database",
    "clickhouse": "ClickHouse", "clickhouse-api": "ClickHouse",
    "mongodb": "MongoDB", "mongodb-zlib": "MongoDB",
    "neo4j": "Neo4j", "neo4j-shell": "Neo4j",
    # ---- Web 应用 / OA ----
    "jira": "Jira", "atlassian-jira": "Jira", "atlassian-bitbucket": "Bitbucket",
    "atlassian": "Atlassian", "confluence": "Confluence", "atlassian-confluence": "Confluence",
    "apache-kylin": "Apache-Kylin", "payaramicro": "PayaraMicro", "h3c": "H3C",
    "jeecg": "Jeecg", "jellyfin": "Jellyfin", "云时空": "云时空", "亿赛通": "亿赛通",
    "昆石网络": "昆石网络", "金蝶oa": "金蝶OA", "aveva": "AVEVA", "huggingface": "Huggingface",
    "泛微oa": "泛微OA", "泛微": "泛微OA",
    "致远oa": "致远OA", "致远": "致远OA",
    "用友": "用友", "用友-nc": "用友", "用友-u8": "用友", "用友-grp": "用友",
    "万户oa": "万户OA", "蓝凌oa": "蓝凌OA", "信呼oa": "信呼OA",
    "金和oa": "金和OA", "金和oa-c6": "金和OA",
    "通达oa": "通达OA", "启莱oa": "启莱OA",
    "nexus": "Nexus", "nexus-repository": "Nexus", "nexus-repository-manager": "Nexus",
    "f5": "F5-BIG-IP", "f5-big": "F5-BIG-IP",
    "jumpserver": "JumpServer", "gogs": "Gogs", "harbor": "Harbor", "gitlab": "GitLab",
    "showdoc": "ShowDoc", "metasphere": "MeterSphere",
    "webmin": "Webmin", "adminer": "Adminer", "coremail": "Coremail",
    "ghostscript": "GhostScript", "imagemagick": "ImageMagick",
    "pgadmin": "pgAdmin", "pgadmin-≤": "pgAdmin",
    "1panel": "1Panel", "afterlogic": "Afterlogic-Aurora",
    "360天擎": "360天擎", "1039家校通": "1039家校通",
    "浪潮clusterenginev4.0": "浪潮ClusterEngineV4.0",
    "深信服": "深信服", "深信服-edr": "深信服", "深信服-ngaf下一代防火墙": "深信服",
    "深信服-应用交付管理系统": "深信服",
    "金山": "金山", "帆软报表": "帆软报表", "若依管理系统": "若依管理系统",
    # ---- IoT / 网络设备 ----
    "d-link": "D-Link", "d-link-dir": "D-Link", "d-link-dsl": "D-Link",
    "d-link-dap": "D-Link", "d-link-dcs": "D-Link", "d-link-ac": "D-Link",
    "tenda": "Tenda", "tenda-w15e": "Tenda", "腾达": "Tenda", "腾达-路由器": "Tenda",
    "zyxel": "Zyxel", "zyxel-nbg2105": "Zyxel",
    "tp-link": "TP-Link", "cisco": "Cisco", "cisco-hyperflex": "Cisco",
    "hikvision": "HIKVISION", "hikvision-ivms": "HIKVISION",
    "hikvision-流媒体管理服务器": "HIKVISION", "hikvision-视频编码设备接入网关": "HIKVISION",
    "大华": "大华", "大华-智慧园区综合管理平台": "大华",
    "锐捷": "锐捷", "锐捷-eg易网关": "锐捷", "锐捷-nbr": "锐捷",
    "网康": "网康", "网康-ns": "网康", "网康-下一代防火墙": "网康",
    "奇安信": "奇安信", "奇安信-网康": "奇安信",
    "安恒": "安恒", "安恒-明御安全网关": "安恒",
    "启明星辰": "启明星辰", "启明星辰-天清汉马usg防火墙": "启明星辰",
    "中科网威": "中科网威", "中科网威-下一代防火墙控制系统": "中科网威",
    "天融信": "天融信", "天融信-topapp": "天融信",
    "绿盟": "绿盟", "绿盟-sas堡垒机": "绿盟",
    "小米": "小米", "小米-路由器": "小米",
    "中国移动": "中国移动", "中国移动-禹路由": "中国移动",
    "wayos": "Wayos", "wayos-防火墙": "Wayos",
    "selea": "Selea", "selea-ocr": "Selea",
    "rconfig": "rConfig", "kyan": "Kyan", "kyan-网络监控设备": "Kyan",
    "宏电": "宏电", "宏电-h8922": "宏电",
    "terraMaster": "TerraMaster", "terramaster-tos": "TerraMaster",
    "apache-apisix": "Apache-APISIX",
    "netmizer": "NetMizer", "netmizer-日志管理系统": "NetMizer",
    # ---- 云原生 / AI / 系统 / 语言 ----
    "kubernetes": "Kubernetes", "docker": "Docker",
    "vmware-vcenter": "VMware-vCenter", "vmware-vcenter-server": "VMware-vCenter",
    "nacos": "Nacos", "minio": "MinIO",
    "ollama": "Ollama", "langflow": "Langflow",
    "linux": "Linux", "linux-kernel": "Linux", "linux-sudo": "Linux",
    "windows": "Windows", "windows-win32k": "Windows",
    "php": "PHP", "php-fpm": "PHP-FPM", "php-利用": "PHP",
    "python": "Python", "python-gradio": "Gradio", "python-pil": "Pillow",
    "java": "Java", "java-rmi": "Java-RMI", "java-rmi-registry": "Java-RMI",
    "microsoft": "Microsoft", "microsoft-exchange": "Microsoft-Exchange",
    "openssh": "OpenSSH", "openssl": "OpenSSL",
}

# 漏洞类型 -> 标签
TAG_RULES = [
    ("SQL注入", ["SQL注入", "sql注入", "SQL-注入"]),
    ("命令执行", ["命令执行", "命令注入"]),
    ("代码执行", ["代码执行", "远程代码执行", "RCE", "rce"]),
    ("反序列化", ["反序列化"]),
    ("任意文件读取", ["任意文件读取", "文件读取", "本地文件包含", "文件包含"]),
    ("任意文件下载", ["文件下载"]),
    ("文件上传", ["文件上传", "getshell", "GetShell"]),
    ("任意文件写入", ["文件写入"]),
    ("任意文件删除", ["文件删除"]),
    ("目录遍历", ["目录遍历", "路径穿越", "目录穿越"]),
    ("SSRF", ["SSRF", "ssrf", "服务端请求伪造"]),
    ("XSS", ["XSS", "xss", "跨站脚本"]),
    ("CSRF", ["CSRF", "跨站请求伪造"]),
    ("未授权访问", ["未授权"]),
    ("认证绕过", ["认证绕过", "身份验证绕过", "鉴权绕过", "权限绕过"]),
    ("信息泄露", ["信息泄露", "信息泄漏", "敏感信息", "源码泄露"]),
    ("SSTI", ["SSTI", "模板注入"]),
    ("XXE", ["XXE", "XML外部实体", "实体注入"]),
    ("弱口令", ["弱口令", "默认口令", "硬编码"]),
    ("提权", ["提权", "权限提升"]),
    ("越权", ["越权", "水平权限", "垂直权限"]),
    ("拒绝服务", ["拒绝服务", "DoS"]),
    ("JNDI注入", ["JNDI"]),
    ("表达式注入", ["SpEL", "SPEL", "表达式注入"]),
]

IMG_PAT = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
LINK_PAT = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def posix_join(a, b):
    if not a or a == ".":
        return b
    return a.rstrip("/") + "/" + b


_SAFE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~/!$&'()*+,;=:@")
_ESC = re.compile(r"[0-9A-Fa-f]{2}")


def urlenc(path):
    """URL 编码：保留已存在的 %XX 转义，其余非安全字符按 UTF-8 编码"""
    out, i = [], 0
    while i < len(path):
        c = path[i]
        if c == "%" and _ESC.match(path[i + 1:i + 3] or ""):
            out.append(path[i:i + 3])
            i += 3
            continue
        if c in _SAFE:
            out.append(c)
        else:
            out.append("".join("%%%02X" % b for b in c.encode("utf-8")))
        i += 1
    return "".join(out)


def safe_name(name):
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip().rstrip(". ")


def extract_product(fname):
    stem = fname[:-3] if fname.lower().endswith(".md") else fname
    toks = [t for t in stem.split("-") if t]
    head = []
    for t in toks:
        if ID_PAT.match(t) or VERSION_PAT.match(t) or STOP_PAT.search(t):
            break
        head.append(t)
    if not head:
        # 中文/无分隔文件名：按漏洞关键词截取首段
        first = STOP_PAT.split(toks[0])[0] if toks else stem
        head = [first] if first else [stem]
    # 去掉尾部“入口/端点”token
    while len(head) > 1:
        last = head[-1]
        if (EXT_PAT.search(last) or SYMBOL_PAT.match(last) or SHORT_PAT.match(last)
                or last.lower().strip("()") in ENTRY_WORDS or ID_PAT.match(last)
                or VERSION_PAT.match(last) or STOP_PAT.search(last)):
            head.pop()
        else:
            break
    if len(head) > 3:
        head = head[:3]
    while len(head) > 1 and (SYMBOL_PAT.match(head[-1]) or SHORT_PAT.match(head[-1])
                             or head[-1].lower() in ENTRY_WORDS):
        head.pop()
    prod = "-".join(head).strip("-")
    if not prod:
        prod = stem[:24]
    prod = apply_alias(prod)
    return safe_name(prod)


def apply_alias(prod):
    toks = prod.split("-")
    keys = []
    for n in (len(toks), 2, 1):
        if n <= len(toks):
            keys.append("-".join(toks[:n]).lower())
    for k in keys:
        if k in PRODUCT_ALIAS:
            return PRODUCT_ALIAS[k]
    return prod


def extract_ids(fname):
    res = re.findall(r"(?:CVE|CNVD|CNNVD|QVD)[-_]\d{4}[-_]\d{3,7}", fname, re.I)
    return list(OrderedDict.fromkeys(res))


def extract_tags(fname, body):
    hay = fname + "\n" + body[:3000]
    tags = []
    for tag, kws in TAG_RULES:
        if any(kw in hay for kw in kws):
            tags.append(tag)
    return tags[:4]


def convert_body(text, rel_dir):
    def img_sub(m):
        alt, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://", "data:", "//")):
            return m.group(0)
        url = url.replace("\\", "/")
        if url.startswith("./"):
            url = url[2:]
        return "![%s](%s/%s)" % (alt, RAW_BASE, urlenc(posix_join(rel_dir, url)))

    def link_sub(m):
        alt, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#", "//")):
            return m.group(0)
        url = url.replace("\\", "/")
        if url.startswith("./"):
            url = url[2:]
        return "[%s](%s/%s)" % (alt, BLOB_BASE, urlenc(posix_join(rel_dir, url)))

    return LINK_PAT.sub(link_sub, IMG_PAT.sub(img_sub, text))


def collect():
    items = []
    for cat, dst_cat in CAT_MAP.items():
        src_dir = os.path.join(SRC_ROOT, cat)
        if not os.path.isdir(src_dir):
            continue
        for root, dirs, files in os.walk(src_dir):
            dirs[:] = [d for d in dirs if d.lower() != "images"]
            rel = os.path.relpath(root, src_dir).replace("\\", "/")
            rel_dir = cat if rel == "." else posix_join(cat, rel)
            for f in sorted(files):
                if not f.endswith(".md") or f.startswith("_") or f == "README.md":
                    continue
                items.append((cat, dst_cat, rel_dir, f, os.path.join(root, f)))
    return items


def main():
    dry = "--dry" in sys.argv
    items = collect()
    if dry:
        lines = []
        for cat, dst_cat, rel_dir, f, _ in items:
            lines.append("%s\t%s\t%s\t%s" % (cat, dst_cat, extract_product(f), f))
        with open(r"e:/AIForCode/githubweb/_products.txt", "w", encoding="utf-8") as fp:
            fp.write("\n".join(lines))
        print("total", len(items))
        return

    import datetime
    base = datetime.datetime(2026, 10, 12, 9, 0, 0)
    cat_order = list(CAT_MAP.keys())
    used = set()
    n = 0
    for i, (cat, dst_cat, rel_dir, f, src_path) in enumerate(items):
        with open(src_path, encoding="utf-8", errors="ignore") as fp:
            raw = fp.read()
        lines = raw.split("\n")
        if lines and lines[0].strip() == "---":  # 去掉可能存在的 front-matter
            for j in range(1, len(lines)):
                if lines[j].strip() == "---":
                    lines = lines[j + 1:]
                    break
        title, body_start = "", 0
        for idx, ln in enumerate(lines[:6]):
            if ln.startswith("# "):
                title = ln[2:].strip()
                body_start = idx + 1
                break
        if not title:
            title = f[:-3]
            body_start = 0
        body = convert_body("\n".join(lines[body_start:]).strip("\n"), rel_dir)
        prod = extract_product(f)
        tags = extract_tags(f, raw)
        ids = extract_ids(f)

        out_dir = os.path.join(DST_ROOT, dst_cat, prod)
        os.makedirs(out_dir, exist_ok=True)
        out_name = safe_name(f[:-3]) + ".md"
        # 同名冲突处理
        key = (dst_cat, prod, out_name.lower())
        if key in used:
            out_name = safe_name(f[:-3]) + "-%d.md" % (i % 1000)
        used.add(key)
        out_path = os.path.join(out_dir, out_name)

        dt = base + datetime.timedelta(days=cat_order.index(cat), seconds=i % 36000)
        fm = ["---", 'title: "%s"' % title.replace('"', "'"),
              "date: %s" % dt.strftime("%Y-%m-%d %H:%M:%S"), "categories:",
              "  - WebSecurity", "  - CVE", '  - "%s"' % dst_cat, '  - "%s"' % prod, "tags:"]
        fm.append('  - "%s"' % prod)
        for t in tags:
            fm.append('  - "%s"' % t)
        for cid in ids[:2]:
            fm.append('  - "%s"' % cid)
        fm.append('  - "漏洞复现"')
        fm += ["---", ""]

        src_link = "%s/%s/%s" % (BLOB_BASE, cat, urllib.parse.quote(f, safe=""))
        footer = "\n\n---\n\n> 资料整理自 [Threekiii/Vulnerability-Wiki](%s)\n" % src_link
        with open(out_path, "w", encoding="utf-8") as fp:
            fp.write("\n".join(fm) + body + footer)
        n += 1
    print("written", n)


if __name__ == "__main__":
    main()
