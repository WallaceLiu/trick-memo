yum（Yellow dog Updater, Modified），主要功能是更方便的添加/删除/更新RPM包，它能自动解决包的倚赖性问题，它能便于管理大量系统的更新问题。
- 列出所指定的软件包,，后面可以加上你想查找的软件包的名字。
```
[root@vcyber src]# yum list
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.btte.net
 * epel: mirrors.opencas.cn
 * extras: mirrors.btte.net
 * updates: mirrors.yun-idc.com
……
```
- 列出所有已安装的软件包
```
[root@vcyber src]# yum list installed
Loaded plugins: fastestmirror
No such command: linst. Please use /usr/bin/yum --help
[root@vcyber src]# yum list installed
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.btte.net
 * epel: mirrors.hustunique.com
 * extras: mirrors.btte.net
 * updates: mirrors.yun-idc.com
……
```
- 列出所有已安裝的软件包信息
```
[root@vcyber src]# yum info installed
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.btte.net
 * epel: mirrors.opencas.cn
 * extras: mirrors.btte.net
 * updates: mirrors.yun-idc.com
……
```
- 安装
```
[root@vcyber src]# yum install grep
Loaded plugins: fastestmirror
Setting up Install Process
Loading mirror speeds from cached hostfile
 * base: mirrors.btte.net
 * epel: mirrors.opencas.cn
 * extras: mirrors.btte.net
 * updates: mirrors.yun-idc.com
Resolving Dependencies
--> Running transaction check
---> Package grep.x86_64 0:2.6.3-6.el6 will be updated
---> Package grep.x86_64 0:2.20-3.el6_7.1 will be an update
--> Finished Dependency Resolution
……
```
- 卸载
```
[root@vcyber src]# yum remove grep
```
包名区分大小写。
