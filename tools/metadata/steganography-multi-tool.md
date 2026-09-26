# Steganography Multi-Tool

> Forensic image steganography analyzer and hidden payload detection utility.

---

## Purpose
Steganography Multi-Tool is an image forensics utility engineered to analyze, detect, and extract concealed textual payloads and hidden binary streams embedded within digital image containers (e.g., PNG, BMP, JPEG) using LSB (Least Significant Bit) manipulation and metadata channel analysis.

## Category
- **Primary**: Metadata Analysis (`metadata`)
- **Secondary**: Image & Forensic Intelligence (`images`), Miscellaneous & Auxiliary Tools (`miscellaneous`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Python 3
- **Platform**: Cross-platform (Linux, Windows, macOS)

## Installation

```bash
# Clone repository
git clone https://github.com/CarterPerez-dev/Cybersecurity-Projects.git
cd Cybersecurity-Projects/PROJECTS/beginner/steganography-multi-tool

# Set up virtual environment and install requirements
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Usage

```bash
# Inspect an image for hidden data
python main.py --decode --image evidence.png

# Encode a secret payload into a carrier image
python main.py --encode --image cover.png --output stego.png --message "Secret payload"
```

## Common Use Cases
1. **Visual Forensic Verification**: Checking suspicious media files encountered in investigations for hidden communications or exfiltrated data.
2. **Watermark and Artifact Inspection**: Validating whether an image has been manipulated with secondary hidden data layers.
3. **CTF and Digital Investigation Education**: Demonstrating steganographic encoding and extraction mechanisms.

## Input
- Carrier image file (`.png`, `.bmp`, `.jpg`).

## Output
- Decoded plain text message, extracted binary files, or generated steganographic carrier images.

## Requirements
- **Dependencies**: Python 3.8+, Pillow (PIL)
- **API Keys**: None required.
- **Account / Authentication**: None required.
- **External Services**: None (operates 100% locally and offline).

## License
- **License**: MIT License

## Source
- **Official Repository**: [https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/beginner/steganography-multi-tool](https://github.com/CarterPerez-dev/Cybersecurity-Projects/tree/main/PROJECTS/beginner/steganography-multi-tool)

## Status
- **Status**: Active

## RAVEN Notes
Steganography Multi-Tool provides essential forensic verification capabilities within RAVEN's metadata section. While ExifTool handles header tags and EXIF data, Steganography Multi-Tool inspects pixel-level color planes and LSB patterns for concealed information, closing a critical gap during visual intelligence triage.
