# RAVEN

`
██████╗  █████╗ ██╗   ██╗███████╗███╗   ██╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║
██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║
██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
`

> **An organized arsenal of open-source OSINT tools.**

[![Status](https://img.shields.io/badge/STATUS-OPERATIONAL-00FF66?style=flat-square&labelColor=0a0a0a)](https://github.com/IamjustaOversizedKidddoo/RAVEN)
[![License](https://img.shields.io/badge/LICENSE-MIT-lightgrey?style=flat-square&labelColor=0a0a0a)](LICENSE)
[![Database](https://img.shields.io/badge/DATABASE-tools.json-blue?style=flat-square&labelColor=0a0a0a)](database/tools.json)
[![Taxonomy](https://img.shields.io/badge/TAXONOMY-33%20Categories-purple?style=flat-square&labelColor=0a0a0a)](database/categories.json)
[![Integrity](https://img.shields.io/badge/INTEGRITY-VALIDATED-success?style=flat-square&labelColor=0a0a0a)](scripts/maintenance/)

---

## 1. What is RAVEN?

**RAVEN** is a structured, searchable, and continuously expandable Open Source Intelligence (OSINT) tool arsenal. 

Rather than serving as an unstructured list of links or bloated repository of vendored submodules, RAVEN acts as a standardized **intelligence armory and catalog**:
- **Search-First Indexing**: Every tool is cataloged with structured metadata, capabilities, interfaces, operational requirements, and searchable taxonomy tags.
- **Actionable Tool Cards**: Each entry contains standardized installation instructions, reproducible syntax examples, practical operational tradecraft notes, and original upstream attribution.
- **Synchronized Master Database**: A normalized JSON database (database/tools.json) backs all documentation, enabling automated validation, duplicate detection, and index generation.
- **Investigation Workflows**: Standardized methodologies mapping investigative targets (usernames, domains, entities, infrastructure) to discovery, enumeration, correlation, and verification phases.

---

## 2. Architecture & Directory Taxonomy

`
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
│   ├── usernames/
│   ├── emails/
│   ├── domains/
│   └── ...                   # Created dynamically upon tool integration
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
``

---

## 3. Quick Navigation

Jump directly to an operational domain:

[Archives](tools/archives/) • [Automation](tools/automation/) • [Aviation](tools/aviation/) • [Breach Intelligence](tools/breach-intelligence/) • [Companies](tools/companies/) • [Crypto](tools/crypto/) • [Dark Web](tools/dark-web/) • [DNS](tools/dns/) • [Documents](tools/documents/) • [Domains](tools/domains/) • [Emails](tools/emails/) • [Geolocation](tools/geolocation/) • [Images](tools/images/) • [Infrastructure](tools/infrastructure/) • [Investigation Frameworks](tools/investigation-frameworks/) • [Maps](tools/maps/) • [Maritime](tools/maritime/) • [Metadata](tools/metadata/) • [Miscellaneous](tools/miscellaneous/) • [Network](tools/network/) • [News](tools/news/) • [Organizations](tools/organizations/) • [People](tools/people/) • [Phone Numbers](tools/phone-numbers/) • [Reconnaissance](tools/reconnaissance/) • [Search Engines](tools/search-engines/) • [Social Media](tools/social-media/) • [Subdomains](tools/subdomains/) • [Threat Intelligence](tools/threat-intelligence/) • [Usernames](tools/usernames/) • [Vehicles](tools/vehicles/) • [Visualization](tools/visualization/) • [Websites](tools/websites/)

---

## 4. OSINT Categories

The table below reflects all operational categories defined in RAVEN's taxonomy and their current tool counts.

<!-- CATEGORY-TABLE:START -->
| Category | Focus & Description | Cataloged Tools | Directory |
| :--- | :--- | :---: | :---: |
| **People & Identity** | Public records, identity verification, background research, and person-of-interest discovery. | `0` | [`people/`](tools/people/) |
| **Usernames & Handles** | Cross-platform username enumeration, account existence validation, and profile correlation. | `0` | [`usernames/`](tools/usernames/) |
| **Email Intelligence** | Email address discovery, mailbox verification, deliverability checking, and domain association. | `0` | [`emails/`](tools/emails/) |
| **Domain Intelligence** | WHOIS lookups, historical domain ownership, registrar analysis, and registration patterns. | `0` | [`domains/`](tools/domains/) |
| **DNS Telemetry** | Forward/reverse DNS resolution, zone transfer auditing, DNS record tracking, and cache snooping. | `0` | [`dns/`](tools/dns/) |
| **Subdomain Enumeration** | Passive and active subdomain discovery, Certificate Transparency logs, and brute-force scanners. | `0` | [`subdomains/`](tools/subdomains/) |
| **Websites & Applications** | Web technology profiling, CMS detection, server headers, and source code reconnaissance. | `0` | [`websites/`](tools/websites/) |
| **Social Media Intelligence** | Platform-specific profiling, follower network graph analysis, post scraping, and temporal tracking. | `0` | [`social-media/`](tools/social-media/) |
| **Image & Forensic Intelligence** | Reverse image search, EXIF metadata extraction, manipulation detection, and visual analysis. | `0` | [`images/`](tools/images/) |
| **Geolocation & Terrain** | IP geolocation, coordinate triangulation, visual terrain matching, and photo location identification. | `0` | [`geolocation/`](tools/geolocation/) |
| **Maps & Geospatial Intelligence** | Satellite imagery analysis, geographic information systems (GIS), mapping tools, and spatial data. | `0` | [`maps/`](tools/maps/) |
| **Metadata Analysis** | Document metadata extraction (PDF, DOCX, XLSX, media), author attribution, and software signatures. | `0` | [`metadata/`](tools/metadata/) |
| **Documents & Public Filings** | Public document scrapers, regulatory filings, government gazettes, and academic paper retrieval. | `0` | [`documents/`](tools/documents/) |
| **Company & Corporate Intelligence** | Corporate registry lookups, beneficial ownership research, financial statements, and business networks. | `0` | [`companies/`](tools/companies/) |
| **Organizations & Entities** | Non-profit records, academic institutions, public bodies, and entity relationship mapping. | `0` | [`organizations/`](tools/organizations/) |
| **Breach & Exposure Intelligence** | Leaked credential queries, exposure verification, paste site indexing, and breach impact analysis. | `0` | [`breach-intelligence/`](tools/breach-intelligence/) |
| **Threat Actor & C2 Intelligence** | Adversary tracking, malicious infrastructure profiling, IOC databases, and malware campaign telemetry. | `0` | [`threat-intelligence/`](tools/threat-intelligence/) |
| **Dark Web & Hidden Services** | Tor onion network indexers, I2P discovery, darknet marketplace monitors, and illicit forum telemetry. | `0` | [`dark-web/`](tools/dark-web/) |
| **Network & IP Intelligence** | Autonomous System (ASN) lookup, BGP routing data, network range discovery, and open port scanning. | `0` | [`network/`](tools/network/) |
| **Infrastructure & Cloud Assets** | Public cloud asset discovery (S3, Azure blobs, GCP buckets), CDN mapping, and SSL certificate reconnaissance. | `0` | [`infrastructure/`](tools/infrastructure/) |
| **Phone Number Intelligence** | Carrier lookups, country dialing analysis, caller identification data, and messaging app footprinting. | `0` | [`phone-numbers/`](tools/phone-numbers/) |
| **Cryptocurrency & Blockchain** | Blockchain ledger explorers, transaction graph tracing, wallet clustering, and smart contract telemetry. | `0` | [`crypto/`](tools/crypto/) |
| **Aviation & Flight Tracking** | ADS-B flight telemetry, aircraft registration lookups, tail number tracing, and flight route history. | `0` | [`aviation/`](tools/aviation/) |
| **Maritime & Vessel Tracking** | AIS ship positioning, maritime fleet databases, port arrivals/departures, and MMSI/IMO resolution. | `0` | [`maritime/`](tools/maritime/) |
| **Vehicle Intelligence** | License plate recognition, vehicle identification number (VIN) checks, and motor registry tools. | `0` | [`vehicles/`](tools/vehicles/) |
| **News & Media Monitoring** | Global news aggregators, RSS feed ingestion, local news search, and media sentiment tracking. | `0` | [`news/`](tools/news/) |
| **Web Archives & Historical Data** | Wayback Machine tools, cached web pages, historical DNS records, and deleted content retrieval. | `0` | [`archives/`](tools/archives/) |
| **Specialized Search Engines & Dorking** | Advanced Google Dorking, IoT/Industrial search engines (Shodan, Censys), and specialized search portals. | `0` | [`search-engines/`](tools/search-engines/) |
| **Workflow Automation & Pipelines** | Multi-tool pipelines, scheduled data collection engines, and automated reconnaissance scripts. | `0` | [`automation/`](tools/automation/) |
| **External Attack Surface Recon** | Broad attack surface management, enterprise perimeter sweeps, and multi-vector target discovery. | `0` | [`reconnaissance/`](tools/reconnaissance/) |
| **Graph Analysis & Visualization** | Entity relationship graphing, link analysis, timeline visualizers, and visual investigation mapping. | `0` | [`visualization/`](tools/visualization/) |
| **Comprehensive OSINT Frameworks** | All-in-one modular platforms, investigation management suites, and unified intelligence frameworks. | `0` | [`investigation-frameworks/`](tools/investigation-frameworks/) |
| **Miscellaneous & Auxiliary Tools** | Format converters, encoding/decoding utilities, timezone calculators, and specialized helper scripts. | `0` | [`miscellaneous/`](tools/miscellaneous/) |
<!-- CATEGORY-TABLE:END -->

---

## 5. Find a Tool (Searchable Index)

Direct index of tools by operational category:

<!-- SEARCH-INDEX:START -->
_Catalog currently empty. As tools are ingested via the contribution protocol, they will be indexed here automatically._
<!-- SEARCH-INDEX:END -->

---

## 6. Tool Matrix

A comparative matrix of tools across interfaces, runtimes, authentication requirements, and maintenance states.

<!-- TOOL-MATRIX:START -->
_No tools cataloged yet. Submit an upstream repository to add the first entry._
<!-- TOOL-MATRIX:END -->

---

## 7. Installation Philosophy

RAVEN does **not** install every tool globally or vendor third-party code as submodules:
1. **Lightweight & Modular**: RAVEN is an indexed catalog and documentation layer. Upstream code is cloned or installed on-demand only when required for an active investigation.
2. **Environment Isolation**: Users are strongly encouraged to deploy tools inside dedicated virtual environments (`venv`, `pipenv`, `conda`) or containerized sandboxes (`Docker`, `Podman`) to prevent dependency conflicts and protect investigator workstations.
3. **No Uncontrolled Vendoring**: Repositories are linked directly to their official upstream creators to preserve provenance, maintainability, and security patching.

---

## 8. Responsible & Lawful Research Boundaries

RAVEN is strictly designed and maintained for **authorized security assessments, law enforcement intelligence, academic research, fraud prevention, and lawful OSINT operations**.

- **Zero Tolerance for Malicious Activity**: Tools cataloged in this repository must not be used for unauthorized system access, credential stuffing, stalking, doxxing, harassment, or mass non-consensual surveillance.
- **No Secret/PII Storage**: Under no circumstances should API keys, session tokens, passwords, or personal identifiable information (PII) be committed to RAVEN.
- **Investigator Responsibility**: Compliance with local and international computer crime statutes (such as the US CFAA, UK Computer Misuse Act, and GDPR) rests entirely with the individual conducting research.

For detailed guidelines and vulnerability reporting, consult [SECURITY.md](SECURITY.md).

---

## 9. Contributing & Integrating Tools

To propose or integrate a new OSINT tool, framework, or utility into RAVEN:
1. Verify it does not already exist using `python scripts/maintenance/check_duplicates.py`.
2. Review the four-step integration protocol in [CONTRIBUTING.md](CONTRIBUTING.md).
3. Ensure schema compliance using `python scripts/maintenance/validate_database.py`.
4. Regenerate repository indexes using `python scripts/maintenance/generate_indexes.py`.
