# HackingTool

> All-in-one offensive security toolkit for Linux providing a unified menu-driven interface to install, manage, and launch over 70 penetration testing and hacking utilities.

---

## Purpose
HackingTool is a comprehensive Linux-based offensive security framework that consolidates installation and execution of over 70 popular penetration testing tools into a single interactive menu-driven CLI. It covers the full attacker kill chain — from anonymous surfing and information gathering through exploitation, payload generation, phishing, and post-exploitation — removing the friction of manually installing and managing individual tools.

## Category
- **Primary**: Comprehensive OSINT Frameworks (`investigation-frameworks`)
- **Secondary**: External Attack Surface Recon (`reconnaissance`), Miscellaneous & Auxiliary Tools (`miscellaneous`)

## Interface
- **CLI** (Interactive Menu)

## Language & Runtime
- **Language**: Python 3
- **Platform**: Linux (Kali, Parrot, Ubuntu, Debian)

## Installation

```bash
# Clone the repository
git clone https://github.com/Z4nzu/hackingtool.git
cd hackingtool

# Run the installer (auto-installs Python dependencies)
chmod +x install.sh
sudo bash install.sh
```

## Usage

```bash
# Launch interactive menu
sudo hackingtool

# Or run directly from source
sudo python3 hackingtool.py
```

## Common Use Cases
1. **Penetration Test Setup**: Rapidly bootstrap a full offensive toolkit on a fresh Linux machine without hunting for individual repositories.
2. **Red Team Operations**: Access payload creation, phishing frameworks, and exploitation suites from a single unified launcher.
3. **CTF & Security Training**: Navigate and learn dozens of tools across categories (hash cracking, wireless attack, SQL injection, steganography) in a structured menu environment.

## Input
- Interactive menu selection (no direct target input at the launcher level; each sub-tool accepts its own targets and arguments).

## Output
- Spawns the selected tool's native CLI or interface. Output is tool-specific.

## Requirements
- **Dependencies**: Python 3, `pip`, `git`, and Linux package manager (`apt`). Individual sub-tool dependencies are installed automatically.
- **API Keys**: None required for the launcher itself.
- **Account / Authentication**: None required.
- **External Services**: Downloads tool packages from their upstream GitHub repositories and package managers.

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool)

## Status
- **Status**: Active

## RAVEN Notes
HackingTool functions as a force-multiplier launcher rather than a standalone intelligence tool. It is best deployed on a dedicated Kali or Parrot OS lab machine. While it does not perform OSINT directly, it provides rapid access to information gathering modules (Sherlock, Maltego, Recon-ng) alongside offensive capabilities, making it valuable as a single-pane-of-glass toolkit manager for operators who need to pivot quickly between recon and exploitation phases.
