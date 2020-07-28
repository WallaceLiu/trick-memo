# 删除本地、远程分支
- 本地
```shell script
git branch -D 20191105_liuning_insurancecontent2
```
- 远程
```shell script
git push origin --delete 20191105_liuning_insurancecontent2
```
# 清除远程分支的本地缓存
```shell script
git fetch -p origin
```
# 覆盖本地分支
```shell script
git fetch --all  
git reset --hard origin/master
  git pull
```
# gitignore生效
```shell script
git rm -r --cached .
git add . 
git commit -m "fixed gitignore"
git push origin 20200101-liun
```
# 取消commit
```shell script
git reset --soft HEAD^
git reset --soft HEAD~1
git reset --soft HEAD~2
```

