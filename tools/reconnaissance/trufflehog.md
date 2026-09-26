# TruffleHog

> High-performance secrets scanner for finding and verifying leaked credentials, private keys, and API tokens across git history, filesystems, and cloud endpoints.

---

## Purpose
TruffleHog is a widely utilized open-source security tool that scans git repositories, commits, branches, filesystems, and S3 buckets for secrets, passwords, private keys, and API tokens. Crucially, TruffleHog actively verifies discovered credentials against their respective service endpoints to determine whether the secret is live or decommissioned.

## Category
- **Primary**: External Attack Surface Recon (`reconnaissance`)
- **Secondary**: Workflow Automation & Pipelines (`automation`), Infrastructure & Cloud Assets (`infrastructure`), Breach & Exposure Intelligence (`breach-intelligence`)

## Interface
- **CLI**

## Language & Runtime
- **Language**: Go (Golang)
- **Platform**: Cross-platform (Linux, Windows, macOS, Docker)

## Installation

```bash
# Install via official shell script
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin

# Or install via Homebrew (macOS/Linux)
brew install trufflehog

# Or install via Go
go install github.com/trufflesecurity/trufflehog/v3@latest
```

## Usage

```bash
# Scan a public or private git repository for secrets
trufflehog git https://github.com/target/repo.git

# Scan an entire GitHub organization
trufflehog github --org=targetorg

# Scan a local filesystem directory
trufflehog filesystem /path/to/target/folder

# Scan an S3 bucket
trufflehog s3 --bucket=target-bucket
```

## Common Use Cases
1. **Developer Code Exposure Reconnaissance**: Scanning target organization GitHub/GitLab repositories for accidentally committed API keys (AWS, OpenAI, Stripe, Slack, private keys).
2. **Credential Verification**: Automatically verifying whether a discovered token is active without manually authenticating against the service.
3. **Attack Surface Discovery**: Uncovering internal endpoints, staging credentials, and infrastructure keys embedded within historical git commits.

## Input
- Git repository URL, GitHub organization name, S3 bucket name, or local directory path.

## Output
- Terminal report and structured JSON output detailing discovered secret type, commit hash, file path, line number, and verification status.

## Requirements
- **Dependencies**: Go 1.20+ or precompiled standalone binary.
- **API Keys**: None required to scan; optional GitHub personal access token for higher API rate limits when scanning organizations.

## License
- **License**: GNU Affero General Public License v3.0 (AGPL-3.0)

## Source
- **Official Repository**: [https://github.com/trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)
- **Website / Docs**: [https://trufflesecurity.com/trufflehog](https://trufflesecurity.com/trufflehog)

## Status
- **Status**: Active

## RAVEN Notes
TruffleHog is essential for attack surface reconnaissance in RAVEN. Unlike generic regex searchers, TruffleHog supports over 700 detector types and performs real-time verification against vendor APIs, eliminating false positives and immediately identifying actionable compromised credentials.
