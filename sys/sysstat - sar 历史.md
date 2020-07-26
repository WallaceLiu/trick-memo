# 查看指定文件CPU使用记录
```
# sar -f /var/log/sa/sa03
```
# 查看指定文件1/5/15分钟平均负载记录
```
# sar -q -f /var/log/sa/sa03
```
# 查看指定文件7点到9点CPU使用记录，如要看负载加参数-q
```
# sar -s 07:00:00 -e 10:00:00 -f /var/log/sa/sa03
```
#  内存分页监控
```
# sar -r -f /var/log/sa29 
```