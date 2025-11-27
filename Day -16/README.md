# Network Fundamentals
---

## IP Addressing Basics
- **Public IP:** Used on the internet; visible to everyone.
- **Private IP:** Used inside home/office networks.
- **Static IP:** IP stays fixed.
- **Dynamic IP (DHCP):** IP changes automatically.
- **IPv4:** Older format (example: 192.168.1.1).
- **IPv6:** Newer format with more addresses (example: 2001:db8::1).
- **IP Structure:** 
  - Network part = identifies the network  
  - Host part = identifies the device inside that network

---

## MAC Address
- Unique **48-bit** hardware address.
- Used for communication **inside a LAN**.
- Helps switches forward frames using MAC table.

---

## Types of Networks
- **LAN:** Small area (home, office).
- **MAN:** City-level network.
- **WAN:** Very large area (countries, internet).

---

## Networking Devices
- **Hub:** Sends data to all devices (not intelligent).
- **Switch:** Forwards data only to the correct device using MAC.
- **Router:** Connects different networks using IP.
- **Firewall:** Protects network by filtering traffic.

---

## How Data Moves
- LAN communication uses **MAC addresses**.
- Different networks communicate using **IP addresses**.
- **ARP:** Finds MAC address using IP.
- `arp -a` shows IP → MAC table.

---

## Routing Concepts
- **Routing Table:** Shows where the router should send packets.
- **Default Gateway:** Router used when no other path is known.
- **Next Hop:** The next router in the path.
- **Best Path:** Router chooses the most efficient route.

---

## Internet Administration
- **IANA:** Distributes IP address blocks.
- **ICANN:** Manages domain names + internet structure.
- **RIRs:** Regional groups that assign IPs (APNIC, ARIN, etc.).
- **RFCs:** Documents that define networking standards.

---

