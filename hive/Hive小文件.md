如果脚本会生成很多小文件怎么办？ 可以尝试以下设置来合并小文件。
```
set hive.merge.mapfiles = true #在Map-only的任务结束时合并小文件
set hive.merge.mapredfiles = true #在Map-Reduce的任务结束时合并小文件
set hive.merge.size.per.task = 256*1000*1000 #合并文件的大小
set hive.merge.smallfiles.avgsize=64000000 #当输出文件的平均大小小于该值时，启动一个独立的map-reduce任务进行文件merge
```
如果文件太大，浪费存储空间怎么办？可以尝试设置压缩编码来降低存储空间。
```
SET mapreduce.output.fileoutputformat.compress.codec=com.hadoop.compression.lzo.LzopCodec;
SET hive.exec.compress.output=true;
SET mapreduce.output.fileoutputformat.compress=true;
```
