#!/usr/bin/env python3
"""
RAVEN Database Validator
Validates database/tools.json schema, categories, and integrity.
"""

import json
import os
import sys
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(ROOT_DIR, "database", "tools.json")
CAT_PATH = os.path.join(ROOT_DIR, "database", "categories.json")

REQUIRED_KEYS = [
    "name",
    "description",
    "category",
    "repository",
    "language",
    "interface",
    "platform",
    "installation",
    "requires_api_key",
    "requires_authentication",
    "paid_dependencies",
    "license",
    "status",
    "tags",
    "added_date",
    "last_verified"
]

VALID_STATUSES = ["Active", "Archived", "Experimental", "Unknown"]

def validate():
    print("=" * 60)
    print("  RAVEN // DATABASE INTEGRITY VALIDATION")
    print("=" * 60)

    if not os.path.exists(DB_PATH):
        print(f"[FAIL] Missing database file: {DB_PATH}")
        sys.exit(1)

    if not os.path.exists(CAT_PATH):
        print(f"[FAIL] Missing categories file: {CAT_PATH}")
        sys.exit(1)

    with open(CAT_PATH, "r", encoding="utf-8") as f:
        categories = json.load(f)
    valid_categories = {c["id"] for c in categories}

    with open(DB_PATH, "r", encoding="utf-8") as f:
        try:
            tools = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[FAIL] Malformed JSON in tools.json: {e}")
            sys.exit(1)

    if not isinstance(tools, list):
        print("[FAIL] tools.json root must be a JSON array.")
        sys.exit(1)

    print(f"[*] Total registered tools: {len(tools)}")
    print(f"[*] Total valid categories: {len(valid_categories)}")

    errors = []
    warnings = []

    for idx, tool in enumerate(tools):
        tname = tool.get("name", f"Entry #{idx+1}")
        
        # Check required keys
        for key in REQUIRED_KEYS:
            if key not in tool:
                errors.append(f"[{tname}] Missing required key: '{key}'")

        # Category check
        cat = tool.get("category")
        if cat and cat not in valid_categories:
            errors.append(f"[{tname}] Invalid category '{cat}'. Must be one of: {sorted(valid_categories)}")

        # Status check
        status = tool.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"[{tname}] Invalid status '{status}'. Must be one of: {VALID_STATUSES}")

        # URL check
        repo = tool.get("repository", "")
        if repo and not (repo.startswith("http://") or repo.startswith("https://")):
            errors.append(f"[{tname}] Invalid repository URL format: '{repo}'")

        # Tags check
        tags = tool.get("tags")
        if not isinstance(tags, list):
            errors.append(f"[{tname}] 'tags' must be a list of strings")

    print("-" * 60)
    if errors:
        print(f"[!] Validation FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"    - {err}")
        sys.exit(1)
    else:
        print("[OK] Database is clean and 100% structurally valid!")

if __name__ == "__main__":
    validate()
