# Virtualization Networking
---

- IOMMU
- PCI passthrough
- SR-IOV (PF/VF, direct mapping)
- Why SR-IOV is fast
- DPDK and its use cases

---

## IOMMU:

**IOMMU = Input Output Memory Management Unit**

- Sits between **devices (like NICs)** and **RAM**.
- Think of it as an MMU, but for I/O devices.

### Works

- **Address translation**  
  Translates device DMA addresses → real physical memory addresses.
- **Isolation and protection**  
  Ensures one device/VM cannot read or corrupt another device/VM’s memory.
- **Enables safe passthrough**  
  Allows assigning a device directly to a VM (PCI passthrough) **safely**.

---

## PCI Passthrough:

**PCI passthrough** = give a **physical PCI device** (e.g., NIC) directly to a **VM**.

- The VM sees the device as if it were **physically attached** to it.
- No full software emulation of the NIC – it’s **direct access**.

### Benefits

- **Very low overhead**  
  Hypervisor is mostly out of the data path.
- **Higher performance and lower latency**  
  Often better than virtio or fully virtual NICs.
- **Better for high packet rates**  
  Especially useful for NFV and packet-processing workloads.

> **IOMMU is required** to ensure that device DMA operations from the VM are **safe, isolated, and controlled**.

---

## SR-IOV Basics

**SR-IOV = Single Root I/O Virtualization**

- Allows **one physical NIC** to appear as **many virtual NICs**.
- Used heavily in cloud/virtualized environments for performance.

### Physical Function (PF)

- The **real PCI function** of the NIC.
- Has **full control** over device configuration and resources.
- Typically managed by the **host OS** or a special management domain.
- From the PF, you **create and configure** Virtual Functions (VFs).

### Virtual Function (VF)

- A **lightweight, virtual PCI function** exposed by the NIC.
- Appears to the OS/VM as a **separate NIC**.
- Has **limited and controlled** access to NIC resources.
- You can assign **each VF** to a different VM using **PCI passthrough**.

### Direct Hardware Mapping into VMs

- Each **VF** is **directly mapped** into a VM.
- The VM’s NIC driver talks **straight to the NIC hardware** via the VF.
- **No heavy software emulation** in the hypervisor.
- **IOMMU** ensures DMA from that VF can only access the VM’s allowed memory.

---

## Why SR-IOV Accelerates Packet Processing

SR-IOV optimizes the data path:

- Packets go **device ↔ VM** with **minimal hypervisor involvement**.
- Reduces:
  - **Context switches**
  - **Data copies**
  - **Scheduling overhead**

### Performance Benefits

- **Lower latency** (fewer layers in the path).
- **Higher throughput** (more packets per second).
- **Near-native performance** (close to running on bare metal).

**high-performance networking workloads** such as:

- VNFs (Virtual Network Functions)
- NFV (Network Function Virtualization)
- High-speed routers, firewalls, load balancers inside VMs

---

## DPDK (Data Plane Development Kit)

**DPDK** is a set of **libraries and drivers** for **fast packet processing in user space**.

### Key Ideas

1. **High-speed packet processing**
   - Uses **polling** instead of interrupts (busy-wait loops).
   - Uses **huge pages** and efficient memory pools.
   - Talks directly to **NIC hardware queues**.

2. **Bypassing the kernel networking stack**
   - **Normal path:**  
     **NIC → kernel network stack → sockets → app**  
     (good for general use, but slow for very high packet rates)
   - **DPDK path:**  
     **NIC → DPDK user-space app**  
     (kernel network stack mostly bypassed)
   - Result: **much higher pps** (packets per second) and **lower latency**.

### Common Use Cases

DPDK is used when you need to handle **millions of packets per second**:

- **Firewall VNFs**
- **Virtual routers**
- **Load balancers**
- **Packet inspection workloads**:
  - DPI (Deep Packet Inspection)
  - IDS/IPS (Intrusion Detection/Prevention Systems)
- Any **high-performance data plane** application.

---

## Putting It All Together

Here’s how these pieces fit in a typical high-performance virtualized setup:

- **IOMMU**  
  - Provides safe, isolated memory access for devices.
  - Enables secure PCI passthrough to VMs.

- **PCI passthrough**  
  - Assigns a **real NIC** (or an SR-IOV **VF**) directly to a VM.
  - The VM can use that device with **near-direct hardware access**.

- **SR-IOV**  
  - Splits **one physical NIC** into **multiple VFs**.
  - Each VF can be **passed through to a different VM**, providing:
    - **Low latency**
    - **High throughput**
    - **Near-native performance**

- **DPDK**  
  - Runs inside those VMs (or on the host) to:
    - **Bypass the kernel network stack**
    - Process packets **extremely fast** in user space.
---

