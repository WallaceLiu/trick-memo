aaa
```
awk '{print $6}' obdServer.log  | awk -F '.' '{print $1}' | sort | uniq -c >groupby.txt
```
aaa
```
tac obdServer.log | awk '{ print $4 }'| awk -F ":" '{print $1}' | grep -v "192.168.*" | sort n
```