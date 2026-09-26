

```text
██████╗  █████╗ ██╗   ██╗███████╗███╗   ██╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║
██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║
██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
```

> **Fast, actionable OSINT & security research arsenal. Open, search, grab the command, and run.**

[![Status](https://img.shields.io/badge/STATUS-OPERATIONAL-00FF66?style=flat-square&labelColor=0a0a0a)](https://github.com/IamjustaOversizedKidddoo/RAVEN)
[![Tools](https://img.shields.io/badge/CATALOGED%20TOOLS-17-blue?style=flat-square&labelColor=0a0a0a)](database/tools.json)
[![Categories](https://img.shields.io/badge/TAXONOMY-33%20DOMAINS-purple?style=flat-square&labelColor=0a0a0a)](database/categories.json)
[![License](https://img.shields.io/badge/LICENSE-MIT-lightgrey?style=flat-square&labelColor=0a0a0a)](LICENSE)

---

## Quick Navigation

Jump directly to an active category:

<!-- NAV:START -->
[Email Intelligence](#email-intelligence-emails) • [Image & Forensic Intelligence](#image-forensic-intelligence-images) • [Metadata Analysis](#metadata-analysis-metadata) • [Dark Web & Hidden Services](#dark-web-hidden-services-dark-web) • [Network & IP Intelligence](#network-ip-intelligence-network) • [Infrastructure & Cloud Assets](#infrastructure-cloud-assets-infrastructure) • [Aviation & Flight Tracking](#aviation-flight-tracking-aviation) • [News & Media Monitoring](#news-media-monitoring-news) • [External Attack Surface Recon](#external-attack-surface-recon-reconnaissance) • [Comprehensive OSINT Frameworks](#comprehensive-osint-frameworks-investigation-frameworks) • [Miscellaneous & Auxiliary Tools](#miscellaneous-auxiliary-tools-miscellaneous)
<!-- NAV:END -->

---

## The Arsenal

<!-- ARSENAL:START -->
### Email Intelligence (`emails`)

#### [MailAccess](https://github.com/KatrielMoses/MailAccess) — `CLI, Web` • `Python, TypeScript`
> **High-throughput email OSINT investigation toolkit and domain-level mailbox harvesting engine.**

**How to use:** Investigate email addresses across breach databases and social networks to build an identity graph, or harvest all corporate employee emails exposed across a target domain.

```bash
mailaccess investigate target@example.com
# Or harvest domain emails:
mailaccess harvest-emails --domain target.com
```

---

### Image & Forensic Intelligence (`images`)

#### [FaceCheck.ID](https://facecheck.id) — `Web, API` • `Python, Web`
> **AI-powered facial recognition search engine to find social media profiles, news articles, and web appearances by photo.**

**How to use:** Upload a photo of a person to reverse-search facial biometrics across public web pages, social media profiles, news publications, and public registries.

```bash
# Access web interface directly:
# Visit: https://facecheck.id

# Or query via unofficial Python API:
pip install requests
# Upload image and search biometric face matches
```

---

### Metadata Analysis (`metadata`)

#### [Steganography Multi-Tool](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/beginner/steganography-multi-tool) — `CLI` • `Python`
> **Forensic image steganography analyzer and hidden payload detection utility.**

**How to use:** Analyze digital image files (PNG, BMP, JPG) for hidden data, perform LSB analysis, and extract concealed textual payloads or embedded binary streams.

```bash
python main.py --decode --image evidence.png
# Encode message:
python main.py --encode --image cover.png --output stego.png --message "Secret"
```

---

### Dark Web & Hidden Services (`dark-web`)

#### [Robin](https://github.com/apurvsinghgautam/robin) — `CLI, Web` • `Python`
> **AI-powered dark web OSINT investigation tool utilizing LLMs for query refinement, intelligent filtering, and onion summarization.**

**How to use:** Conduct AI-assisted dark web intelligence gathering; Robin uses LLMs (OpenAI, Claude, Gemini, or local Ollama) to rephrase search queries, crawl onion engines, and summarize findings.

```bash
# Run Web UI mode via Docker (requires running Tor daemon):
docker run -d -p 5000:5000 --env-file .env apurvsg/robin:latest

# Or CLI investigation:
python robin.py --query "target alias or keyword" --llm gpt-4
```

#### [TorBot](https://github.com/DedSecInside/TorBot) — `CLI` • `Python`
> **Dark web OSINT crawler, hidden services mapper, and link tree visualizer for the Tor network.**

**How to use:** Crawl and map .onion hidden services, verify live uptime of onion endpoints, and generate interactive link-tree graphs illustrating dark web infrastructure dependencies.

```bash
python torbot -u http://<target-service>.onion --status
# Recursive crawl and save link tree:
python torbot -u http://<target-service>.onion --depth 2 --save json
```

---

### Network & IP Intelligence (`network`)

#### [Awesome Networking (Facyber)](https://github.com/facyber/awesome-networking) — `Web` • `Markdown`
> **Curated list of essential computer networking resources, protocols, packet analysis tools, and RFCs.**

**How to use:** Consult curated reference guides covering protocol specifications (TCP/IP, BGP, OSPF), RFC standards, packet structure, and network troubleshooting utilities.

```bash
git clone https://github.com/facyber/awesome-networking.git
```

#### [Awesome Networking (Nyquist)](https://github.com/nyquist/awesome-networking) — `Web` • `Markdown`
> **Curated index of modern network engineering tools, libraries, BGP frameworks, and performance analyzers.**

**How to use:** Reference modern network engineering libraries, kernel-bypass capture frameworks, and routing daemons when researching large-scale internet topology and BGP routing.

```bash
git clone https://github.com/nyquist/awesome-networking.git
```

#### [Scapy](https://github.com/secdev/scapy) — `CLI, Library` • `Python`
> **Powerful interactive packet manipulation library and network reconnaissance engine.**

**How to use:** Craft custom packet probes (TCP/UDP/ICMP), perform low-level network tracerouting, audit firewall rule boundaries, or sniff and dissect live interface frames.

```bash
scapy
# Example SYN probe:
>>> sr1(IP(dst="192.168.1.1")/TCP(dport=80, flags="S"), timeout=2)
```

#### [Sniffnet](https://github.com/GyulyVGC/sniffnet) — `GUI` • `Rust`
> **Cross-platform application to monitor and analyze Internet network traffic comfortably and multilingually.**

**How to use:** Monitor live network traffic through a cross-platform GUI to analyze connection bandwidth, track peer IP countries, and inspect communicating Autonomous Systems (ASNs).

```bash
sniffnet
```

---

### Infrastructure & Cloud Assets (`infrastructure`)

#### [Containerlab](https://github.com/srl-labs/containerlab) — `CLI` • `Go`
> **Declarative container-based network lab orchestration system for simulating complex network topologies.**

**How to use:** Deploy and manage containerized networking labs (Nokia, Cisco, Arista routers) from declarative YAML files to simulate target enterprise network topologies in Docker.

```bash
sudo containerlab deploy --topo topology.clab.yml
# Inspect running topology:
sudo containerlab inspect --all
```

#### [System Design 101](https://github.com/ByteByteGoHq/system-design-101) — `Web` • `Markdown`
> **Comprehensive visual reference and deep-dive compendium for system architecture and large-scale infrastructure design.**

**How to use:** Study visual architectural blueprints of distributed systems (load balancers, CDN edge caching, reverse proxies, and microservices) to model and analyze enterprise attack surfaces.

```bash
git clone https://github.com/ByteByteGoHq/system-design-101.git
cd system-design-101
```

---

### Aviation & Flight Tracking (`aviation`)

#### [Airplanes.live](https://airplanes.live) — `Web, API` • `Web, API`
> **Community-driven, unfiltered live ADS-B flight tracking platform providing global aircraft telemetry and route histories.**

**How to use:** Track civil, commercial, and military aircraft in real time with unfiltered ADS-B telemetry; search by tail number, ICAO hex code, callsign, or squawk.

```bash
# Open global live flight map:
# Visit: https://airplanes.live

# Query API for a specific aircraft by ICAO hex code:
curl -s "https://api.airplanes.live/v2/hex/a1b2c3" | jq .
```

---

### News & Media Monitoring (`news`)

#### [Security News Scraper](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/security-news-scraper) — `CLI` • `Go`
> **Automated cybersecurity news aggregator, RSS harvester, and threat advisory scraper.**

**How to use:** Scrape, aggregate, and parse the latest cybersecurity news, vendor zero-day advisories, and extracted CVE identifiers into structured feeds for daily threat monitoring.

```bash
go run main.go
# Or build binary:
go build -o news-scraper main.go && ./news-scraper
```

---

### External Attack Surface Recon (`reconnaissance`)

#### [TruffleHog](https://github.com/trufflesecurity/trufflehog) — `CLI` • `Go`
> **High-performance secrets scanner for finding and verifying leaked credentials, private keys, and API tokens across git history, filesystems, and cloud endpoints.**

**How to use:** Scan git repositories, entire GitHub organizations, S3 buckets, or local filesystems to detect and automatically verify live leaked credentials, private keys, and API tokens.

```bash
# Scan a git repository for exposed secrets and verify their validity:
trufflehog git https://github.com/target/repo.git

# Scan an entire GitHub organization:
trufflehog github --org=targetorg

# Scan local directory:
trufflehog filesystem /path/to/target
```

---

### Comprehensive OSINT Frameworks (`investigation-frameworks`)

#### [Horus](https://github.com/6abd/horus) — `CLI` • `Python`
> **Multi-purpose OSINT and digital forensics assistant for unified artifact investigation and data synthesis.**

**How to use:** Perform multi-vector OSINT triage, correlate indicators (usernames, domains, hashes), inspect metadata, and decode suspect artifacts via a unified terminal interface.

```bash
python main.py --target "identifier" --module osint
```

---

### Miscellaneous & Auxiliary Tools (`miscellaneous`)

#### [Multiplayer Networking Resources](https://github.com/0xFA11/MultiplayerNetworkingResources) — `Web` • `Markdown`
> **Comprehensive technical index of real-time UDP network protocols, state synchronization, and packet architectures.**

**How to use:** Analyze low-level UDP socket communication, state synchronization algorithms, and packet serialization when reverse-engineering custom network protocols.

```bash
git clone https://github.com/0xFA11/MultiplayerNetworkingResources.git
```

#### [Rveng](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/advanced/rveng) — `CLI` • `Python`
> **Advanced binary analysis and reverse engineering framework for executable inspection and disassembly.**

**How to use:** Disassemble compiled PE/ELF binaries, analyze import tables and headers, and harvest hardcoded C2 addresses and configuration strings offline during sample triage.

```bash
python main.py --file target_sample.bin --disassemble
# Inspect headers:
python main.py --file target_sample.exe --headers
```

---
<!-- ARSENAL:END -->

---

## Investigation Workflows

Standardized, step-by-step lawful OSINT playbooks:

* [**01: Username Investigation**](docs/workflows/01_username_investigation.md) — Cross-platform handles, profile correlation, and persona clustering.
* [**02: Email Intelligence**](docs/workflows/02_email_investigation.md) — Deliverability verification, mailbox handshakes, and breach checks.
* [**03: Domain Reconnaissance**](docs/workflows/03_domain_recon.md) — WHOIS/RDAP, DNS telemetry, and hosting topology mapping.
* [**04: Subdomain Discovery**](docs/workflows/04_subdomain_discovery.md) — Certificate Transparency, passive DNS, and attack surface enumeration.
* [**05: Image Intelligence**](docs/workflows/05_image_investigation.md) — EXIF extraction, reverse visual search, and shadow chronolocation.
* [**06: Social Media Research**](docs/workflows/06_social_media_research.md) — Follower graph extraction, post timing, and bot detection.
* [**07: Corporate Intelligence**](docs/workflows/07_company_research.md) — Official company registers, regulatory filings, and corporate trees.
* [**08: Geolocation Analysis**](docs/workflows/08_geolocation.md) — Coordinate triangulation, visual terrain matching, and sun angles.
* [**09: Cyber Threat Intelligence**](docs/workflows/09_threat_intelligence.md) — Technical IoC enrichment, C2 infrastructure, and ATT&CK mapping.
* [**10: Document Metadata Forensics**](docs/workflows/10_metadata_analysis.md) — Container forensics, author tracking, and internal XML inspection.

---

## Fast Search from Terminal

Search your local catalog instantly without opening a browser:

```bash
# Search by tag
python scripts/utilities/query_tools.py --tag dark-web

# Search by category
python scripts/utilities/query_tools.py --category emails

# Search by keyword
python scripts/utilities/query_tools.py --keyword traffic

# Catalog overview
python scripts/utilities/query_tools.py --stats
```

---

## How to Add Tools

Whenever you find a useful OSINT repository, tool, or script:
1. Provide the GitHub URL.
2. RAVEN automatically categorizes it, adds the copy-paste command, and updates the index.
