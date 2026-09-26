# Rveng

> Advanced binary analysis, disassembly, and reverse engineering engine for executable inspection.

---

## Purpose
Rveng is an advanced reverse engineering project from the Cybersecurity-Projects portfolio designed to analyze compiled binary executables, disassemble machine instructions, parse PE/ELF headers, and identify embedded functions, strings, and suspicious imports during forensic investigations.

## Category
- **Primary**: Miscellaneous & Auxiliary Tools (`miscellaneous`)
- **Secondary**: Metadata Analysis (`metadata`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Python 3
- **Platform**: Cross-platform (Linux, Windows)

## Installation

```bash
# Clone repository
git clone https://github.com/CarterPerez-dev/Cybersecurity-Projects.git
cd Cybersecurity-Projects/PROJECTS/advanced/rveng

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Analyze a compiled binary executable
python main.py --file target_sample.bin --disassemble

# Extract strings and header metadata
python main.py --file target_sample.exe --headers
```

## Common Use Cases
1. **Malicious Sample Triage**: Disassembling unknown executable binaries recovered during digital forensic investigations.
2. **Header & Timestamp Extraction**: Inspecting binary compilation timestamps, rich headers, and import address tables (IAT).
3. **Embedded String Harvesting**: Extracting hardcoded C2 IP addresses, domains, and configuration strings from compiled binaries.

## Input
- Binary executable file (PE, ELF, or raw binary stream).

## Output
- Disassembly listings, control flow data, extracted strings, and header inspection reports.

## Requirements
- **Dependencies**: Python 3.8+, Capstone / pefile.
- **API Keys**: None required.
- **Account / Authentication**: None required.
- **External Services**: None (runs completely offline).

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/advanced/rveng](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/advanced/rveng)

## Status
- **Status**: Active

## RAVEN Notes
Rveng fills the technical reverse-engineering niche in RAVEN's auxiliary armory. When an OSINT investigation uncovers an unknown binary file or dropper from an adversary infrastructure node, Rveng provides local, offline disassembly and string extraction without uploading samples to third-party multiscanners.
