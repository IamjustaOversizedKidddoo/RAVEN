#!/usr/bin/env python3
"""
RAVEN Index and Statistics Generator
Computes live category counts and regenerates README tables and indexes from tools.json.
"""

import json
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DB_PATH = os.path.join(ROOT_DIR, 'database', 'tools.json')
CAT_PATH = os.path.join(ROOT_DIR, 'database', 'categories.json')
README_PATH = os.path.join(ROOT_DIR, 'README.md')

def generate():
    print('=' * 60)
    print('  RAVEN // REGENERATING REPOSITORY INDEXES')
    print('=' * 60)

    with open(CAT_PATH, 'r', encoding='utf-8') as f:
        categories = json.load(f)

    with open(DB_PATH, 'r', encoding='utf-8') as f:
        tools = json.load(f)

    # Count tools per category
    counts = {c['id']: 0 for c in categories}
    cat_tools = {c['id']: [] for c in categories}

    for t in tools:
        cat = t.get('category', '')
        if cat in counts:
            counts[cat] += 1
            cat_tools[cat].append(t)

    total_tools = len(tools)
    print(f'[*] Total cataloged tools: {total_tools}')

    # Build category markdown table
    cat_table_rows = [
        '| Category | Focus & Description | Cataloged Tools | Directory |',
        '| :--- | :--- | :---: | :---: |'
    ]

    for c in categories:
        cid = c['id']
        cname = c['name']
        cdesc = c['description']
        cpath = c['path']
        count = counts.get(cid, 0)
        cat_table_rows.append(f'| **{cname}** | {cdesc} | `{count}` | [`{cid}/`]({cpath}/) |')

    cat_table_md = '\n'.join(cat_table_rows)

    # Build Searchable Index
    search_index_rows = []
    has_tools = False
    for c in categories:
        cid = c['id']
        cname = c['name']
        tools_in_cat = cat_tools.get(cid, [])
        if tools_in_cat:
            has_tools = True
            search_index_rows.append(f'### {cname}')
            for t in tools_in_cat:
                tname = t['name']
                tdesc = t['description']
                doc_path = f'tools/{cid}/{tname.lower().replace(" ", "-")}.md'
                search_index_rows.append(f'- **[{tname}]({doc_path})** — {tdesc}')
            search_index_rows.append('')

    if has_tools:
        search_index_md = '\n'.join(search_index_rows)
    else:
        search_index_md = '_Catalog currently empty. As tools are ingested via the contribution protocol, they will be indexed here automatically._'

    # Build Tool Matrix Table
    if tools:
        matrix_rows = [
            '| Tool | Category | Interface | Language | API Key | Status | Repository |',
            '| :--- | :--- | :--- | :--- | :---: | :---: | :--- |'
        ]
        for t in tools:
            name = t.get('name', '')
            cat = t.get('category', '')
            ifaces = ', '.join(t.get('interface', []))
            langs = ', '.join(t.get('language', []))
            api = 'Required' if t.get('requires_api_key') else 'None'
            status = t.get('status', 'Unknown')
            repo = t.get('repository', '')
            matrix_rows.append(f'| **{name}** | `{cat}` | {ifaces} | {langs} | `{api}` | `{status}` | [Source]({repo}) |')
        tool_matrix_md = '\n'.join(matrix_rows)
    else:
        tool_matrix_md = '_No tools cataloged yet. Submit an upstream repository to add the first entry._'

    # Update README if markers exist
    if os.path.exists(README_PATH):
        with open(README_PATH, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace CATEGORY-TABLE
        if '<!-- CATEGORY-TABLE:START -->' in content and '<!-- CATEGORY-TABLE:END -->' in content:
            pre = content.split('<!-- CATEGORY-TABLE:START -->')[0]
            post = content.split('<!-- CATEGORY-TABLE:END -->')[1]
            content = pre + '<!-- CATEGORY-TABLE:START -->\n' + cat_table_md + '\n<!-- CATEGORY-TABLE:END -->' + post

        # Replace SEARCH-INDEX
        if '<!-- SEARCH-INDEX:START -->' in content and '<!-- SEARCH-INDEX:END -->' in content:
            pre = content.split('<!-- SEARCH-INDEX:START -->')[0]
            post = content.split('<!-- SEARCH-INDEX:END -->')[1]
            content = pre + '<!-- SEARCH-INDEX:START -->\n' + search_index_md + '\n<!-- SEARCH-INDEX:END -->' + post

        # Replace TOOL-MATRIX
        if '<!-- TOOL-MATRIX:START -->' in content and '<!-- TOOL-MATRIX:END -->' in content:
            pre = content.split('<!-- TOOL-MATRIX:START -->')[0]
            post = content.split('<!-- TOOL-MATRIX:END -->')[1]
            content = pre + '<!-- TOOL-MATRIX:START -->\n' + tool_matrix_md + '\n<!-- TOOL-MATRIX:END -->' + post

        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print('[OK] README.md updated with live catalog statistics!')

    print('[OK] Index generation complete!')

if __name__ == '__main__':
    generate()
