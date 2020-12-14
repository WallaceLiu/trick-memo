语法：
```
LOAD DATA [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name'
    [REPLACE | IGNORE]
    INTO TABLE tbl_name
    [PARTITION (partition_name,...)]
    [CHARACTER SET charset_name]
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
    [IGNORE number {LINES | ROWS}]
    [(col_name_or_user_var,...)]
    [SET col_name = expr,...]
```
数据data.txt：
```
"我爱你","20","相貌平常，经常耍流氓！哈哈"
"李奎","21","相貌平常，经常耍流氓！哈哈"
"王二米","20","相貌平常，经常耍流氓！哈哈"
"老三","24","很强"
"老四","34","XXXXX"
"老五","52","***%*￥*￥*￥*￥"
"小猫","45","中间省略。。。"
"小狗","12","就会叫"
"小妹","21","PP的很"
"小坏蛋","52","表里不一"
"上帝他爷","96","非常英俊"
"MM来了","10","。。。"
"歌颂党","20","社会主义好"
"人民好","20","的确是好"
"老高","10","学习很好"
"斜三","60","眼睛斜了"
"中华之子","100","威武的不行了"
"大米","63","我爱吃"
"苹果","15","好吃"
```
假设放在c根目录下。
表结构：
```
CREATE TABLE `t0` (
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` CHAR(20) NOT NULL,
  `age` TINYINT(3) UNSIGNED NOT NULL,
  `description` TEXT NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `idx_name` (`name`)
) ENGINE=MYISAM DEFAULT CHARSET=utf8 | 
```
示例1：
在 Windows 环境下：
```
LOAD DATA LOCAL INFILE 'c:\\data.txt' 
INTO TABLE t0
CHARACTER 
SET utf8
FIELDS TERMINATED BY '#' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(
  name,
  age,
  description
) ;
```
> 注意：
> - 路径中有转义
> - 列是已“#”号分隔
> - 列是已双引号包裹
> - 行结束是\r\n，Windows环境

示例3：
```
LOAD DATA LOCAL INFILE 'c:\\data.txt' 
INTO TABLE t0 
CHARACTER SET utf8
FIELDS TERMINATED BY '#' 
LINES TERMINATED BY '\r\n'
IGNORE 0 LINES  
(
  name,
  age,
  description
) ;
```
# 参考
- [MySQL load data](https://dev.mysql.com/doc/refman/5.7/en/load-data.html)