# Network Troubleshooting
---

## Troubleshooting Basics

### Layer-by-layer checks
1. **Physical** – Cable plugged in? Link light on?
2. **Data Link** – Correct VLAN?
3. **Network** – Correct IP, mask, gateway, routes?
4. **Transport** – Ports open (TCP/UDP)?
5. **Application** – Service running (HTTP, DNS, etc.)?

### Useful commands
- **ping** – Check basic reachability.
- **traceroute** – See path/hops to a destination.
- **arp** – Show IP ↔ MAC mapping.
- **show ip interface brief** – Check interface status & IP.
- **show ip route** – Check routing table.

### Common problems
- Wrong **VLAN**
- Wrong **default gateway**
- **Missing routes**
- **Ports blocked** by ACL/firewall

---

## ACL (Access Control List) Basics

- ACLs **permit or deny** traffic.

### Standard vs Extended ACLs
- **Standard ACL** – Filter by **source IP only**.
- **Extended ACL** – Filter by **source IP, destination IP, protocol, port**.

### Logic
- Rules are read **top to bottom**.
- First match wins.
- There is always an **implicit **deny all**** at the end.

### Inbound vs Outbound
- **Inbound** – Filter traffic **coming into** an interface.
- **Outbound** – Filter traffic **going out of** an interface.

### Segmentation with ACLs
- Use ACLs to:
  - Allow users to reach only needed servers/ports.
  - Block user access to management networks.
  - Separate VLANs / subnets logically.

---

## Firewall Fundamentals

### Stateless vs Stateful
- **Stateless** – Looks at each packet alone (like simple ACL).
- **Stateful** – Remembers connections (TCP handshake) and allows return traffic.

### Rule components
- **Source IP**
- **Destination IP**
- **Protocol** (TCP, UDP, ICMP)
- **Port** (e.g., 80, 443, 22)
- **Action**: permit or deny

### Allow list vs Deny list
- **Allow list (best practice)**:
  - Default: **deny everything**.
  - Then **allow only required** traffic.
- **Deny list**:
  - Default: allow.
  - Block only known-bad.

### Basic security tips
- **Drop-all-by-default**
- **Permit only needed services**
- **Enable logging and monitoring**

---

## Traffic Analysis (Wireshark)

What to recognize:

- **ARP** – “Who has this IP? Tell me your MAC.”
- **ICMP** – Used by **ping**, error messages.
- **TCP handshake** – **SYN** → **SYN-ACK** → **ACK**.
- **Broadcast** – To all devices in LAN.
- **Multicast** – To a group of interested receivers.

---
