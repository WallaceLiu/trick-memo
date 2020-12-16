# 访问本地 MySQL
```
# mysql -u root -p
Enter password:
```
# 访问远程 MySQL
授权法。例如，你想myuser使用mypassword从任何主机连接到mysql服务器的话。
```sql
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
Query OK, 0 rows affected (0.04 sec)

mysql>
```
```
# mysql -h 192.168.1.10 -u root -p
Enter password:
```



