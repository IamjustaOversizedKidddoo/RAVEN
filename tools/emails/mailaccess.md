# MailAccess

> High-throughput email OSINT investigation toolkit and domain-level mailbox harvesting engine.

---

## Purpose
MailAccess is an open-source email intelligence engine engineered to investigate individual email addresses and harvest corporate address patterns from target domains. It aggregates and correlates intelligence across breach disclosures, public repositories, DNS telemetry, and identity providers to build a consolidated, non-black-box identity graph with confidence scoring.

## Category
- **Primary**: Email Intelligence (`emails`)
- **Secondary**: External Attack Surface Recon (`reconnaissance`), Breach & Exposure Intelligence (`breach-intelligence`), Domain Intelligence (`domains`)

## Interface
- **CLI**
- **Web** (local API & web server)

## Language & Runtime
- **Language**: Python (98.5%), TypeScript (1.5%)
- **Platform**: Cross-platform (Linux, macOS, Windows)

## Installation

```bash
# Recommended installation via pip
pip install mailaccess

# Alternative installation from source
git clone https://github.com/KatrielMoses/MailAccess.git
cd MailAccess
pip install -r requirements.txt
```

## Usage

```bash
# Investigate a specific email target
mailaccess investigate target@example.com

# Harvest all discovered email addresses associated with a corporate domain
mailaccess harvest-emails --domain example.com

# Launch the local web server and API interface
mailaccess serve --port 8080
```

## Common Use Cases
1. **Target Account Footprinting**: Determining digital services, developer profiles, and social accounts associated with an email handle.
2. **Corporate Attack Surface Mapping**: Harvesting publicly exposed employee email addresses from target domain infrastructure during reconnaissance.
3. **Breach Correlation**: Verifying if an email address has appeared in historical leaks and public breach datasets without delivering probe emails.

## Input
- Single email address (e.g. `analyst@domain.com`) or target root domain (e.g. `domain.com`).

## Output
- Structured JSON identity graph, terminal summary reports, or web dashboard visualizations detailing mailbox status, domain MX validity, verified account links, and confidence metrics.

## Requirements
- **Dependencies**: Python 3.9+
- **API Keys**: Over 65 of 75+ modules function with zero API keys required; optional API keys for commercial threat feeds.
- **Account / Authentication**: None required for core modules.
- **External Services**: Queries public DNS servers, Certificate Transparency logs, Common Crawl, and open web registries.

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/KatrielMoses/MailAccess](https://github.com/KatrielMoses/MailAccess)
- **Website / Docs**: [https://mailaccess.pro](https://mailaccess.pro)

## Status
- **Status**: Active

## RAVEN Notes
MailAccess is the recommended primary engine for email pivoting within RAVEN. Compared to single-source checkers or legacy CLI scripts like `holehe` or `theHarvester`, MailAccess synthesizes results into an identity graph with explicit confidence scoring, offers a local API/web server, and operates predominantly without paid API dependencies.
