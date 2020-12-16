Hive 是基于Hadoop 构建的一套数据仓库分析系统，它提供了丰富的SQL查询方式来分析存储在hadoop 分布式文件系统中的数据，可以将结构化的数据文件映射为一张数据库表，并提供完整的SQL查询功能，可以将SQL语句转换为MapReduce任务进行运行，通过自己的SQL 去查询分析需要的内容，这套SQL 简称hive SQL，使不熟悉mapreduce 的用户很方便的利用SQL 语言查询，汇总，分析数据。而mapreduce开发人员可以把己写的mapper 和reducer 作为插件来支持Hive 做更复杂的数据分析。

它与关系型数据库的SQL 略有不同，但支持了绝大多数的语句如DDL、DML 以及常见的聚合函数、连接查询、条件查询。HIVE不适合用于联机online)事务处理，也不提供实时查询功能。它最适合应用在基于大量不可变数据的批处理作业。

HIVE的特点：可伸缩（在Hadoop的集群上动态的添加设备），可扩展，容错，输入格式的松散耦合。

请参考：http://wiki.apache.org/hadoop/Hive/LanguageManual

# DDL
## 建表
```
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name 
  [(col_name data_type [COMMENT col_comment], ...)] 
  [COMMENT table_comment] 
  [PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)] 
  [CLUSTERED BY (col_name, col_name, ...) 
  [SORTED BY (col_name [ASC|DESC], ...)] INTO num_buckets BUCKETS] 
  [ROW FORMAT row_format] 
  [STORED AS file_format] 
  [LOCATION hdfs_path]
```
- CREATE TABLE 创建一个指定名字的表。如果相同名字的表已经存在，则抛出异常；用户可以用 IF NOT EXIST 选项来忽略这个异常
- EXTERNAL 关键字可以让用户创建一个外部表，在建表的同时指定一个指向实际数据的路径（LOCATION）
- LIKE 复制现有的表结构，但不复制数据
- COMMENT 可以为表与字段增加描述
- 用户在建表的时候可以自定义 SerDe 或者使用自带的 SerDe。如果没有指定 ROW FORMAT 或者 ROW FORMAT DELIMITED，将会使用自带的 SerDe。在建表的时候，用户还需要为表指定列，用户在指定表的列的同时也会指定自定义的 SerDe，Hive 通过 SerDe 确定表的具体的列的数据。
```
ROW FORMAT
    DELIMITED [FIELDS TERMINATED BY char] [COLLECTION ITEMS TERMINATED BY char]
        [MAP KEYS TERMINATED BY char] [LINES TERMINATED BY char]
   | SERDE serde_name [WITH SERDEPROPERTIES (property_name=property_value, property_name=property_value, ...)]
```

- STORED AS
            SEQUENCEFILE
            | TEXTFILE
            | RCFILE    
            | INPUTFORMAT input_format_classname OUTPUTFORMAT             output_format_classname

如果文件数据是纯文本，可以使用 STORED AS TEXTFILE。如果数据需要压缩，使用 STORED AS SEQUENCE 。
### 创建简单表
```
hive> CREATE TABLE pokes (foo INT, bar STRING); 
```
### 创建外部表
```
CREATE EXTERNAL TABLE page_view(viewTime INT, userid BIGINT,
     page_url STRING, referrer_url STRING,
     ip STRING COMMENT 'IP Address of the User',
     country STRING COMMENT 'country of origination')
 COMMENT 'This is the staging page view table'
 ROW FORMAT DELIMITED FIELDS TERMINATED BY '\054'
 STORED AS TEXTFILE
 LOCATION '<hdfs_location>';
```
### 建分区表
```
CREATE TABLE par_table(viewTime INT, userid BIGINT,
     page_url STRING, referrer_url STRING,
     ip STRING COMMENT 'IP Address of the User')
 COMMENT 'This is the page view table'
 PARTITIONED BY(date STRING, pos STRING)
ROW FORMAT DELIMITED ‘\t’
   FIELDS TERMINATED BY '\n'
STORED AS SEQUENCEFILE;
```
### 建Bucket表
```
CREATE TABLE par_table(viewTime INT, userid BIGINT,
     page_url STRING, referrer_url STRING,
     ip STRING COMMENT 'IP Address of the User')
 COMMENT 'This is the page view table'
 PARTITIONED BY(date STRING, pos STRING)
 CLUSTERED BY(userid) SORTED BY(viewTime) INTO 32 BUCKETS
 ROW FORMAT DELIMITED ‘\t’
   FIELDS TERMINATED BY '\n'
STORED AS SEQUENCEFILE;
```
### 创建表及索引字段ds
```
hive> CREATE TABLE invites (foo INT, bar STRING) PARTITIONED BY (ds STRING); 
```
### 复制一个空表
```
CREATE TABLE empty_key_value_store
LIKE key_value_store;
```
### 例子
```
create table  user_info (user_id int, cid string, ckid string, username string) 
row format delimited 
fields terminated by '\t'
 lines terminated by '\n';
 ```
导入数据表的数据格式是：字段之间是tab键分割，行之间是断行。
及要我们的文件内容格式：
```
100636  100890  c5c86f4cddc15eb7        yyyvybtvt
100612  100865  97cc70d411c18b6f        gyvcycy
100078  100087  ecd6026a15ffddf5        qa000100
```
## 显示表
显示所有表：
```
hive> SHOW TABLES;
```
按正条件（正则表达式）显示表：
```
hive> SHOW TABLES '.*s';
```
## 修改表
- 表添加一列 
```
hive> ALTER TABLE pokes ADD COLUMNS (new_col INT);
```
- 添加一列并增加列字段注释
```
hive> ALTER TABLE invites ADD COLUMNS (new_col2 INT COMMENT 'a comment');
```
- 更改表名：
```
hive> ALTER TABLE events RENAME TO 3koobecaf;
```
- 删除列：
```
hive> DROP TABLE pokes;
```
- 增加分区
```
ALTER TABLE table_name ADD [IF NOT EXISTS] partition_spec [ LOCATION 'location1' ] partition_spec [ LOCATION 'location2' ] ...
      partition_spec:
  : PARTITION (partition_col = partition_col_value, partition_col = partiton_col_value, ...)
```
- 删除分区
```
ALTER TABLE table_name DROP partition_spec, partition_spec,...
```
- 重命名表
```
ALTER TABLE table_name RENAME TO new_table_name 
```
- 修改列的名字、类型、位置、注释：
```
ALTER TABLE table_name CHANGE [COLUMN] col_old_name col_new_name column_type [COMMENT col_comment] [FIRST|AFTER column_name]
```
这个命令可以允许改变列名、数据类型、注释、列位置或者它们的任意组合
- 表添加一列 ：
```
hive> ALTER TABLE pokes ADD COLUMNS (new_col INT);
```
- 添加一列并增加列字段注释
```
hive> ALTER TABLE invites ADD COLUMNS (new_col2 INT COMMENT 'a comment');
```
- 增加/更新列
```
ALTER TABLE table_name ADD|REPLACE COLUMNS (col_name data_type [COMMENT col_comment], ...)  
```    
ADD是代表新增一字段，字段位置在所有列后面(partition列前)REPLACE则是表示替换表中所有字段。
- 增加表的元数据信息
```
ALTER TABLE table_name SET TBLPROPERTIES table_properties table_properties:
         :[property_name = property_value…..]
```
用户可以用这个命令向表中增加metadata
- 改变表文件格式与组织
```
ALTER TABLE table_name SET FILEFORMAT file_format
ALTER TABLE table_name CLUSTERED BY(userid) SORTED BY(viewTime) INTO num_buckets BUCKETS
```
这个命令修改了表的物理存储属性
# 创建／删除视图
## 增加视图
```
CREATE VIEW [IF NOT EXISTS] view_name [ (column_name [COMMENT column_comment], ...) ][COMMENT view_comment][TBLPROPERTIES (property_name = property_value, ...)] AS SELECT
```
- 如果没有提供表名，视图列的名字将由定义的SELECT表达式自动生成
- 如果修改基本表的属性，视图中不会体现，无效查询将会失败
- 视图是只读的，不能用LOAD/INSERT/ALTER
## 删除视图
```
DROP VIEW view_name
```
# 创建数据库
```
CREATE DATABASE name
```
# 显示命令
```
show tables;
show databases;
show partitions;
show functions
describe extended table_name dot col_name
```

# DML

# DQL

# 从SQL到HiveQL应转变的习惯

# 实例