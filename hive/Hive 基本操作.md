# 进入hive控制台
```
~ bin/hive shell
Logging initialized using configuration in file:/home/cos/toolkit/hive-0.9.0/conf/hive-log4j.properties
Hive history file=/tmp/cos/hive_job_log_cos_201307160003_95040367.txt
hive>
```
# 创建表
- 创建数据

文本以tab分隔
```
~ vi /home/cos/demo/t_hive.txt

16      2       3
61      12      13
41      2       31
17      21      3
71      2       31
1       12      34
11      2       34
```
- 创建新表
```
hive> CREATE TABLE t_hive (a int, b int, c int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

```
- 导入数据t_hive.txt到t_hive表
```
hive> LOAD DATA LOCAL INPATH '/home/cos/demo/t_hive.txt' OVERWRITE INTO TABLE t_hive ;

hive> show tables;
OK
t_hive
Time taken: 0.099 seconds

hive>show tables '*t*';
OK
t_hive
Time taken: 0.065 seconds
```
- 查看表数据
```
hive> select * from t_hive;
OK
16      2       3
61      12      13
41      2       31
17      21      3
71      2       31
1       12      34
11      2       34
Time taken: 0.264 seconds
```
- 查看表结构
```
hive> desc t_hive;
OK
a       int
b       int
c       int
Time taken: 0.1 seconds
```
# 修改表
- 增加一个字段
```
hive> ALTER TABLE t_hive ADD COLUMNS (new_col String);
OK
Time taken: 0.186 seconds

hive> desc t_hive;
OK
a       int
b       int
c       int
new_col string
Time taken: 0.086 seconds
```
- 重命令表名
```
hive> ALTER TABLE t_hive RENAME TO t_hadoop;
OK
Time taken: 0.45 seconds
hive> show tables;
OK
t_hadoop
Time taken: 0.07 seconds
```
# 删除表
```
hive> DROP TABLE t_hadoop;
OK
Time taken: 0.767 seconds

hive> show tables;
OK
Time taken: 0.064 seconds
```
# Hive交互式模式
- quit,exit:  退出交互式shell
- reset: 重置配置为默认值
- set <key>=<value> : 修改特定变量的值
- set :  输出用户覆盖的hive配置变量
- set -v : 输出所有Hadoop和Hive的配置变量
- add FILE[S] *, add JAR[S] *, add ARCHIVE[S] * : 添加 一个或多个 file, jar, archives到分布式缓存
- list FILE[S], list JAR[S], list ARCHIVE[S] : 输出已经添加到分布式缓存的资源。
- list FILE[S] *, list JAR[S] *,list ARCHIVE[S] * : 检查给定的资源是否添加到分布式缓存
- delete FILE[S] *,delete JAR[S] *,delete ARCHIVE[S] * : 从分布式缓存删除指定的资源
- ! <command> :  从Hive shell执行一个shell命令
- dfs <dfs command> :  从Hive shell执行一个dfs命令
- <query string> : 执行一个Hive 查询，然后输出结果到标准输出
- source FILE <filepath>:  在CLI里执行一个hive脚本文件
# 数据导入
还以刚才的t_hive为例。
- 创建表结构
```
hive> CREATE TABLE t_hive (a int, b int, c int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';
```
- 从操作本地文件系统加载数据(LOCAL)
```
hive> LOAD DATA LOCAL INPATH '/home/cos/demo/t_hive.txt' OVERWRITE INTO TABLE t_hive;

```
- 在HDFS中查找刚刚导入的数据
```
~ hadoop fs -cat /user/hive/warehouse/t_hive/t_hive.txt

16      2       3
61      12      13
41      2       31
17      21      3
71      2       31
1       12      34
11      2       34
```
- 从HDFS加载数据

创建表t_hive2
```
hive> CREATE TABLE t_hive2 (a int, b int, c int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';
```
从HDFS加载数据
```
hive> LOAD DATA INPATH '/user/hive/warehouse/t_hive/t_hive.txt' OVERWRITE INTO TABLE t_hive2;

```
查看数据
```
hive> select * from t_hive2;
OK
16      2       3
61      12      13
41      2       31
17      21      3
71      2       31
1       12      34
11      2       34
Time taken: 0.287 seconds
```
- 从其他表导入数据
```
hive> INSERT OVERWRITE TABLE t_hive2 SELECT * FROM t_hive ;

hive> select * from t_hive2;
OK
16      2       3
61      12      13
41      2       31
17      21      3
71      2       31
1       12      34
11      2       34
Time taken: 0.134 seconds
```
- 创建表并从其他表导入数据
删除表
```
hive> DROP TABLE t_hive;
```
创建表并从其他表导入数据
```
hive> CREATE TABLE t_hive AS SELECT * FROM t_hive2;

hive> select * from t_hive;
OK
16      2       3
61      12      13
41      2       31
17      21      3
71      2       31
1       12      34
11      2       34
Time taken: 0.109 seconds
```
仅复制表结构不导数据
```
hive> CREATE TABLE t_hive3 LIKE t_hive;

hive> select * from t_hive3;

```
# 数据导出
从HDFS复制到HDFS其他位置
```
~ hadoop fs -cp /user/hive/warehouse/t_hive /

~ hadoop fs -ls /t_hive
Found 1 items
-rw-r--r--   1 cos supergroup         56 2013-07-16 10:41 /t_hive/000000_0

~ hadoop fs -cat /t_hive/000000_0
1623
611213
41231
17213
71231
11234
11234
```
通过Hive导出到本地文件系统
```
hive> INSERT OVERWRITE LOCAL DIRECTORY '/tmp/t_hive' SELECT * FROM t_hive;

```
查看本地操作系统
```
hive> ! cat /tmp/t_hive/000000_0;
hive> 1623
611213
41231
17213
71231
11234
11234
```
# Hive查询HiveQL
## 普通查询：排序，列别名，嵌套子查询
```
hive> FROM (
    >   SELECT b,c as c2 FROM t_hive
    > ) t
    > SELECT t.b, t.c2
    > WHERE b>2
    > LIMIT 2;
12      13
21      3
```
## 连接查询：JOIN
```
hive> SELECT t1.a,t1.b,t2.a,t2.b
    > FROM t_hive t1 JOIN t_hive2 t2 on t1.a=t2.a
    > WHERE t1.c>10;

1       12      1       12
11      2       11      2
41      2       41      2
61      12      61      12
71      2       71      2
```
## 聚合查询1：count, avg
```
hive> SELECT count(*), avg(a) FROM t_hive;
7       31.142857142857142
```
## 聚合查询2：count, distinct
```
hive> SELECT count(DISTINCT b) FROM t_hive;
3
```
## 聚合查询3：GROUP BY, HAVING
```
hive> SELECT avg(a),b,sum(c) FROM t_hive GROUP BY b,c
16.0    2       3
56.0    2       62
11.0    2       34
61.0    12      13
1.0     12      34
17.0    21      3


hive> SELECT avg(a),b,sum(c) FROM t_hive GROUP BY b,c HAVING sum(c)>30
56.0    2       62
11.0    2       34
1.0     12      34
```
## Hive视图
Hive视图和数据库视图的概念是一样的，我们还以t_hive为例。
```
hive> CREATE VIEW v_hive AS SELECT a,b FROM t_hive where c>30;
hive> select * from v_hive;
41      2
71      2
1       12
11      2
```
### 删除视图
```
hive> DROP VIEW IF EXISTS v_hive;
OK
Time taken: 0.495 seconds
```
## Hive分区表
分区表是数据库的基本概念，但很多时候数据量不大，我们完全用不到分区表。Hive是一种OLAP数据仓库软件，涉及的数据量是非常大的，所以分区表在这个场景就显得非常重要！！

下面我们重新定义一个数据表结构：t_hft

创建数据
```

~ vi /home/cos/demo/t_hft_20130627.csv
000001,092023,9.76
000002,091947,8.99
000004,092002,9.79
000005,091514,2.2
000001,092008,9.70
000001,092059,9.45

~ vi /home/cos/demo/t_hft_20130628.csv
000001,092023,9.76
000002,091947,8.99
000004,092002,9.79
000005,091514,2.2
000001,092008,9.70
000001,092059,9.45
创建数据表

DROP TABLE IF EXISTS t_hft;
CREATE TABLE t_hft(
SecurityID STRING,
tradeTime STRING,
PreClosePx DOUBLE
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
创建分区数据表
根据业务：按天和股票ID进行分区设计

DROP TABLE IF EXISTS t_hft;
CREATE TABLE t_hft(
SecurityID STRING,
tradeTime STRING,
PreClosePx DOUBLE
) PARTITIONED BY (tradeDate INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
导入数据

#20130627
hive> LOAD DATA LOCAL INPATH '/home/cos/demo/t_hft_20130627.csv' OVERWRITE INTO TABLE t_hft PARTITION (tradeDate=20130627);
Copying data from file:/home/cos/demo/t_hft_20130627.csv
Copying file: file:/home/cos/demo/t_hft_20130627.csv
Loading data to table default.t_hft partition (tradedate=20130627)

#20130628
hive> LOAD DATA LOCAL INPATH '/home/cos/demo/t_hft_20130628.csv' OVERWRITE INTO TABLE t_hft PARTITION (tradeDate=20130628);
Copying data from file:/home/cos/demo/t_hft_20130628.csv
Copying file: file:/home/cos/demo/t_hft_20130628.csv
Loading data to table default.t_hft partition (tradedate=20130628)

查看分区表


hive> SHOW PARTITIONS t_hft;
tradedate=20130627
tradedate=20130628
Time taken: 0.082 seconds
查询数据


hive> select * from t_hft where securityid='000001';
000001  092023  9.76    20130627
000001  092008  9.7     20130627
000001  092059  9.45    20130627
000001  092023  9.76    20130628
000001  092008  9.7     20130628
000001  092059  9.45    20130628

hive> select * from t_hft where tradedate=20130627 and PreClosePx<9;
000002  091947  8.99    20130627
000005  091514  2.2     20130627
```
