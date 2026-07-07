import re
import os
import json

input_file = '/home/kali/.gemini/antigravity/brain/1b193ecb-9e84-4ff0-9a9c-f807d971f90f/.system_generated/steps/200/output.txt'
output_file = '/home/kali/Desktop/B/OffensiveSecurityOS/pages/bug-bounty-os.md'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The output from evaluate_script is usually wrapped. Let's find the JSON string.
json_str = ""
for line in lines:
    if line.startswith('"') and line.strip().endswith('"'):
        json_str = line.strip()
        break

if not json_str:
    # fallback if it's somehow just a giant string
    raw_text = "".join(lines)
    # try to unescape \n manually if json loads fails
    try:
        # The output format is:
        # Script ran on page and returned:
        # ```json
        # "string\ncontent"
        # ```
        # We need to extract the content inside the ```json blocks
        start = raw_text.find('```json\n') + 8
        end = raw_text.rfind('\n```')
        json_content = raw_text[start:end]
        parsed_text = json.loads(json_content)
    except:
        parsed_text = raw_text.replace('\\n', '\n')
else:
    parsed_text = json.loads(json_str)

lines = parsed_text.split('\n')
md_lines = []
md_lines.append("# 🎯 Ultimate Bug Bounty OS\n")
md_lines.append("> [!info]\n> The master dashboard for tracking bug bounty hunting from Rules of Engagement (ROE) to the Final Report. Connects Subdomains, Assets, and Vulnerabilities.\n")

md_lines.append("## 📌 1. Rules of Engagement & Scope\n")
md_lines.append("- [ ] Review target scope and out-of-scope assets.\n")
md_lines.append("- [ ] Verify allowed testing types (e.g., no DDoS/Social Engineering).\n")
md_lines.append("- [ ] Set up project structure: `mkdir -p ~/bugbounty/{recon,screenshots,notes,tools}`\n")
md_lines.append("- [ ] Configure Burp Suite, VPN, and Note-taking system.\n\n")

md_lines.append("## 🗄️ 2. Connected Databases (Notion Sync)\n")
md_lines.append("- **Subdomains DB:** Track all discovered subdomains and open ports.\n")
md_lines.append("- **Vulnerabilities DB:** Map findings to subdomains and CVSS scores.\n\n")

md_lines.append("## ⚔️ 3. Execution Checklist\n")

in_code_block = False
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Skip noise
    if "Mark Complete" in line or "Progress" in line or "marked as complete!" in line or "Script ran on page" in line or line == "```":
        continue
        
    if line == "$":
        if not in_code_block:
            in_code_block = True
            md_lines.append("```bash")
        continue
        
    if in_code_block:
        if line.startswith("curl ") or line.startswith("sqlmap ") or line.startswith("python ") or line.startswith("nmap ") or line.startswith("'") or line.startswith("#") or line.startswith("mkdir ") or line.startswith("git ") or line.startswith("cd "):
            md_lines.append(line)
        else:
            in_code_block = False
            md_lines.append("```\n")
            
    if not in_code_block:
        if len(line) < 50 and not line.startswith("-") and line[0].isalpha() and line[0].isupper():
            md_lines.append(f"\n### 🔍 {line}")
        elif len(line) > 10:
            md_lines.append(f"- [ ] {line}")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
