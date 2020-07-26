[dstat 官网](http://dag.wiee.rs/home-made/dstat/)

[dstat dstat.1.adoc](https://github.com/dagwieers/dstat/blob/master/docs/dstat.1.adoc)

[dstat paper](https://github.com/dagwieers/dstat/blob/master/docs/dstat-paper.adoc)
```
Usage: dstat [-afv] [options..] [delay [count]]
```
```
Dstat options:
  -c, --cpu              开启cpu统计
     -C 0,3,total           include cpu0, cpu3 and total
  -d, --disk             开启磁盘统计
     -D total,hda           include hda and total
  -g, --page             开启内存页统计
  -i, --int              开启 interrupt 统计
     -I 5,eth2              include int5 and interrupt used by eth2
  -l, --load             开启负载统计
  -m, --mem              开启内存统计
  -n, --net              开启网络统计
     -N eth1,total          include eth1 and total
  -p, --proc             开启 process 统计
  -r, --io               开启io统计 (已完成请求的I/O)
  -s, --swap             开启交换区统计
     -S swap1,total         include swap1 and total
  -t, --time             开启 time/date output
  -T, --epoch            开启 time counter (seconds since epoch)
  -y, --sys              开启系统统计

  --aio                  开启 aio 统计
  --fs, --filesystem     开启 fs 统计
  --ipc                  开启 ipc 统计
  --lock                 开启 lock 统计
  --raw                  开启 raw 统计
  --socket               开启 socket 统计
  --tcp                  开启 tcp 统计
  --udp                  开启 udp 统计
  --unix                 开启 unix 统计
  --vm                   开启 vm 统计

  --plugin-name          开启 plugins by plugin name (see manual)
  --list                 list all available plugins

  -a, --all              equals -cdngy (default)
  -f, --full             automatically expand -C, -D, -I, -N and -S lists
  -v, --vmstat           equals -pmgdsc -D total

  --bw, --blackonwhite   change colors for white background terminal
  --float                force float values on screen
  --integer              force integer values on screen
  --nocolor              disable colors (implies --noupdate)
  --noheaders            disable repetitive headers
  --noupdate             disable intermediate updates
  --output file          write CSV output to file

delay is the delay in seconds between each update (default: 1)
count is the number of updates to display before exiting (default: unlimited)
```
> 说明
> - CPU状态：CPU的使用率。这项报告更有趣的部分是显示了用户，系统和空闲部分，这更好地分析了CPU当前的使用状况。如果你看到"wait"一栏中，CPU的状态是一个高使用率值，那说明系统存在一些其它问题。当CPU的状态处在"waits"时，那是因为它正在等待I/O设备（例如内存，磁盘或者网络）的响应而且还没有收到。
> - 磁盘统计：磁盘的读写操作，这一栏显示磁盘的读、写总数。
> - 网络统计：网络设备发送和接受的数据，这一栏显示的网络收、发数据总数。
> - 分页统计：系统的分页活动。分页指的是一种内存管理技术用于查找系统场景，一个较大的分页表明系统正在使用大量的交换空间，或者说内存非常分散，大多数情况下你都希望看到page in（换入）和page out（换出）的值是0 0。
> - 系统统计：这一项显示的是中断（int）和上下文切换（csw）。这项统计仅在有比较基线时才有意义。这一栏中较高的统计值通常表示大量的进程造成拥塞，需要对CPU进行关注。你的服务器一般情况下都会运行运行一些程序，所以这项总是显示一些数值。
```
# dstat -c
----total-cpu-usage----
usr sys idl wai hiq siq
  0   0 100   0   0   0
  2   1  96   0   0   1
  2   1  97   0   0   0
  2   1  96   0   0   1
```
> 说明
> - hiq，硬中断次数。
> - siq，软中断次数。
```
# dstat -d
-dsk/total-
 read  writ
1362B   16k
   0     0
   0    32k
   0     0
   0     0
```
```
# dstat -g
---paging--
  in   out
   0     0
   0     0
   0     0
   0     0
   0     0
```
```
# dstat -i
----interrupts---
  32    34    35
   1     0   324
   0     0  2895
   0     0  2470
   0     0  2951
   0     0  2410
   4     0  2974
   0     0  2430
   6     0  2911
   0     0  2441
   0     0  2920
   5     0  2394
   0     0  2878
```
```
# dstat -l
---load-avg---
 1m   5m  15m
   0    0    0
   0    0    0
   0    0    0
```
```
# dstat -m
------memory-usage-----
 used  buff  cach  free
 463M 51.6M  985M 14.0G
 463M 51.6M  986M 14.0G
 464M 51.6M  987M 14.0G
 463M 51.6M  988M 14.0G
 464M 51.6M  989M 14.0G
```
```
# dstat -n
-net/total-
 recv  send
   0     0
1015k 1363k
1004k 1335k
1001k 1382k
1004k 1361k
1004k 1359k
......
# dstat -N eth0,total
----total-cpu-usage---- -dsk/total- --net/eth0---net/total- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send: recv  send|  in   out | int   csw
  0   0 100   0   0   0|1357B   20k|   0     0 :   0     0 |   0     0 | 637  1517
  2   1  96   0   0   0|   0     0 |1044k 1405k:1044k 1405k|   0     0 |5740    12k
  2   1  96   0   0   0|   0    12k| 992k 1332k: 992k 1332k|   0     0 |6720    13k
  2   1  97   0   0   0|   0     0 |1033k 1394k:1033k 1394k|   0     0 |5474    12k
  2   1  96   0   0   1|   0     0 | 989k 1337k: 989k 1337k|   0     0 |6478    12k
  4   1  95   0   0   0|   0     0 |1036k 1395k:1036k 1395k|   0     0 |5711    11k
  2   1  96   0   0   0|   0     0 | 983k 1323k: 983k 1323k|   0     0 |6563    13k
  2   1  96   0   0   1|   0    12k|1041k 1401k:1041k 1401k|   0     0 |5529    11k
  2   1  96   1   0   0|4096B   16M| 983k 1326k: 983k 1326k|   0     0 |6651    13k
  2   1  96   0   0   1|   0    17M|1041k 1403k:1041k 1403k|   0     0 |5625    11k
  2   1  96   0   0   0|   0     0 | 983k 1324k: 983k 1324k|   0     0 |6514    12k
  4   1  95   0   0   0|   0     0 |1041k 1400k:1041k 1400k|   0     0 |5695    11k
```
> 说明
> - int，系统的中断次数（interrupt）
> - csw，系统的上下文切换（context switch）
```
# dstat -p
---procs---
run blk new
  0   0 0.4
  0   0   0
  0   0   0
  0   0   0
  0   0   0
  0   0   0
  0   0   0
  0   0   0
```
```
# dstat -r
--io/total-
 read  writ
0.05  0.43
   0     0
   0     0
   0     0
```
```
# dstat -s
----swap---
 used  free
   0  8008M
   0  8008M
   0  8008M
   0  8008M
```
```
# dstat -T
--epoch---
  epoch
1484635984
1484635985
1484635986
1484635987
1484635988
1484635989
1484635990
```
# 系统统计
```
# dstat -y
---system--
 int   csw
 642  1527
1034  2045
1012  2012
1018  2024
```
```
# dstat --aio
async
 #aio
   0
   0
   0
   0
   0
```
# 文件系统
```
# dstat --fs
--filesystem-
files  inodes
15648  27217
15648  27217
15648  27217
15648  27217
15648  27217
```
```
# dstat --ipc
--sysv-ipc-
msg sem shm
  0   2   0
  0   2   0
  0   2   0
  0   2   0
  0   2   0
  0   2   0
```
# 文件锁
```
# dstat --lock
---file-locks--
pos lck rea wri
  0 3.0   0 3.0
  0 3.0   0 3.0
  0 3.0   0 3.0
  0 3.0   0 3.0
  0 3.0   0 3.0
```
```
# dstat --raw
raw
raw
  0
  0
  0
  0
```
# 网络
```
# dstat --socket
------sockets------
tot tcp udp raw frg
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
 15   6   0   0   0
# dstat --tcp
----tcp-sockets----
lis act syn tim clo
  6   3   0   0  15
  6   3   0   0  15
  6   3   0   0  15
  6   3   0   0  15
  6   3   0   0  15
  6   3   0   0  15
  6   3   0   0  15
  6   3   0   0  15
# dstat --udp
--udp--
lis act
  0   0
  0   0
  0   0
  0   0
  1   0
  1   0
  1   0
  1   0
  1   0
  1   0
  1   0
```
```
# dstat --unix
--unix-sockets-
dgm str lis act
 13  75  23  52
 13  75  23  52
 13  75  23  52
```
# 虚拟内存
```
# dstat --vm
-----virtual-memory----
majpf minpf alloc  free
   0    69    90   126
   0    12     0     0
   0     1     1     3
   0     0     1     1
   0     0     0     1
   0     0     0     0
   0     0     0     2
```
```
# dstat -c --top-cpu -d --top-bio --top-latency
----total-cpu-usage---- -most-expensive- -dsk/total- ----most-expensive---- --highest-total--
usr sys idl wai hiq siq|  cpu process   | read  writ|  block i/o process   | latency process
  0   0 100   0   0   0|obdServer    0.2|1233B  112k|obdServer     0    92k|tail           72
  2   2  96   0   0   0|obdServer    3.2|   0    20k|obdServer     0  1660k|tail         4517
  2   2  95   0   0   0|obdServer    3.6|   0     0 |obdServer     0  1748k|tail         2561
  4   2  94   0   0   0|obdServer    5.4|   0     0 |obdServer     0  1652k|tail           10
  2   2  96   0   0   0|obdServer    3.6|   0     0 |obdServer     0  1756k|tail         2772
  2   2  96   0   0   0|obdServer    3.4|   0     0 |obdServer     0  1656k|tail         2803
  2   2  96   0   0   0|obdServer    3.6|   0    16k|obdServer     0  1752k|tail         3180
  2   2  96   0   0   0|obdServer    3.4|   0     0 |obdServer     0  1652k|tail         3387
  2   2  95   0   0   0|obdServer    3.6|   0     0 |obdServer     0  1756k|tail         2605
  4   2  94   0   0   0|obdServer    5.4|   0     0 |obdServer     0  1656k|ksoftirqd/7    12
  2   2  95   0   0   0|obdServer    3.6|   0     0 |obdServer     0  1752k|tail         2758
  2   2  96   0   0   0|obdServer    3.5|   0    16k|obdServer     0  1656k|tail         2709
```
Using dstat to relate disk-throughput with network-usage (eth0), total CPU-usage and system counters:
```
# dstat -dnyc -N eth0 -C total -f 5
--dsk/sda-- --net/eth0- ---system-- ----total-cpu-usage----
 read  writ| recv  send| int   csw |usr sys idl wai hiq siq
1230B  117k|   0     0 | 955  2329 |  0   0 100   0   0   0
   0  3405k|1035k 1974k|5045    17k|  2   2  96   0   0   0
   0    11k|1063k 2026k|5211    18k|  3   2  95   0   0   0
   0  4096B|1034k 1973k|5041    17k|  2   2  95   0   0   0
   0  3277B|1060k 2023k|5084    17k|  2   2  96   0   0   0
   0  3277B|1038k 1976k|5030    17k|  2   2  96   0   0   0
   0  6861k|1061k 2023k|5211    18k|  2   2  95   0   0   0
   0  3390k|1038k 1977k|5032    17k|  2   2  95   0   0   0
   0  6554B|1063k 2025k|5166    18k|  2   2  95   0   0   0
   0  9011B|1036k 1974k|5046    17k|  2   2  96   0   0   0
```
Checking dstat’s behaviour and the system impact of dstat:
```
# dstat -taf --debug
Module dstat_time
Module dstat_cpu requires ['/proc/stat']
Module dstat_disk requires ['/proc/diskstats']
Module dstat_net requires ['/proc/net/dev']
Module dstat_page requires ['/proc/vmstat']
Module dstat_sys requires ['/proc/stat']
Terminal width too small, trimming output.
------system------ --dsk/sda-- --net/eth0- ---paging-- ---system-->
    date/time     | read  writ| recv  send|  in   out | int   csw >
17-01 17:40:48.971|1228B  119k|   0     0 |   0     0 | 960  2348 >  0.65ms
17-01 17:40:49.972|   0     0 |1044k 1994k|   0     0 |4945    17k>  0.69ms
17-01 17:40:50.971|   0     0 |1057k 2009k|   0     0 |4951    17k>  0.69ms
17-01 17:40:51.972|   0    16k|1050k 2001k|   0     0 |4916    17k>  0.69ms
17-01 17:40:52.971|   0     0 |1051k 2003k|   0     0 |5076    17k>  0.69ms
17-01 17:40:53.972|   0     0 |1046k 2000k|   0     0 |5031    17k>  0.69ms
17-01 17:40:54.972|   0     0 |1054k 2007k|   0     0 |4829    17k>  0.68ms
17-01 17:40:55.972|   0     0 |1054k 2001k|   0     0 |5022    17k>  0.68ms
17-01 17:40:56.972|   0    16k|1048k 1999k|   0     0 |4904    17k>  0.68ms
17-01 17:40:57.972|   0     0 |1050k 2000k|   0     0 |4967    17k>  0.71ms
```
Using the time plugin together with cpu, net, disk, system, load, proc and top_cpu plugins:
```
# dstat -tcndylp --top-cpu
----system---- ----total-cpu-usage---- -net/total- -dsk/total- ---system-- ---load-avg--- ---procs--- -most-expensive-
  date/time   |usr sys idl wai hiq siq| recv  send| read  writ| int   csw | 1m   5m  15m |run blk new|  cpu process
17-01 17:44:23|  0   0 100   0   0   0|   0     0 |1226B  122k| 968  2378 |0.83 0.50 1.08|  0   0 0.5|obdServer    0.2
17-01 17:44:24|  2   2  96   0   0   0|1041k 1983k|   0     0 |4953    17k|0.83 0.50 1.08|  0   0   0|obdServer    3.8
17-01 17:44:25|  2   2  96   0   0   0|1062k 2024k|   0     0 |5073    18k|0.83 0.50 1.08|  0   0   0|obdServer    3.5
17-01 17:44:26|  2   2  96   0   0   0|1039k 1980k|   0     0 |5002    17k|0.83 0.50 1.08|1.0   0   0|obdServer    3.6
17-01 17:44:27|  2   2  96   0   0   1|1062k 2023k|   0    16k|4905    17k|0.84 0.51 1.08|  0   0   0|obdServer    3.4
17-01 17:44:28|  4   2  94   0   0   0|1050k 1997k|   0     0 |5144    17k|0.84 0.51 1.08|  0   0   0|obdServer    5.6
17-01 17:44:29|  2   2  96   0   0   0|1069k 2025k|   0     0 |4988    16k|0.84 0.51 1.08|  0   0   0|obdServer    3.4
17-01 17:44:30|  2   2  96   0   0   0|1040k 1982k|   0     0 |4987    17k|0.84 0.51 1.08|  0   0   0|obdServer    3.6
17-01 17:44:31|  2   2  96   0   0   0|1061k 2021k|   0     0 |4911    17k|0.84 0.51 1.08|  0   0   0|obdServer    3.2
17-01 17:44:32|  2   2  95   0   0   0|1036k 1979k|   0    16k|5028    17k|0.85 0.51 1.08|  0   0   0|obdServer    3.6
```
this is identical to
```
# dstat --time --cpu --net --disk --sys --load --proc --top-cpu
----system---- ----total-cpu-usage---- -net/total- -dsk/total- ---system-- ---load-avg--- ---procs--- -most-expensive-
  date/time   |usr sys idl wai hiq siq| recv  send| read  writ| int   csw | 1m   5m  15m |run blk new|  cpu process
17-01 17:45:15|  0   0 100   0   0   0|   0     0 |1225B  123k| 970  2386 |0.71 0.52 1.06|  0   0 0.5|obdServer    0.2
17-01 17:45:16|  2   2  96   0   0   0|1037k 1979k|   0     0 |5106    17k|0.71 0.52 1.06|  0   0   0|obdServer    3.5
17-01 17:45:17|  4   2  94   0   0   0|1056k 2020k|   0    16k|5626    19k|0.66 0.52 1.05|  0   0   0|obdServer    5.4
17-01 17:45:18|  2   2  96   0   0   0|1033k 1974k|   0     0 |5128    17k|0.66 0.52 1.05|  0   0   0|obdServer    3.6
17-01 17:45:19|  2   2  96   0   0   0|1063k 2021k|   0    84k|5328    18k|0.66 0.52 1.05|  0   0   0|obdServer    3.5
17-01 17:45:20|  2   2  96   0   0   0|1038k 1980k|   0     0 |5071    18k|0.66 0.52 1.05|  0   0   0|obdServer    3.5
17-01 17:45:21|  2   2  96   0   0   0|1059k 2019k|   0     0 |5285    19k|0.66 0.52 1.05|  0   0   0|obdServer    3.6
17-01 17:45:22|  2   2  96   0   0   0|1033k 1975k|   0    16k|5108    17k|0.60 0.51 1.04|  0   0   0|obdServer    3.4
17-01 17:45:23|  4   2  94   0   0   0|1061k 2023k|   0     0 |5617    19k|0.60 0.51 1.04|  0   0   0|obdServer    5.5
```
Using dstat to relate advanced cpu stats with interrupts per device:
```
# dstat -t  -yif
----system---- ---system-- ----------------interrupts---------------
  date/time   | int   csw |  16    23    25    31    32    34    35
17-01 17:47:11| 975  2402 |   1     0     0     0     1     0   441
17-01 17:47:12|5361    19k|   1     0     0     0     5     0  1936
17-01 17:47:13|4883    17k|   1     0     0     0     0     0  1787
17-01 17:47:14|5540    18k|   1     0     0     0     0     0  1987
17-01 17:47:15|4819    17k|   1     0     0     0     0     0  1766
17-01 17:47:16|5170    18k|   1     0     0     0     0     0  1938
17-01 17:47:17|4830    17k|   1     0     0     0     4     0  1743
17-01 17:47:18|5276    18k|   1     0     0     0     7     0  1927
17-01 17:47:19|4742    16k|   1     0     0     0     0     0  1757
```
