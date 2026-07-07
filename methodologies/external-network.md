# 🌍 External Network Methodology

> [!info]
> This methodology outlines the standard operating procedure for external perimeter penetration testing. Use this page to track progress across the attack surface.

## 📋 Engagement Details
- **Scope Size:** `[Number of IPs/Domains]`
- **Primary Domain:** `[Domain]`
- **Rules of Engagement:** `[Link to RoE]`

---

## 1. Passive Reconnaissance (OSINT)
- [ ] Identify registered domains and subdomains (ASN, WHOIS)
- [ ] Search public code repositories (GitHub, GitLab) for leaked secrets
- [ ] Analyze breach databases for compromised employee credentials
- [ ] Discover cloud storage buckets (S3, Azure Blobs)
- [ ] Enumerate employee profiles (LinkedIn)

## 2. Active Reconnaissance & Scanning
- [ ] Perform port scanning (TCP/UDP) across in-scope IPs
- [ ] Enumerate active services and versions
- [ ] Perform vulnerability scanning (Nessus, Nuclei, OpenVAS)
- [ ] Map perimeter devices (Firewalls, VPNs, Load Balancers)

## 3. Vulnerability Identification & Exploitation
- [ ] Test for known CVEs on exposed services
- [ ] Brute-force/Spray exposed login portals (SSH, RDP, OWA, VPN)
- [ ] Exploit misconfigurations (Anonymous FTP, Open Relays)
- [ ] Attempt bypass of Web Application Firewalls (WAF)

## 4. Post-Exploitation (If Applicable)
- [ ] Establish persistence (if permitted by RoE)
- [ ] Pivot to internal networks (if permitted by scope)
- [ ] Demonstrate impact of external breach

---

## 📝 Scan Results & Notes

| Host / IP | Port | Service | Vulnerability | Status |
| :--- | :--- | :--- | :--- | :--- |
| 192.168.1.100 | 443 | HTTPS | Heartbleed | Investigating |
|  |  |  |  |  |
