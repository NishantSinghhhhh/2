#!/usr/bin/env python3
import os
import re
import shutil
import glob

BASE = "/home/nishant/LOCAL_DISK_D/2/1"
TUTORIALS_DIR = os.path.join(BASE, "content/imported/tutorials")
STATIC_IMAGES = os.path.join(BASE, "static/images")

def fix_permalinks():
    """Replace permalink: with url: in all markdown frontmatter"""
    for root, _, files in os.walk(TUTORIALS_DIR):
        for fname in files:
            if fname.endswith(".md"):
                filepath = os.path.join(root, fname)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                def replace_fm(m):
                    return re.sub(r'^permalink:', 'url:', m.group(0), flags=re.MULTILINE)
                new_content = re.sub(r'^---.*?^---', replace_fm, content, count=1, flags=re.DOTALL|re.MULTILINE)
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"  ✅ fixed permalink: {fname}")

def copy_images():
    """Copy all tutorial images to static/images"""
    os.makedirs(STATIC_IMAGES, exist_ok=True)
    count = 0
    for img_dir in glob.glob(os.path.join(TUTORIALS_DIR, "*/images")):
        for img in os.listdir(img_dir):
            src = os.path.join(img_dir, img)
            dst = os.path.join(STATIC_IMAGES, img)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                count += 1
    print(f"  📸 copied {count} images to static/images")

if __name__ == "__main__":
    print("🔧 Fixing permalinks...")
    fix_permalinks()
    print("🔧 Copying images...")
    copy_images()
    print("✨ Done!")
