This tutorial assumes you are starting fresh and have no existing Kafka or ZooKeeper data. Since Kafka console scripts are different for Unix-based and Windows platforms, on Windows platforms use bin\windows\instead of bin/, and change the script extension to .bat.
# 第一步：下载安装
Download the 0.10.1.0 release and un-tar it.
```
> tar -xzf kafka_2.11-0.10.1.0.tgz
> cd kafka_2.11-0.10.1.0
```
# 第二步：启动服务
Kafka使用ZooKeeper（以下简称 ZK），如果没有，你需要先启动ZooKeeper服务。你可以使用kafka包里自带的脚本，启动一个单节点的 ZK 实例。
```
> bin/zookeeper-server-start.sh config/zookeeper.properties
[2013-04-22 15:01:37,495] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
...
```
现在启动Kafka服务：
```
> bin/kafka-server-start.sh config/server.properties
[2013-04-22 15:01:47,028] INFO Verifying properties (kafka.utils.VerifiableProperties)
[2013-04-22 15:01:47,051] INFO Property socket.send.buffer.bytes is overridden to 1048576 (kafka.utils.VerifiableProperties)
...
```
# 第三步：创建一个topic
创建一个名为“test”的topic，只有一个分区和一个副本：
```
> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
Created topic "test".
用下面命令列出topic，可以通过ZK查询kafka上的topic：
> bin/kafka-topics.sh --list --zookeeper localhost:2181
test
```
另外，不用手动创建topic，也可以配置broker，当topic不存在时，自动创建。
# 第四步：发送消息
Kafka有命令行客户端，在终端从文件或是命令输入，并发送到Kakfa集群。 默认，每行将被发送并作为一个单独的消息。
启动生产者（producer），在终端输入一些信息，发送给服务器。
```
> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
This is a message
This is another message
```
# 第五步：开始一个消费者
Kafka也有命令行消费者，把信息输出到终端命令行。
```
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
This is a message
This is another message
If you have each of the above commands running in a different terminal then you should now be able to type messages into the producer terminal and see them appear in the consumer terminal.
All of the command line tools have additional options; running the command with no arguments will display usage information documenting them in more detail.
```
# 第六步：创建一个多broker的集群
目前为止，我们只启动单个broker。对Kafka来说，a single broker is just a cluster of size one, so nothing much changes other than starting a few more broker instances. But just to get feel for it, 现在扩展集群到三个节点（仍然在本地机器上）。
此时，你不用停止上面启动的Kafka。
首先，为每个broker创建一个配置文件：
```
> cp config/server.properties config/server-1.properties
> cp config/server.properties config/server-2.properties
```
现在，编辑这些文件，设置如下属性：
```
config/server-1.properties:
    broker.id=1
    listeners=PLAINTEXT://:9093
    log.dir=/tmp/kafka-logs-1

config/server-2.properties:
    broker.id=2
    listeners=PLAINTEXT://:9094
    log.dir=/tmp/kafka-logs-2
```
The broker.id property is the unique and permanent name of each node in the cluster. We have to override the port and log directory only because we are running these all on the same machine and we want to keep the brokers from all trying to register on the same port or overwrite each other's data.
We already have Zookeeper and our single node started, so we just need to start the two new nodes:
```
> bin/kafka-server-start.sh config/server-1.properties &
...
> bin/kafka-server-start.sh config/server-2.properties &
...
```
现在创建一个新的topic，有三个副本：
```
> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 1 --topic my-replicated-topic
```
Okay but now that we have a cluster how can we know which broker is doing what? To see that run the "describe topics" command:
```
> bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic
Topic:my-replicated-topic	PartitionCount:1	ReplicationFactor:3	Configs:
	Topic: my-replicated-topic	Partition: 0	Leader: 1	Replicas: 1,2,0	Isr: 1,2,0
```
含义如下。The first line gives a summary of all the partitions, each additional line gives information about one partition. Since we have only one partition for this topic there is only one line.
- "leader" is the node responsible for all reads and writes for the given partition. Each node will be the leader for a randomly selected portion of the partitions.
- "replicas" is the list of nodes that replicate the log for this partition regardless of whether they are the leader or even if they are currently alive.
- "isr" is the set of "in-sync" replicas. This is the subset of the replicas list that is currently alive and caught-up to the leader.
注意：在我的例子中，node 1 是leader，负责topic的分区。
我们可以运行同样的命令，查看刚开始创建的“test”topic，会看到如下信息：
```
> bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic test
Topic:test	PartitionCount:1	ReplicationFactor:1	Configs:
	Topic: test	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```
So there is no surprise there—the original topic has no replicas and is on server 0, the only server in our cluster when we created it.
发布一些消息到新的topic：
```
> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my-replicated-topic
...
my test message 1
my test message 2
^C
```
现在，消费这些消息：
```
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic my-replicated-topic
...
my test message 1
my test message 2
^C
```
现在，让我们测试 fault-tolerance。Broker 1 扮演 leader，因此杀掉它的进程：
```
> ps aux | grep server-1.properties
7564 ttys002    0:15.91 /System/Library/Frameworks/JavaVM.framework/Versions/1.8/Home/bin/java...
> kill -9 7564
```
Leader会切换到slaves和node 1中的一个，不会出现在in-sync replica的集合中，如下所示：
```
> bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic
Topic:my-replicated-topic	PartitionCount:1	ReplicationFactor:3	Configs:
	Topic: my-replicated-topic	Partition: 0	Leader: 2	Replicas: 1,2,0	Isr: 2,0
```
但是消息对消费者来说，仍然可靠，even though the leader that took the writes originally is down:
```
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic my-replicated-topic
...
my test message 1
my test message 2
^C
```
# 第七步：使用kakfa连接导入/导出数据
Writing data from the console and writing it back to the console is a convenient place to start, but you'll probably want to use data from other sources or export data from Kafka to other systems. For many systems, instead of writing custom integration code you can use Kafka Connect to import or export data.
Kafka Connect is a tool included with Kafka that imports and exports data to Kafka. It is an extensible tool that runs connectors, which implement the custom logic for interacting with an external system. In this quickstart we'll see how to run Kafka Connect with simple connectors that import data from a file to a Kafka topic and export data from a Kafka topic to a file.
First, we'll start by creating some seed data to test with:
```
> echo -e "foo\nbar" > test.txt
```
Next, we'll start two connectors running in standalone mode, which means they run in a single, local, dedicated process. We provide three configuration files as parameters. The first is always the configuration for the Kafka Connect process, containing common configuration such as the Kafka brokers to connect to and the serialization format for data. The remaining configuration files each specify a connector to create. These files include a unique connector name, the connector class to instantiate, and any other configuration required by the connector.
```
> bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
```
These sample configuration files, included with Kafka, use the default local cluster configuration you started earlier and create two connectors: the first is a source connector that reads lines from an input file and produces each to a Kafka topic and the second is a sink connector that reads messages from a Kafka topic and produces each as a line in an output file.
During startup you'll see a number of log messages, including some indicating that the connectors are being instantiated. Once the Kafka Connect process has started, the source connector should start reading lines fromtest.txt and producing them to the topic connect-test, and the sink connector should start reading messages from the topic connect-test and write them to the file test.sink.txt. We can verify the data has been delivered through the entire pipeline by examining the contents of the output file:
```
> cat test.sink.txt
foo
bar
```
Note that the data is being stored in the Kafka topic connect-test, so we can also run a console consumer to see the data in the topic (or use custom consumer code to process it):
```
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic connect-test --from-beginning
{"schema":{"type":"string","optional":false},"payload":"foo"}
{"schema":{"type":"string","optional":false},"payload":"bar"}
...
```
The connectors continue to process data, so we can add data to the file and see it move through the pipeline:
```
> echo "Another line" >> test.txt
```
You should see the line appear in the console consumer output and in the sink file.
# 第八步：使用Kafka流处理数据
Kafka Streams is a client library of Kafka for real-time stream processing and analyzing data stored in Kafka brokers. This quickstart example will demonstrate how to run a streaming application coded in this library. Here is the gist of the WordCountDemo example code (converted to use Java 8 lambda expressions for easy reading).
```
KTable wordCounts = textLines
    // Split each text line, by whitespace, into words.
    .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))

    // Ensure the words are available as record keys for the next aggregate operation.
    .map((key, value) -> new KeyValue<>(value, value))

    // Count the occurrences of each word (record key) and store the results into a table named "Counts".
    .countByKey("Counts")
```
It implements the WordCount algorithm, which computes a word occurrence histogram from the input text. However, unlike other WordCount examples you might have seen before that operate on bounded data, the WordCount demo application behaves slightly differently because it is designed to operate on an infinite, unbounded stream of data. Similar to the bounded variant, it is a stateful algorithm that tracks and updates the counts of words. However, since it must assume potentially unbounded input data, it will periodically output its current state and results while continuing to process more data because it cannot know when it has processed "all" the input data.
We will now prepare input data to a Kafka topic, which will subsequently be processed by a Kafka Streams application.
```
> echo -e "all streams lead to kafka\nhello kafka streams\njoin kafka summit" > file-input.txt
```
Next, we send this input data to the input topic named streams-file-input using the console producer (in practice, stream data will likely be flowing continuously into Kafka where the application will be up and running):
```
> bin/kafka-topics.sh --create \
            --zookeeper localhost:2181 \
            --replication-factor 1 \
            --partitions 1 \
            --topic streams-file-input

> bin/kafka-console-producer.sh --broker-list localhost:9092 --topic streams-file-input < file-input.txt
```
运行WordCount应用程序处理输入的数据：
```
> bin/kafka-run-class.sh org.apache.kafka.streams.examples.wordcount.WordCountDemo
```
There won't be any STDOUT output except log entries as the results are continuously written back into another topic named streams-wordcount-output in Kafka. The demo will run for a few seconds and then, unlike typical stream processing applications, terminate automatically.
We can now inspect the output of the WordCount demo application by reading from its output topic:
```
> bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
            --topic streams-wordcount-output \
            --from-beginning \
            --formatter kafka.tools.DefaultMessageFormatter \
            --property print.key=true \
            --property print.value=true \
            --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
            --property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer
```
with the following output data being printed to the console:
```
all     1
lead    1
to      1
hello   1
streams 2
join    1
kafka   3
summit  1
```
Here, the first column is the Kafka message key, and the second column is the message value, both in in java.lang.String format. Note that the output is actually a continuous stream of updates, where each data record (i.e. each line in the original output above) is an updated count of a single word, aka record key such as "kafka". For multiple records with the same key, each later record is an update of the previous one.
Now you can write more input messages to the streams-file-input topic and observe additional messages added to streams-wordcount-output topic, reflecting updated word counts (e.g., using the console producer and the console consumer, as described above).
You can stop the console consumer via Ctrl-C.