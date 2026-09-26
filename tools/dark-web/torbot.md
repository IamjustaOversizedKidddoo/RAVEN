# TorBot

> Dark web OSINT crawler, hidden services mapper, and link tree visualizer for the Tor network.

---

## Purpose
TorBot is a specialized dark web intelligence gathering tool designed to crawl, index, and analyze `.onion` hidden services on the Tor network. It automates hidden service discovery, extracts page metadata, tracks hyperlinks between darknet sites, and generates interactive tree graphs illustrating infrastructure relationships across deep web services.

## Category
- **Primary**: Dark Web & Hidden Services (`dark-web`)
- **Secondary**: Graph Analysis & Visualization (`visualization`), Specialized Search Engines & Dorking (`search-engines`), External Attack Surface Recon (`reconnaissance`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Python 3
- **Platform**: Linux, macOS, Docker

## Installation

```bash
# Prerequisites: Ensure Tor service is running locally on port 9050 or 9150
sudo apt update && sudo apt install tor -y
sudo systemctl start tor

# Clone and install TorBot
git clone https://github.com/DedSecInside/TorBot.git
cd TorBot
pip install -r requirements.txt
```

## Usage

```bash
# Basic crawl of a target .onion site with status verification
python torbot -u http://examplehidden.onion --status

# Extract page metadata and title from a hidden service
python torbot -u http://examplehidden.onion --info

# Perform deep recursive crawl and export discovered link relationships to JSON
python torbot -u http://examplehidden.onion --depth 2 --save json
```

## Common Use Cases
1. **Dark Web Infrastructure Mapping**: Crawling and visualizing link dependencies between illicit forums, marketplaces, and paste sites.
2. **Hidden Service Availability Auditing**: Monitoring whether threat actor infrastructure or leak portals remain active or sinkholed.
3. **Threat Intelligence Harvesting**: Extracting title tags, internal page links, and server headers from onion services for IOC generation.

## Input
- Target `.onion` address (V3 hidden service URL).

## Output
- Structured JSON link tree, terminal crawling logs, and interactive visualization files mapping inter-connected onion nodes.

## Requirements
- **Dependencies**: Python 3.8+, Tor SOCKS5 proxy running on `127.0.0.1:9050` (or `9150` with Tor Browser).
- **API Keys**: None required.
- **Account / Authentication**: None required.
- **External Services**: Local or remote Tor routing daemon.

## License
- **License**: GNU General Public License v3.0 (GPL-3.0)

## Source
- **Official Repository**: [https://github.com/DedSecInside/TorBot](https://github.com/DedSecInside/TorBot)

## Status
- **Status**: Active

## RAVEN Notes
TorBot is RAVEN's foundational tool for dark web surface mapping. While general web crawlers cannot resolve `.onion` names without custom routing, TorBot handles SOCKS proxy negotiation natively and provides link graph output that can be piped into network visualization tools. Always maintain strict operational security (OPSEC) when routing traffic over Tor.
