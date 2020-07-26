```
#关闭Selinux#####################################################
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
setenforce 0

#关闭防火墙######################################################
/etc/init.d/iptables stop
chkconfig iptables off

#调整字符集utf-8#################################################
echo 'LANG="zh_CN.UTF-8"' >/etc/sysconfig/i18n
/bin/sh /etc/sysconfig/i18n

#时间同步########################################################
yum -y install ntpdate
/usr/sbin/ntpdate time.nist.gov

#添加crontab#####################################################
/bin/echo '*/5 * * * * /usr/sbin/ntpdate time.nist.gov' >/dev/null 2>&1 >>/var/spool/cron/root

#调整linxu文件描述符数量##########################################
echo '*    -    nofile    65535 ' >>/etc/security/limits.conf

#优化内核参数#####################################################
echo 'net.ipv4.tcp_fin_timeout = 2' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_tw_reuse = 1' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_tw_recycle = 1' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_syncookies = 1' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_keepalive_time = 600' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_max_syn_backlog = 16384' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_max_tw_buckets = 36000' >>/etc/sysctl.conf
echo 'net.ipv4.route.gc_timeout = 100' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_syn_retries = 1' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_synack_retries = 1' >>/etc/sysctl.conf
echo 'net.core.somaxconn = 16384' >>/etc/sysctl.conf
echo 'net.core.netdev_max_backlog = 16384' >>/etc/sysctl.conf
echo 'net.ipv4.tcp_max_orphans = 16384' >>/etc/sysctl.conf
/sbin/sysctl -p

#清除postfix垃圾文件###############################################
/bin/echo '* * * */2 * /bin/find /var/spool/postfix/maildrop/ -type f|xargs rm -f' >/dev/null 2>&1 >>/var/spool/cron/root

#升级已知软件漏洞到最新版本########################################
yum install openssl openssh bash vim wget -y
```