Mac 挂载NTFS移动硬盘进行读写操作 （Read-only file system）
# 查看设备node
```
$ diskutil info /Volumes/CJK
   Device Identifier:        disk3s1
   Device Node:              /dev/disk3s1
   Whole:                    No
   Part of Whole:            disk3

   Volume Name:              CJK
   Mounted:                  Yes
   Mount Point:              /Volumes/CJK
   ......
```
# 弹出移动硬盘
```
$ hdiutil eject /Volumes/CJK
"disk1" unmounted.
"disk1" ejected.
```
# 创建一个目录，稍后将mount到这个目录
```
$ sudo mkdir /Volumes/MYHD
```
# 将NTFS硬盘 挂载 mount 到mac
```
$ sudo mount_ntfs -o rw,nobrowse /dev/disk3s1 /Volumes/MYHD/
```
使用完成后卸载。
```
sudo umount /dev/disk3s1
```