# 📑 Standard Report Structure

> [!info]
> This structure is used for the final deliverables provided to clients or internal stakeholders. It is designed to be easily exported to PDF.

## 1. Executive Summary
- **Objective:** Brief statement of the engagement's purpose.
- **Scope:** High-level overview of what was tested.
- **Key Findings:** A non-technical summary of the most critical vulnerabilities.
- **Overall Risk Posture:** An assessment of the organization's current security maturity based on the engagement.

## 2. Assessment Methodology
- Summary of the approach taken (e.g., OWASP, PTES).
- Identification of tools used and manual testing techniques.

## 3. Finding Summary (Dashboard)
| Finding | Severity | CVSS | Status |
| :--- | :--- | :--- | :--- |
| [Finding Name] | Critical | 9.8 | Open |

## 4. Detailed Technical Findings
> *Import findings here using the `finding-template.md`.*

## 5. Appendices
- **Appendix A:** Tool output (if required by RoE)
- **Appendix B:** Full asset inventory
- **Appendix C:** Definitions of severity rankings (CVSS base metrics)
