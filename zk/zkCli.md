# 连接zookeeper
```shell script
[root@bigdata05 bin]# ./zkCli.sh -server localhost:2181
```

# 查看帮助信息
```shell script
[zk: localhost:2181(CONNECTED) 0] help
ZooKeeper -server host:port cmd args
	addauth scheme auth
	close
    ...
```

# 查看当前节点列表
```shell script
[zk: localhost:2181(CONNECTED) 1] ls /
[zookeeper, yarn-leader-election, hadoop-ha]
```

# 创建节点
```text
create [-s][-e] path data acl
其中，-s或-e分别指定节点特性，顺序或临时节点，若不指定，则创建持久节点；ac1用来进行权限控制
```
```shell script
[zookeeper, yarn-leader-election, hadoop-ha]
[zk: localhost:2181(CONNECTED) 2] create /test "test"
Created /test
[zk: localhost:2181(CONNECTED) 4] create /test/test "test"
Created /test/test
```

# 查看、设置节点数据
```shell script
[zk: localhost:2181(CONNECTED) 7] get /test
test
[zk: localhost:2181(CONNECTED) 8] set /test "666666"
666666
```

# 删除节点
```shell script
[zk: localhost:2181(CONNECTED) 11] delete /test
Node not empty: /test
[zk: localhost:2181(CONNECTED) 12] delete /test/test
[zk: localhost:2181(CONNECTED) 13]
```
