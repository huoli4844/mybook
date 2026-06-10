#!/usr/bin/env python3
"""Check for common issues in Ch3 and Ch4 markdown files."""
import re

files = [
    "/Users/huoli4844/Desktop/电磁兼容教材/output/第3章-电磁骚扰源.md",
    "/Users/huoli4844/Desktop/电磁兼容教材/output/第4章-电磁耦合途径.md",
]

for path in files:
    fname = path.rsplit("/", 1)[-1]
    print(f"\n{'='*60}")
    print(f"Checking: {fname}")
    print('='*60)
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Check equation tag duplicates
    tags = re.findall(r'\\tag\{([^}]+)\}', content)
    tag_counts = {}
    for t in tags:
        tag_counts[t] = tag_counts.get(t, 0) + 1
    dupes = {t: c for t, c in tag_counts.items() if c > 1}
    if dupes:
        print(f"⚠️ DUPLICATE EQUATION TAGS: {dupes}")
    else:
        print(f"✅ No duplicate equation tags ({len(tags)} unique tags)")
    
    # 2. Check for broken LaTeX (unmatched braces)
    # Count standalone braces in math blocks
    math_blocks = re.findall(r'\$\$(.*?)\$\$', content, re.DOTALL)
    math_inline = re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', content)
    
    brace_issues = 0
    for i, block in enumerate(math_blocks):
        open_b = block.count('{')
        close_b = block.count('}')
        if open_b != close_b:
            print(f"⚠️  Math block {i} has {open_b} open vs {close_b} close braces")
            brace_issues += 1
    
    # 3. Check for markdown syntax issues
    # Double section headers
    headers = re.findall(r'^##+\s', content, re.MULTILINE)
    
    # 4. Count lines
    lines = content.split('\n')
    print(f"   File size: {len(lines)} lines, {len(content)} chars")
    
    # 5. Check for chapter structure
    h2_sections = re.findall(r'^##\s+\S', content, re.MULTILINE)
    print(f"   H2 sections: {len(h2_sections)}")
    
    # 6. Check newline before/after equations
    orphan_tags = re.findall(r'(?<!\n)\n\\\\tag\{', content)
    if orphan_tags:
        print(f"   ⚠️ Orphaned equation tags (not on own line)")
    
    # 7. Check for (2-x) old numbering that should be chapter-specific
    old_2x_refs = re.findall(r'\\tag\{2-\d+\}', content)
    if old_2x_refs:
        print(f"   ℹ️ Found {len(old_2x_refs)} tag references from old chapter 2")
    
    # 8. Check for (4-x) tag refs in Ch4
    if "第4章" in fname:
        ch4_tags = re.findall(r'\\tag\{4-\d+\}', content)
        print(f"   Chapter 4 equation tags: {len(ch4_tags)}")
    
    if brace_issues == 0:
        print(f"✅ No brace mismatches in math blocks")

print(f"\n{'='*60}")
print("VALIDATION COMPLETE")
print('='*60)
