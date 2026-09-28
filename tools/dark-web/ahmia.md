# Ahmia

> Clearnet and Tor-accessible search engine for indexing, discovering, and querying .onion hidden services on the Tor network.

---

## Purpose
Ahmia is an open-source, publicly accessible search engine purpose-built for the Tor dark web. Unlike general web crawlers that cannot resolve `.onion` addresses, Ahmia indexes hidden services through its own Scrapy-based crawler, stores results in an Elasticsearch backend, and serves them through a Django web interface accessible on both the clearnet (ahmia.fi) and via a `.onion` mirror. It applies filtering to block abusive content from appearing in results, making it the most widely used legitimate Tor search engine for threat intelligence and dark web OSINT research.

## Category
- **Primary**: Dark Web & Hidden Services (`dark-web`)
- **Secondary**: Specialized Search Engines & Dorking (`search-engines`), External Attack Surface Recon (`reconnaissance`)

## Interface
- **Web** (clearnet and .onion)
- **CLI** (self-hosted via Docker/Django)

## Language & Runtime
- **Language**: Python (Django), Scrapy, Elasticsearch
- **Platform**: Linux, Docker

## Installation

```bash
# Self-host the full Ahmia stack (site + crawler + index)

# 1. Clone and run the Django search frontend
git clone https://github.com/ahmia/ahmia-site.git
cd ahmia-site
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# 2. Clone and run the Scrapy crawler separately
git clone https://github.com/ahmia/ahmia-crawler.git
cd ahmia-crawler
pip install -r requirements.txt

# 3. Set up Elasticsearch index
git clone https://github.com/ahmia/ahmia-index.git
cd ahmia-index
# Follow README for Elasticsearch configuration
```

## Usage

```bash
# Use the public web interface (no install needed):
# Clearnet: https://ahmia.fi
# Tor .onion: http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion

# Query the Ahmia API for .onion search results:
curl "https://ahmia.fi/search/?q=target+keyword" 

# Self-hosted search via Django dev server:
python manage.py runserver
# Then visit: http://127.0.0.1:8000/search/?q=your+query
```

## Common Use Cases
1. **Threat Intelligence Harvesting**: Search for references to target organizations, leaked credentials, or infrastructure indicators across indexed dark web sites.
2. **Dark Web Surface Mapping**: Discover active `.onion` services in a specific topic area (markets, forums, paste sites) without running your own full crawler.
3. **Self-Hosted Intelligence Platform**: Deploy Ahmia's full stack (site + crawler + index) internally to build a private, filtered dark web search index for a threat intelligence team.

## Input
- Plain-language or keyword search queries via web interface or REST API.

## Output
- Paginated list of matching `.onion` service URLs with page titles and descriptions; API returns structured JSON results.

## Requirements
- **Dependencies** (self-hosted): Python 3.8+, Django 3.x, Scrapy, Elasticsearch 7.x, Tor daemon.
- **API Keys**: None required.
- **Account / Authentication**: None required for public instance.
- **External Services**: Public instance uses ahmia.fi; self-hosted requires a running Elasticsearch cluster and Tor SOCKS proxy.

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/ahmia](https://github.com/ahmia) (org — ahmia-site, ahmia-crawler, ahmia-index)
- **Website / Docs**: [https://ahmia.fi](https://ahmia.fi)

## Status
- **Status**: Active

## RAVEN Notes
Ahmia is RAVEN's recommended entry point for structured dark web keyword searches. It occupies a distinct niche from crawlers like TorBot: where TorBot traverses link graphs from a known seed URL, Ahmia provides keyword-driven discovery across a pre-indexed corpus of thousands of onion services. For investigators without access to a Tor Browser, ahmia.fi is reachable directly over the clearnet. Always maintain OPSEC when following returned `.onion` links — use Tor Browser or a properly configured SOCKS5 proxy, never a direct connection.
