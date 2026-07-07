# 🎣 Phishing Campaign Playbook

> [!info]
> Standard operating procedure for conducting targeted email social engineering (spear-phishing) engagements.

## 1. Reconnaissance & Setup
- [ ] Register lookalike domains (e.g., `company-portal-login.com`).
- [ ] Setup email infrastructure (Postfix, Mailgun) and configure SPF, DKIM, and DMARC to bypass spam filters.
- [ ] Harvest employee emails (OSINT, LinkedIn, Hunter.io).
- [ ] Clone the target authentication portal (e.g., using GoPhish + Evilginx2 for MFA bypass).

## 2. Campaign Design
- [ ] Draft pretext (e.g., "Urgent IT Update", "Benefits Enrollment").
- [ ] Create the email template incorporating the pretext and payload link.
- [ ] Define success metrics (Open rate, Click rate, Credential submission, MFA bypass).

## 3. Execution
- [ ] Send a test batch to client-provided test accounts to verify deliverability.
- [ ] Launch the campaign to the target list.
- [ ] Monitor infrastructure to ensure it hasn't been flagged or taken down.

## 4. Analysis & Reporting
- [ ] Aggregate metrics from GoPhish.
- [ ] Securely handle and purge captured credentials.
- [ ] Generate a report highlighting vulnerable departments and recommending security awareness training improvements.
