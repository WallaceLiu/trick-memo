```
Failure to connet:dial tcp 127.0.0.1:8888: socket: too many open files
```
一般这种报错是由于MacOSX默认的open files数值过小导致的。查看当前系统的默认文件打开数：
```
capdeMacBook-Pro:~ cap$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
file size               (blocks, -f) unlimited
max locked memory       (kbytes, -l) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 4864
pipe size            (512 bytes, -p) 1
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 709
virtual memory          (kbytes, -v) unlimited
capdeMacBook-Pro:~ cap$
```
可以看到默认的open files数值为256，解决办法将此数值调大即可。先查看以下两个数值：
```
capdeMacBook-Pro:~ cap$ sysctl kern.maxfiles
kern.maxfiles: 12288
capdeMacBook-Pro:~ cap$ sysctl kern.maxfilesperproc
kern.maxfilesperproc: 10240
```
> - kern.maxfiles：系统中最多同时开启的文件数量。 
> - kern.maxfilesperproc：每个进程能同时打开的最大文件数量。 

要么用 ulimit -n，但如果超过以上两个数值，会报错，不超过就不会报错：
```
capdeMacBook-Pro:~ cap$ ulimit -n 65535
-bash: ulimit: open files: cannot modify limit: Invalid argument
```
或者直接调大上述两个配置的数值：
```
$sudo sysctl -w kern.maxfiles=1048600
$sudo sysctl -w kern.maxfilesperproc=1048576
```


