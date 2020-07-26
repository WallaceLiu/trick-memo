```
usage: netstat [-veenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vnNcaeol] [<Socket> ...]
       netstat { [-veenNac] -I[<Iface>] | [-veenNac] -i | [-cnNe] -M | -s } [delay]

        -r, --route                display routing table
        -I, --interfaces=<Iface>   display interface table for <Iface>
        -i, --interfaces           display interface table
        -g, --groups               display multicast group memberships
        -s, --statistics           display networking statistics (like SNMP)
        -M, --masquerade           display masqueraded connections

        -v, --verbose              be verbose
        -n, --numeric              don't resolve names
        --numeric-hosts            don't resolve host names
        --numeric-ports            don't resolve port names
        --numeric-users            don't resolve user names
        -N, --symbolic             resolve hardware names
        -e, --extend               display other/more information
        -p, --programs             display PID/Program name for sockets
        -c, --continuous           continuous listing

        -l, --listening            display listening server sockets
        -a, --all, --listening     display all sockets (default: connected)
        -o, --timers               display timers
        -F, --fib                  display Forwarding Information Base (default)
        -C, --cache                display routing cache instead of FIB
        -T, --notrim               stop trimming long addresses
        -Z, --context              display SELinux security context for sockets

  <Iface>: Name of interface to monitor/list.
  <Socket>={-t|--tcp} {-u|--udp} {-S|--sctp} {-w|--raw} {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25)
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP)
    x25 (CCITT X.25)
```