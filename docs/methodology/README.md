# OSINT Investigation Methodology

RAVEN structures open-source intelligence collection around the standardized **Intelligence Cycle**.

```text
    ┌────────────────────────┐
    │ 1. PLANNING & DIRECTION│  Define scope, targets, and legal boundaries.
    └───────────┬────────────┘
                │
    ┌───────────▼────────────┐
    │ 2. TARGET DISCOVERY    │  Broad reconnaissance & perimeter identification.
    └───────────┬────────────┘
                │
    ┌───────────▼────────────┐
    │ 3. ENUMERATION & HARVEST  Deep queries (usernames, DNS, metadata, records).
    └───────────┬────────────┘
                │
    ┌───────────▼────────────┐
    │ 4. CORRELATION & PIVOT │  Cross-referencing entities, graph linking, timelines.
    └───────────┬────────────┘
                │
    ┌───────────▼────────────┐
    │ 5. VERIFICATION & REPORT  Multi-source validation, confidence scoring, reporting.
    └────────────────────────┘
```

## Core Principles
1. **Source Redundancy:** Never rely on a single data point. Confirm findings across at least two independent platforms.
2. **Operational Security (OPSEC):** Match collection intensity to threat level. Never query target-controlled infrastructure without proper isolation and authorization.
3. **Defensive Telemetry:** Understand what artifacts your queries leave behind (e.g. DNS queries, web server access logs, social media view notifications).
