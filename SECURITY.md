# Security Policy & Operational Safety

## 1. Zero Credential & PII Policy
RAVEN is strictly a **catalog and documentation index** for open-source intelligence tools. 

Under no circumstances should this repository ever contain:
* Real API keys, tokens, or session cookies
* Passwords, secrets, or credential dumps
* Personally Identifiable Information (PII) of living individuals
* Defanged or live malware payloads
* Leaked databases or proprietary documents

When documenting tools that require API keys or authentication, use standardized placeholder flags:
```markdown
API_KEY_REQUIRED=true
AUTH_TYPE="Bearer Token"
```
Always link to the official provider documentation where researchers can safely obtain their own legitimate credentials.

## 2. Legal & Ethical Boundary
All tools indexed within RAVEN are intended solely for:
* Authorized security audits, red-teaming, and penetration testing
* Lawful investigative journalism and human rights research
* Incident response, fraud detection, and threat intelligence
* Academic research and CTF / defensive cyber training

**Strictly Prohibited:**
* Stalking, harassment, or non-consensual tracking of private individuals
* Doxxing or public disclosure of private sensitive data
* Circumvention of access controls or unauthorized system penetration
* Automated mass scraping violating terms of service or privacy laws

## 3. Reporting Vulnerabilities
If you discover an exposed credential, security issue, or broken link within RAVEN, please file an issue or submit a pull request immediately.
