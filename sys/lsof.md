lsof(list open files)是一个列出当前系统打开文件的工具。

在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。所以如传输控制协议 (TCP) 和用户数据报协议 (UDP) 套接字等，系统在后台都为该应用程序分配了一个文件描述符，无论这个文件的本质如何，该文件描述符为应用程序与基础操作系统之间的交互提供了通用接口。因为应用程序打开文件的描述符列表提供了大量关于这个应用程序本身的信息，因此通过lsof工具能够查看这个列表对系统监测以及排错将是很有帮助的。

用法：
```
 usage: [-?abhlnNoOPRtUvV] [+|-c c] [+|-d s] [+D D] [+|-f[cgG]]
 [-F [f]] [-g [s]] [-i [i]] [+|-L [l]] [+|-M] [-o [o]] [-p s]
 [+|-r [t]] [-s [p:s]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]
Defaults in parentheses; comma-separated set (s) items; dash-separated ranges.
  -?|-h list help          -a AND selections (OR)     -b avoid kernel blocks
  -c c  cmd c ^c /c/[bix]  +c w  COMMAND width (9)    +d s  dir s files
  -d s  select by FD set   +D D  dir D tree *SLOW?*   -i select IPv[46] files
  -l list UID numbers      -n no host names           -N select NFS files
  -o list file offset      -O no overhead *RISKY*     -P no port names
  -R list paRent PID       -s list file size          -t terse listing
  -T disable TCP/TPI info  -U select Unix socket      -v list version info
  -V verbose search        +|-w  Warnings (+)         -- end option scan
  +f|-f  +filesystem or -file names     +|-f[cgG] Ct flaGs
  -F [f] select fields; -F? for help
  +|-L [l] list (+) suppress (-) link counts < l (0 = all; default = 0)
  +|-M   portMap registration (-)       -o o   o 0t offset digits (8)
  -p s   exclude(^)|select PIDs         -S [t] t second stat timeout (15)
  -T fqs TCP/TPI Fl,Q,St (s) info
  -g [s] exclude(^)|select and print process group IDs
  -i i   select by IPv[46] address: [46][proto][@host|addr][:svc_list|port_list]
  +|-r [t[m<fmt>]] repeat every t seconds (15);  + until no files, - forever.
       An optional suffix to t is m<fmt>; m must separate t from <fmt> and
      <fmt> is an strftime(3) format for the marker line.
  -s p:s  exclude(^)|select protocol (p = TCP|UDP) states by name(s).
  -u s   exclude(^)|select login|UID set s
  -x [fl] cross over +d|+D File systems or symbolic Links
  names  select named files or files on named file systems
Anyone can list all files; /dev warnings disabled; kernel ID check disabled.
```

- lsof
```
capdeMacBook-Pro:MYHD cap$ lsof
COMMAND     PID USER   FD      TYPE             DEVICE   SIZE/OFF    NODE NAME
loginwind   107  cap  cwd       DIR                1,4       1156       2 /
loginwind   107  cap  txt       REG                1,4    1202112 6639149 /System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow
loginwind   107  cap  txt       REG                1,4   25918784 6632216 /usr/share/icu/icudt57l.dat
......
```
> 说明：
> - COMMAND，进程的名称
> - PID，进程标识符
> - USER，进程所有者
> - FD，文件描述符，应用程序通过文件描述符识别该文件。如cwd、txt等
> - TYPE，文件类型，如DIR、REG等
> - DEVICE，指定磁盘的名称
> - SIZE，文件的大小
> - NODE，索引节点（文件在磁盘上的标识）
> - NAME，打开文件的确切名称

> FD列中的文件描述符
> - cwd，表示应用程序的当前工作目录，这是该应用程序启动的目录，除非它本身对这个目录进行更改
> - txt，表示程序代码，如应用程序二进制文件本身或共享库，如上列表中显示的 /sbin/init 程序。
> - 数值开头，表示应用程序的文件描述符，这是打开该文件时返回的一个整数。
> - u，表示该文件被打开并处于读取/写入模式，而不是只读 ® 或只写 (w) 模式。
> - 同时还有大写的W，表示该应用程序具有对整个文件的写锁。该文件描述符用于确保每次只能打开一个应用程序实例。初始打开每个应用程序时，都具有三个文件描述符，从 0 到 2，分别表示标准输入、输出和错误流。所以大多数应用程序所打开的文件的 FD 都是从 3 开始。

> 与 FD 列相比，Type 列则比较直观。文件和目录分别称为 REG 和 DIR。而CHR 和 BLK，分别表示字符和块设备；或者 UNIX、FIFO 和 IPv4，分别表示 UNIX 域套接字、先进先出队列和网际协议 (IP) 套接字。

- 显示开启文件abc.txt的进程
```
lsof abc.txt 
```
- 列出进程号为1234的进程所打开的文件
```
lsof -c -p 1234
```
- 显示归属gid的进程情况
```
lsof -g gid 
```
- 显示目录下被进程开启的文件
```
lsof +d /usr/local/
```
- 同上，但是会搜索目录下的目录，时间较长
```
lsof +D /usr/local/
```
- 显示使用fd为4的进程
```
lsof -d 4 
```
- 哪个进程在使用apache的可执行文件
```
lsof `which httpd`
```
- 那个进程在占用/etc/passwd
```
lsof /etc/passwd
```
- 那个进程在占用hda6
```
lsof /dev/hda6
```
- 那个进程在占用光驱
```
lsof /dev/cdrom
```
- 查看sendmail进程的文件使用情况
```
lsof -c sendmail
```
- 显示那些文件被以courier打头的进程打开，但是并不属于用户zahn
```
lsof -c courier -u ^zahn
```
- 显示那些文件被pid为30297的进程打开
```
lsof -p 30297
```
- 显示所有在/tmp文件夹中打开的instance和文件的进程。但是symbol文件并不在列
```
lsof -D /tmp 
```
# 查看某个用户名或UID进程使用
- 查看uid是100的用户的进程的文件使用情况
```
lsof -u 1000
```
- 查看用户tony的进程的文件使用情况
```
lsof -u tony
```
- 查看不是用户tony的进程的文件使用情况(^是取反的意思)
```
lsof -u ^tony
```
# 显示符合条件的进程情况
```
lsof -i [46] [protocol][@hostname|hostaddr][:service|port]
```
> - 46，IPv4 or IPv6
> - protocol，TCP or UDP
> - hostname，Internet host name
> - hostaddr，IPv4地址
> - service，/etc/service中的 service name (可以不止一个)
> - port，端口号

- 显示所有打开的端口
```
lsof -i
```
- 显示所有打开80端口的进程
```
lsof -i :80
```
- 显示所有打开的端口和UNIX domain文件
```
lsof -i -U
```
- 显示那些进程打开了到www.akadia.com的UDP的123(ntp)端口的链接
```
lsof -i UDP@[url]www.akadia.com:123
```
- 不断查看目前ftp连接的情况(-r，lsof会永远不断的执行，直到收到中断信号,+r，lsof会一直执行，直到没有档案被显示,缺省是15s刷新)
```
lsof -i tcp@ohaha.ks.edu.tw:ftp -r
```
- lsof -n 不将IP转换为hostname，缺省是不加上-n参数
```
lsof -i tcp@ohaha.ks.edu.tw:ftp -n
```