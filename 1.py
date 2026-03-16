#!/usr/bin/env python3
"""
Bootstrap 3 to Bootstrap 5 Migration Script
For preCICE website (Hugo)
"""

import os
import re
import sys
import shutil
import argparse

# File extensions to process
EXTENSIONS = {'.html', '.css', '.js', '.md', '.yml', '.yaml'}

# Backup extension
BACKUP_EXT = '.bs3bak'

# ─────────────────────────────────────────────
# REPLACEMENTS: (pattern, replacement, is_regex)
# ─────────────────────────────────────────────
REPLACEMENTS = [

    # ── CDN links ──────────────────────────────────────────────────────────
    (r'https://maxcdn\.bootstrapcdn\.com/bootstrap/3[\d.]+/css/bootstrap\.min\.css',
     'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css', True),
    (r'https://maxcdn\.bootstrapcdn\.com/bootstrap/3[\d.]+/js/bootstrap\.min\.js',
     'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js', True),
    (r'https://stackpath\.bootstrapcdn\.com/bootstrap/3[\d.]+/css/bootstrap\.min\.css',
     'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css', True),
    (r'https://stackpath\.bootstrapcdn\.com/bootstrap/3[\d.]+/js/bootstrap\.min\.js',
     'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js', True),

    # ── data-* attributes ──────────────────────────────────────────────────
    (r'\bdata-toggle=', 'data-bs-toggle=', False),
    (r'\bdata-target=', 'data-bs-target=', False),
    (r'\bdata-dismiss=', 'data-bs-dismiss=', False),
    (r'\bdata-ride=', 'data-bs-ride=', False),
    (r'\bdata-slide=', 'data-bs-slide=', False),
    (r'\bdata-slide-to=', 'data-bs-slide-to=', False),
    (r'\bdata-spy=', 'data-bs-spy=', False),
    (r'\bdata-offset=', 'data-bs-offset=', False),
    (r'\bdata-parent=', 'data-bs-parent=', False),

    # ── Navbar ─────────────────────────────────────────────────────────────
    (r'\bnavbar-inverse\b', 'navbar-dark bg-dark', False),
    (r'\bnavbar-static-top\b', 'sticky-top', False),
    (r'\bnavbar-fixed-top\b', 'fixed-top', False),
    (r'\bnavbar-fixed-bottom\b', 'fixed-bottom', False),
    (r'\bnavbar-right\b', 'ms-auto', False),
    (r'\bnavbar-left\b', 'me-auto', False),
    (r'\bnavbar-toggle\b', 'navbar-toggler', False),
    (r'\bnavbar-collapse\b', 'navbar-collapse', False),
    (r'\bnavbar-header\b', 'navbar-header', False),  # keep but flag
    (r'\bnavbar-form\b', 'navbar-form', False),

    # ── Grid ───────────────────────────────────────────────────────────────
    (r'\bcol-xs-(\d+)\b', r'col-\1', True),
    (r'\bcol-xs-offset-(\d+)\b', r'offset-\1', True),
    (r'\bcol-sm-offset-(\d+)\b', r'offset-sm-\1', True),
    (r'\bcol-md-offset-(\d+)\b', r'offset-md-\1', True),
    (r'\bcol-lg-offset-(\d+)\b', r'offset-lg-\1', True),

    # ── Buttons ────────────────────────────────────────────────────────────
    (r'\bbtn-default\b', 'btn-secondary', False),
    (r'\bbtn-xs\b', 'btn-sm', False),

    # ── Panel → Card ───────────────────────────────────────────────────────
    (r'\bpanel-default\b', 'card', False),
    (r'\bpanel-primary\b', 'card border-primary', False),
    (r'\bpanel-success\b', 'card border-success', False),
    (r'\bpanel-info\b', 'card border-info', False),
    (r'\bpanel-warning\b', 'card border-warning', False),
    (r'\bpanel-danger\b', 'card border-danger', False),
    (r'\bpanel-heading\b', 'card-header', False),
    (r'\bpanel-body\b', 'card-body', False),
    (r'\bpanel-footer\b', 'card-footer', False),
    (r'\bpanel-title\b', 'card-title', False),
    (r'\bpanel\b', 'card', False),

    # ── Well → Card ────────────────────────────────────────────────────────
    (r'\bwell\b', 'card card-body', False),
    (r'\bthumbnail\b', 'card', False),

    # ── Labels/Badges ──────────────────────────────────────────────────────
    (r'\blabel-default\b', 'badge bg-secondary', False),
    (r'\blabel-primary\b', 'badge bg-primary', False),
    (r'\blabel-success\b', 'badge bg-success', False),
    (r'\blabel-info\b', 'badge bg-info', False),
    (r'\blabel-warning\b', 'badge bg-warning', False),
    (r'\blabel-danger\b', 'badge bg-danger', False),
    (r'\blabel\b(?!\s*=)', 'badge', False),
    (r'\bbadge-pill\b', 'rounded-pill', False),

    # ── Images ─────────────────────────────────────────────────────────────
    (r'\bimg-responsive\b', 'img-fluid', False),
    (r'\bimg-circle\b', 'rounded-circle', False),
    (r'\bimg-rounded\b', 'rounded', False),
    (r'\bcenter-block\b', 'mx-auto d-block', False),

    # ── Typography / alignment ─────────────────────────────────────────────
    (r'\btext-right\b', 'text-end', False),
    (r'\btext-left\b', 'text-start', False),
    (r'\bpull-right\b', 'float-end', False),
    (r'\bpull-left\b', 'float-start', False),

    # ── Visibility ─────────────────────────────────────────────────────────
    (r'\bhidden-xs\b', 'd-none d-sm-block', False),
    (r'\bhidden-sm\b', 'd-sm-none d-md-block', False),
    (r'\bhidden-md\b', 'd-md-none d-lg-block', False),
    (r'\bhidden-lg\b', 'd-lg-none d-xl-block', False),
    (r'\bvisible-xs\b', 'd-block d-sm-none', False),
    (r'\bvisible-sm\b', 'd-none d-sm-block d-md-none', False),
    (r'\bvisible-md\b', 'd-none d-md-block d-lg-none', False),
    (r'\bvisible-lg\b', 'd-none d-lg-block', False),

    # ── Misc ───────────────────────────────────────────────────────────────
    (r'\bsr-only\b', 'visually-hidden', False),
    (r'\bform-group\b', 'mb-3', False),
    (r'\bcontrol-label\b', 'form-label', False),
    (r'\binput-group-addon\b', 'input-group-text', False),
    (r'\btable-condensed\b', 'table-sm', False),
    (r'\bcollapse in\b', 'collapse show', False),
    (r'\baffix\b', 'sticky-top', False),
]

# Patterns that need a TODO comment (can't auto-fix)
TODO_PATTERNS = [
    (r'navgoco', 'TODO-BS5: navgoco is not compatible with Bootstrap 5, replace with a BS5 accordion or collapse'),
    (r'\$\(.*\)\.modal\(', 'TODO-BS5: jQuery modal() — use Bootstrap 5 Modal JS API instead'),
    (r'\$\(.*\)\.tooltip\(', 'TODO-BS5: jQuery tooltip() — use Bootstrap 5 Tooltip JS API instead'),
    (r'\$\(.*\)\.popover\(', 'TODO-BS5: jQuery popover() — use Bootstrap 5 Popover JS API instead'),
    (r'\$\(.*\)\.scrollspy\(', 'TODO-BS5: jQuery scrollspy() — use Bootstrap 5 ScrollSpy JS API instead'),
    (r'bootstrap\.min\.js(?!.*bundle)', 'TODO-BS5: Use bootstrap.bundle.min.js (includes Popper)'),
]


def should_process(filepath):
    _, ext = os.path.splitext(filepath)
    return ext.lower() in EXTENSIONS


def process_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        original = f.read()

    content = original

    # Apply replacements
    for pattern, replacement, is_regex in REPLACEMENTS:
        if is_regex:
            content = re.sub(pattern, replacement, content)
        else:
            content = content.replace(pattern, replacement)

    # Add TODO comments for things that need manual attention
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line)
        for pattern, todo_msg in TODO_PATTERNS:
            if re.search(pattern, line):
                # Add TODO comment on next line
                indent = len(line) - len(line.lstrip())
                new_lines.append(' ' * indent + f'<!-- {todo_msg} -->')
                break
    content = '\n'.join(new_lines)

    if content == original:
        return False  # No changes

    if not dry_run:
        # Backup original
        shutil.copy2(filepath, filepath + BACKUP_EXT)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated: {filepath}")
    else:
        print(f"  ~ Would update: {filepath}")

    return True


def main():
    parser = argparse.ArgumentParser(description='Migrate Bootstrap 3 → 5')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--path', default='.', help='Root path to process (default: current dir)')
    args = parser.parse_args()

    root = os.path.abspath(args.path)
    dry_run = args.dry_run

    print(f"\n{'DRY RUN - ' if dry_run else ''}Bootstrap 3 → 5 Migration")
    print(f"Root: {root}\n")

    changed = 0
    skipped = 0

    # Directories to skip
    skip_dirs = {'.git', 'node_modules', '__pycache__', '.hugo_build.lock'}

    for dirpath, dirnames, filenames in os.walk(root):
        # Skip unwanted directories
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if not should_process(filepath):
                continue
            # Skip backup files
            if filepath.endswith(BACKUP_EXT):
                continue
            try:
                if process_file(filepath, dry_run):
                    changed += 1
                else:
                    skipped += 1
            except Exception as e:
                print(f"  ✗ Error processing {filepath}: {e}")

    print(f"\n{'Would change' if dry_run else 'Changed'}: {changed} files")
    print(f"Unchanged: {skipped} files")

    if not dry_run and changed > 0:
        print(f"\nBackups saved as *{BACKUP_EXT}")
        print("To undo: find . -name '*{BACKUP_EXT}' | while read b; do cp \"$b\" \"${{b%{BACKUP_EXT}}}\"; rm \"$b\"; done")


if __name__ == '__main__':
    main()