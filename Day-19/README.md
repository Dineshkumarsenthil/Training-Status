# Routing Fundamentals
---
### Routing:
 -  Routing is how data packets move from your device (source) to another device (destination) across intermediate devices (routers).
### Router:
 - device that examines the destination address of a packet and decides which next network (next hop) it should be sent to.
### Route: 
 - A path that data takes through one or more routers to reach its destination.
### Routing Table:
 - For this destination or network → send via this interface/next hop.
---
### Types:

##### Static Routing
 - Routes are manually configured by a network administrator.
 - Does not change automatically if the network changes.
 - Used in small or simple networks.
```
ip route 192.168.2.0 255.255.255.0 192.168.1.2
```
##### Dynamic Routing
 - Routers automatically learn and update routes using routing protocols.
 - Adapts to network changes link failures, new networks.
 - Common routing protocols(RIP, OSPF, EIGRP, BGP).
---
##### Default Route (Gateway of Last Resort)
 - If a router doesn’t know a specific route, it uses a default route like a catch-all path.
##### Metric
 - A value used to choose the best path when multiple routes exist (hop count, bandwidth, delay).
---
