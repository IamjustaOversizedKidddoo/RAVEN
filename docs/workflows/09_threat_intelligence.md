# Cyber Threat Intelligence (CTI) & Indicator Enrichment

## Objective
Structured process for analyzing and enriching technical Indicators of Compromise (IoCs)—including IP addresses, domains, file hashes, and TLS certificates—to track adversary infrastructure and campaigns.

---

## Intelligence Lifecycle

```
TARGET
  │  [Indicator of Compromise: IP, Domain, Hash, URL, JA3/JA4 Fingerprint]
  ▼
DISCOVERY
  │  Query passive DNS, reputation feeds, WHOIS history, and malware repositories
  ▼
ENUMERATION
  │  Extract related network infrastructure, SSL certs, ASN routes, and samples
  ▼
CORRELATION
  │  Map to MITRE ATT&CK techniques, known threat actor TTPs, and campaign activity
  ▼
VERIFICATION
  │  Filter out sinkholes, CDN edge nodes, security scanner IPs, and false positives
  ▼
DOCUMENTATION
     Produce STIX/JSON bundle, infrastructure graph, and actionable briefing
```

---

### Phase 1: Indicator Categorization
1. **Network Indicators**: IPv4, IPv6, FQDN, URI.
2. **File Artifacts**: MD5, SHA-1, SHA-256, SSDEEP, TLSH.
3. **Cryptographic & Protocol**: SSL/TLS SHA-1 thumbprint, JA3/JA4 hash, JARM hash.

### Phase 2: Enrichment & Contextualization
1. **Multi-Engine Scanners**:
   - VirusTotal, AlienVault OTX, AbuseIPDB, ThreatFox, URLhaus.
2. **Passive DNS & Historical Telemetry**:
   - Track previous domain resolutions and shared hosting timelines.
3. **Certificate Graphing**:
   - Track malicious infrastructure sharing identical self-signed certificates or serial numbers.

### Phase 3: Campaign & Adversary Correlation
1. **MITRE ATT&CK Mapping**:
   - Correlate observed behavior with tactics, techniques, and procedures (TTPs).
2. **Infrastructure Overlap**:
   - Identify common registrants, naming conventions, dynamic DNS providers, or bulletproof hosters.

### Phase 4: False Positive Filtering
1. Identify and exclude:
   - Major CDN/cloud edge providers (Cloudflare, Akamai, CloudFront).
   - Legitimate public DNS resolvers (8.8.8.8, 1.1.1.1).
   - Active security vendor sinkholes.

### Phase 5: Reporting & Dissemination
1. Export structured IoC lists with threat levels, confidence scores, and context tags.

---

## Ethical & Legal Boundaries
- Strictly adhere to authorized CTI collection.
- Never directly interact with or compromise adversary command-and-control (C2) servers.
