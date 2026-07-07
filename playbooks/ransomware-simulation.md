# 🦠 Ransomware Simulation Playbook

> [!WARNING]
> This playbook outlines a controlled simulation. Ensure strict scoping and client authorization before execution. Do not use actual destructive malware.

## 1. Preparation Phase
- [ ] Finalize Rules of Engagement (RoE) specifying allowed target hosts.
- [ ] Confirm the simulation will use benign encryption (e.g., encrypting specific dummy files) or simulated indicators of compromise (IoCs).
- [ ] Establish an out-of-band communication channel with the blue team/client.

## 2. Initial Access & Propagation (Simulated)
- [ ] Assume breach (start with a standard user shell) OR execute a payload on a designated test machine.
- [ ] Attempt lateral movement to map internal network reachability.
- [ ] Identify critical file shares (Target Data).

## 3. Data Exfiltration (Simulated)
- [ ] Read dummy sensitive files from file shares.
- [ ] Attempt to exfiltrate data to a safe external C2 server via DNS/HTTPS to test DLP controls.

## 4. Encryption / Impact Phase
- [ ] Drop a benign `readme_ransom.txt` on desktops/shares.
- [ ] (Optional) Encrypt a designated folder of dummy data using a known key.
- [ ] Trigger an alert to the SOC to begin the incident response timeline.

## 5. Reporting
- [ ] Evaluate SOC Time-to-Detect (TTD) and Time-to-Respond (TTR).
- [ ] Document gaps in network segmentation and endpoint protection.
