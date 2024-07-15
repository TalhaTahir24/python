# DHCP Pools
```
conf t
ip dhcp pool b2
network 192.168.2.0 255.255.255.0
default-router 192.168.2.1
dns-server 192.168.2.1
exit
int vlan 2
ip add 192.168.2.1 255.255.255.0
no shutdown

conf t
ip dhcp pool b3
network 192.168.3.0 255.255.255.0
default-router 192.168.3.1
dns-server 192.168.3.1
exit
int vlan 3
ip add 192.168.3.1 255.255.255.0
no shutdown

conf t
int f0/4
sw mo tr

conf t
int f0/1
sw mo tr

conf t
int f0/3
sw ac vl 2
exit
conf t
int f0/4
sw ac vlan 3

conf t
int f0/5
sw mo tr

conf t
int fa0/1
sw mo tr
exit
int f0/4
sw ac vl 2
exit
int f0/3
sw ac vl 3
```
