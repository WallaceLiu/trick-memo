[systat 官网](http://sebastien.godard.pagesperso-orange.fr/documentation.html)

sar 命令行的常用格式
```
sar [options] [-A] [-o file] t [n] 
```
n 和t 两个参数组合起来定义采样间隔和次数，t为采样间隔，是必须有 
的参数，n为采样次数，是可选的，默认值是1，-o file表示将命令结果以二进制格式 
存放在文件中，file 在此处不是关键字，是文件名。options 为命令行选项

```
	-b	I/O 和传输速率信息状况
	-B	分页状况
	-d	块设备状况
	-I { <中断> | SUM | ALL | XALL }
		中断信息状况
	-m	电源管理信息状况
	-n { <关键词> [,...] | ALL }
		网络统计信息
		关键词可以是：
		DEV	网卡
		EDEV	网卡 (错误)
		NFS	NFS 客户端
		NFSD	NFS 服务器
		SOCK	Sockets (套接字)	(v4)
		IP	IP 流	(v4)
		EIP	IP 流	(v4) (错误)
		ICMP	ICMP 流	(v4)
		EICMP	ICMP 流	(v4) (错误)
		TCP	TCP 流	(v4)
		ETCP	TCP 流	(v4) (错误)
		UDP	UDP 流	(v4)
		SOCK6	Sockets (套接字)	(v6)
		IP6	IP 流	(v6)
		EIP6	IP 流	(v6) (错误)
		ICMP6	ICMP 流	(v6)
		EICMP6	ICMP 流	(v6) (错误)
		UDP6	UDP 流	(v6)
	-q	队列长度和平均负载
	-r	内存利用率
	-R	内存状况
	-S	交换空间利用率
	-u [ ALL ]
		CPU 利用率
	-v	Kernel table 状况
	-w	任务创建与系统转换统计信息
	-W	交换信息
	-y	TTY 设备状况
```
sdaf功能类似，但是格式不太友好。

# 查看CPU
```
[root@localhost ~]# sar -u 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时20分42秒     CPU     %user     %nice   %system   %iowait    %steal     %idle
14时20分43秒     all      0.00      0.00      0.00      0.00      0.00    100.00
14时20分44秒     all      0.00      0.00      0.00      0.38      0.00     99.62
平均时间:     all      0.00      0.00      0.00      0.19      0.00     99.81
[root@localhost ~]#
```
在显示内容包括： 
- %usr：CPU处在用 户模式下的时间百分比。 
- %sys：CPU处在系统模式下的时间百分比。 
- %wio：CPU等待输入输出完成时间的百分比。 
- %idle：CPU空闲时间百分比。 

主要注意%wio和%idle，%wio的值过高,表示硬盘存在I/O瓶颈；%idle值高，表示CPU较空闲；如果%idle值高但系统响应慢时，有可能是CPU等待分配内存，此时应加大内存容量；如果%idle值持续低于10,那么系统的CPU处理能力相对较低，表明系统中最需要解决的资源是CPU。 
```
[root@localhost ~]# sar -v 1 3
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时28分00秒 dentunusd   file-nr  inode-nr    pty-nr
14时28分01秒     10385      1792     14540        16
14时28分02秒     10385      1792     14541        16
14时28分03秒     10385      1792     14542        16
平均时间:     10385      1792     14541        16
[root@localhost ~]#
```
> - proc-sz：目前核心中正在使用或分配的进程表的表项数，由核心参数MAX-PROC控制。 
> - inod-sz：目前核心中正在使用或分配的i节点表的表项数，由核心参数MAX- INODE控制。 
> - file-sz：目前核心中正在使用或分配的文件表的表项数，由核心参数MAX-FILE控制。 
> - ov：溢出出现的次数。 
> - Lock-sz：目前核心中正在使用或分配的记录加锁的表项数，由核心参数MAX-FLCKRE控制。

显示格式为：实际使用表项/可以使用的表项数 

显示内容表示，核心使用完全正常，三个表没有出现 溢出现象，核心参数不需调整，如果出现溢出时，要调整相应的核心参数，将对应的表项数加大。

```
[root@localhost ~]# sar -d 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时33分12秒       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
14时33分13秒    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
14时33分13秒  dev253-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
14时33分13秒  dev253-1      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
14时33分13秒  dev253-2      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

14时33分13秒       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
14时33分14秒    dev8-0      4.00      0.00     32.00      8.00      0.04      8.75      8.75      3.50
14时33分14秒  dev253-0      4.00      0.00     32.00      8.00      0.04      8.75      8.75      3.50
14时33分14秒  dev253-1      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
14时33分14秒  dev253-2      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

平均时间:       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
平均时间:    dev8-0      2.00      0.00     16.00      8.00      0.02      8.75      8.75      1.75
平均时间:  dev253-0      2.00      0.00     16.00      8.00      0.02      8.75      8.75      1.75
平均时间:  dev253-1      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
平均时间:  dev253-2      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
[root@localhost ~]#
```
> - device： sar命令正在监视的块设备的名字。 
> - %busy： 设备忙时，传送请求所占时间的百分比。 
> - avque： 队列满时，未完成请求数量的平均值。 
> - r+w/s： 每秒传送到设备或从设备传出的数据量。 
> - blks/s： 每秒传送的块数，每块512字节。 
> - avwait：队列满时传送请求等待队列空闲的平均时间。 
> - avserv：完成传送请求所需平均时间（毫秒）。 

%busy值较小，说明用于处理传送请求的有效时间太少，文件系统效率不高。一般，%busy值高些，avque值低些，文件系统的效率比较高，如果%busy和avque值相对比较高，说明硬盘传输速度太慢，需调整。 

# I/O和传送速率监控
```
[root@localhost ~]# sar -b 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时37分49秒       tps      rtps      wtps   bread/s   bwrtn/s
14时37分50秒      0.00      0.00      0.00      0.00      0.00
14时37分51秒      9.00      0.00      9.00      0.00     80.00
平均时间:      4.50      0.00      4.50      0.00     40.00
[root@localhost ~]#
```
> - bread/s： 每秒从硬盘读入系统缓冲区buffer的物理块数。 
> - lread/s： 平均每秒从系统buffer读出的逻辑块数。 
> - %rcache： 在buffer cache中进行逻辑读的百分比。 
> - bwrit/s： 平均每秒从系统buffer向磁盘所写的物理块数。 
> - lwrit/s： 平均每秒写到系统buffer逻辑块数。 
> - %wcache： 在buffer cache中进行逻辑读的百分比。 
> - pread/s： 平均每秒请求物理读的次数。 
> - pwrit/s： 平均每秒请求物理写的次数。 

最重要的是%cache 和%wcache两列，它们的值体现着buffer的使用效 
率，%rcache的值小于90或者%wcache的值低于65，应适当增加系统 buffer的数量，buffer 
数量由核心参数NBUF控制，使%rcache达到90左右，%wcache达到80左右。但buffer参 数值的多少影响I/O效率，增加buffer，应在较大内存的情况下，否则系统效率反而得不到提高。

# 队列长度和平均负载
```
[root@localhost ~]# sar -q 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时42分28秒   runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15
14时42分29秒         0       185      0.00      0.00      0.00
14时42分30秒         0       185      0.00      0.00      0.00
平均时间:         0       185      0.00      0.00      0.00
[root@localhost ~]#
```
> - runq-sz：运行队列的长度（等待运行的进程数）
> - plist-sz：进程列表中进程（processes）和线程（threads）的数量
> - ldavg-1：最后1分钟的系统平均负载
> - ldavg-5：过去5分钟的系统平均负载
> - ldavg-15：过去15分钟的系统平均负载
# 内存使用状况
```
[root@localhost ~]# sar -r 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时43分11秒 kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit
14时43分12秒  15879196    386272      2.37     38616    136668     54232      0.22
14时43分13秒  15879196    386272      2.37     38616    136668     54232      0.22
平均时间:  15879196    386272      2.37     38616    136668     54232      0.22
[root@localhost ~]#
```
> - kbmemfree：这个值和free命令中的free值基本一致,所以它不包括buffer和cache的空间.
> - kbmemused：这个值和free命令中的used值基本一致,所以它包括buffer和cache的空间.
> - %memused：物理内存使用率，这个值是kbmemused和内存总量(不包括swap)的一个百分比.
> - kbbuffers和kbcached：这两个值就是free命令中的buffer和cache.
> - kbcommit：保证当前系统所需要的内存,即为了确保不溢出而需要的内存(RAM+swap).
> - %commit：这个值是kbcommit与内存总量(包括swap)的一个百分比.
# 页面交换发生状况
页面发生交换时，服务器的吞吐量会大幅下降；服务器状况不良时，如果怀疑因为内存不足而导致了页面交换的发生，可以使用这个命令来确认是否发生了大量的交换.
```
[root@localhost myserver]# sar -W 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月13日 	_x86_64_	(8 CPU)

16时17分13秒  pswpin/s pswpout/s
16时17分14秒      0.00      0.00
16时17分15秒      0.00      0.00
平均时间:      0.00      0.00
[root@localhost myserver]#
```
> - pswpin/s：每秒系统换入的交换页面（swap page）数量
> - pswpout/s：每秒系统换出的交换页面（swap page）数量

```
[root@localhost ~]# sar -w 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时43分55秒    proc/s   cswch/s
14时43分56秒      0.00     52.00
14时43分57秒      0.00     40.00
平均时间:      0.00     46.00
[root@localhost ~]#
```

```
[root@localhost ~]# sar -y 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时44分19秒       TTY   rcvin/s   xmtin/s framerr/s prtyerr/s     brk/s   ovrun/s
14时44分20秒         0      0.00      0.00      0.00      0.00      0.00      0.00

14时44分20秒       TTY   rcvin/s   xmtin/s framerr/s prtyerr/s     brk/s   ovrun/s
14时44分21秒         0      0.00      0.00      0.00      0.00      0.00      0.00

平均时间:       TTY   rcvin/s   xmtin/s framerr/s prtyerr/s     brk/s   ovrun/s
平均时间:         0      0.00      0.00      0.00      0.00      0.00      0.00
[root@localhost ~]#
```
> - rawch/s 每秒输入的字符数（原始队列） 
> - canch/s 每秒由正则队列（canonical queue）处理的输入字符数。进行正则处理过程中，可以识别出一些有特殊意义的字符。比如，(中断字符)，(退出符)，(退格键)等。因此，canch/s中的计数不包括这些有特殊意义的字符。 
> - outch/s 每秒输出的字符数。 
> - rcvin/s 每秒接收的硬件中断次数。 
> - xmtin/s 每秒发出的硬件中断次数。 
> - mdmin/s 每秒modem中断次数。 
内存分页监控

# 监控内存分页
```
[root@localhost ~]# sar -B 1 2
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月12日 	_x86_64_	(8 CPU)

14时47分33秒  pgpgin/s pgpgout/s   fault/s  majflt/s  pgfree/s pgscank/s pgscand/s pgsteal/s    %vmeff
14时47分34秒      0.00      0.00     36.00      0.00     69.00      0.00      0.00      0.00      0.00
14时47分35秒      0.00      4.00     40.00      0.00     66.00      0.00      0.00      0.00      0.00
平均时间:      0.00      2.00     38.00      0.00     67.50      0.00      0.00      0.00      0.00
[root@localhost ~]#
```
> - pgpgin/s：表示每秒从磁盘或SWAP置换到内存的字节数(KB)
> - pgpgout/s：表示每秒从内存置换到磁盘或SWAP的字节数(KB)
> - fault/s：每秒钟系统产生的缺页数,即主缺页与次缺页之和(major + minor)
> - majflt/s：每秒钟产生的主缺页数.
> - pgfree/s：每秒被放入空闲队列中的页个数
> - pgscank/s：每秒被kswapd扫描的页个数
> - pgscand/s：每秒直接被扫描的页个数
> - pgsteal/s：每秒钟从cache中被清除来满足内存需要的页个数
> - %vmeff：每秒清除的页(pgsteal)占总扫描页(pgscank+pgscand)的百分比

