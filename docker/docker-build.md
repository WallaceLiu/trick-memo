# add
```
docker build -t idockerhub.jd.com/socrates_model/train:tf2.0 -f Dockerfile-base .     
```
# 交互模式启动一个容器,在容器内执行/bin/bash命令
```shell script
docker run -it idockerhub.jd.com/socrates_model/webapp:v0.4 /bin/bash 
```
```shell script
docker run -it idockerhub.jd.com/socrates_model/train:tf2.0 /bin/bash
```


