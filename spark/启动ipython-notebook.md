# pyspark启动ipython notebook


先安装ipython，再配置spark-env.sh 添加如下行：

```
export PYSPARK_PYTHON=/Users/liuning11/anaconda3/envs/lr/bin/python3
export PYSPARK_DRIVER_PYTHON=/Users/liuning11/anaconda3/envs/lr/bin/ipython3
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
```

- IPYTHON, 启用ipython
- PYSPARK_PYTHON, pyspark对应的python版本
- PYSPARK_DRIVER_PYTHON, pyspark启动时使用ipython

之后，为了方便定位目录，还需要设置notebook工作目录。

# 设置notebook 工作路径
```
jupyter notebook --generate-config
```

在用户路径下生成一个py文件：

```
Writing default config to: /Users/cap/.jupyter/jupyter_notebook_config.py
```

修改：

```
c.NotebookApp.notebook_dir = '指定的工作路径'
```
