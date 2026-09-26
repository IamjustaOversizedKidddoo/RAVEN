# RAVEN

```text
██████╗  █████╗ ██╗   ██╗███████╗███╗   ██╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║
██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║
██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
```

> **An organized arsenal of open-source OSINT tools, network intelligence frameworks, and investigative tradecraft.**

[![Status](https://img.shields.io/badge/STATUS-OPERATIONAL-00FF66?style=flat-square&labelColor=0a0a0a)](https://github.com/IamjustaOversizedKidddoo/RAVEN)
[![License](https://img.shields.io/badge/LICENSE-MIT-lightgrey?style=flat-square&labelColor=0a0a0a)](LICENSE)
[![Database](https://img.shields.io/badge/DATABASE-tools.json-blue?style=flat-square&labelColor=0a0a0a)](database/tools.json)
[![Taxonomy](https://img.shields.io/badge/TAXONOMY-33%20Categories-purple?style=flat-square&labelColor=0a0a0a)](database/categories.json)
[![Integrity](https://img.shields.io/badge/INTEGRITY-VALIDATED-success?style=flat-square&labelColor=0a0a0a)](scripts/maintenance/)

---

## Table of Contents

- [1. What is RAVEN?](#1-what-is-raven)
- [2. Cataloged Arsenal (Tool Matrix)](#2-cataloged-arsenal-tool-matrix)
- [3. Searchable Arsenal Index (Find a Tool)](#3-searchable-arsenal-index-find-a-tool)
- [4. OSINT Operational Categories](#4-osint-operational-categories)
- [5. Investigation Workflows](#5-investigation-workflows)
- [6. Architecture & Directory Layout](#6-architecture--directory-layout)
- [7. Installation Philosophy](#7-installation-philosophy)
- [8. Responsible Research & Legal Boundaries](#8-responsible-research--legal-boundaries)
- [9. Contributing & Maintenance Engine](#9-contributing--maintenance-engine)

---

## 1. What is RAVEN?

**RAVEN** is a structured, searchable, and continuously expandable Open Source Intelligence (OSINT) tool arsenal. 

Rather than serving as an unstructured list of arbitrary bookmarks or a bloated repository of vendored third-party code, RAVEN acts as a standardized **intelligence armory and catalog**:

* **Search-First Indexing**: Every tool is cataloged with structured metadata, capabilities, interfaces, operational requirements, and searchable taxonomy tags.
* **Actionable Tool Cards**: Each entry contains standardized installation snippets, reproducible syntax examples, practical tradecraft notes, and original upstream attribution.
* **Synchronized Master Database**: A normalized JSON database ([database/tools.json](database/tools.json)) backs all documentation, enabling automated validation, duplicate detection, and index generation.
* **Investigation Playbooks**: Standardized methodologies mapping investigative targets (usernames, domains, entities, infrastructure) to discovery, enumeration, correlation, and verification phases.

---

## 2. Cataloged Arsenal (Tool Matrix)

A quick-reference comparative matrix of all integrated tools across interfaces, runtimes, authentication requirements, and upstream repositories:

<!-- TOOL-MATRIX:START -->
| Tool | Category | Interface | Language | API Key | Status | Upstream Source | Card |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: |
| **Awesome Networking (Facyber)** | `network` | Web | Markdown | `None` | `Active` | [GitHub Repository](https://github.com/facyber/awesome-networking) | [Inspect Card](tools/network/awesome-networking-(facyber).md) |
| **Awesome Networking (Nyquist)** | `network` | Web | Markdown | `None` | `Active` | [GitHub Repository](https://github.com/nyquist/awesome-networking) | [Inspect Card](tools/network/awesome-networking-(nyquist).md) |
| **Containerlab** | `infrastructure` | CLI | Go | `None` | `Active` | [GitHub Repository](https://github.com/srl-labs/containerlab) | [Inspect Card](tools/infrastructure/containerlab.md) |
| **Horus** | `investigation-frameworks` | CLI | Python | `None` | `Active` | [GitHub Repository](https://github.com/6abd/horus) | [Inspect Card](tools/investigation-frameworks/horus.md) |
| **MailAccess** | `emails` | CLI, Web | Python, TypeScript | `None` | `Active` | [GitHub Repository](https://github.com/KatrielMoses/MailAccess) | [Inspect Card](tools/emails/mailaccess.md) |
| **Multiplayer Networking Resources** | `miscellaneous` | Web | Markdown | `None` | `Active` | [GitHub Repository](https://github.com/0xFA11/MultiplayerNetworkingResources) | [Inspect Card](tools/miscellaneous/multiplayer-networking-resources.md) |
| **Rveng** | `miscellaneous` | CLI | Python | `None` | `Active` | [GitHub Repository](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/advanced/rveng) | [Inspect Card](tools/miscellaneous/rveng.md) |
| **Scapy** | `network` | CLI, Library | Python | `None` | `Active` | [GitHub Repository](https://github.com/secdev/scapy) | [Inspect Card](tools/network/scapy.md) |
| **Security News Scraper** | `news` | CLI | Go | `None` | `Active` | [GitHub Repository](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/security-news-scraper) | [Inspect Card](tools/news/security-news-scraper.md) |
| **Sniffnet** | `network` | GUI | Rust | `None` | `Active` | [GitHub Repository](https://github.com/GyulyVGC/sniffnet) | [Inspect Card](tools/network/sniffnet.md) |
| **Steganography Multi-Tool** | `metadata` | CLI | Python | `None` | `Active` | [GitHub Repository](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/beginner/steganography-multi-tool) | [Inspect Card](tools/metadata/steganography-multi-tool.md) |
| **System Design 101** | `infrastructure` | Web | Markdown | `None` | `Active` | [GitHub Repository](https://github.com/ByteByteGoHq/system-design-101) | [Inspect Card](tools/infrastructure/system-design-101.md) |
| **TorBot** | `dark-web` | CLI | Python | `None` | `Active` | [GitHub Repository](https://github.com/DedSecInside/TorBot) | [Inspect Card](tools/dark-web/torbot.md) |
<!-- TOOL-MATRIX:END -->

---

## 3. Searchable Arsenal Index (Find a Tool)

Quickly locate tools organized by their primary operational intelligence domain:

<!-- SEARCH-INDEX:START -->
### Email Intelligence
- **[MailAccess](tools/emails/mailaccess.md)** ([Upstream](https://github.com/KatrielMoses/MailAccess)) - High-throughput email OSINT investigation toolkit and domain-level mailbox harvesting engine.

### Metadata Analysis
- **[Steganography Multi-Tool](tools/metadata/steganography-multi-tool.md)** ([Upstream](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/beginner/steganography-multi-tool)) - Forensic image steganography analyzer and hidden payload detection utility.

### Dark Web & Hidden Services
- **[TorBot](tools/dark-web/torbot.md)** ([Upstream](https://github.com/DedSecInside/TorBot)) - Dark web OSINT crawler, hidden services mapper, and link tree visualizer for the Tor network.

### Network & IP Intelligence
- **[Scapy](tools/network/scapy.md)** ([Upstream](https://github.com/secdev/scapy)) - Powerful interactive packet manipulation library and network reconnaissance engine.
- **[Sniffnet](tools/network/sniffnet.md)** ([Upstream](https://github.com/GyulyVGC/sniffnet)) - Cross-platform application to monitor and analyze Internet network traffic comfortably and multilingually.
- **[Awesome Networking (Facyber)](tools/network/awesome-networking-(facyber).md)** ([Upstream](https://github.com/facyber/awesome-networking)) - Curated list of essential computer networking resources, protocols, packet analysis tools, and RFCs.
- **[Awesome Networking (Nyquist)](tools/network/awesome-networking-(nyquist).md)** ([Upstream](https://github.com/nyquist/awesome-networking)) - Curated index of modern network engineering tools, libraries, BGP frameworks, and performance analyzers.

### Infrastructure & Cloud Assets
- **[Containerlab](tools/infrastructure/containerlab.md)** ([Upstream](https://github.com/srl-labs/containerlab)) - Declarative container-based network lab orchestration system for simulating complex network topologies.
- **[System Design 101](tools/infrastructure/system-design-101.md)** ([Upstream](https://github.com/ByteByteGoHq/system-design-101)) - Comprehensive visual reference and deep-dive compendium for system architecture and large-scale infrastructure design.

### News & Media Monitoring
- **[Security News Scraper](tools/news/security-news-scraper.md)** ([Upstream](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/security-news-scraper)) - Automated cybersecurity news aggregator, RSS harvester, and threat advisory scraper.

### Comprehensive OSINT Frameworks
- **[Horus](tools/investigation-frameworks/horus.md)** ([Upstream](https://github.com/6abd/horus)) - Multi-purpose OSINT and digital forensics assistant for unified artifact investigation and data synthesis.

### Miscellaneous & Auxiliary Tools
- **[Rveng](tools/miscellaneous/rveng.md)** ([Upstream](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/advanced/rveng)) - Advanced binary analysis and reverse engineering framework for executable inspection and disassembly.
- **[Multiplayer Networking Resources](tools/miscellaneous/multiplayer-networking-resources.md)** ([Upstream](https://github.com/0xFA11/MultiplayerNetworkingResources)) - Comprehensive technical index of real-time UDP network protocols, state synchronization, and packet architectures.

<!-- SEARCH-INDEX:END -->

---

## 4. OSINT Operational Categories

Jump directly to an operational domain:

[Archives](tools/archives/) • [Automation](tools/automation/) • [Aviation](tools/aviation/) • [Breach Intelligence](tools/breach-intelligence/) • [Companies](tools/companies/) • [Crypto](tools/crypto/) • [Dark Web](tools/dark-web/) • [DNS](tools/dns/) • [Documents](tools/documents/) • [Domains](tools/domains/) • [Emails](tools/emails/) • [Geolocation](tools/geolocation/) • [Images](tools/images/) • [Infrastructure](tools/infrastructure/) • [Investigation Frameworks](tools/investigation-frameworks/) • [Maps](tools/maps/) • [Maritime](tools/maritime/) • [Metadata](tools/metadata/) • [Miscellaneous](tools/miscellaneous/) • [Network](tools/network/) • [News](tools/news/) • [Organizations](tools/organizations/) • [People](tools/people/) • [Phone Numbers](tools/phone-numbers/) • [Reconnaissance](tools/reconnaissance/) • [Search Engines](tools/search-engines/) • [Social Media](tools/social-media/) • [Subdomains](tools/subdomains/) • [Threat Intelligence](tools/threat-intelligence/) • [Usernames](tools/usernames/) • [Vehicles](tools/vehicles/) • [Visualization](tools/visualization/) • [Websites](tools/websites/)

The table below reflects all operational categories defined in RAVEN's taxonomy and their current tool counts.

<!-- CATEGORY-TABLE:START -->
| Category | Operational Domain & Focus | Cataloged Tools | Directory |
| :--- | :--- | :---: | :---: |
| **People & Identity** | Public records, identity verification, background research, and person-of-interest discovery. | `0` | [`people/`](tools/people/) |
| **Usernames & Handles** | Cross-platform username enumeration, account existence validation, and profile correlation. | `0` | [`usernames/`](tools/usernames/) |
| **Email Intelligence** | Email address discovery, mailbox verification, deliverability checking, and domain association. | `1` | [`emails/`](tools/emails/) |
| **Domain Intelligence** | WHOIS lookups, historical domain ownership, registrar analysis, and registration patterns. | `0` | [`domains/`](tools/domains/) |
| **DNS Telemetry** | Forward/reverse DNS resolution, zone transfer auditing, DNS record tracking, and cache snooping. | `0` | [`dns/`](tools/dns/) |
| **Subdomain Enumeration** | Passive and active subdomain discovery, Certificate Transparency logs, and brute-force scanners. | `0` | [`subdomains/`](tools/subdomains/) |
| **Websites & Applications** | Web technology profiling, CMS detection, server headers, and source code reconnaissance. | `0` | [`websites/`](tools/websites/) |
| **Social Media Intelligence** | Platform-specific profiling, follower network graph analysis, post scraping, and temporal tracking. | `0` | [`social-media/`](tools/social-media/) |
| **Image & Forensic Intelligence** | Reverse image search, EXIF metadata extraction, manipulation detection, and visual analysis. | `0` | [`images/`](tools/images/) |
| **Geolocation & Terrain** | IP geolocation, coordinate triangulation, visual terrain matching, and photo location identification. | `0` | [`geolocation/`](tools/geolocation/) |
| **Maps & Geospatial Intelligence** | Satellite imagery analysis, geographic information systems (GIS), mapping tools, and spatial data. | `0` | [`maps/`](tools/maps/) |
| **Metadata Analysis** | Document metadata extraction (PDF, DOCX, XLSX, media), author attribution, and software signatures. | `1` | [`metadata/`](tools/metadata/) |
| **Documents & Public Filings** | Public document scrapers, regulatory filings, government gazettes, and academic paper retrieval. | `0` | [`documents/`](tools/documents/) |
| **Company & Corporate Intelligence** | Corporate registry lookups, beneficial ownership research, financial statements, and business networks. | `0` | [`companies/`](tools/companies/) |
| **Organizations & Entities** | Non-profit records, academic institutions, public bodies, and entity relationship mapping. | `0` | [`organizations/`](tools/organizations/) |
| **Breach & Exposure Intelligence** | Leaked credential queries, exposure verification, paste site indexing, and breach impact analysis. | `0` | [`breach-intelligence/`](tools/breach-intelligence/) |
| **Threat Actor & C2 Intelligence** | Adversary tracking, malicious infrastructure profiling, IOC databases, and malware campaign telemetry. | `0` | [`threat-intelligence/`](tools/threat-intelligence/) |
| **Dark Web & Hidden Services** | Tor onion network indexers, I2P discovery, darknet marketplace monitors, and illicit forum telemetry. | `1` | [`dark-web/`](tools/dark-web/) |
| **Network & IP Intelligence** | Autonomous System (ASN) lookup, BGP routing data, network range discovery, and open port scanning. | `4` | [`network/`](tools/network/) |
| **Infrastructure & Cloud Assets** | Public cloud asset discovery (S3, Azure blobs, GCP buckets), CDN mapping, and SSL certificate reconnaissance. | `2` | [`infrastructure/`](tools/infrastructure/) |
| **Phone Number Intelligence** | Carrier lookups, country dialing analysis, caller identification data, and messaging app footprinting. | `0` | [`phone-numbers/`](tools/phone-numbers/) |
| **Cryptocurrency & Blockchain** | Blockchain ledger explorers, transaction graph tracing, wallet clustering, and smart contract telemetry. | `0` | [`crypto/`](tools/crypto/) |
| **Aviation & Flight Tracking** | ADS-B flight telemetry, aircraft registration lookups, tail number tracing, and flight route history. | `0` | [`aviation/`](tools/aviation/) |
| **Maritime & Vessel Tracking** | AIS ship positioning, maritime fleet databases, port arrivals/departures, and MMSI/IMO resolution. | `0` | [`maritime/`](tools/maritime/) |
| **Vehicle Intelligence** | License plate recognition, vehicle identification number (VIN) checks, and motor registry tools. | `0` | [`vehicles/`](tools/vehicles/) |
| **News & Media Monitoring** | Global news aggregators, RSS feed ingestion, local news search, and media sentiment tracking. | `1` | [`news/`](tools/news/) |
| **Web Archives & Historical Data** | Wayback Machine tools, cached web pages, historical DNS records, and deleted content retrieval. | `0` | [`archives/`](tools/archives/) |
| **Specialized Search Engines & Dorking** | Advanced Google Dorking, IoT/Industrial search engines (Shodan, Censys), and specialized search portals. | `0` | [`search-engines/`](tools/search-engines/) |
| **Workflow Automation & Pipelines** | Multi-tool pipelines, scheduled data collection engines, and automated reconnaissance scripts. | `0` | [`automation/`](tools/automation/) |
| **External Attack Surface Recon** | Broad attack surface management, enterprise perimeter sweeps, and multi-vector target discovery. | `0` | [`reconnaissance/`](tools/reconnaissance/) |
| **Graph Analysis & Visualization** | Entity relationship graphing, link analysis, timeline visualizers, and visual investigation mapping. | `0` | [`visualization/`](tools/visualization/) |
| **Comprehensive OSINT Frameworks** | All-in-one modular platforms, investigation management suites, and unified intelligence frameworks. | `1` | [`investigation-frameworks/`](tools/investigation-frameworks/) |
| **Miscellaneous & Auxiliary Tools** | Format converters, encoding/decoding utilities, timezone calculators, and specialized helper scripts. | `2` | [`miscellaneous/`](tools/miscellaneous/) |
<!-- CATEGORY-TABLE:END -->

---

## 5. Investigation Workflows

RAVEN includes standardized, step-by-step investigative workflows following the 6-phase intelligence lifecycle:

```text
TARGET ➔ DISCOVERY ➔ ENUMERATION ➔ CORRELATION ➔ VERIFICATION ➔ DOCUMENTATION
```

* [**01: Username Investigation**](docs/workflows/01_username_investigation.md) — Cross-platform handle enumeration, profile correlation, and persona clustering.
* [**02: Email Intelligence**](docs/workflows/02_email_investigation.md) — Passive SMTP handshakes, deliverability checking, and breach correlation.
* [**03: Domain Reconnaissance**](docs/workflows/03_domain_recon.md) — WHOIS/RDAP analysis, DNS zone mapping, and hosting infrastructure profiling.
* [**04: Subdomain Discovery**](docs/workflows/04_subdomain_discovery.md) — Certificate Transparency logs, passive DNS datasets, and attack surface enumeration.
* [**05: Image Intelligence**](docs/workflows/05_image_investigation.md) — Forensic EXIF extraction, reverse visual search, and chronolocation.
* [**06: Social Media Research**](docs/workflows/06_social_media_research.md) — Follower graph extraction, post timing, and bot detection.
* [**07: Corporate Intelligence**](docs/workflows/07_company_research.md) — Official company registers, regulatory filings, and corporate group mapping.
* [**08: Geolocation Analysis**](docs/workflows/08_geolocation.md) — Coordinate triangulation, visual terrain matching, and sun shadow calculations.
* [**09: Cyber Threat Intelligence**](docs/workflows/09_threat_intelligence.md) — Technical IoC enrichment, C2 infrastructure tracking, and ATT&CK mapping.
* [**10: Document Metadata Forensics**](docs/workflows/10_metadata_analysis.md) — File stream analysis, author identification, and internal XML forensics.

---

## 6. Architecture & Directory Layout

```text
RAVEN/
├── README.md                  # Armory index, catalog matrix, and quick navigation
├── LICENSE                    # MIT Open Source License
├── CONTRIBUTING.md           # Tool integration protocol, templates, and validation criteria
├── SECURITY.md               # Legal boundaries, responsible use, and disclosure policy
│
├── database/                 # Normalized JSON database & schema definitions
│   ├── categories.json       # Formal taxonomy of 33 OSINT operational categories
│   ├── schema.json           # JSON Schema (Draft 2020-12) enforcing tool metadata integrity
│   └── tools.json            # Master tool catalog
│
├── tools/                    # Modular tool cards organized by operational category
│   ├── emails/               # Email intelligence tools
│   ├── dark-web/             # Dark web and Tor hidden services
│   ├── network/              # Network analysis and packet inspection
│   ├── infrastructure/       # Lab orchestration and system design
│   ├── news/                 # News scrapers and advisory monitors
│   ├── metadata/             # Image forensics and steganography
│   └── investigation-frameworks/ # Multi-vector OSINT assistants
│
├── docs/                     # Tradecraft, playbooks, and reference manuals
│   ├── methodology/          # The 5-phase intelligence cycle (Target → Documentation)
│   ├── workflows/            # Investigation playbooks (usernames, domains, companies, etc.)
│   ├── cheatsheets/          # Command syntax, dorks, and quick-reference guides
│   └── references/           # Primary registries, authoritative databases, and compliance
│
└── scripts/                  # Automated management, validation, and maintenance suite
    ├── installation/         # Category-specific deployment & setup helpers
    ├── utilities/            # Search & query utilities across the tool catalog
    └── maintenance/          # Integrity checkers, duplicate detectors, and index generators
```

---

## 7. Installation Philosophy

RAVEN does **not** install every tool globally or bundle third-party code as submodules:

1. **Lightweight & Modular**: RAVEN is an indexed catalog and documentation layer. Upstream code is cloned or installed on-demand only when required for an active investigation.
2. **Environment Isolation**: Users are strongly encouraged to deploy tools inside dedicated virtual environments (`venv`, `pipenv`, `conda`) or containerized sandboxes (`Docker`, `Podman`) to prevent dependency conflicts and protect investigator workstations.
3. **No Uncontrolled Vendoring**: Repositories are linked directly to their official upstream creators to preserve provenance, maintainability, and security patching.

---

## 8. Responsible Research & Legal Boundaries

RAVEN is strictly designed and maintained for **authorized security assessments, law enforcement intelligence, academic research, fraud prevention, and lawful OSINT operations**.

* **Zero Tolerance for Malicious Activity**: Tools cataloged in this repository must not be used for unauthorized system access, credential stuffing, stalking, doxxing, harassment, or mass non-consensual surveillance.
* **No Secret/PII Storage**: Under no circumstances should API keys, session tokens, passwords, or personal identifiable information (PII) be committed to RAVEN.
* **Investigator Responsibility**: Compliance with local and international computer crime statutes (such as the US CFAA, UK Computer Misuse Act, and GDPR) rests entirely with the individual conducting research.

For detailed guidelines and vulnerability reporting, consult [SECURITY.md](SECURITY.md).

---

## 9. Contributing & Maintenance Engine

To propose or integrate a new OSINT tool, framework, or utility into RAVEN:

1. Verify it does not already exist:
   ```bash
   python scripts/maintenance/check_duplicates.py
   ```
2. Review the four-step integration protocol in [CONTRIBUTING.md](CONTRIBUTING.md).
3. Ensure schema compliance:
   ```bash
   python scripts/maintenance/validate_database.py
   ```
4. Regenerate repository indexes:
   ```bash
   python scripts/maintenance/generate_indexes.py
   ```
