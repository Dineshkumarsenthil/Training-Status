# STP, Redundancy & Loop Avoidance
---
## **Why Loops Occur in L2 Networks**

Layer 2 Ethernet frames do not have a TTL (Time To Live). When switches are connected in redundant topologies:

  - Broadcast and unknown unicast frames are flooded.
   - Frames can circulate indefinitely.
   - Switches continuously relearn MAC addresses.

This creates **Layer 2 loops**, causing severe network instability.

---

## **Broadcast Storms & MAC Instability**

### **Broadcast Storm**

Occurs when broadcast/multicast frames loop endlessly and multiply, consuming bandwidth.

**Effects:**

* High CPU utilization on switches
* Congestion on all links
* Network becomes unusable

### **MAC Instability (MAC Flapping)**

Happens when the same MAC address is seen on different ports repeatedly.

**Effects:**

* Incorrect forwarding decisions
* Frame loss
* Instability in switching tables

---

## **Spanning Tree Protocol (STP)**

STP prevents L2 loops by placing redundant links in a **blocking** state.

Key functions:

* Elects a **Root Bridge**
* Calculates optimal path using **path cost**
* Moves ports through **Blocking → Listening → Learning → Forwarding** states
* Provides automatic failover if a link fails

---

## **STP Variants**

### **PVST (Per VLAN Spanning Tree)** – Cisco

* One STP instance per VLAN
* Fine-grained control but uses more resources

### **PVST+**

* Enhanced Cisco version compatible with 802.1D STP

### **RSTP (Rapid Spanning Tree Protocol – IEEE 802.1w)**

* Faster convergence (1–3 seconds)
* Modern port roles and states

### **Rapid-PVST**

* Cisco RSTP implementation per VLAN
* Fast + per-VLAN topology

### **MSTP (Multiple Spanning Tree Protocol – 802.1s)**

* Maps multiple VLANs to a single STP instance
* Highly scalable for enterprise networks

---

## **Network Redundancy Design**

Redundancy ensures uninterrupted service during failures.

Common L2 redundancy methods:

### ** Dual-Homed Access Switches**

Two uplinks from access to distribution switches.

### **Triangular / Meshed L2 Topologies**

Uses STP to block loops.

### **EtherChannel / Port-Channel**

Combines multiple physical links:

* No STP blocking on bundled links
* Increased bandwidth and redundancy

### **First-Hop Redundancy (Layer 3)**

Uses HSRP/VRRP/GLBP (beyond L2 but relevant for design).

---

## **Bridge ID**

STP elects the Root Bridge using the **Bridge ID**.

**Bridge ID = Bridge Priority + MAC Address**

* Default priority: **32768**
* Lower value wins
* Used to determine the root bridge for the topology

Example:

```
SW1 Priority 32768, MAC aaaa.aaaa.aaaa
SW2 Priority 32768, MAC bbbb.bbbb.bbbb
→ SW1 becomes Root Bridge (lower MAC)
```

---


