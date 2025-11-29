# Switching Fundamentals
---
#### VLANs
 - A VLAN is like creating separate groups within a single network, even if all devices are plugged into the same switch.
##### Works:
###### Assign Devices to VLANs:
 - The network administrator decides which devices belong to which group (VLAN).

###### Switch Tags the Traffic:
 - The switch adds a special label (called a "tag") to the data from each group.

###### Traffic Separation:
 - Devices in one VLAN can only talk to others in the same VLAN, keeping their network traffic private.
---
###### Access Port:
 - An access port connects a device (like a computer) to the switch and carries traffic for only one VLAN.

###### Trunk Port:
 - A trunk port connects switches together and carries traffic for multiple VLANs at the same time.

##### L3 Switching:
 - L3 switching means a network switch can do routing (like a router) as well as switching.
 - It works at Layer 3 of the OSI model, which is the Network Layer.


##### L3 Switch Inter-VLAN Routing:
 - Inter-VLAN routing is the process that lets devices in different VLANs communicate with each other.
 - An L3 switch can perform this routing internally no need for an external router.
---
