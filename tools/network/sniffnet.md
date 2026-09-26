# Sniffnet

> Cross-platform GUI network traffic monitor and packet analysis application.

---

## Purpose
Sniffnet is a multi-threaded network monitoring tool written in Rust that allows investigators to observe and analyze network traffic in real time. It provides visual metrics, autonomous system (ASN) lookups, geographic location profiling for peer IP addresses, and alerts for anomalous network activity through a clean, intuitive graphical interface.

## Category
- **Primary**: Network & IP Intelligence (`network`)
- **Secondary**: Graph Analysis & Visualization (`visualization`), Infrastructure & Cloud Assets (`infrastructure`)

## Interface
- **GUI** (Graphical User Interface)

## Language & Runtime
- **Language**: Rust
- **Platform**: Cross-platform (Linux, Windows, macOS)

## Installation

```bash
# Install via Cargo (Rust package manager)
cargo install sniffnet

# Or install on macOS via Homebrew
brew install sniffnet

# Or install on Windows via winget
winget install GyulyVGC.Sniffnet
```

## Usage

```bash
# Launch Sniffnet GUI application
sniffnet
```

## Common Use Cases
1. **Investigative Machine Traffic Auditing**: Monitoring external connections established by OSINT tools to verify absence of data leakage.
2. **Host IP & ASN Profiling**: Quickly identifying the geographic countries, domain names, and autonomous systems communicating with a target host.
3. **Bandwidth & Connection Telemetry**: Isolating high-bandwidth connections and unauthorized background outbound sockets.

## Input
- Local network adapter selection.

## Output
- Real-time graphical network telemetry, peer IP geolocation summaries, ASN data, and exported pcap capture files.

## Requirements
- **Dependencies**: `libpcap` (Linux/macOS) or `Npcap` (Windows).
- **API Keys**: None required.
- **Account / Authentication**: Elevated privileges (root / Administrator) for packet capture.
- **External Services**: None.

## License
- **License**: MIT License / Apache-2.0

## Source
- **Official Repository**: [https://github.com/GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet)
- **Website / Docs**: [https://sniffnet.net](https://sniffnet.net)

## Status
- **Status**: Active

## RAVEN Notes
Sniffnet provides a polished, visual approach to network traffic analysis without the steep complexity of Wireshark. It is especially useful in an OSINT lab to inspect outbound connections in real time and ensure investigators maintain proper OPSEC.
