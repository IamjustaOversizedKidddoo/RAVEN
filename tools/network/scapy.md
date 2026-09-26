# Scapy

> Powerful interactive packet manipulation library, packet generator, and network reconnaissance engine.

---

## Purpose
Scapy is a Python-based packet manipulation program and library capable of forging or decoding packets of a wide number of protocols, sending them on the wire, capturing them, matching requests and replies, and much more. It can easily handle tasks like network scanning, tracerouting, probing, unit tests, attacks, or network discovery.

## Category
- **Primary**: Network & IP Intelligence (`network`)
- **Secondary**: External Attack Surface Recon (`reconnaissance`), Infrastructure & Cloud Assets (`infrastructure`)

## Interface
- **CLI**
- **Library** (Python Module)

## Language & Runtime
- **Language**: Python 3
- **Platform**: Cross-platform (Linux, Windows, macOS)

## Installation

```bash
# Recommended installation via pip
pip install scapy

# For full feature set (cryptography, plotting, 2D/3D graphics)
pip install scapy[basic]
```

## Usage

```bash
# Launch Scapy interactive shell
scapy

# Basic Python script example for TCP SYN scanning
from scapy.all import IP, TCP, sr1

target = "192.168.1.1"
syn_packet = IP(dst=target)/TCP(dport=80, flags="S")
response = sr1(syn_packet, timeout=2)

if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
    print(f"Port 80 is OPEN on {target}")
```

## Common Use Cases
1. **Low-Level Network Reconnaissance**: Forging custom ICMP, TCP, and UDP probe packets to fingerprint network devices and firewalls.
2. **Network Protocol Auditing**: Dissecting proprietary or obscure protocol frames during technical intelligence operations.
3. **Passive Network Sniffing**: Inspecting raw network traffic on promiscuous interfaces and writing pcap captures.

## Input
- IP addresses, target subnets, or raw pcap files.

## Output
- Captured packets, response dissects, graphical traceroute plots, and pcap traces.

## Requirements
- **Dependencies**: Python 3.8+, `libpcap` (Linux) or `Npcap` (Windows).
- **API Keys**: None required.
- **Account / Authentication**: Elevated privileges (root / Administrator) for raw socket access.
- **External Services**: Local network interfaces.

## License
- **License**: GNU General Public License v2.0 (GPL-2.0)

## Source
- **Official Repository**: [https://github.com/secdev/scapy](https://github.com/secdev/scapy)
- **Website / Docs**: [https://scapy.net](https://scapy.net)

## Status
- **Status**: Active

## RAVEN Notes
Scapy is the gold standard for custom network packet fabrication and forensic protocol analysis. Within RAVEN, use Scapy when off-the-shelf scanners like Nmap cannot construct the specific low-level probe packets or protocol permutations required for your investigation.
