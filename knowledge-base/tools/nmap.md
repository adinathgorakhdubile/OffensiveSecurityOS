# 🗺️ Nmap (Network Mapper)

> [!info]
> Nmap is the industry standard for network discovery and security auditing.

## 🚀 Quick Scans

| Scan Type | Command | Description |
| :--- | :--- | :--- |
| **Ping Sweep** | `nmap -sn 192.168.1.0/24` | Discover live hosts without port scanning. |
| **Fast Scan** | `nmap -F 192.168.1.1` | Scan the top 100 common ports quickly. |
| **Full TCP Scan** | `nmap -p- 192.168.1.1` | Scan all 65,535 TCP ports. |
| **Service Enum** | `nmap -sV 192.168.1.1` | Determine service/version info. |
| **OS Enum** | `nmap -O 192.168.1.1` | Attempt to guess the operating system. |

## 🛡️ Stealth & Evasion
- **SYN Stealth Scan:** `nmap -sS [Target]` (Requires root)
- **Fragment Packets:** `nmap -f [Target]`
- **Decoy Scan:** `nmap -D RND:10,RND:11 [Target]`

## 📜 Nmap Scripting Engine (NSE)
Use NSE scripts to automate vulnerability detection:

```bash
# General Vuln scan
nmap --script vuln 192.168.1.1

# SMB Enumeration
nmap -p 445 --script smb-os-discovery 192.168.1.1
```
