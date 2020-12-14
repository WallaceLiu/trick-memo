```
cd /opt/conda/envs/py35
zip -r py35.zip *
hadoop fs -mkdir /tmp/liuning11
hadoop fs -put py35.zip /tmp/liuning11/
hadoop fs -put -f py35.zip /tmp/liuning11/
spark-submit --master yarn --deploy-mode client --driver-memory 10g --driver-cores 5 --num-executors 5 --executor-memory 16G --executor-cores 4  --conf spark.yarn.dist.archives=hdfs://ns1/tmp/liuning11/py35.zip#py35 run.py

```