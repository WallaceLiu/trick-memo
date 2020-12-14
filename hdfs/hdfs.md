# 文件大小
```shell script

```
# 小文件
```shell script
hdfs dfs -du -h /hive/warehouse/test.db/*/*/ | awk '{print $1$2 "\t" $5}' | awk '{if($1 ~/K/ || $1 ~/M/) print $0}' | awk '{if($1 ~/M/) print $0}'|sed 's/M//g'| awk '{if($1 <128) print $1"M""\t"$2}' 
```
```shell script
hdfs dfs -du -h /hive/warehouse/test.db/*/*/ | awk '{print $1$2 "\t" $5}' | awk '{if($1 ~/K/ || $1 ~/M/) print $0}' |awk '{if($1 ~/K/) print $0}' |egrep -v '2018|2019' 
```