# 🕸️ Web Application Methodology

> [!info]
> This methodology follows the OWASP Top 10 and OWASP Web Security Testing Guide (WSTG). Use this as a checklist and tracking page for each web application engagement.

## 📋 Engagement Details
- **Target URL:** `[URL]`
- **Application Name:** `[App Name]`
- **Tech Stack:** `[Stack]`

---

## 1. Information Gathering & Reconnaissance
- [ ] Subdomain enumeration
- [ ] Directory and file brute-forcing
- [ ] Identify web application framework
- [ ] Map application architecture
- [ ] Review `robots.txt`, `sitemap.xml`, and source code comments

## 2. Authentication & Authorization Testing
- [ ] Test for default/weak credentials
- [ ] Bypass authentication controls
- [ ] Test password reset mechanisms
- [ ] Check for privilege escalation (Horizontal/Vertical)
- [ ] Analyze session management (Cookie flags, entropy, expiration)

## 3. Input Validation Testing
- [ ] Cross-Site Scripting (Reflected, Stored, DOM)
- [ ] SQL Injection (Error-based, Blind, Time-based)
- [ ] Command Injection
- [ ] XML External Entity (XXE) Injection
- [ ] Server-Side Request Forgery (SSRF)

## 4. Business Logic & API Testing
- [ ] Test for Insecure Direct Object References (IDOR)
- [ ] Analyze GraphQL/REST endpoints for unauthorized access
- [ ] Bypass business logic restrictions (e.g., pricing manipulation)
- [ ] Check for race conditions

## 5. Cryptography & Configuration
- [ ] Verify TLS/SSL configuration
- [ ] Check for sensitive data exposure in transit or at rest
- [ ] Review security headers (CORS, CSP, HSTS)

---

## 📝 Assessment Notes

| Finding | Severity | Description | Status |
| :--- | :--- | :--- | :--- |
| Example finding | High | Brief description | Open / Closed |
|  |  |  |  |
