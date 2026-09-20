
## ISO 27001 Controls Covered

| Control | Name | What It Checks |
|---|---|---|
| A.8.4 | Access to Source Code | Hardcoded credentials/secrets |
| A.8.8 | Technical Vulnerability Management | Known vulnerable dependencies |
| A.8.9 | Configuration Management | Insecure default configs |
| A.8.24 | Cryptography | Weak/hardcoded encryption |
| A.8.28 | Secure Coding | Injection, XSS, unsafe functions |

## Tech Stack

- **GitHub Actions** — CI/CD trigger on push
- **Semgrep** — open-source static application security testing (SAST)
- **n8n** — workflow automation (self-hosted)
- **Google Sheets** — audit trail / compliance log

All tools used are free / open-source.

## How It Works

1. On every push to `main`, GitHub Actions runs a Semgrep scan against 
   the codebase using three rulesets: general security audit, secrets 
   detection, and OWASP Top 10 patterns.
2. Results are sent as JSON to an n8n webhook.
3. A custom mapping layer translates each technical finding (e.g., 
   `hardcoded-secret`) into its corresponding ISO 27001 control 
   (e.g., `A.8.4`), assigns a Pass/Fail status, and generates 
   remediation guidance.
4. Every scan result is appended to a Google Sheet, creating a 
   time-stamped compliance record.
5. Failed controls trigger an automated notification via Email/Slack.

## Sample Output

| Date | Control | Status | Finding | Remediation |
|---|---|---|---|---|
| 2026-09-20 | A.8.4 | FAIL | Hardcoded secret in app.py | Move credentials to environment variables / secrets manager |
| 2026-09-20 | A.8.28 | PASS | — | — |

## What This Demonstrates

This project sits at the intersection of security engineering and 
governance, risk, and compliance (GRC). The technical scanning is 
automated — the judgment layer (mapping findings to specific 
regulatory controls, deciding severity, writing defensible 
remediation guidance) is the part that required domain expertise to 
design.

## Setup

1. Fork this repo
2. Set up an n8n instance (self-hosted or cloud)
3. Create a webhook workflow in n8n with the mapping logic (see 
   `/workflow` folder for reference)
4. Update the webhook URL in `.github/workflows/iso-scan.yml`
5. Connect a Google Sheet for logging
6. Push code and watch the pipeline run under the Actions tab

## Author

Hassaan Kashif — GRC Automation Engineer  
[LinkedIn](https://linkedin.com/in/hassaan-kashif-993865328) | 
[GitHub](https://github.com/HassaanKashif-CY)
