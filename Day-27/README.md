# Security in Virtualized Environments & Cloud VM Basics
---

## Security Challenges in Virtualization

- **VM escape attacks**  
  - Attacker breaks out of a VM and reaches the hypervisor or other VMs.

- **Misconfigured virtual switches**  
  - Wrong VLAN or port settings may allow unwanted traffic between VMs.

- **Insecure snapshots/clones**  
  - Old snapshots may contain weak passwords, old keys, or unpatched software.  
  - Cloned VMs may reuse IPs, hostnames, or SSH keys.

- **Lack of isolation between tenants**  
  - In multi-tenant environments, poor isolation can leak data or allow one tenant to affect others.

---

## VM Hardening Techniques

- **Disable unused services**  
  - Turn off services like Telnet, FTP, unused web services to reduce attack surface.

- **Firewall rules at host + VM level**  
  - Host firewall: protect hypervisor and management interfaces.  
  - VM firewall: allow only required ports (e.g., SSH, HTTP/HTTPS, app ports).

- **Secure VM templates**  
  - Use patched and hardened “golden images”.  
  - No hardcoded passwords or keys in templates.

- **Network segmentation**  
  - **VLAN segmentation**: separate management, user, storage, and DMZ traffic.  
  - **Host-only / isolated networks**: for labs and internal-only workloads.

---

## Cloud VM Basics (AWS / GCP / Azure)

### Creating VMs in Cloud

General steps (names differ per provider):

1. Choose an OS image (Linux/Windows).
2. Select VM size (CPU, RAM, storage).
3. Attach storage (disk/volume).
4. Place VM in a network (VPC/VNet + subnet).
5. Configure firewall/security rules.
6. Access via SSH key or password.

### Cloud Network Basics

- **VPC / VNet**  
  - Your private virtual network in the cloud.

- **Subnets**  
  - Smaller networks inside the VPC (e.g., public and private subnets).

- **Firewall rules**  
  - Control which IPs/ports/protocols can reach your VMs.

### Security Groups & Key Pairs

- **Security groups**  
  - Virtual firewalls attached to VMs.  
  - Define inbound and outbound rules (e.g., allow SSH from office IP).

- **Key pair authentication**  
  - Use SSH key pairs to log in to Linux VMs.  
  - Private key stays with you; public key is on the VM.

---

## Telecom Use Cases for Cloud VMs

- **Telecom labs**  
  - Build lab environments with multiple VMs for core network, RAN simulators, routers, etc.

- **OSS/BSS workloads**  
  - Run OSS (network management) and BSS (billing/CRM) on scalable cloud VMs.

- **Demos and PoCs**  
  - Quickly spin up demo setups and tear them down after customer sessions.

---

