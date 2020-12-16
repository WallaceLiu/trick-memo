- 创建一个表
```
CREATE TABLE u_data (
userid INT,
movieid INT,
rating INT,
unixtime STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '/t'
STORED AS TEXTFILE;
```
- 下载示例数据文件，并解压缩
```
wget http://www.grouplens.org/system/files/ml-data.tar__0.gz
tar xvzf ml-data.tar__0.gz
```
- 加载数据到表中:
```
LOAD DATA LOCAL INPATH 'ml-data/u.data'
OVERWRITE INTO TABLE u_data;
```
- 统计数据总量:
```
SELECT COUNT(1) FROM u_data;
```
现在做一些复杂的数据分析:
- 创建一个 weekday_mapper.py: 文件，作为数据按周进行分割 
```
import sys
import datetime
for line in sys.stdin:
line = line.strip()
userid, movieid, rating, unixtime = line.split('/t')
weekday = datetime.datetime.fromtimestamp(float(unixtime)).isoweekday()
print '/t'.join([userid, movieid, rating, str(weekday)])
```
- 使用映射脚本

创建表，按分割符分割行中的字段值
```
CREATE TABLE u_data_new (
userid INT,
movieid INT,
rating INT,
weekday INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '/t';
```
将Python文件加载到系统
```
add FILE weekday_mapper.py;
```
将数据按周进行分割
```
INSERT OVERWRITE TABLE u_data_new
SELECT
TRANSFORM (userid, movieid, rating, unixtime)
USING 'python weekday_mapper.py'
AS (userid, movieid, rating, weekday)
FROM u_data;
SELECT weekday, COUNT(1)
FROM u_data_new
GROUP BY weekday;
```
- 处理Apache Weblog 数据

将WEB日志先用正则表达式进行组合，再按需要的条件进行组合输入到表中
```
add jar ../build/contrib/hive_contrib.jar;
CREATE TABLE apachelog (
host STRING,
identity STRING,
user STRING,
time STRING,
request STRING,
status STRING,
size STRING,
referer STRING,
agent STRING)
ROW FORMAT SERDE 'org.apache.hadoop.hive.contrib.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
"input.regex" = "([^ ]*) ([^ ]*) ([^ ]*) (-|//[[^//]]*//]) ([^ /"]*|/"[^/"]*/") (-|[0-9]*) (-|[0-9]*)(?: ([^ /"]*|/"[^/"]*/") ([^ /"]*|/"[^/"]*/"))?",
"output.format.string" = "%1$s %2$s %3$s %4$s %5$s %6$s %7$s %8$s %9$s"
)
STORED AS TEXTFILE;
```