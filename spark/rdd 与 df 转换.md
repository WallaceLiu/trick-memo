# df 到 rdd
```python
rdd = df.rdd.map(lambda x: map(lambda a: a))
```
转换后默认是Row类型，需要用python map 函数进行转换
# rdd 到 df
方式1：
```python
df = rdd.map(lambda x: Row(id=x[0], name=x[1])).toDF()
```
方式2：
```python
fields = [StructField(x, StringType(), True) for x in "id, name".split()]
df = hiveContext.createDataFrame(rdd, structType(fields))
```
方式1方便，如果rdd为空，则只能用方式2转换成df，用方式1将报错！