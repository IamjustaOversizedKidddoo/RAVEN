# EmailOSINT

> Multi-source email address intelligence tool for querying breach databases, social platform presence, and public records tied to a target email account.

---

## Purpose
EmailOSINT is a Python-based command-line OSINT tool designed to aggregate intelligence about a target email address from multiple public sources simultaneously. It queries breach disclosure databases, major social media platforms, and open web registries to determine where an email address has been registered, what accounts are associated with it, and whether it has appeared in known data breaches. It provides investigators with a fast, consolidated view of an email address's digital footprint without requiring manual lookups across individual services.

## Category
- **Primary**: Email Intelligence (`emails`)
- **Secondary**: Breach & Exposure Intelligence (`breach-intelligence`), External Attack Surface Recon (`reconnaissance`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Python 3
- **Platform**: Cross-platform (Linux, macOS, Windows)

## Installation

```bash
# Clone the repository
git clone https://github.com/krishpranav/emailosint.git
cd emailosint

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run a full OSINT lookup against a target email address
python3 emailosint.py -e target@example.com

# Check social platform presence
python3 emailosint.py -e target@example.com --social

# Query breach databases only
python3 emailosint.py -e target@example.com --breach
```

## Common Use Cases
1. **Email Footprinting**: Determine which social networks, developer platforms, and services a target email is registered on, building a cross-platform identity profile.
2. **Breach Exposure Verification**: Rapidly confirm whether an email address appears in known credential dumps or paste sites for pre-engagement reconnaissance.
3. **Fraud & Impersonation Investigation**: Identify all publicly linked accounts and registrations associated with a suspicious email address during fraud or social engineering investigations.

## Input
- A single target email address (e.g. `target@example.com`).

## Output
- Terminal report listing matched social platforms, breach appearances, and public registrations associated with the queried address.

## Requirements
- **Dependencies**: Python 3.6+, `requests`, `beautifulsoup4` (installed via `requirements.txt`).
- **API Keys**: None required for core modules.
- **Account / Authentication**: None required.
- **External Services**: Queries public web endpoints and breach notification APIs; no private data access required.

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/krishpranav/emailosint](https://github.com/krishpranav/emailosint)
- **Website / Docs**: [https://emailosint.org](https://emailosint.org)

## Status
- **Status**: Active

## RAVEN Notes
EmailOSINT is a lightweight, zero-dependency-key entry point for email address pivoting. It complements RAVEN's heavier email engine (MailAccess) well: use EmailOSINT for fast, breadth-first social presence checks, then escalate to MailAccess for deep identity graph construction with confidence scoring. This tool is best combined with username OSINT (Sherlock, WhatsMyName) after extracting the handle portion of the email address for cross-platform correlation.
