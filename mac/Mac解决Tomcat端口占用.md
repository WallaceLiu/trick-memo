Tomcat启动时报以下错误

错误: 代理抛出异常错误: java.rmi.server.ExportException: Port already in use: 1099; nested exception is: 
java.net.BindException: Address already in use
查看占用该端口的进程
```
lsof -i tcp:1099
```
会列出占用该端口的进程
```
COMMAND  PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
java    3794  cyh   34u  IPv6 0x183121c1ceacb43b      0t0  TCP *:rmiregistry (LISTEN)
```
kill掉该进程
```
kill -9 3794
```