分两步：重命名分支后，删除之前的分支。
```
liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (dev_tushucuxiao)
$ git branch -av
  0-a                            90861ee 1
  dev                            98fe25f 促销二期忘记注销写死的变量
  dev_liuning39                  2eb04e2 test
* dev_tushucuxiao                fb24d51 单量预测促销二期重构
  master                         98fe25f 促销二期忘记注销写死的变量
  remotes/origin/0-a             90861ee 1
  remotes/origin/HEAD            -> origin/master
  remotes/origin/dev             98fe25f 促销二期忘记注销写死的变量
  remotes/origin/dev_liuning39   2eb04e2 test
  remotes/origin/dev_tushucuxiao fb24d51 单量预测促销二期重构
  remotes/origin/master          98fe25f 促销二期忘记注销写死的变量
  remotes/origin/order2nd        792916c merge spring-config.xml
```
- 重命名分支：
```
$ git branch -m dev_tushucuxiao cuxiao
```
- push到新分支：
```
$ git push origin cuxiao
Total 0 (delta 0), reused 0 (delta 0)
remote: Updating references: 100% (1/1)
To http://source.jd.com/app/pfs.git
 * [new branch]      cuxiao -> cuxiao
 
$ git branch -a
  0-a
* cuxiao
  dev
  dev_liuning39
  master
  remotes/origin/0-a
  remotes/origin/HEAD -> origin/master
  remotes/origin/cuxiao
  remotes/origin/dev
  remotes/origin/dev_liuning39
  remotes/origin/dev_tushucuxiao
  remotes/origin/master
  remotes/origin/order2nd

liuning11@ZB-PC0J468T MINGW64 /e/project/pfs (cuxiao)
$
```
- 删除旧分支
```
$ git push --delete origin dev_tushucuxiao
remote: Updating references: 100% (1/1)
To http://source.jd.com/app/pfs.git
 - [deleted]         dev_tushucuxiao

```