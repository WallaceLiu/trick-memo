# install postgresql
安装最新版本
```shell script
~ brew install postgresql
......
If you need to have krb5 first in your PATH run:
  echo 'export PATH="/usr/local/opt/krb5/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/usr/local/opt/krb5/sbin:$PATH"' >> ~/.zshrc

For compilers to find krb5 you may need to set:
  export LDFLAGS="-L/usr/local/opt/krb5/lib"
  export CPPFLAGS="-I/usr/local/opt/krb5/include"

For pkg-config to find krb5 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/krb5/lib/pkgconfig"

==> postgresql
To migrate existing data from a previous major version of PostgreSQL run:
  brew postgresql-upgrade-database

This formula has created a default database cluster with:
  initdb --locale=C -E UTF-8 /usr/local/var/postgres
For more details, read:
  https://www.postgresql.org/docs/13/app-initdb.html

To have launchd start postgresql now and restart at login:
  brew services start postgresql
Or, if you don't want/need a background service you can just run:
  pg_ctl -D /usr/local/var/postgres start
```
- 查看版本
```shell script
~ postgres -V
postgres (PostgreSQL) 13.1
~
```
- 启动
```shell script
brew services start postgresql
```
- 访问
```shell script
~ psql postgres
psql (13.1)
Type "help" for help.

postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 shanshu   | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

postgres=#
```
- 退出
```shell script
postgres=# \q # quits
```
