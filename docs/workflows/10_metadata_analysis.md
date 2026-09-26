# Document & File Metadata Forensics Workflow

## Objective
Forensic extraction, inspection, and analysis of embedded metadata across common document formats (PDF, DOCX, XLSX, PPTX, ODF) to identify authors, editing software, organizations, and document history.

---

## Intelligence Lifecycle

```
TARGET
  │  [Document File: PDF, Office OpenXML, RTF, Image, Audio]
  ▼
DISCOVERY
  │  Identify MIME type, file container structure, and embedded streams
  ▼
ENUMERATION
  │  Extract standard metadata fields (Author, Title, Company, Created/Modified dates)
  ▼
CORRELATION
  │  Decompress internal XML files to uncover revision history, paths, and printers
  ▼
VERIFICATION
  │  Check metadata timestamps against known real-world timeline of events
  ▼
DOCUMENTATION
     Generate forensic metadata summary, diff analysis, and preservation hashes
```

---

### Phase 1: File Integrity & Preservation
1. **Cryptographic Hashing**:
   - Compute SHA-256 and MD5 hashes before opening or inspecting the file.
2. **Forensic Working Copy**:
   - Always perform analysis on a copy of the target file to avoid modifying filesystem access times.

### Phase 2: Standard Metadata Extraction
1. **Core Attributes**:
   - Creator / Author name.
   - Organization / Company name.
   - Operating System / Software version (e.g., Microsoft Word 16.0, Acrobat Distiller).
   - Creation Date, Modification Date, Last Printed Date.
2. **Tooling**:
   - Utilize ExifTool, pdfinfo, and native Office property inspectors.

### Phase 3: Deep Container Forensics (Office OpenXML / PDF)
1. **Office OpenXML (`.docx`, `.xlsx`)**:
   - Unpack zip container (`unzip document.docx -d extracted/`).
   - Inspect `docProps/core.xml` (Dublin Core metadata).
   - Inspect `docProps/app.xml` (Total editing time, word count, application name).
   - Search `word/_rels/` and `word/document.xml` for internal file paths, usernames, and UNC network shares.
2. **PDF Object Stream Inspection**:
   - Scan for incremental updates (`trailer` dictionary objects) that preserve previously deleted or redacted text.
   - Check for embedded attachments or unredacted layers.

### Phase 4: Correlation & Anomaly Detection
1. **Timestamp Anomalies**:
   - Check if Modification Date precedes Creation Date (indicative of manual tampering or timezone shift).
2. **Author Correlation**:
   - Cross-reference extracted usernames with corporate directories, code commits, and email formats.

### Phase 5: Documentation
1. Export full JSON/text metadata dump.
2. Highlight significant forensic findings (internal file paths, usernames, software versions).

---

## Ethical & Legal Boundaries
- Analyze only lawfully acquired documents.
- Respect confidential or privileged information contained in document streams.
