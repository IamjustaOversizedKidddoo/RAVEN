#!/usr/bin/env python3
"""
RAVEN Quick-Arsenal Generator
Generates clean, direct, copy-paste tool blocks for README.md.
"""

import json
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DB_PATH = os.path.join(ROOT_DIR, "database", "tools.json")
CAT_PATH = os.path.join(ROOT_DIR, "database", "categories.json")
README_PATH = os.path.join(ROOT_DIR, "README.md")

def generate():
    with open(CAT_PATH, "r", encoding="utf-8") as f:
        categories = json.load(f)

    with open(DB_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Group tools by category
    cat_tools = {c["id"]: [] for c in categories}
    cat_names = {c["id"]: c["name"] for c in categories}

    for t in tools:
        cat = t.get("category", "")
        if cat in cat_tools:
            cat_tools[cat].append(t)

    # Build direct, clean tool blocks
    blocks = []
    
    for c in categories:
        cid = c["id"]
        cname = c["name"]
        tlist = cat_tools.get(cid, [])
        if not tlist:
            continue

        blocks.append(f"### {cname} (`{cid}`)\n")
        
        for t in sorted(tlist, key=lambda x: x["name"].lower()):
            name = t["name"]
            repo = t.get("repository", "")
            desc = t.get("description", "")
            ifaces = ", ".join(t.get("interface", []))
            langs = ", ".join(t.get("language", []))
            how_to = t.get("how_to_use", "")
            cmd = t.get("command_example", "")

            badges = f"`{ifaces}` • `{langs}`"
            blocks.append(f"#### [{name}]({repo}) — {badges}")
            blocks.append(f"> **{desc}**\n")
            blocks.append(f"**How to use:** {how_to}\n")
            if cmd:
                blocks.append(f"```bash\n{cmd}\n```\n")
        blocks.append("---\n")

    arsenal_md = "\n".join(blocks).strip()

    # Update README
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        if "<!-- ARSENAL:START -->" in content and "<!-- ARSENAL:END -->" in content:
            pre = content.split("<!-- ARSENAL:START -->")[0]
            post = content.split("<!-- ARSENAL:END -->")[1]
            content = pre + "<!-- ARSENAL:START -->\n" + arsenal_md + "\n<!-- ARSENAL:END -->" + post

            with open(README_PATH, "w", encoding="utf-8") as f:
                f.write(content)
            print("[OK] README.md updated with clean arsenal blocks!")

if __name__ == "__main__":
    generate()
