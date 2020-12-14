# 服务端
- 启动
```shell script
To have launchd start redis@3.2 now and restart at login:
//使用launchctl brew启动
  brew services start redis@3.2
```
使用配置文件启动
Or, if you don't want/need a background service you can just run:
```shell script
redis-server /usr/local/etc/redis.conf
```
- 关闭
```shell script
sudo pkill redis-server
```
# 客户端
- 启动
```shell script
redis-cli
```
```shell script
redis-cli -h 127.0.0.1 -p 6379
```
- 关闭
```shell script
redis-cli shutdown
```


