# 安装
```
yum install sysstat
```
# 命令格式
```
sar -n { DEV | EDEV | NFS | NFSD | SOCK | ALL }
```
sar 提供六种不同的语法选项来显示网络信息。
-n选项使用6个不同的开关：DEV | EDEV | NFS | NFSD | SOCK | ALL 。
- DEV显示网络接口信息
- EDEV显示关于网络错误的统计数据
- NFS统计活动的NFS客户端的信息
- NFSD统计NFS服务器的信息
- SOCK显示套接字信息
- ALL显示所有5个开关。

它们可以单独或者一起使用。
```
[root@localhost fs]# sar -n DEV 2 10
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月10日 	_x86_64_	(8 CPU)

15时55分38秒     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
15时55分40秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
15时55分40秒      eth0   1450.51    809.60     96.87    216.33      0.00      0.00      0.00

15时55分40秒     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
15时55分42秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
15时55分42秒      eth0   1465.50    816.00     98.03    220.22      0.00      0.00      0.00

15时55分42秒     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
15时55分44秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
15时55分44秒      eth0   1440.40    793.43     96.14    206.56      0.00      0.00      0.00

15时55分44秒     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
15时55分46秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
15时55分46秒      eth0   1419.00    751.00     94.74    137.26      0.00      0.00      0.00
......
```
> - IFACE：LAN接口
> - rxpck/s：每秒钟接收的数据包
> - txpck/s：每秒钟发送的数据包
> - rxbyt/s：每秒钟接收的字节数
> - txbyt/s：每秒钟发送的字节数
> - rxcmp/s：每秒钟接收的压缩数据包
> - txcmp/s：每秒钟发送的压缩数据包
> - rxmcst/s：每秒钟接收的多播数据包
```
[root@localhost fs]# sar -n EDEV 2 10
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月10日 	_x86_64_	(8 CPU)

16时48分23秒     IFACE   rxerr/s   txerr/s    coll/s  rxdrop/s  txdrop/s  txcarr/s  rxfram/s  rxfifo/s  txfifo/s
16时48分25秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
16时48分25秒      eth0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

16时48分25秒     IFACE   rxerr/s   txerr/s    coll/s  rxdrop/s  txdrop/s  txcarr/s  rxfram/s  rxfifo/s  txfifo/s
16时48分27秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
16时48分27秒      eth0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

16时48分27秒     IFACE   rxerr/s   txerr/s    coll/s  rxdrop/s  txdrop/s  txcarr/s  rxfram/s  rxfifo/s  txfifo/s
16时48分29秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
16时48分29秒      eth0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

16时48分29秒     IFACE   rxerr/s   txerr/s    coll/s  rxdrop/s  txdrop/s  txcarr/s  rxfram/s  rxfifo/s  txfifo/s
16时48分31秒        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
16时48分31秒      eth0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
......
```
> - IFACE：LAN接口
> - rxerr/s：每秒钟接收的坏数据包 
> - txerr/s：每秒钟发送的坏数据包
> - coll/s：每秒冲突数
> - rxdrop/s：因为缓冲充满，每秒钟丢弃的已接收数据包数
> - txdrop/s：因为缓冲充满，每秒钟丢弃的已发送数据包数
> - txcarr/s：发送数据包时，每秒载波错误数
> - rxfram/s：每秒接收数据包的帧对齐错误数
> - rxfifo/s：接收的数据包每秒FIFO过速的错误数
> - txfifo/s：发送的数据包每秒FIFO过速的错误数
```
[root@localhost fs]# sar -n SOCK 2 5
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月10日 	_x86_64_	(8 CPU)

16时49分35秒    totsck    tcpsck    udpsck    rawsck   ip-frag    tcp-tw
16时49分37秒      9982         6         0         0         0         0
16时49分39秒      9986         6         0         0         0         0
16时49分41秒      9990         6         0         0         0         0
16时49分43秒      9994         6         0         0         0         0
16时49分45秒      9998         6         0         0         0         0
平均时间:      9990         6         0         0         0         0
```
> - totsck:使用的套接字总数量
> - tcpsck:使用的TCP套接字数量
> - udpsck:使用的UDP套接字数量
> - rawsck:使用的raw套接字数量
> - ip-frag:使用的IP段数量


```
# sar -n TCP 1 10
Linux 2.6.32-431.el6.x86_64 (localhost) 	2017年01月16日 	_x86_64_	(8 CPU)

17时08分08秒  active/s passive/s    iseg/s    oseg/s
17时08分09秒      0.00      0.00   1157.14    634.69
17时08分10秒      0.00      0.00   1109.18    610.20
17时08分11秒      0.00      0.00   1132.00    621.00
17时08分12秒      0.00      0.00   1088.00    599.00
17时08分13秒      0.00      0.00   1155.10    632.65
17时08分14秒      0.00      0.00   1108.16    609.18
17时08分15秒      0.00      0.00   1156.12    634.69
17时08分16秒      0.00      0.00   1078.00    593.00
17时08分17秒      0.00      0.00   1165.31    638.78
17时08分18秒      0.00      0.00   1076.00    592.00
平均时间:      0.00      0.00   1122.27    616.40
```
说明：
> - active/s，The number of times TCP connections have made a direct transition to the SYN-SENT state from the CLOSED state per second [tcpActiveOpens].
> - passive/s，The number of times TCP connections have made a direct transition to the SYN-RCVD state from the LISTEN state per second [tcpPassiveOpens].
> - iseg/s，The total number of segments received per second, including those received in error [tcpInSegs]. This count includes segments received on
currently established connections.
> - oseg/s，The total number of segments sent per second, including those on current connections but excluding those containing only retransmitted octets [tcpOutSegs].