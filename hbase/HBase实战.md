HBase Shell

功能 | 命令
---|---
创建表 | create '表名称', '列名称1','列名称2','列名称N'
添加记录 | put '表名称', '行名称', '列名称:', '值'
查看记录 | get '表名称', '行名称'
查看表中的记录总数 | count '表名称'
删除记录 | delete '表名' ,'行名称' , '列名称'
删除一张表 | 先禁用该表，才能删除，第一步 disable '表名称'；第二步drop '表名称'
查看所有记录 | scan "表名称"
查看某个表某个列中所有数据 | scan "表名称" , ['列名称:']
更新记录 | 就是重写一遍进行覆盖

# 查询服务器状态
```shell
hbase(main):024:0>status
1 active master, 0 backup masters, 1 servers, 0 dead, 2.0000 average load
```
# 查询版本
```shell
hbase(main):025:0>version
1.2.4, r67592f3d062743907f8c5ae00dbbe1ae4f69e5af, Tue Oct 25 18:10:20 CDT 2016
```
# 创建member表
包含三个列族：member_id、address、info。
显然，address、info可以包含很多列。
```shell
hbase(main):011:0>create 'member','member_id','address','info'
0 row(s) in 1.3030 seconds

=> Hbase::Table - member
```
# 列出表
```shell
hbase(main):012:0>list
TABLE
member
1 row(s) in 0.0200 seconds

=> ["member"]
```
# 获得表描述
```shell
hbase(main):006:0>describe 'member'
Table member is ENABLED
member
COLUMN FAMILIES DESCRIPTION
{NAME => 'address', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', COMPRESSION => 'N
ONE', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}
{NAME => 'info', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', COMPRESSION => 'NONE
', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}
{NAME => 'member_id', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', COMPRESSION =>
'NONE', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}
3 row(s) in 10.1160 seconds
```
# 删除列族
前面建了3个列族，删除member_id列族。
```shell
hbase(main):003:0>alter 'member',{NAME=>'member_id',METHOD=>'delete'}
Updating all regions with the new schema...
1/1 regions updated.
Done.
0 row(s) in 1.9400 seconds
hbase(main):009:0> describe 'member'
Table member is ENABLED
member
COLUMN FAMILIES DESCRIPTION
{NAME => 'address', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', COMPRESSION => 'N
ONE', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}
{NAME => 'info', BLOOMFILTER => 'ROW', VERSIONS => '1', IN_MEMORY => 'false', KEEP_DELETED_CELLS => 'FALSE', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', COMPRESSION => 'NONE
', MIN_VERSIONS => '0', BLOCKCACHE => 'true', BLOCKSIZE => '65536', REPLICATION_SCOPE => '0'}
2 row(s) in 0.0220 seconds
```
之前的hbase版本，删除列族前，必须禁用表。
# 禁用表
```shell
hbase(main):004:0>disable 'member'
0 row(s) in 2.2640 seconds
```
# 启用表
```shell
hbase(main):008:0> enable 'member'
0 row(s) in 2.0420 seconds
```
## 列出所有的表
```shell
hbase(main):028:0>list
TABLE
member
2 row(s) in 0.0150seconds
```
## 删除表
```shell
hbase(main):029:0>drop 'temp_table'
ERROR: Table member is enabled. Disable it first.

Here is some help for this command:
Drop the named table. Table must first be disabled:
  hbase> drop 't1'
  hbase> drop 'ns1:t1'
hbase(main):029:0>disable 'temp_table'
0 row(s) in 2.0590 seconds

hbase(main):030:0>drop 'temp_table'
0 row(s) in 1.1070 seconds
```
删除表之前，必须禁用表。
## 查询表是否存在
```shell
hbase(main):021:0>exists 'member'
Table member does exist
0 row(s) in 0.1610 seconds
```
## 判断表是否enable或disable
```shell
hbase(main):034:0>is_enabled 'member'
true
0 row(s) in 0.0110 seconds

hbase(main):032:0>is_disabled 'member'
false
0 row(s) in 0.0110 seconds
```
# DML操作
## 插入记录
命令“put'member','scutshuxue'”，'scutshuxue'是RowKey。

向HBase表中添加数据时，只能一列一列添加，不能同时添加多列。
```shell
hbase(main):024:0> put'member','scutshuxue','info:age','24'
0 row(s) in 0.1050 seconds

hbase(main):025:0> put'member','scutshuxue','info:birthday','1987-06-17'
0 row(s) in 0.0050 seconds

hbase(main):026:0> put'member','scutshuxue','info:company','alibaba'
0 row(s) in 0.0080 seconds

hbase(main):027:0> put'member','scutshuxue','address:contry','china'
0 row(s) in 0.0060 seconds

hbase(main):028:0> put'member','scutshuxue','address:province','zhejiang'
0 row(s) in 0.0070 seconds

hbase(main):029:0> put'member','scutshuxue','address:city','hangzhou'
0 row(s) in 0.0050 seconds

hbase(main):030:0>
hbase(main):031:0* put'member','xiaofeng','info:birthday','1987-4-17'
0 row(s) in 0.0030 seconds

hbase(main):032:0> put'member','xiaofeng','info:favorite','movie'
0 row(s) in 0.0050 seconds

hbase(main):033:0> put'member','xiaofeng','info:company','alibaba'
0 row(s) in 0.0040 seconds

hbase(main):034:0> put'member','xiaofeng','address:contry','china'
0 row(s) in 0.0080 seconds

hbase(main):035:0> put'member','xiaofeng','address:province','guangdong'
0 row(s) in 0.0030 seconds

hbase(main):036:0> put'member','xiaofeng','address:city','jieyang'
0 row(s) in 0.0030 seconds

hbase(main):037:0> put'member','xiaofeng','address:town','xianqiao'
0 row(s) in 0.0110 seconds
```
## 获取单条数据
根据id获得所有列族的所有数据
```shell
hbase(main):001:0>get 'member','scutshuxue'
COLUMN                                        CELL
 address:city                                 timestamp=1482059587034, value=hangzhou
 address:contry                               timestamp=1482059586982, value=china
 address:province                             timestamp=1482059587011, value=zhejiang
 info:age                                     timestamp=1482059586879, value=24
 info:birthday                                timestamp=1482059586922, value=1987-06-17
 info:company                                 timestamp=1482059586959, value=alibaba
6 row(s) in 0.0380 seconds
```
根据id获得某个列族的所有数据
```shell
hbase(main):002:0>get 'member','scutshuxue','info'
COLUMN                                        CELL
 info:age                                     timestamp=1482059586879, value=24
 info:birthday                                timestamp=1482059586922, value=1987-06-17
 info:company                                 timestamp=1482059586959, value=alibaba
3 row(s) in 0.0170 seconds
```
根据id获得某个列族的某个列的数据
```shell
hbase(main):002:0>get 'member','scutshuxue','info:age' 
COLUMN                                        CELL
 info:age                                     timestamp=1482059586879, value=24
1 row(s) in 0.0180 seconds
hbase(main):001:0> get 'member','scutshuxue','info:age','info:birthday'
COLUMN                                        CELL
 info:age                                     timestamp=1482059586879, value=24
 info:birthday                                timestamp=1482059586922, value=1987-06-17
2 row(s) in 10.2440 seconds
```
## 更新一条记录
将scutshuxue的年龄改成99
```shell
hbase(main):002:0> put 'member','scutshuxue','info:age' ,'99'
0 row(s) in 0.0620 seconds

hbase(main):003:0> get 'member','scutshuxue','info:age'
COLUMN                                        CELL
 info:age                                     timestamp=1482060341559, value=99
1 row(s) in 0.0150 seconds
```
## 通过timestamp获取指定版本的数据
```
hbase(main):010:0>get 'member','scutshuxue',{COLUMN=>'info:age',TIMESTAMP=>1321586238965}
COLUMN                                   CELL                                                                                                               
info:age                               timestamp=1321586238965, value=24                                                                                  
1 row(s) in 0.0140seconds

hbase(main):011:0>get 'member','scutshuxue',{COLUMN=>'info:age',TIMESTAMP=>1321586571843}
COLUMN                                   CELL                                                                                                               
info:age                               timestamp=1321586571843, value=99                                                                                  
1 row(s) in 0.0180seconds
```
## 全表扫描
```
hbase(main):013:0>scan 'member'
ROW                                     COLUMN+CELL
scutshuxue                             column=address:city, timestamp=1321586240244, value=hangzhou                                                       
scutshuxue                             column=address:contry, timestamp=1321586239126, value=china                                                        
scutshuxue                             column=address:province, timestamp=1321586239197, value=zhejiang                                                   
scutshuxue                              column=info:age,timestamp=1321586571843, value=99                                                                 
scutshuxue                             column=info:birthday, timestamp=1321586239015, value=1987-06-17                                                    
scutshuxue                             column=info:company, timestamp=1321586239071, value=alibaba                                                        
temp                                   column=info:age, timestamp=1321589609775, value=59                                                                 
xiaofeng                               column=address:city, timestamp=1321586248400, value=jieyang                                                        
xiaofeng                               column=address:contry, timestamp=1321586248316, value=china                                                        
xiaofeng                               column=address:province, timestamp=1321586248355, value=guangdong                                                  
xiaofeng                               column=address:town, timestamp=1321586249564, value=xianqiao                                                       
xiaofeng                               column=info:birthday, timestamp=1321586248202, value=1987-4-17                                                     
xiaofeng                               column=info:company, timestamp=1321586248277, value=alibaba                                                        
xiaofeng                               column=info:favorite, timestamp=1321586248241, value=movie                                                         
3 row(s) in 0.0570seconds
```
## 删除id为temp的值的‘info:age’字段
```
hbase(main):016:0>delete 'member','temp','info:age'
0 row(s) in 0.0150seconds
hbase(main):018:0>get 'member','temp'
COLUMN                                   CELL
0 row(s) in 0.0150seconds
```
## 删除整行
```
hbase(main):001:0>deleteall 'member','xiaofeng'
0 row(s) in 0.3990seconds
```
## 查询表中有多少行
```
hbase(main):019:0>count 'member'
2 row(s) in 0.0160seconds
```
## 给‘xiaofeng’这个id增加'info:age'字段，并使用counter实现递增
```
hbase(main):057:0>incr 'member','xiaofeng','info:age'
COUNTER VALUE = 1

hbase(main):058:0>get 'member','xiaofeng','info:age' 
COLUMN                                   CELL
info:age                               timestamp=1321590997648, value=\x00\x00\x00\x00\x00\x00\x00\x01                                                    
1 row(s) in 0.0140seconds

hbase(main):059:0>incr 'member','xiaofeng','info:age'
COUNTER VALUE = 2

hbase(main):060:0>get 'member','xiaofeng','info:age' 
COLUMN                                   CELL
info:age                               timestamp=1321591025110, value=\x00\x00\x00\x00\x00\x00\x00\x02                                                    
1 row(s) in 0.0160seconds
```
获取当前count的值
```
hbase(main):069:0>get_counter 'member','xiaofeng','info:age'
COUNTER VALUE = 2
```
## 将整张表清空
```
hbase(main):035:0>truncate 'member'
Truncating 'member'table (it may take a while):
- Disabling table...
- Dropping table...
- Creating table...
0 row(s) in 4.3430seconds
```
可以看出，hbase是先将掉disable掉，然后drop掉后重建表来实现truncate的功能的。
# 扫描
```
hbase(main):035:0>scan ‘member' 
```
还可以指定修饰词：TIMERANGE, FILTER, LIMIT, STARTROW, STOPROW, TIMESTAMP, MAXLENGTH,or COLUMNS。

没任何修饰词，就是上边例句，就会显示所有数据行。


