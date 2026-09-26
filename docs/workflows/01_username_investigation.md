# Username Investigation Workflow

## Objective
Standardized methodology for investigating online handles, aliases, and screen names across digital platforms to identify digital footprint, active services, and potential attribution while adhering to lawful intelligence standards.

---

## Intelligence Lifecycle

```
TARGET
  │  [Seed Handle / Alias / Screen Name]
  ▼
DISCOVERY
  │  Identify presence across top-tier platforms, namespaces, and services
  ▼
ENUMERATION
  │  Check profile existence, status codes, response bodies, and API endpoints
  ▼
CORRELATION
  │  Analyze profile artifacts (avatars, bios, location fields, linked accounts)
  ▼
VERIFICATION
  │  Validate account ownership, activity timestamps, and avoid false positives
  ▼
DOCUMENTATION
     Log evidence, archive URLs, compute cryptographic hashes, and export timeline
```

---

### Phase 1: Target Definition & Normalization
1. **Identify Seed Handle**: Record exact string, character case, and special characters (`_`, `.`, `-`).
2. **Handle Variations**:
   - Generate permutations (e.g., prefix `the_`, suffix `_dev`, `_official`, replacement of `0` for `o`).
   - Note common namespace substitutions across regional services.

### Phase 2: Discovery & Enumeration
1. **Automated Namespace Checking**:
   - Run multi-platform checks to query HTTP status codes (`200 OK` vs `404 Not Found`).
   - Filter false-positive soft-404 redirects (e.g., platforms returning 200 with "User not found" HTML).
2. **Platform Categorization**:
   - Code repositories (GitHub, GitLab, Bitbucket).
   - Social networks (X/Twitter, Reddit, LinkedIn).
   - Tech forums and developer communities (Stack Overflow, Hacker News).

### Phase 3: Correlation & Artifact Extraction
1. **Biographical Artifacts**:
   - Display names, location claims, biographical statements.
   - Pinned links, personal domains, portfolio sites.
2. **Visual Footprint**:
   - Avatar image hash extraction (pHash / reverse image search).
   - Unique banners or branding iconography.
3. **Temporal Analysis**:
   - Account creation timestamps.
   - Posting cadence, active timezone indicators.

### Phase 4: Verification & Anti-Impersonation
1. **Cross-Link Validation**: Verify whether Account B links back to Account A (bi-directional confirmation).
2. **Cryptographic Signatures**: Check for verified PGP keys, Keybase proofs, or verified badges.
3. **Activity Consistency**: Compare writing style, language patterns, and technical focus areas.

### Phase 5: Documentation & Evidence Preservation
1. **Web Archival**: Preserve public profiles using trusted archive services or local WARC files.
2. **Hash Verification**: Compute SHA-256 hashes of acquired screenshots and raw HTML responses.
3. **Chronological Logging**: Record findings in the investigation timeline.

---

## Ethical & Legal Boundaries
- Collect only publicly accessible information.
- Do not attempt password resets, credential stuffing, or session hijacking.
- Strictly respect rate limits and terms of service.
