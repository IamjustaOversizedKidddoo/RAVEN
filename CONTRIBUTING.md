# Contributing to RAVEN

Thank you for contributing to **RAVEN**. To keep the arsenal organized, professional, and searchable, all tool additions must follow this strict 4-step workflow.

---

## Tool Integration System

### STEP 1 — Analyze the Tool
Before writing any documentation, thoroughly inspect the target tool repository:
* **Tool Name**: Exact official name.
* **Description**: Concise, single-sentence summary of primary capability.
* **Primary Category**: Must match one of the 33 categories in `database/categories.json`.
* **Secondary Categories**: Optional related domains.
* **Language & Runtime**: e.g., Python 3, Go, Rust, TypeScript, Bash.
* **Interface**: CLI, Web, GUI, API, Browser Extension, or Library.
* **Platform**: Linux, macOS, Windows, Docker.
* **Installation Method**: Minimal command sequence (pip, git clone, docker, go install).
* **Dependencies & Requirements**: External services, API keys required, local database.
* **Maintenance Status**: Active, Archived, Experimental, or Unknown.
* **License**: Upstream license (e.g., MIT, GPL-3.0, Apache-2.0).

---

### STEP 2 — Duplicate Prevention
Before adding a tool, run the duplicate detection script:

```bash
python scripts/maintenance/check_duplicates.py
```

* Verify that neither the tool name nor the upstream repository URL already exists in `database/tools.json`.
* If the tool already exists, update the existing entry rather than creating a duplicate.

---

### STEP 3 — Source Validation & Attribution
* Always link directly to the **original upstream author/organization**.
* Never link to unofficial mirrors or untrusted forks unless the original repository is deleted and the fork is the community-accepted continuation.
* Never claim authorship of third-party tools.

---

### STEP 4 — Documentation & Database Registration

#### 1. Create the Tool Markdown Entry
If adding a tool to `tools/<category>/`, create `<tool-name>.md` using this exact structure:

```markdown
# [TOOL NAME]

> [One-line concise description of what the tool does.]

## Purpose
[Explain exactly what the tool does, its primary focus, and its strengths.]

## Category
* **Primary:** [Category ID]
* **Secondary:** [Optional secondary categories]

## Interface & Environment
* **Interface:** CLI / Web / GUI / API
* **Language:** Python / Go / Rust / TypeScript
* **Platform:** Linux / macOS / Windows / Docker

## Installation
\`\`\`bash
# Official installation commands
\`\`\`

## Basic Usage
\`\`\`bash
# Minimal working command example
\`\`\`

## Common Use Cases
1. **[Use Case 1]:** [Description]
2. **[Use Case 2]:** [Description]
3. **[Use Case 3]:** [Description]

## Input & Output
* **Input:** [What the user provides: domain, email, username, file, IP]
* **Output:** [What the tool produces: JSON report, CSV, terminal table, graph]

## Requirements & Dependencies
* **API Key Required:** Yes / No
* **Authentication Required:** Yes / No
* **External Services:** [List any required services]

## License & Source
* **License:** [Upstream License]
* **Official Repository:** [GitHub URL]
* **Status:** Active / Archived / Experimental / Unknown

## RAVEN Operational Notes
[Short, practical field notes explaining when an investigator should choose this tool over alternatives.]
```

#### 2. Register in `database/tools.json`
Append the tool record to `database/tools.json` adhering to the master schema.

#### 3. Validate and Update Indexes
Run the automated verification suite:

```bash
# 1. Validate database schema
python scripts/maintenance/validate_database.py

# 2. Verify duplicate prevention
python scripts/maintenance/check_duplicates.py

# 3. Regenerate README statistics
python scripts/maintenance/generate_indexes.py
```
