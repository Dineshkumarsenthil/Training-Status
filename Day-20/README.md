# Dynamic Routing: RIP & Basic OSPF
---
## Why Dynamic Routing Is Needed

Dynamic routing allows routers to:

* Automatically learn routes instead of manual static routes.
* Adjust routes when network topology changes.
* Scale easily in medium and large networks.
* Recover quickly after link failures.
* Reduce admin workload and human error.

Static routing works only for small, simple networks; dynamic routing is essential when multiple paths and frequent changes exist.

---

## RIP (Routing Information Protocol)

### • Distance Vector Protocol

RIP advertises routes based on what the neighbor router tells it—“routing by rumor.”

### • Hop Count Metric

* Best path = lowest hop count.
* Max hops = **15**; 16 = unreachable.
* Not suitable for large networks.

### • Routing Updates

* Sends the **entire routing table every 30 seconds**.
* RIP v1: broadcast
* RIP v2: multicast (224.0.0.9)

### • Split Horizon

Prevents loops by **not advertising a route back out of the same interface from which it was learned**.

### • Route Poisoning

When a route becomes invalid, it is advertised with **hop 16** (infinite metric) to tell neighbors it is unreachable.

---

## OSPF (Open Shortest Path First)

### • Link-State Protocol

OSPF maintains a full map of the network and uses the **SPF (Shortest Path First) algorithm**.

### • Router IDs

* Unique 32-bit identifier for each router.
* Highest loopback IP is chosen automatically.
* Can be manually set for consistency.

### • Areas

* OSPF is divided into areas for scalability.
* **Area 0 = Backbone area (mandatory).**
* Multi-area design reduces CPU load and SPF calculations.

### • Adjacency Formation

Routers become neighbors by exchanging:

1. Hello packets
2. Database Description (DBD)
3. Link State Request (LSR)
4. Link State Update (LSU)
5. Link State Acknowledgment (LSAck)

All parameters (hello timers, area ID, mask) must match.

### • LSAs & SPF Algorithm Basics

* **LSAs**: Advertise router links and topology information.
* **SPF Algorithm (Dijkstra)**: Calculates best paths using **cost**.

  * Cost = 100,000,000 ÷ bandwidth

### • Convergence & Failure Recovery

* **OSPF**: Fast; sends LSAs immediately after changes.
* **RIP**: Slow; waits for periodic updates and timers.
* OSPF recalculates SPF and updates routes quickly when a link fails.

---

