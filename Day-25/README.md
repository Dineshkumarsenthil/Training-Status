# Storage Virtualization & Disk Provisioning

- Common virtual disk formats
- Thick vs thin provisioning
- Basic storage virtualization concepts
- How storage performance affects VNFs and labs

---

## Virtual Disk Formats

### VMDK

- **VMDK** = VMware virtual disk format.
- Commonly used by **vSphere, ESXi, Workstation**.
- Can be:
  - **Thin or thick**
  - Used with snapshots and clones.

### RAW

- **RAW** = Unstructured, raw disk image.
- No metadata, just a **plain byte-for-byte** disk representation.
- **Pros:**
  - Very simple.
  - Often **highest performance** (no extra processing).
- **Cons:**
  - Larger size (no compression).
  - Fewer advanced features compared to qcow2 (e.g., internal snapshots).

### QCOW2

- **QCOW2** = QEMU Copy-On-Write v2, common in **KVM/QEMU**.
- Features:
  - **Compression**
  - **Sparse allocation** (grows as data is written)
  - **Internal snapshots**
  - Optional **encryption**
- Good for lab and cloud images, slightly more overhead than RAW.

---

## Thick vs Thin Provisioning

### Thin Provisioning

- Disk file **starts small** and **grows on demand** as data is written.
- **Pros:**
  - Saves space on the datastore.
  - Good for labs where many VMs share limited storage.
- **Cons:**
  - Can cause **unpredictable performance** if storage fills up or grows frequently.
  - Risk of **overcommit** (allocated to VMs > physical space).

### Thick Provisioning

- Disk space is **pre-allocated in full** at creation time.
- **Pros:**
  - More **predictable performance**.
  - Avoids fragmentation and allocation delays.
- **Cons:**
  - Uses full disk space from day one.
  - Less efficient in terms of storage utilization.

> In short:
> - **Thin** → saves space, variable performance.  
> - **Thick** → uses more space, usually **more stable performance**.

---

## Storage Virtualization Concepts

### Image Templates

- A **base VM image** with OS + common tools pre-installed.
- Used to **rapidly clone** new VMs with identical base configuration.
- Example: A **golden image** for a firewall VNF or router VNF.

### Snapshots

- **Point-in-time copies** of a VM’s disk state (and sometimes memory).
- Use cases:
  - Before upgrades or config changes (easy rollback).
  - Lab testing: quickly revert to a *clean* state.
- Too many snapshots or long-lived snapshots can **hurt performance**.

### Clones

- A **full copy** of a VM (or disk) created from a template or another VM.
- Types:
  - **Full clone**: independent copy, uses full storage.
  - **Linked clone**: shares blocks with parent but depends on it.
- Used for:
  - Spinning up multiple VNFs / lab nodes quickly.
  - Replicating test environments.

### Virtual SAN / File-Based Storage

- **Virtual SAN (vSAN)** or similar: aggregates local disks from multiple hosts into a **shared, virtual storage pool**.
- **File-based storage** (NFS, SMB):
  - VMs store their virtual disks as **files** on a network share.
  - Easy to manage and back up.
- These provide:
  - **Shared storage** for features like VM migration, HA, DRS.
  - Centralized management and scaling.

---

## Storage Performance & Its Impact on VNFs / Labs

Storage I/O matters a lot for **network functions** and **lab environments**:

### For VNFs (Virtual Network Functions)

- VNFs like **firewalls, IDS/IPS, DPI, routers**:
  - Might be **I/O heavy** (logs, state, databases, caches).
  - Slow storage → **higher latency**, **slower boot**, **slower log writes**.
- With poor storage:
  - Packet processing itself (CPU/NIC) might be fast, but:
    - Analytics, logging, and state sync can **lag**.
    - VNF scaling/upgrades can be **slow**.

---
