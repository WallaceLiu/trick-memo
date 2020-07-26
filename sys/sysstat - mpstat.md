mpstat提供多处理器系统CPU利用率的统计.

mpstat 也可以加参数，用-P来指定哪个 CPU，处理器的ID是从0开始的。

- ##查看第一个CPU，每二秒数据更新一次，总共要显示10次数据
```
# mpstat -P 0 2 10
```
- 查看第二个CPU
```
# mpstat -p 1 2 10
```
- 查看所有CPU
```
# mpstat 2 10
```