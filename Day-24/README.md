## Virtualization Basics for Modern IT & Telecom
---

## Virtualization

`Virtualization` is the technology that lets you run multiple `virtual machines (VMs)` on a single physical server.

- Each VM looks and behaves like a separate physical machine:
  - Has its own OS (Linux, Windows)
  - Has its own virtual CPU, memory, disk, network.
- But `all VMs share the same physical hardware` underneath.

You get:

- Better hardware utilization (no idle servers).
- Isolation between workloads.
- Flexibility to spin up / delete environments quickly.

### foundational for modern IT & telecom

- `Cloud computing` (AWS, Azure, GCP) is built heavily on virtualization.
- `Telecom / NFV`: network functions (routers, firewalls, EPC, 5G core, etc.) moved from dedicated hardware boxes to `software VNFs` running on standard x86 servers.
- Benefits:
  - Rapid deployment of services.
  - Easier scaling up/down.
  - Lower CAPEX/OPEX (standard servers instead of proprietary hardware).
  - Better multi-tenancy (multiple customers on the same physical infrastructure).

---

## Types of Virtualization

Here we focus on `server virtualization` (VMs), which is most relevant for IT and telecom NFV.

### Full Virtualization

`Idea:` Guest OS is `not aware` that it is running inside a VM.

- The hypervisor `fully emulates` the underlying hardware.
- Guest OS thinks it is on a real physical machine.
- No modification to the guest OS is needed.

`Examples:`

- VMware ESXi
- KVM (Kernel-based Virtual Machine) in typical modes
- Microsoft Hyper-V

`Pros:`

- Any OS that runs on the physical architecture can run as a VM.
- Good isolation between VMs.

`Cons:`

- Historically more overhead because the hypervisor had to emulate privileged CPU instructions.
- Modern CPUs with VT-x/AMD-V greatly reduce this overhead.

---

### Para-Virtualization (What exactly is this?)

`Para‑Virtualization` means the `guest OS knows it is virtualized` and is modified to cooperate with the hypervisor.

Instead of pretending to be real hardware, the hypervisor exposes special `interfaces (hypercalls)` that the guest OS uses directly.

- The guest OS is `modified` to:
  - Avoid problematic instructions that are hard to virtualize.
  - Use hypercalls to request privileged operations from the hypervisor.

`Key points:`

- `Guest aware:` guest OS is virtualization‑aware.
- `Optimized:` can perform better than pure full virtualization on old/limited hardware.
- `Requires support in the guest OS kernel.`

`Examples:`

- Xen para‑virtualized guests (PV mode).
- Early KVM modes using virtio/para-virtualized drivers.
- Modern setups often use `para‑virtualized drivers` (e.g., virtio for disk/network) inside otherwise fully virtualized guests to improve performance.

So:

- Full virtualization: “OS thinks it’s on bare metal.”
- Para‑virtualization: “OS knows it’s inside a VM and uses optimized calls/drivers.”

---

### Hardware-Assisted Virtualization

Modern CPUs add hardware features to make virtualization fast and efficient.

- Intel: `VT-x`, `EPT`
- AMD: `AMD‑V`, `RVI`

These features let the hypervisor:

- Run guest OS `almost at native speed` (near bare-metal).
- Trap and handle privileged instructions efficiently.
- Maintain separate memory mappings for each VM.

`Result:`

- Much less overhead than early software-only virtualization.
- Full virtualization + hardware assist is now the default (e.g., KVM on Linux with VT‑x/AMD‑V).

---

## Types of Hypervisors

A `hypervisor` (Virtual Machine Monitor, VMM) is the software layer that creates and manages VMs.

### Type 1 – Bare-Metal Hypervisor

Runs `directly on the physical hardware`, without a host OS.

- Examples:
  - VMware ESXi
  - Microsoft Hyper-V (Core)
  - Xen (when used as a bare‑metal hypervisor)
- Used commonly in data centers and telecom NFV infrastructure.

`Characteristics:`

- High performance.
- Smaller attack surface compared to full host OS.
- Designed for production workloads.

---

### Type 2 – Hosted Hypervisor

Runs `on top of a host operating system` (Windows, Linux, macOS).

- Examples:
  - VMware Workstation
  - Oracle VirtualBox
  - Parallels Desktop
- Used mostly on developer laptops, desktops, small labs.

`Characteristics:`

- Easier to install and use.
- Slightly more overhead because it goes:
  - VM → Hypervisor → Host OS → Hardware.

---

## Virtualization Stack Overview

A simplified view:

```text
+------------------------------+
|      Applications (in VM)    |
+------------------------------+
|       Guest Operating System |
+------------------------------+
|         Virtual Hardware     |
+------------------------------+
|           Hypervisor         |
+------------------------------+
|        Physical Hardware     |
| (CPU, RAM, Disk, NIC, etc.)  |
+------------------------------+
