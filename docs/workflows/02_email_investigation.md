# Email Intelligence & Verification Workflow

## Objective
Methodology for analyzing, verifying, and enriching email addresses to determine validity, mail exchange infrastructure, public mentions, and associated digital services without alerting the target.

---

## Intelligence Lifecycle

```
TARGET
  │  [Seed Email Address / Mail Domain]
  ▼
DISCOVERY
  │  Verify MX records, SPF, DKIM, and mailbox deliverability
  ▼
ENUMERATION
  │  Query public registries, code commits, breach disclosures, and public keys
  ▼
CORRELATION
  │  Link to domain ownership, affiliated organizations, and online services
  ▼
VERIFICATION
  │  Perform passive SMTP handshakes without delivering messages
  ▼
DOCUMENTATION
     Export mail exchange telemetry, verification reports, and provenance
```

---

### Phase 1: Target & Format Validation
1. **Syntax Checking**: Confirm RFC 5322 compliance.
2. **Domain Classification**:
   - Corporate/Enterprise domain vs Public webmail (Gmail, Proton, Outlook) vs Disposable/Temp-mail.

### Phase 2: DNS & Mail Exchange Discovery
1. **MX Record Analysis**: Identify hosting provider (Google Workspace, Microsoft 365, self-hosted Postfix).
2. **Security & Authentication Records**:
   - SPF (`v=spf1 ...`) - Inspect authorized sending IP ranges.
   - DMARC (`_dmarc.domain.com`) - Check enforcement policy (`reject`, `quarantine`, `none`).

### Phase 3: Passive Enumeration & Correlation
1. **Public Key Infrastructure**:
   - Query PGP keyservers (OpenPGP, MIT) for email-associated keys and identity packets.
2. **Open Source Repositories**:
   - Search public git repositories for commit author signatures and patch submissions.
3. **Breach Intelligence**:
   - Cross-reference known leak datasets (HaveIBeenPwned API) to assess presence in historical disclosures.

### Phase 4: Mailbox Deliverability Verification
1. **Passive SMTP Simulation**:
   - Initiate SMTP handshake (`HELO/EHLO`, `MAIL FROM`, `RCPT TO`).
   - Observe server response code (`250 OK` = valid mailbox, `550 User unknown` = invalid).
   - Terminate connection with `RST`/`QUIT` before sending payload.
   - Note: Account for catch-all configurations that accept any mailbox.

### Phase 5: Documentation
1. Log SMTP server banners, IP addresses, and response headers.
2. Record all verified public associations.

---

## Ethical & Legal Boundaries
- Never send phishing emails, tracking pixels, or deceptive communication.
- Do not attempt unauthorized mailbox authentication.
