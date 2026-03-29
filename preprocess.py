#!/usr/bin/env python3
import os
import re

DIRS = [
    "content/imported/tutorials",
    "content/imported/openfoam-adapter",
    "content/imported/aste",
    "content/imported/micro-manager",
    "content/imported/fmi-runner",
    "content/imported/su2-adapter",
    "content/imported/dune-adapter",
    "content/imported/dumux-adapter",
    "content/imported/preeco-orga",
]

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Only replace permalink: inside frontmatter block
    def replace_fm(m):
        return re.sub(r'^permalink:', 'url:', m.group(0), flags=re.MULTILINE)
    
    new_content = re.sub(r'^---.*?^---', replace_fm, content, count=1, flags=re.DOTALL|re.MULTILINE)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  ✅ {filepath}")

def main():
    base = "/home/nishant/LOCAL_DISK_D/2/1"
    for d in DIRS:
        full = os.path.join(base, d)
        if not os.path.isdir(full):
            continue
        for root, _, files in os.walk(full):
            for fname in files:
                if fname.endswith(".md"):
                    fix_file(os.path.join(root, fname))
    print("✨ Done!")

if __name__ == "__main__":
    main()
