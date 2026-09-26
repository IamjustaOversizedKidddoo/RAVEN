# Subdomain Enumeration & Surface Mapping

## Objective
Comprehensive identification of valid subdomains belonging to a target organization to understand external attack surface, exposed environments, and shadow IT assets.

---

## Intelligence Lifecycle

```
TARGET
  │  [Root Domain Name]
  ▼
DISCOVERY
  │  Query Certificate Transparency logs, search engine dorks, and web archives
  ▼
ENUMERATION
  │  Passive aggregation from threat intelligence feeds and DNS datasets
  ▼
CORRELATION
  │  Map CNAME aliases, cloud hosting buckets (S3, Azure Blob), and CDNs
  ▼
VERIFICATION
  │  Resolve hosts, detect wildcard DNS configurations, and verify active status
  ▼
DOCUMENTATION
     Generate asset inventory table with IPs, CNAME chains, and HTTP status codes
```

---

### Phase 1: Passive Aggregation
1. **Certificate Transparency (CT)**:
   - Query crt.sh, Censys, and Certspotter for all historical and active certificates.
2. **Search Engine Indexing**:
   - Utilize search dorks: `site:example.com -www.example.com`.
3. **Passive DNS Databases**:
   - Query VirusTotal, SecurityTrails, AlienVault OTX, and DNSDumpster.

### Phase 2: Active & Permutative Enumeration (Authorized Only)
1. **Targeted Wordlist Resolution**:
   - Resolve high-probability environment prefixes (`dev`, `staging`, `vpn`, `api`, `internal`, `test`).
2. **Wildcard Detection**:
   - Resolve random non-existent UUID hostnames (`random-xyz-test.example.com`).
   - If returned with an A record, filter out wildcard entries.

### Phase 3: Infrastructure & CNAME Verification
1. **CNAME Canonical Names**:
   - Identify dangling CNAME pointers pointing to decommissioned services (GitHub Pages, AWS S3, Heroku).
2. **Service Classification**:
   - Flag administration panels, login portals, development staging servers, and remote desktop endpoints.

### Phase 4: Documentation
1. Export structured CSV/JSON with hostname, IP, CNAME, and HTTP status code.

---

## Ethical & Legal Boundaries
- Perform active brute-forcing only within an authorized scope of engagement.
- Passive enumeration requires no direct packet transmission to target infrastructure.
