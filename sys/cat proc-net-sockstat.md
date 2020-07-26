TCPIPV4统计
```
[root@localhost myserver]# cat /proc/net/sockstat
sockets: used 227
TCP: inuse 5 orphan 0 tw 0 alloc 108 mem 22
UDP: inuse 0 mem 0
UDPLITE: inuse 0
RAW: inuse 0
FRAG: inuse 0 memory 0
```
说明：
- sockets: used：
已使用的所有协议套接字总量
- TCP: inuse：正在侦听的TCP套接字数量。
其值约等于 netstat –lnt | grep ^tcp | wc –l
```
# netstat -lnt | grep ^tcp | wc -l
6
```
- TCP: orphan：无主（不属于任何进程）的TCP连接数（无用、待销毁的TCP socket数）
- TCP: tw：等待关闭的TCP连接数。其值等于netstat –ant | grep TIME_WAIT | wc –l
- TCP：alloc(allocated)：已分配（已建立、已申请到sk_buff）的TCP套接字数量。其值等于
netstat –ant | grep ^tcp | wc –l
```
# netstat -ant | grep ^tcp | wc -l
108
```
- TCP：mem：套接字缓冲区使用量（单位不详。用scp实测，速度在4803.9kB/s时：其值=11，netstat –ant 中相应的22端口的Recv-Q＝0，Send-Q≈400）
- UDP：inuse：正在使用的UDP套接字数量
- RAW: inuse
- FRAG：使用的IP段数量
