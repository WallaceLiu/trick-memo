# Please, commit your changes or stash them before you can merge.
> 表明，代码存在冲突。
```
liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (dev)
$ git pull
Updating 0ad7a94..95c94e0
error: Your local changes to the following files would be overwritten by merge:
        pfs-web/src/main/java/com/jd/pfs/web/service/UploadService.java
        pfs-web/src/main/resources/spring-config.xml
Please, commit your changes or stash them before you can merge.
Aborting
```
如果系统中有一些配置文件在服务器上做了配置修改,然后后续开发又新添加一些配置项的时候,
在发布这个配置文件的时候,会发生代码冲突:

如果希望保留生产服务器上所做的改动,仅仅并入新配置项, 处理方法如下:
```
liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (dev)
$ git stash
Saved working directory and index state WIP on dev: 0ad7a94 1
HEAD is now at 0ad7a94 1

liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (dev)
$ git pull
Updating 0ad7a94..95c94e0
Fast-forward
 .../web/controller/ForecastMonitorController.java  | 234 +++++++++++++++--
 .../com/jd/pfs/web/dao/ForecastMonitorDao.java     |  13 +-
 .../jd/pfs/web/service/ForecastMonitorService.java |  45 +++-
 .../com/jd/pfs/web/service/HBaseServiceImpl.java   | 257 ++++++++++++-------
 .../java/com/jd/pfs/web/service/HrService.java     |   1 +
 .../java/com/jd/pfs/web/service/UploadService.java | 189 ++++++++++++--
 .../src/main/resources/conf/tempright.properties   |  79 ++++++
 pfs-web/src/main/resources/spring-config.xml       |   2 +
 .../src/main/resources/sqlmap/ForecastMonitor.xml  |  26 +-
 .../src/main/webapp/WEB-INF/vm/pfs/pfs_monitor.vm  |  18 +-
 .../webapp/WEB-INF/vm/pfs/pfs_monitor_leader.vm    | 276 +++++++++++++++++++++
 pfs-web/src/main/webapp/js/pfs/pfs_monitor.js      |   6 +
 pfs-web/src/test/java/com/jd/pfs/web/MD5Test.java  |   5 +-
 pfs-web/src/test/java/com/jd/pfs/web/RintTest.java |  11 +
 .../src/test/java/com/jd/pfs/web/StringTest.java   |  61 +++++
 15 files changed, 1070 insertions(+), 153 deletions(-)
 create mode 100644 pfs-web/src/main/resources/conf/tempright.properties
 create mode 100644 pfs-web/src/main/webapp/WEB-INF/vm/pfs/pfs_monitor_leader.vm
 create mode 100644 pfs-web/src/test/java/com/jd/pfs/web/RintTest.java
 create mode 100644 pfs-web/src/test/java/com/jd/pfs/web/StringTest.java

liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (dev)
$ git stash pop
Auto-merging pfs-web/src/main/resources/spring-config.xml
CONFLICT (content): Merge conflict in pfs-web/src/main/resources/spring-config.xml
Auto-merging pfs-web/src/main/java/com/jd/pfs/web/service/UploadService.java
CONFLICT (content): Merge conflict in pfs-web/src/main/java/com/jd/pfs/web/service/UploadService.java
Removing pfs-web/src/main/java/com/jd/pfs/web/common/Export.java
Removing pfs-web/src/main/java/com/jd/pfs/web/common/CommonUtils.java
Removing pfs-web/src/main/java/com/jd/pfs/web/common/Canstants.java

liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (dev)
$
```
> 说明：
> “git stash”是把本地的所有修改就都暂时存储。用“git stash list”可以看到缓存的信息。

> “git pull”是从远端获得最新代码

> git stash pop

此时，你会在代码中看到如下信息：
```
<<<<<<< Updated upstream
……
=======
……
>>>>>>> Stashed changes
```
删掉“Stashed changes”和“=======”之间的代码。

然后，使用“Git diff -w 文件名”来确认代码自动合并的情况。

但是，如果想用远端代码完全覆盖本地工作版本. 方法如下:
```
git reset --hard
git pull
```
其中，“git reset”是针对版本,如果想针对文件回退本地修改,使用
“git checkout HEAD file/to/restore”。 

# Changes not staged for commit:
无。
# 本地Commit之后，Push提示大文件被拒绝，如何处理？
处理已经Commit的大文件

只Reset最后一次commit
```
git reset --mixed HEAD^
```
Reset最后2次commit
```
git reset --mixed HEAD~2
```
依次类推，Reset最后N次commit
```
git reset --mixed HEAD~N
```
如果可以丢弃commit内容，可以直接使用 --hard 参数替换 --mixed