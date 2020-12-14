http://hbase.apache.org/book.html#quickstart
# 下载HBase
hbase-1.2.4-bin.tar.gz ，地址 http://apache.fayea.com/hbase/
# 解压
```
$ tar -zxf hbase-1.0.1.1-bin.tar.gz
$ cd hbase-1.0.1.1
```
# 配置HBase
## 编辑 conf/hbase-env.sh
```
export JAVA_HOME=JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_101.jdk/Contents/Home
export HBASE_MANAGES_ZK=true
```
Hbase依赖zookeeper，所有的节点和客户端都必须能够访问zookeeper。

HBase自带ZooKeeper， HBASE_MANAGES_ZK 环境变量用来设置，是使用自带的 Zookeeper，还是独立的。

HBASE_MANAGES_ZK 为 false ，使用独立的；为 true，自带ZK，Hbase启动时同时也启动ZooKeeper。
## 编辑 conf/hbase-site.xml
```
<configuration>
        <property>
                <name>hbase.rootdir</name>
                <value>file:///home/songlee/hbase-1.0.1.1/data</value>
        </property>
</configuration>
```
默认情况下Hbase是写到/tmp的，在重启的时候/tmp会被清空，数据就会丢失。
# 启动HBase
HBase提供的启动脚本：
```
$ bin/start-hbase.sh 
starting master, logging to /home/songlee/hbase-1.0.1.1/bin/../logs/hbase-songlee-master-songlee.out
```
查看Java进程：
```
$ jps
5464 HMaster
5561 Jps
```
可以看到 HMaster 进程已经启动了。
# HBase Shell交互
HBase Shell是一个封装了Java API的JRuby应用软件，通过它可以与HBase集群进行交互。
```
$ bin/hbase shell
2015-07-16 12:37:07,171 WARN  [main] util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
HBase Shell; enter 'help<RETURN>' for list of supported commands.
Type "exit<RETURN>" to leave the HBase Shell
Version 1.0.1.1, re1dbf4df30d214fca14908df71d038081577ea46, Sun May 17 12:34:26 PDT 2015
```