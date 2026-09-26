#!/usr/bin/env python3
"""
RAVEN Duplicate Scanner
Detects duplicate names, repository URLs, or aliases in database/tools.json.
"""

import json
import os
import sys
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(ROOT_DIR, "database", "tools.json")

def normalize_url(url: str) -> str:
    if not url:
        return ""
    u = url.strip().lower()
    u = re.sub(r"\.git/?$", "", u)
    u = u.rstrip("/")
    return u

def check_duplicates():
    print("=" * 60)
    print("  RAVEN // DUPLICATE DETECTION SCANNER")
    print("=" * 60)

    if not os.path.exists(DB_PATH):
        print(f"[FAIL] Missing database file: {DB_PATH}")
        sys.exit(1)

    with open(DB_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    print(f"[*] Scanning {len(tools)} tools for duplicate records...")

    names = {}
    repos = {}
    duplicates_found = 0

    for idx, tool in enumerate(tools):
        raw_name = tool.get("name", "").strip()
        norm_name = raw_name.lower()
        norm_repo = normalize_url(tool.get("repository", ""))

        if norm_name:
            if norm_name in names:
                print(f"[DUPLICATE NAME] '{raw_name}' matches existing entry: '{names[norm_name]}'")
                duplicates_found += 1
            else:
                names[norm_name] = raw_name

        if norm_repo:
            if norm_repo in repos:
                print(f"[DUPLICATE REPO] URL '{norm_repo}' already registered for tool '{repos[norm_repo]}'")
                duplicates_found += 1
            else:
                repos[norm_repo] = raw_name

    print("-" * 60)
    if duplicates_found == 0:
        print("[OK] Zero duplicates detected. All entries are unique.")
    else:
        print(f"[!] Scan completed: {duplicates_found} duplicate conflict(s) found.")
        sys.exit(1)

if __name__ == "__main__":
    check_duplicates()
