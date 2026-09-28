

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

* **About**: An open-source email intelligence engine that runs dozens of OSINT modules in parallel across breach databases, social networks, and DNS records to construct a unified identity graph with confidence scores.
* **Who Can Use It**: OSINT Investigators, Corporate Security Analysts, Fraud Examiners, and Penetration Testers.
* **How It Can Be Used**: Trace individual email handles to uncover associated accounts and breach disclosures, or harvest employee email addresses across an entire corporate domain.

```bash
mailaccess investigate target@example.com
# Or harvest domain emails:
mailaccess harvest-emails --domain target.com
```

---

### Image & Forensic Intelligence (`images`)

#### [FaceCheck.ID](https://facecheck.id) — `Web, API` • `Python, Web`
> **AI-powered facial recognition search engine to find social media profiles, news articles, and web appearances by photo.**

* **About**: An AI-powered facial recognition search platform indexing faces from public websites, social media platforms, news articles, video thumbnails, and public mugshot registries.
* **Who Can Use It**: Private Investigators, Cyber Threat Researchers, Due Diligence Analysts, and Anti-Scam Verification Specialists.
* **How It Can Be Used**: Upload an image containing an unidentified face to locate matching public profiles, social accounts, and public record appearances with biometric confidence rankings.

```bash
# Access web interface directly:
# Visit: https://facecheck.id

# Or query via Python API wrapper:
pip install requests
# Upload image and search biometric face matches
```

---

### Metadata Analysis (`metadata`)

#### [Steganography Multi-Tool](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/beginner/steganography-multi-tool) — `CLI` • `Python`
> **Forensic image steganography analyzer and hidden payload detection utility.**

* **About**: A digital image forensics utility designed to detect, encode, and extract concealed textual data and binary streams using Least Significant Bit (LSB) manipulation.
* **Who Can Use It**: Digital Forensics Analysts, Incident Responders, Security Educators, and CTF Competitors.
* **How It Can Be Used**: Inspect suspicious image files recovered during investigations for hidden data, or test covert communications channels in forensic exercises.

```bash
python main.py --decode --image evidence.png
# Encode message:
python main.py --encode --image cover.png --output stego.png --message "Secret"
```

---

### Dark Web & Hidden Services (`dark-web`)

#### [Robin](https://github.com/apurvsinghgautam/robin) — `CLI, Web` • `Python`
> **AI-powered dark web OSINT investigation tool utilizing LLMs for query refinement, intelligent filtering, and onion summarization.**

* **About**: An AI-augmented dark web intelligence tool that pairs Tor search engines with Large Language Models (LLMs) to automatically optimize query syntax, filter noise, and summarize findings.
* **Who Can Use It**: Threat Intelligence Teams, SOC Analysts, Brand Protection Investigators, and Red Teams.
* **How It Can Be Used**: Query dark web search engines using plain language; Robin refines the search with underground jargon, retrieves live onion links, and outputs AI-synthesized briefings.

```bash
# Run Web UI mode via Docker (requires running Tor daemon):
docker run -d -p 5000:5000 --env-file .env apurvsg/robin:latest

# Or CLI investigation:
python robin.py --query "target company credentials" --llm gpt-4
```

#### [TorBot](https://github.com/DedSecInside/TorBot) — `CLI` • `Python`
> **Dark web OSINT crawler, hidden services mapper, and link tree visualizer for the Tor network.**

* **About**: A specialized dark web OSINT crawler designed to safely navigate, index, and analyze .onion hidden services, tracking link graphs and verifying service uptime.
* **Who Can Use It**: Dark Web Threat Analysts, Cybercrime Investigators, Law Enforcement OSINT Teams, and CTI Researchers.
* **How It Can Be Used**: Verify if illicit marketplaces or leak sites are active, crawl dark web nodes recursively, and export relationship link trees for network graph analysis.

```bash
python torbot -u http://<target-service>.onion --status
# Recursive crawl and save link tree:
python torbot -u http://<target-service>.onion --depth 2 --save json
```

---

### Network & IP Intelligence (`network`)

#### [Awesome Networking (Facyber)](https://github.com/facyber/awesome-networking) — `Web` • `Markdown`
> **Curated list of essential computer networking resources, protocols, packet analysis tools, and RFCs.**

* **About**: A curated technical directory of computer networking fundamentals, protocol specifications, RFC standards, packet analysis methodologies, and network troubleshooting tools.
* **Who Can Use It**: Network Engineers, Infrastructure Analysts, Students, and Technical Intelligence Researchers.
* **How It Can Be Used**: Quickly look up protocol header structures, subnetting calculations, and standard networking RFCs when analyzing infrastructure and network telemetry.

```bash
git clone https://github.com/facyber/awesome-networking.git
```

#### [Awesome Networking (Nyquist)](https://github.com/nyquist/awesome-networking) — `Web` • `Markdown`
> **Curated index of modern network engineering tools, libraries, BGP frameworks, and performance analyzers.**

* **About**: An advanced index of modern network engineering tools, high-speed packet capture engines (DPDK, XDP), BGP routing daemons, and internet-scale telemetry systems.
* **Who Can Use It**: Telecommunications Engineers, Cloud Architects, Internet Topology Researchers, and BGP Analysts.
* **How It Can Be Used**: Locate carrier-grade routing tools, Looking Glass servers, and high-performance packet capture libraries when investigating autonomous system (ASN) perimeters.

```bash
git clone https://github.com/nyquist/awesome-networking.git
```

#### [Scapy](https://github.com/secdev/scapy) — `CLI, Library` • `Python`
> **Powerful interactive packet manipulation library and network reconnaissance engine.**

* **About**: The premier Python interactive packet manipulation program capable of forging, decoding, transmitting, and dissecting raw network packets for hundreds of protocols.
* **Who Can Use It**: Network Engineers, Penetration Testers, Security Researchers, and Protocol Reverse Engineers.
* **How It Can Be Used**: Construct custom network probes, audit firewall packet-filtering rules, trace complex network hops, or capture and dissect live promiscuous interface traffic.

```bash
scapy
# Example TCP SYN probe:
>>> sr1(IP(dst="192.168.1.1")/TCP(dport=80, flags="S"), timeout=2)
```

#### [Sniffnet](https://github.com/GyulyVGC/sniffnet) — `GUI` • `Rust`
> **Cross-platform application to monitor and analyze Internet network traffic comfortably and multilingually.**

* **About**: A modern, cross-platform graphical network traffic monitor written in Rust that visualizes live bandwidth, connection channels, peer geographic locations, and autonomous systems.
* **Who Can Use It**: Security Analysts, System Administrators, Network Engineers, and Privacy-Conscious Investigators.
* **How It Can Be Used**: Launch the GUI during investigations to audit outbound network connections from your lab workstation in real time, identify communicating country endpoints, and export pcaps.

```bash
sniffnet
```

---

### Infrastructure & Cloud Assets (`infrastructure`)

#### [Containerlab](https://github.com/srl-labs/containerlab) — `CLI` • `Go`
> **Declarative container-based network lab orchestration system for simulating complex network topologies.**

* **About**: A declarative CLI tool that launches containerized network routing topologies using Docker and Linux namespaces to simulate multi-vendor network hardware (Cisco, Arista, Nokia, FRR).
* **Who Can Use It**: Network Architects, Security Lab Builders, DevOps Engineers, and Red/Blue Teams.
* **How It Can Be Used**: Define target enterprise routing topologies in YAML and spin up simulated hardware appliances locally to validate routing paths and firewall policies harmlessly.

```bash
sudo containerlab deploy --topo topology.clab.yml
# Inspect running topology:
sudo containerlab inspect --all
```

#### [System Design 101](https://github.com/ByteByteGoHq/system-design-101) — `Web` • `Markdown`
> **Comprehensive visual reference and deep-dive compendium for system architecture and large-scale infrastructure design.**

* **About**: A visual encyclopedia by ByteByteGo explaining the inner architecture of large-scale distributed systems, CDNs, microservices, load balancers, and database clusters.
* **Who Can Use It**: Security Architects, Infrastructure Analysts, Technical Investigators, and Systems Engineers.
* **How It Can Be Used**: Study visual blueprints of enterprise web infrastructure (OAuth flows, reverse proxy caching, cloud load balancing) to model target digital perimeters accurately.

```bash
git clone https://github.com/ByteByteGoHq/system-design-101.git
cd system-design-101
```

---

### Aviation & Flight Tracking (`aviation`)

#### [Airplanes.live](https://airplanes.live) — `Web, API` • `Web, API`
> **Community-driven, unfiltered live ADS-B flight tracking platform providing global aircraft telemetry and route histories.**

* **About**: An open, unfiltered flight tracking service powered by a global volunteer ADS-B radio network that provides raw, uncensored telemetry for civil and military aircraft worldwide.
* **Who Can Use It**: Aviation OSINT Researchers, Investigative Journalists, Geopolitical Analysts, and Defense Observers.
* **How It Can Be Used**: Track state VIP transports, military aircraft, and corporate jets by registration or ICAO hex code without censorship, or query the live REST API for regional airframes.

```bash
# Access web radar: https://airplanes.live

# Query aircraft by ICAO hex code:
curl -s "https://api.airplanes.live/v2/hex/a1b2c3" | jq .
```

---

### News & Media Monitoring (`news`)

#### [Security News Scraper](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/intermediate/security-news-scraper) — `CLI` • `Go`
> **Automated cybersecurity news aggregator, RSS harvester, and threat advisory scraper.**

* **About**: A high-performance command-line scraper built in Go that automatically monitors, scrapes, and parses cybersecurity publications and vendor bulletins for CVE disclosures.
* **Who Can Use It**: Threat Intelligence Analysts, Security Operations (SOC) Teams, Vulnerability Managers, and Tech Journalists.
* **How It Can Be Used**: Run scheduled or on-demand sweeps across security news sites to generate structured feeds of zero-day exploits and trending CVE advisories for intelligence reports.

```bash
go run main.go
# Or build standalone binary:
go build -o news-scraper main.go && ./news-scraper
```

---

### External Attack Surface Recon (`reconnaissance`)

#### [TruffleHog](https://github.com/trufflesecurity/trufflehog) — `CLI` • `Go`
> **High-performance secrets scanner for finding and verifying leaked credentials, private keys, and API tokens across git history, filesystems, and cloud endpoints.**

* **About**: A high-speed security scanner that detects secrets, private keys, passwords, and API tokens across git histories, filesystems, and S3 buckets, actively verifying if they are live.
* **Who Can Use It**: AppSec Engineers, External Attack Surface Analysts, Red Teamers, and Penetration Testers.
* **How It Can Be Used**: Scan target organization code repositories and cloud buckets to uncover accidentally exposed credentials and verify active permissions without manual testing.

```bash
# Scan a public git repository for exposed secrets:
trufflehog git https://github.com/target/repo.git

# Scan an entire GitHub organization:
trufflehog github --org=targetorg
```

---

### Comprehensive OSINT Frameworks (`investigation-frameworks`)

#### [Horus](https://github.com/6abd/horus) — `CLI` • `Python`
> **Multi-purpose OSINT and digital forensics assistant for unified artifact investigation and data synthesis.**

* **About**: A unified Python OSINT and digital forensics assistant that combines indicator triage, metadata extraction, steganography checks, and encoding routines in a single shell.
* **Who Can Use It**: Incident Responders, OSINT Analysts, Forensics Investigators, and Security Researchers.
* **How It Can Be Used**: Perform rapid multi-vector triage on unclassified indicators (handles, IP addresses, domains, files) from an interactive CLI before launching specialized heavyweight tools.

```bash
python main.py --target "identifier" --module osint
```

---

### Miscellaneous & Auxiliary Tools (`miscellaneous`)

#### [Multiplayer Networking Resources](https://github.com/0xFA11/MultiplayerNetworkingResources) — `Web` • `Markdown`
> **Comprehensive technical index of real-time UDP network protocols, state synchronization, and packet architectures.**

* **About**: A technical repository compiling architectures, whitepapers, and protocol implementations for real-time UDP communication, packet framing, and state replication.
* **Who Can Use It**: Network Protocol Reverse Engineers, Game Developers, IoT Engineers, and Security Researchers.
* **How It Can Be Used**: Reference low-level socket communication paradigms, lag compensation, and packet serialization when analyzing custom real-time network streams.

```bash
git clone https://github.com/0xFA11/MultiplayerNetworkingResources.git
```

#### [Rveng](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/advanced/rveng) — `CLI` • `Python`
> **Advanced binary analysis and reverse engineering framework for executable inspection and disassembly.**

* **About**: An advanced binary analysis and reverse engineering framework designed to disassemble executable binaries, parse PE/ELF headers, and inspect function tables.
* **Who Can Use It**: Malware Analysts, Reverse Engineers, Forensics Specialists, and Security Students.
* **How It Can Be Used**: Disassemble unknown binary executables recovered during investigations, extract hardcoded C2 strings, and analyze import address tables (IAT) offline.

```bash
python main.py --file target_sample.bin --disassemble
# Inspect PE headers:
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
