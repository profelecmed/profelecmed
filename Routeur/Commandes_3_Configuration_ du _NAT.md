# Configuration du NAT

    ip access-list standard NAT_ACL

    permit 192.168.100.0 0.0.0.255

    ip nat inside source list NAT_ACL interface GigabitEthernet0/0/0 overload

    ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0/0
