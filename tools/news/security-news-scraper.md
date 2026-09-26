# Security News Scraper

> Automated cybersecurity news aggregator, RSS harvester, and threat advisory scraper.

---

## Purpose
Security News Scraper is an automated collection utility built in Go that monitors, scrapes, and parses threat intelligence advisories, vulnerability disclosures, and cybersecurity publications (e.g. Krebs on Security, The Hacker News, BleepingComputer). It extracts CVE identifiers, publication dates, and incident summaries for automated threat monitoring and OSINT reporting.

## Category
- **Primary**: News & Media Monitoring (`news`)
- **Secondary**: Threat Actor & C2 Intelligence (`threat-intelligence`), Workflow Automation & Pipelines (`automation`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Go (Golang)
- **Platform**: Cross-platform (Linux, Windows, macOS)

## Installation

```bash
# Clone the repository
git clone https://github.com/CarterPerez-dev/Cybersecurity-Projects.git
cd Cybersecurity-Projects/PROJECTS/intermediate/security-news-scraper

# Build the Go binary
go build -o security-news-scraper main.go
```

## Usage

```bash
# Run news scraper directly
go run main.go

# Or execute compiled binary
./security-news-scraper
```

## Common Use Cases
1. **Daily Threat Landscape Tracking**: Aggregating the latest zero-day reports, vendor security advisories, and breach announcements.
2. **Automated CVE Alerting**: Extracting mentioned Common Vulnerabilities and Exposures (CVEs) across published technical news feeds.
3. **OSINT Feed Ingestion**: Providing structured news feeds to supply threat intelligence dashboards and incident briefing pipelines.

## Input
- Pre-configured target news sources and RSS feed endpoints (configurable in source/config).

## Output
- Formatted console output, structured feeds with article titles, source publications, timestamps, and extracted CVE identifiers.

## Requirements
- **Dependencies**: Go 1.19+ runtime
- **API Keys**: None required.
- **Account / Authentication**: None required.
- **External Services**: Public HTTP/HTTPS access to news portal endpoints.

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/security-news-scraper](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/security-news-scraper)

## Status
- **Status**: Active

## RAVEN Notes
Security News Scraper satisfies the automated collection requirement for open-source media intelligence. Its standalone Go implementation offers high execution speed and zero runtime interpreter dependencies compared to heavy Python scrapers, making it ideal for scheduled cron jobs or containerized threat monitoring.
