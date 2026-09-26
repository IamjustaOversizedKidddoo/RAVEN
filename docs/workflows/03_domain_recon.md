# Domain Reconnaissance & Infrastructure Mapping

## Objective
Systematic analysis of an Internet domain name to map organizational ownership, infrastructure dependencies, hosting topology, and historical administrative footprints.

---

## Intelligence Lifecycle

```
TARGET
  │  [Fully Qualified Domain Name (FQDN) / Apex Domain]
  ▼
DISCOVERY
  │  Query WHOIS, RDAP, registrar history, and nameservers
  ▼
ENUMERATION
  │  Map DNS zones, mail infrastructure, IP allocations, and ASN blocks
  ▼
CORRELATION
  │  Correlate shared hosting, IP neighbors, historical SOA, and SSL certificates
  ▼
VERIFICATION
  │  Validate active routing via BGP looking glasses and HTTP responses
  ▼
DOCUMENTATION
     Generate infrastructure graph, registration timeline, and hosting dossiers
```

---

### Phase 1: Registration & Ownership Analysis
1. **RDAP / WHOIS Query**:
   - Inspect registrar identity, creation date, expiration date, and last modified date.
   - Check privacy proxy services vs exposed registrant contact details.
2. **Historical WHOIS**:
   - Review archival registration records to identify pre-GDPR/pre-privacy registrant data.

### Phase 2: DNS & Infrastructure Mapping
1. **Core DNS Records**:
   - A, AAAA (IPv4/IPv6 endpoints).
   - NS (Authoritative nameservers - Cloudflare, AWS Route53, self-hosted BIND).
   - TXT (Site verification tokens: Google, Microsoft, Atlassian, Stripe).
2. **Autonomous System (AS) Profiling**:
   - Determine ASN, BGP prefix announcements, and geographic hosting location.

### Phase 3: Correlation & Shared Infrastructure
1. **Reverse IP Lookups**:
   - Identify virtual hosts sharing the same IP address.
2. **Certificate Transparency (CT)**:
   - Search CT logs (crt.sh) for issued certificates and SANs (Subject Alternative Names).
3. **Analytics & Tracking IDs**:
   - Extract Google Analytics (`UA-`, `G-`), Google Tag Manager (`GTM-`), or AdSense identifiers to find co-owned sites.

### Phase 4: Verification & Documentation
1. Confirm active endpoints with non-intrusive HTTP `HEAD` requests.
2. Export comprehensive network architecture diagrams.

---

## Ethical & Legal Boundaries
- Stick to passive DNS and public registry lookups.
- Avoid unauthorized zone transfer attempts against unpermissioned nameservers.
