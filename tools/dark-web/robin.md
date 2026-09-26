# Robin

> AI-powered dark web OSINT investigation tool utilizing LLMs for query refinement, intelligent filtering, and onion summarization.

---

## Purpose
Robin is an AI-driven dark web intelligence tool designed to accelerate Tor investigations. It connects Large Language Models (LLMs) with dark web search engines to automatically optimize search queries, filter irrelevant links, identify high-priority threat indicators (e.g. leaked databases, credentials), and generate intelligence briefings.

## Category
- **Primary**: Dark Web & Hidden Services (`dark-web`)
- **Secondary**: Specialized Search Engines & Dorking (`search-engines`), External Attack Surface Recon (`reconnaissance`), Threat Actor & C2 Intelligence (`threat-intelligence`)

## Interface
- **CLI**
- **Web** (Docker Web UI)

## Language & Runtime
- **Language**: Python 3
- **Platform**: Linux, Docker, macOS

## Installation

```bash
# Recommended deployment via Docker
docker pull apurvsg/robin:latest

# Clone repository for source installation
git clone https://github.com/apurvsinghgautam/robin.git
cd robin
pip install -r requirements.txt
```

## Usage

```bash
# Run Web UI via Docker (requires running local Tor service)
docker run -d -p 5000:5000 --env-file .env apurvsg/robin:latest

# Or launch CLI investigation
python robin.py --query "target alias or credential dump" --llm gpt-4
```

## Common Use Cases
1. **Threat Actor Profiling**: Searching deep web forums and paste sites for handles, PGP keys, or email aliases with automated LLM summarization.
2. **Breach Data Discovery**: Monitoring hidden marketplaces for mentions of enterprise domain assets or corporate credentials.
3. **Automated Onion Triage**: Filtering noise from dark web search engine results and scoring threat intelligence relevance.

## Input
- Investigation keyword, alias, enterprise domain, or search topic.

## Output
- Ranked onion links, structured summaries, and intelligence briefings.

## Requirements
- **Dependencies**: Python 3.9+, Tor daemon running locally on port `9050`.
- **API Keys**: API key for chosen LLM provider (OpenAI, Anthropic, Gemini) or a local Ollama instance.

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/apurvsinghgautam/robin](https://github.com/apurvsinghgautam/robin)

## Status
- **Status**: Active

## RAVEN Notes
Robin pairs darknet crawling with modern generative AI reasoning. Where tools like TorBot map onion link topologies, Robin interprets and filters page content, drastically reducing investigator fatigue when searching through dark web search engines.
