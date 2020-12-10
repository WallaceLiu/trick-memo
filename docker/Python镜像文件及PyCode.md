Python镜像文件及PyCode

# 结构
```text
.
├── docker-build.md
├── docker.md
├── dockerfile
├── dockerfile-bak
├── py
│   ├── __init__.py
│   ├── calander.py
│   ├── hello.py
│   ├── mysql.py
│   └── opencv.py
├── requirements.txt
```
## Dockerfile
```text
FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
COPY ./hello.py /usr/src/app/
VOLUME /usr/src/app
ENTRYPOINT ["python"]
```
## requirements.txt
```text
PyMySQL
opencv-python
```
## py files
- Hello.py
- Calander.py
- Mysql.py
- Opencv.py

# 部署运行
## Hello world
```shell script
sudo docker run --rm -v /Users/liuning11/project/docker-py/py:/usr/src/app dockerpy hello.py
sudo docker run -v /Users/liuning11/project/docker-py/py:/usr/src/ app -w /usr/src/app python python hello.py
 
```
## Calander
```shell script
sudo docker run -it --rm -v /home/ubuntu/docker-py/py:/usr/src/app dockerpy calander.py
```
> 注意：由于用到了input，需要输入内容，因此运行容器的时候需要用到-it参数，
> 否则会报EOFError: EOF when reaeding a line的错误。

## MySql
注意：运行mysql.py前要先运行数据库容器。然后通过 --link=容器名:容器别名 
命令可以实现容器间的互访，否则由于容器间的隔离性，py容器会找不到数据库容器,即出现下图错误
```shell script
sudo docker run -it --rm -v /home/ubuntu/docker-py/py:/usr/src/app --link=laughing_satoshi:laughing_satoshi dockerpy mysql.py
```

## OpenCv
```shell script
sudo docker run -it --rm -v /home/ubuntu/docker-py/py:/usr/src/app dockerpy opencv.py
```

# 实验心得
这次实验花费时间在3个小时左右，相对前俩次实验可以说是简单多了，属于比较入门的内容，感觉跟直接在linux下运行py代码差别不大。
