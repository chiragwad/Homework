# static routing

```R1

enable
configure terminal
interface fastethernet 0/0
ip address 192.168.12.1 255.255.255.0 # Assigns an IP address and subnet mask to that interface
no shutdown # enables the interface

exit
exit
show ip route # Displays the routing table of the router

# check connection
ping 192.168.12.2

# setup static route
ip route 192.168.2.0 255.255.255.0 192.168.1.2
end

```

```R2

enable
configure terminal
interface fastethernet 0/0
ip address 192.168.12.2 255.255.255.0
no shutdown

ip route 192.168.3.0 255.255.255.0 192.168.1.1
end

```

# DHCP


```R1

# configure router interface
enable
configure terminal
interface fastEthernet0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit

# configure dhcp server
configure terminal
ip dhcp pool LAN_POOL
network 192.168.10.0 255.255.255.0 # defines address-range for the pool
default-router 192.168.10.1
dns-server 8.8.8.8
exit

# check dhcp bindings
show ip dhcp bindings # displays all currently leased IP addresses
```

```PC1
# configure pcs to use dhcp
ip dhcp # request an ip address from dhcp server automatically
show ip

# check connection with router
ping 192.168.10.1

# check connection with pc
ping 192.168.10.5

```

# RIP


```R1
# configure router interfacs
configure terminal
interface f0/0
ip add 192.168.1.1 255.255.255.0
no sh
exit
interface f1/0
ip add 10.0.12.1 255.255.255.0
no sh
exit
# setup ripv2
router rip
version 2
no auto-summary
network 192.168.1.0
network 10.0.12.0
exit
exit
```

```R2
configure terminal
interface f0/0
ip add 10.0.12.2 255.255.255.0
no sh
exit
interface f1/0
ip add 10.0.23.1 255.255.255.0
no sh
exit
router rip
version 2
no auto-summary
network 10.0.12.0
network 10.0.23.0
exit
exit

```


```R3
configure terminal
interface f0/0
ip add 10.0.23.2 255.255.255.0
no sh
exit
interface f1/0
ip add 192.168.2.1 255.255.255.0
no sh
exit
router rip
version 2
no auto-summary
network 10.0.23.0
network 192.168.2.0
exit
exit
```

```PC1
ip 192.168.1.5 255.255.255.0 192.168.1.1

#check connection
ping 192.168.2.5
```


```PC2
ip 192.168.2.5 255.255.255.0 192.168.2.1

#check connection
ping 192.168.1.5
```