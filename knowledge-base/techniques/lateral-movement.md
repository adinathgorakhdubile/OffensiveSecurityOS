# 🔀 Lateral Movement

> [!info]
> Techniques used by attackers to progressively move through a network, searching for key data and assets.

## 🔑 Common Vectors
- **Pass-the-Hash (PtH):** Reusing captured NTLM hashes to authenticate.
- **Pass-the-Ticket (PtT):** Reusing Kerberos TGT/TGS tickets.
- **Remote Services:** Exploiting RDP, SSH, SMB, or WinRM.

## 🛠️ Tools of the Trade
| Tool | Use Case | Command Example |
| :--- | :--- | :--- |
| **CrackMapExec** | SMB/WinRM spreading | `cme smb 10.0.0.0/24 -u user -p pass` |
| **Impacket** | WMI/SMB execution | `wmiexec.py DOMAIN/user:pass@10.0.0.5` |
| **BloodHound** | AD Attack Path Mapping | (Used for planning the route) |

## 🛡️ Mitigation & Detection
- Implement Network Segmentation and Microsegmentation.
- Restrict Local Admin rights (LAPS).
- Monitor for anomalous Windows Event Logs (e.g., Event ID 4624 Logon Type 3).
