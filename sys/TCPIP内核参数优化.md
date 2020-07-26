若以8核CPU、16G内存服务器为例。
```
net.core.netdev_max_backlog=400000
#40万
#该参数决定网络设备接收数据包的速率比内核处理这些包的速率快时，允许送到队列的数据包的最大数量。

net.core.somaxconn=100000
#10万。
#定义系统中每个socket最大监听队列backlog长度，这是个全局参数。

net.core.optmem_max=10000000
#该参数指定了每个socket监听所允许的最大缓冲区（单位：字节）。

net.core.rmem_default=10000000
#指定了接收套接字缓冲区的大小（单位：字节）。

net.core.rmem_max=10000000
#指定了接收套接字缓冲区的大小（单位：字节）。

net.core.wmem_default=11059200
#定义默认的发送窗口大小；对于更大的BDP来说，这个大小也应该更大。（单位：字节）。

net.core.wmem_max=11059200
#定义发送窗口的最大大小；对于更大的BDP来说，这个大小也应该更大。（单位：字节）。
```
```
net.ipv4.conf.all.rp_filter=1

net.ipv4.conf.default.rp_filter=1
#启用
#1为严谨模式 (推荐)，0为松散模式
```
```
net.ipv4.tcp_congestion_control=bic
#默认推荐设置是 htcp

net.ipv4.tcp_window_scaling=0
#关闭tcp_window_scaling
#启用 RFC 1323 定义的 window scaling；要支持超过 64KB 的窗口，必须启用该值（1表示启用）。
#TCP窗口最大至1GB，TCP连接双方都启用时才生效。

net.ipv4.tcp_ecn=0
#把TCP的直接拥塞通告(tcp_ecn)关掉

net.ipv4.tcp_sack=1
#关闭tcp_sack
#启用有选择的应答（Selective Acknowledgment），
#这可以通过有选择地应答乱序接收到的报文来提高性能（这样可以让发送者只发送丢失的报文段）；
#（对于广域网通信来说）这个选项应该启用，但是这会增加对 CPU 的占用。

net.ipv4.tcp_fack=1
#启用转发应答，可以进行有选择应答（SACK）从而减少拥塞情况的发生，这个选项也应该启用。
```
```
net.ipv4.tcp_max_tw_buckets=10000
#表示系统同时保持TIME_WAIT套接字的最大数量

net.ipv4.tcp_max_syn_backlog=8192
#表示SYN队列长度，默认1024，改成8192，可以容纳更多等待连接的网络连接数。
#如果服务器经常出现过载，可以尝试增加这个数字。

net.ipv4.tcp_low_latency=0
#允许TCP/IP栈适应在高吞吐量情况下低延时的情况，这个选项应该禁用。

net.ipv4.tcp_westwood=0
#启用发送者端的拥塞控制算法，它可以维护对吞吐量的评估，并试图对带宽的整体利用情况进行优化，对于WAN 通信来说应该启用这个选项。

net.ipv4.tcp_bic=1
#为快速长距离网络启用Binary Increase Congestion，这样可以更好地利用以GB速度进行操作的链接，对于WAN通信应该启用这个选项。
```
```
net.ipv4.tcp_syncookies=1
#表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭。

net.ipv4.tcp_timestamps=1
#开启TCP时间戳（会在TCP包头增加12个字节）,为了实现更好的性能应该启用这个选项。
#以一种比重发超时更精确的方法（请参阅 RFC 1323）来启用对 RTT 的计算
```
```
net.ipv4.tcp_tw_reuse=1
#启用。
#允许将TIME-WAIT sockets重新用于新的TCP连接，默认关闭为0；

net.ipv4.tcp_tw_recycle=1
#表示开启TCP连接中TIME-WAIT sockets的快速回收，默认关闭为0。
```
```
net.ipv4.tcp_fin_timeout=10
#表示对于本端断开的socket连接，TCP保持在FIN-WAIT-2状态的时间（秒）。对方可能会断开连接或一直不结束连接或不可预料的进程死亡。
```
```
net.ipv4.tcp_keepalive_time=1800
#表示TCP发送keepalive探测消息的间隔时间（秒），用于确认TCP连接是否有效。
#缺省2小时(7200秒)，改为30分钟。

net.ipv4.tcp_keepalive_probes=3
#在认定TCP连接失效之前，最多发送多少个keepalive探测消息。

net.ipv4.tcp_keepalive_intvl=15
#keepalive探测消息未获得响应时，重发该消息的间隔时间（秒）。
```
```
net.ipv4.tcp_mem=131072  262144  524288
#确定TCP栈应该如何反映内存使用；单位都是内存页（通常是 4KB）。
#第一个值是内存使用的下限。
#第二个值是内存压力模式开始对缓冲区使用应用压力的上限。
#第三个值是内存上限。在这个层次上可以将报文丢弃，从而减少对内存的使用。对于较大的 BDP 可以增大这些值
#（但要记住，其单位是内存页，而不是字节）。

net.ipv4.tcp_wmem=8760 256960 4088000
#为自动调优定义每个socket使用的内存。
#第一个值是为socket的发送缓冲区分配的最少字节数。
#第二个值是默认值（该值会被 wmem_default 覆盖），缓冲区在系统负载不重的情况下可以增长到这个值。
#第三个值是发送缓冲区空间的最大字节数（该值会被 wmem_max 覆盖）。

net.ipv4.tcp_rmem=8760 256960 4088000
#与tcp_wmem类似，不过它表示的是为自动调优所使用的接收缓冲区的值。

net.ipv4.ip_local_port_range=102465000
#表示用于向外连接的端口范围。缺省情况下很小：32768到61000，改为1024到65000。

net.ipv4.netfilter.ip_conntrack_max=204800
#设置系统对最大跟踪的TCP连接数的限制

net.ipv4.tcp_slow_start_after_idle=0
#关闭tcp的连接传输的慢启动，即先休止一段时间，再初始化拥塞窗口。
net.ipv4.route.gc_timeout=100
#路由缓存刷新频率，当一个路由失败后多长时间跳到另一个路由，默认是300。

net.ipv4.tcp_syn_retries=1
#在内核放弃建立连接之前发送SYN包的数量。
```
```
net.ipv4.icmp_echo_ignore_broadcasts=1
# 避免放大攻击

net.ipv4.icmp_ignore_bogus_error_responses=1
# 开启恶意icmp错误消息保护

net.inet.udp.checksum=1
#防止不正确的udp包的攻击

net.ipv4.conf.default.accept_source_route=0
#是否接受含有源路由信息的ip包。参数值为布尔值，1表示接受，0表示不接受。
#在充当网关的linux主机上缺省值为1，在一般的linux主机上缺省值为0。
#从安全性角度出发，建议你关闭该功能。
```