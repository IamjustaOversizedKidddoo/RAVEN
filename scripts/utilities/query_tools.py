#!/usr/bin/env python3
"""
RAVEN Catalog Query Utility
Fast command-line search tool to query database/tools.json by category, tag, interface, or keyword.

Usage:
    python query_tools.py --category usernames
    python query_tools.py --tag recon
    python query_tools.py --keyword "social media"
    python query_tools.py --stats
"""

import argparse
import json
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(ROOT_DIR, "database", "tools.json")
CAT_PATH = os.path.join(ROOT_DIR, "database", "categories.json")

def load_data():
    if not os.path.exists(DB_PATH):
        print(f"[!] Database file not found: {DB_PATH}")
        sys.exit(1)
    with open(DB_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)
    categories = []
    if os.path.exists(CAT_PATH):
        with open(CAT_PATH, "r", encoding="utf-8") as f:
            categories = json.load(f)
    return tools, categories

def display_tool(t):
    name = t.get("name", "Unknown")
    desc = t.get("description", "")
    cat = t.get("category", "")
    ifaces = ", ".join(t.get("interface", []))
    langs = ", ".join(t.get("language", []))
    repo = t.get("repository", "")
    status = t.get("status", "Unknown")
    api = "Required" if t.get("requires_api_key") else "None"
    tags = ", ".join(t.get("tags", []))

    print(f"\n{'=' * 60}")
    print(f"  TOOL: {name}  [{status}]")
    print(f"{'=' * 60}")
    print(f"  Description : {desc}")
    print(f"  Category    : {cat}")
    print(f"  Interface   : {ifaces}")
    print(f"  Language    : {langs}")
    print(f"  API Key     : {api}")
    print(f"  Tags        : {tags}")
    print(f"  Repository  : {repo}")

def main():
    parser = argparse.ArgumentParser(description="RAVEN OSINT Catalog Query Engine")
    parser.add_argument("--category", "-c", help="Filter by primary category ID (e.g. usernames, emails)")
    parser.add_argument("--tag", "-t", help="Filter by tag (e.g. recon, breach, dork)")
    parser.add_argument("--interface", "-i", help="Filter by interface (e.g. CLI, Web, GUI, API)")
    parser.add_argument("--keyword", "-k", help="Search name and description for a keyword")
    parser.add_argument("--stats", "-s", action="store_true", help="Display catalog summary statistics")
    args = parser.parse_args()

    tools, categories = load_data()

    if args.stats or len(sys.argv) == 1:
        print("=" * 60)
        print("  RAVEN // CATALOG STATISTICS")
        print("=" * 60)
        print(f"  Total Categories : {len(categories)}")
        print(f"  Total Tools      : {len(tools)}")
        if not tools:
            print("  Status           : Catalog ready for tool ingestion.")
        return

    results = []
    for t in tools:
        match = True
        if args.category and t.get("category", "").lower() != args.category.lower():
            match = False
        if args.tag:
            tags = [x.lower() for x in t.get("tags", [])]
            if args.tag.lower() not in tags:
                match = False
        if args.interface:
            ifaces = [x.lower() for x in t.get("interface", [])]
            if args.interface.lower() not in ifaces:
                match = False
        if args.keyword:
            kw = args.keyword.lower()
            name = t.get("name", "").lower()
            desc = t.get("description", "").lower()
            if kw not in name and kw not in desc:
                match = False
        if match:
            results.append(t)

    print(f"[*] Found {len(results)} matching tool(s).")
    for r in results:
        display_tool(r)

if __name__ == "__main__":
    main()
