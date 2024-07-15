# NAT Configration #
```

en
conf t
hostname R-1

int g0/0
ip add dhcp
no sh

int g0/1 
ip add 192.168.1.2 255.255.255.0
no shutdown

router ospf 1
int g0/1
ip ospf 1 area 0

access-list 1 permit any
ip nat inside source list 1 int g1/0

int g0/0
ip nat outside
int g0/1
ip nat inside
 
ip domain-lookup
ip name 8.8.8.8 
--------------
R-1	

en
conf t
hostname R-2

int g0/0
ip add 192.168.1.3 255.255.255.0
no sh 

int g0/1
ip add 10.10.10.1 255.255.255.0
no sh
ip route 0.0.0.0 0.0.0.0 192.168.1.2
router ospf 1
int g0/1
ip ospf 1 area 0  
int g0/0 
ip ospf 1 area 0

ip domain-lookup
ip name 8.8.8.8 
--------------
```
 
