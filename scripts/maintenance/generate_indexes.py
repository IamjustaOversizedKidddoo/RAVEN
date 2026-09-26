#!/usr/bin/env python3
"""
RAVEN Index and Statistics Generator
Computes live category counts and regenerates README tables and usage blocks from tools.json.
"""

import json
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(ROOT_DIR, "database", "tools.json")
CAT_PATH = os.path.join(ROOT_DIR, "database", "categories.json")
README_PATH = os.path.join(ROOT_DIR, "README.md")

def generate():
    print("=" * 60)
    print("  RAVEN // REGENERATING REPOSITORY INDEXES")
    print("=" * 60)

    with open(CAT_PATH, "r", encoding="utf-8") as f:
        categories = json.load(f)

    with open(DB_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Count tools per category
    counts = {c["id"]: 0 for c in categories}
    cat_tools = {c["id"]: [] for c in categories}

    for t in tools:
        cat = t.get("category", "")
        if cat in counts:
            counts[cat] += 1
            cat_tools[cat].append(t)

    total_tools = len(tools)
    print(f"[*] Total cataloged tools: {total_tools}")

    # Build category markdown table
    cat_table_rows = [
        "| Category | Operational Domain & Focus | Cataloged Tools | Directory |",
        "| :--- | :--- | :---: | :---: |"
    ]

    for c in categories:
        cid = c["id"]
        cname = c["name"]
        cdesc = c["description"]
        cpath = c["path"]
        count = counts.get(cid, 0)
        cat_table_rows.append(f"| **{cname}** | {cdesc} | `{count}` | [`{cid}/`]({cpath}/) |")

    cat_table_md = "\n".join(cat_table_rows)

    # Build Searchable Index with Actionable Usage Blocks
    search_index_rows = []
    has_tools = False
    for c in categories:
        cid = c["id"]
        cname = c["name"]
        tools_in_cat = cat_tools.get(cid, [])
        if tools_in_cat:
            has_tools = True
            search_index_rows.append(f"### {cname}")
            search_index_rows.append("")
            for t in tools_in_cat:
                tname = t["name"]
                tdesc = t["description"]
                repo = t.get("repository", "")
                ifaces = ", ".join(t.get("interface", []))
                langs = ", ".join(t.get("language", []))
                how_to = t.get("how_to_use", "")
                cmd = t.get("command_example", "")

                search_index_rows.append(f"#### [{tname}]({repo})")
                search_index_rows.append(f"- **Purpose**: {tdesc}")
                search_index_rows.append(f"- **Interface / Stack**: `{ifaces}` • `{langs}`")
                search_index_rows.append(f"- **How It Can Be Used**: {how_to}")
                if cmd:
                    search_index_rows.append("```bash")
                    search_index_rows.append(cmd)
                    search_index_rows.append("```")
                search_index_rows.append("")

    if has_tools:
        search_index_md = "\n".join(search_index_rows)
    else:
        search_index_md = "_Catalog currently empty. Submit an upstream repository to add the first entry._"

    # Build Tool Matrix Table (WITHOUT Card, API Key, or Status; WITH How It Can Be Used)
    if tools:
        matrix_rows = [
            "| Tool | Category | Interface | Language | How It Can Be Used | Upstream Source |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |"
        ]
        for t in sorted(tools, key=lambda x: x["name"].lower()):
            name = t.get("name", "")
            cat = t.get("category", "")
            ifaces = ", ".join(t.get("interface", []))
            langs = ", ".join(t.get("language", []))
            how_to = t.get("how_to_use", t.get("description", ""))
            repo = t.get("repository", "")
            matrix_rows.append(f"| **{name}** | `{cat}` | {ifaces} | {langs} | {how_to} | [GitHub Repository]({repo}) |")
        tool_matrix_md = "\n".join(matrix_rows)
    else:
        tool_matrix_md = "_No tools cataloged yet. Submit an upstream repository to add the first entry._"

    # Update README if markers exist
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace CATEGORY-TABLE
        if "<!-- CATEGORY-TABLE:START -->" in content and "<!-- CATEGORY-TABLE:END -->" in content:
            pre = content.split("<!-- CATEGORY-TABLE:START -->")[0]
            post = content.split("<!-- CATEGORY-TABLE:END -->")[1]
            content = pre + "<!-- CATEGORY-TABLE:START -->\n" + cat_table_md + "\n<!-- CATEGORY-TABLE:END -->" + post

        # Replace SEARCH-INDEX
        if "<!-- SEARCH-INDEX:START -->" in content and "<!-- SEARCH-INDEX:END -->" in content:
            pre = content.split("<!-- SEARCH-INDEX:START -->")[0]
            post = content.split("<!-- SEARCH-INDEX:END -->")[1]
            content = pre + "<!-- SEARCH-INDEX:START -->\n" + search_index_md + "\n<!-- SEARCH-INDEX:END -->" + post

        # Replace TOOL-MATRIX
        if "<!-- TOOL-MATRIX:START -->" in content and "<!-- TOOL-MATRIX:END -->" in content:
            pre = content.split("<!-- TOOL-MATRIX:START -->")[0]
            post = content.split("<!-- TOOL-MATRIX:END -->")[1]
            content = pre + "<!-- TOOL-MATRIX:START -->\n" + tool_matrix_md + "\n<!-- TOOL-MATRIX:END -->" + post

        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print("[OK] README.md updated with live catalog statistics and usage blocks!")

    print("[OK] Index generation complete!")

if __name__ == "__main__":
    generate()
