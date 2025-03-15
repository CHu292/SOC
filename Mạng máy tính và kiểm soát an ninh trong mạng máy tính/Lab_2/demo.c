IOU1:

Tạo VLAN:
configure terminal
vlan 110
name Printer
vlan 120
name Computers
vlan 130
name Phones
exit

Gán cổng trunk:
interface Ethernet0/0
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface Ethernet0/1
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface Ethernet0/2
switchport trunk encapsulation dot1q
switchport mode trunk
exit

exit
write memory
-------------------------------------------------------
IOU2:

Tạo VLAN:
configure terminal
vlan 110
name Printer
vlan 120
name Computers
exit

Gán cổng trunk:
interface Ethernet0/0
switchport trunk encapsulation dot1q
switchport mode trunk
exit

Gán cổng Acccess:
interface Ethernet0/1
switchport mode access
switchport access vlan 110
exit

interface Ethernet0/2
switchport mode access
switchport access vlan 120
exit

exit
write memory
-------------------------------------------------------
IOU3:

Tạo VLAN:
configure terminal
vlan 120
name Computers
vlan 130
name Phones
exit

Gán cổng trunk:
interface Ethernet0/0
switchport trunk encapsulation dot1q
switchport mode trunk
exit

Gán cổng Access:
interface Ethernet0/1
switchport mode access
switchport access vlan 120
exit

interface range Ethernet0/2-3
switchport mode access
switchport access vlan 130
exit

exit
write memory
-------------------------------------------------------

R1:

Tạo sub_interface:
interface Ethernet0/0
no shutdown
exit

interface Ethernet0/0.110
encapsulation dot1Q 110
ip address 192.168.110.254 255.255.255.0
exit

interface Ethernet0/0.120
encapsulation dot1Q 120
ip address 192.168.120.254 255.255.255.0
exit

interface Ethernet0/0.130
encapsulation dot1Q 130
ip address 192.168.130.254 255.255.255.0
exit







exit
write memory
-------------------------------------------------------

DHCP Server:

ip dhcp excluded-address 192.168.110.1 192.168.110.10
ip dhcp pool Printer
 network 192.168.110.0 255.255.255.0
 default-router 192.168.110.254
 dns-server 8.8.8.8
 lease 7
exit

ip dhcp excluded-address 192.168.120.1 192.168.120.10
ip dhcp pool Computers
network 192.168.120.0 255.255.255.0
default-router 192.168.120.254
dns-server 8.8.8.8
lease 7
exit

ip dhcp excluded-address 192.168.130.1 192.168.130.10
ip dhcp pool Phones
network 192.168.130.0 255.255.255.0
default-router 192.168.130.254
dns-server 8.8.8.8
lease 7
exit

exit
write memory

Test:
PC1> ping 192.168.120.254
PC2> ping 192.168.130.254
-------------------------------------------------------

Port's security:

IOU2:
interface Ethernet0/1
switchport mode access
switchport access vlan 110
switchport port-security
switchport port-security maximum 1
switchport port-security violation restrict
switchport port-security mac-address sticky
no shutdown
exit

exit
write memory

IOU3: 
Cấu hình trên cổng Ethernet0/1 (Kết nối PC3 - VLAN 120):
interface Ethernet0/1
switchport mode access
switchport access vlan 120
switchport port-security
switchport port-security maximum 1
switchport port-security violation restrict
switchport port-security mac-address sticky
no shutdown
exit

Cấu hình trên cổng Ethernet0/2 và Ethernet0/3 (Kết nối PC4, PC5 - VLAN 130)
interface range Ethernet0/2-3
switchport mode access
switchport access vlan 130
switchport port-security
switchport port-security maximum 1
switchport port-security violation restrict
switchport port-security mac-address sticky
no shutdown
exit

-------------------------------------------------------

Dhcp snooping:


IOU1:
ip dhcp snooping
ip dhcp snooping vlan 110,120,130

interface Ethernet0/0
ip dhcp snooping trust
exit
interface Ethernet0/2
ip dhcp snooping trust
exit

IOU2:
ip dhcp snooping
ip dhcp snooping vlan 110,120,130
exit

IOU3:
ip dhcp snooping
ip dhcp snooping vlan 110,120,130

interface Ethernet0/0
ip dhcp snooping trust
exit

exit
write memory

-----------------------------
IOU1:
conf t
! Bật DHCP Snooping trên switch
ip dhcp snooping
! Chỉ bật DHCP Snooping trên VLAN 110, 120, 130
ip dhcp snooping vlan 110,120,130
! Đặt cổng e0/0 là cổng tin cậy để nhận DHCP Offer và DHCP ACK từ R1
interface Ethernet0/0
 ip dhcp snooping trust
exit
! Đặt cổng e0/1, e0/2 là cổng tin cậy để chuyển tiếp DHCP giữa các switch
interface Ethernet0/1
 ip dhcp snooping trust
exit
interface Ethernet0/2
 ip dhcp snooping trust
exit
exit
! Lưu cấu hình
wr

IOU2:
conf t
ip dhcp snooping
ip dhcp snooping vlan 110,120,130
! Đặt cổng e0/0 là cổng tin cậy để chuyển tiếp DHCP với IOU1
interface Ethernet0/0
 ip dhcp snooping trust
exit
! Các cổng kết nối với PC1, PC2 phải là không tin cậy (Untrusted)
interface Ethernet0/1
 no ip dhcp snooping trust
exit
interface Ethernet0/2
 no ip dhcp snooping trust
exit
exit
wr

conf t
! Bật DHCP Snooping trên switch
ip dhcp snooping
! Chỉ bật DHCP Snooping trên VLAN 110, 120, 130
ip dhcp snooping vlan 110,120,130
! Thiết lập tất cả các cổng trên IOU3 là cổng tin cậy
interface Ethernet0/0
 ip dhcp snooping trust
exit
interface Ethernet0/1
 ip dhcp snooping trust
exit
interface Ethernet0/2
 ip dhcp snooping trust
exit
interface Ethernet0/3
 ip dhcp snooping trust
exit
interface Ethernet1/0
 ip dhcp snooping trust
exit
exit
wr
