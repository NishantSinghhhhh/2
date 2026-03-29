#!/usr/bin/env python3
"""
fix_tutorials.py
Replaces 'permalink:' with 'url:' in frontmatter of all README.md files
under imported/tutorials/
"""

import os
import re

TUTORIALS_DIR = "/home/nishant/LOCAL_DISK_D/2/1/content/imported/tutorials"


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    def replace_in_frontmatter(m):
        fm = m.group(0)
        new_fm = re.sub(r'^permalink:', 'url:', fm, flags=re.MULTILINE)
        return new_fm

    new_content = re.sub(r'^---.*?^---', replace_in_frontmatter, content, count=1, flags=re.DOTALL | re.MULTILINE)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  ✅ fixed: {os.path.basename(os.path.dirname(filepath))}/README.md")
    else:
        print(f"  — no change: {os.path.basename(os.path.dirname(filepath))}/README.md")


def main():
    print(f"\n🔧 Replacing 'permalink' with 'url' in all tutorial READMEs\n")

    count = 0
    for entry in sorted(os.scandir(TUTORIALS_DIR), key=lambda e: e.name):
        if entry.is_dir():
            readme = os.path.join(entry.path, "README.md")
            if os.path.isfile(readme):
                fix_file(readme)
                count += 1

    print(f"\n✨ Done! Processed {count} files.")


if __name__ == "__main__":
    main()