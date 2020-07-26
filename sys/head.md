head命令用来查看文件内容的前多少行或多少字节的内容。还可以通过awk、sed等命令来获取前多少行，但是相比之下head更擅长轻量，并且比其他都快速
命令用法
```
-c 用来获取前多少字节的内容，还可加上单位,默认是字节。1(byte) 、1k(1KB）、1m（1MB）
-n用于获取前多上行
-q 获取多个文件的时候不显示文件头部
-v 获取多个文件的内容是显示头部，也是默认选项
```
# 常见用法举例
- 获取前多少字节内容
–c n ，获取前n个字节的内容。可以加上单位1(byte) 、1k(1KB）、1m（1MB）默认但是是字节
-c 10     所以这里是10 byte，获取前两个字符（ASCII编码的时候）
```
[root@master lianxi]# head -c 10 test
lwgarmstro[root@master lianxi]# –
```
-c 1k 获取前1KB大小的内容，-c 1m 就是获取前1MB字节大小的内容
```
[root@master lianxi]# head -c 1k /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
       ......后面省略
```
- 获取前多少行内容
-n number ，比如 –n 3 就是获取前3行内容
```
[root@master lianxi]# cat -n /etc/passwd | head -n 3
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
```
- 同时获取多个文件的前多上行或字节的内容
获取多个文件的前多少行或字节 的内容时候，默认会显示头部信息。
-v 显示头部信息（默认），-q 不显示头部信息
```
 [root@master lianxi]# head -v -n 1 1.lua  2.lua 
 ==> 1.lua <==
 arr = {23,21,89,289,34,23,1,32,434,21,1}

 ==> 2.lua <==
print("hello world")
```
```
 [root@master lianxi]# head -q -n 1 1.lua  2.lua  
 arr = {23,21,89,289,34,23,1,32,434,21,1}
print("hello world")
```
