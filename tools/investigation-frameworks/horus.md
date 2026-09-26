# Horus

> Multi-purpose OSINT and digital forensics assistant for unified artifact investigation and data synthesis.

---

## Purpose
Horus (formerly Sentinel) is a modular OSINT and digital forensics CLI assistant built to streamline multi-vector investigations. It centralizes common investigative routines—including entity correlation, geographic data parsing, forensic decoding, steganographic inspection, and API orchestration—into a single command-line interface.

## Category
- **Primary**: Comprehensive OSINT Frameworks (`investigation-frameworks`)
- **Secondary**: Metadata Analysis (`metadata`), Geolocation & Terrain (`geolocation`), External Attack Surface Recon (`reconnaissance`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Python 3
- **Platform**: Cross-platform (Linux, macOS, Windows)

## Installation

```bash
# Clone repository from upstream
git clone https://github.com/6abd/horus.git
cd horus

# Install required dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Launch interactive terminal shell
python main.py

# Query target information using specific modules
python main.py --target "identifier" --module osint
```

## Common Use Cases
1. **Multi-Vector Entity Profiling**: Conducting rapid reconnaissance across disparate data sources without juggling independent one-off scripts.
2. **Artifact Decoding & Triage**: Performing cryptographic, encoding, and forensic checks on unidentified files or strings recovered during investigations.
3. **Forensic Steganography & Location Validation**: Inspecting suspect images for hidden coordinates and embedded data payloads.

## Input
- Target indicators (domains, usernames, hashes, image files, or encoded strings).

## Output
- Terminal data dumps, decoded strings, extracted EXIF/metadata summaries, and reconnaissance logs.

## Requirements
- **Dependencies**: Python 3.8+
- **API Keys**: Optional for specialized external enrichment modules; core modules operate locally.
- **Account / Authentication**: None required.
- **External Services**: Open intelligence endpoints depending on activated module.

## License
- **License**: GNU General Public License v3.0 (GPL-3.0)

## Source
- **Official Repository**: [https://github.com/6abd/horus](https://github.com/6abd/horus)

## Status
- **Status**: Active

## RAVEN Notes
Horus functions as a lightweight, Swiss-Army-knife investigation assistant within RAVEN. Use Horus when you need rapid triage across multiple technical facets (metadata, basic forensics, initial recon) before escalating to specialized deep-dive tools like SpiderFoot or Maltego.
