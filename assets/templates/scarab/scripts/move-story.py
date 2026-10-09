#!/usr/bin/env python3
"""
Move a story or bug between stage folders, updating all description.md links.

Handles epics: updates child links in the epic's Child Stories table, and
updates the **Epic** back-link in every child story's description.md.

Handles child stories: updates the **Epic** back-link in the moved story and
updates the story's entry (link + status) in the parent epic's Child Stories table.

Run from anywhere — all paths are resolved relative to this script's location.

Usage:
    python scripts/move-story.py <id-or-slug> <target-stage> [--type story|bug]

Arguments:
    id-or-slug    Numeric ID prefix (e.g. 26050408) or full folder name
    target-stage  inbox | processing | complete

Options:
    --type        story (default) or bug
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

STAGES = {
    "inbox":      ("01-inbox",      "Inbox"),
    "processing": ("02-processing", "Processing"),
    "complete":   ("03-complete",   "Complete"),
}

DEV_DIR = Path(__file__).resolve().parent.parent

STATUS_RE    = re.compile(r'^(\*\*Status\*\*:[ \t]*)(\S+)', re.MULTILINE)
TYPE_EPIC_RE = re.compile(r'^\*\*Type\*\*:[ \t]*Epic\b', re.MULTILINE)
EPIC_LINK_RE = re.compile(r'(\*\*Epic\*\*:[ \t]*\[[^\]]*\]\()([^)]+)(\))', re.MULTILINE)
CHILD_ROW_RE = re.compile(r'(\|[ \t]*\[\d+\]\()([^)]+)(\))', re.MULTILINE)


def find_item(base_dir: Path, id_or_slug: str):
    for stage_name, (folder_dir, _) in STAGES.items():
        stage_path = base_dir / folder_dir
        if not stage_path.is_dir():
            continue
        for item in sorted(stage_path.iterdir()):
            if item.is_dir() and (item.name == id_or_slug or item.name.startswith(id_or_slug)):
                return item, stage_name
    return None, None


def rel_link(from_desc: Path, to_desc: Path) -> str:
    """Return a forward-slash relative path from from_desc's directory to to_desc."""
    return Path(os.path.relpath(str(to_desc), str(from_desc.parent))).as_posix()


def resolve_link(from_desc: Path, link: str) -> Path:
    """Resolve a markdown link (relative to from_desc's directory) to an absolute path."""
    return Path(os.path.normpath(str(from_desc.parent / link)))


def update_status(text: str, status: str) -> str:
    return STATUS_RE.sub(r'\g<1>' + status, text, count=1)


def update_epic_link(text: str, from_desc: Path, epic_desc: Path) -> str:
    """Rewrite the **Epic** back-link using a path relative to from_desc."""
    new_rel = rel_link(from_desc, epic_desc)
    return EPIC_LINK_RE.sub(r'\g<1>' + new_rel + r'\3', text, count=1)


def update_child_links_in_epic(text: str, old_epic_desc: Path, new_epic_desc: Path) -> str:
    """Rewrite every child link in an epic's Child Stories table after the epic moves."""
    def replace(m):
        child_abs = resolve_link(old_epic_desc, m.group(2))
        return m.group(1) + rel_link(new_epic_desc, child_abs) + m.group(3)
    return CHILD_ROW_RE.sub(replace, text)


def update_child_row_in_epic(
    text: str,
    epic_desc: Path,
    old_child_desc: Path,
    new_child_desc: Path,
    new_status: str,
) -> str:
    """Rewrite a child story's link and status column in an epic's Child Stories table."""
    old_rel = rel_link(epic_desc, old_child_desc)
    new_rel = rel_link(epic_desc, new_child_desc)
    pattern = re.compile(
        r'(\|[ \t]*\[\d+\]\()' + re.escape(old_rel) + r'(\)[ \t]*\|[^\|]+\|[ \t]*)(\w+)([ \t]*\|)',
        re.MULTILINE,
    )
    return pattern.sub(
        lambda m: m.group(1) + new_rel + m.group(2) + new_status + m.group(4),
        text,
        count=1,
    )


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('id_or_slug', help='Numeric ID prefix or full folder name')
    parser.add_argument('target_stage', choices=list(STAGES.keys()), help='Target stage')
    parser.add_argument('--type', dest='item_type', choices=['story', 'bug'], default='story')
    args = parser.parse_args()

    base_dir = DEV_DIR / {'story': 'stories', 'bug': 'bugs'}[args.item_type]

    src_folder, src_stage = find_item(base_dir, args.id_or_slug)
    if src_folder is None:
        print(f"Error: '{args.id_or_slug}' not found under {base_dir}", file=sys.stderr)
        sys.exit(1)

    if src_stage == args.target_stage:
        print(f"'{src_folder.name}' is already in '{args.target_stage}'.")
        return

    target_folder_dir, target_status = STAGES[args.target_stage]
    dst_folder = base_dir / target_folder_dir / src_folder.name
    src_desc = src_folder / 'description.md'
    dst_desc = dst_folder / 'description.md'

    # Read and analyse before moving so relative links resolve correctly.
    text = src_desc.read_text(encoding='utf-8')
    epic = bool(TYPE_EPIC_RE.search(text))

    epic_link_m = EPIC_LINK_RE.search(text)
    epic_desc_abs = resolve_link(src_desc, epic_link_m.group(2)) if epic_link_m else None

    child_links = []  # (old_rel_str, child_abs_path)
    if epic:
        for m in CHILD_ROW_RE.finditer(text):
            child_links.append((m.group(2), resolve_link(src_desc, m.group(2))))

    # Move the folder.
    print(f"Moving '{src_folder.name}' -> {target_folder_dir}/")
    shutil.move(str(src_folder), str(dst_folder))

    # Update this story's description.md.
    text = update_status(text, target_status)
    if epic:
        text = update_child_links_in_epic(text, src_desc, dst_desc)
    if epic_link_m:
        text = update_epic_link(text, dst_desc, epic_desc_abs)
    dst_desc.write_text(text, encoding='utf-8')

    # If epic: rewrite the **Epic** back-link in every child story.
    if epic:
        for _, child_abs in child_links:
            if not child_abs.exists():
                print(f"  Warning: child not found at {child_abs}", file=sys.stderr)
                continue
            child_text = child_abs.read_text(encoding='utf-8')
            child_text = update_epic_link(child_text, child_abs, dst_desc)
            child_abs.write_text(child_text, encoding='utf-8')
            print(f"  Updated epic link in {child_abs.parent.name}/")

    # If child story: update its entry in the parent epic's Child Stories table.
    if epic_desc_abs is not None:
        if not epic_desc_abs.exists():
            print(f"  Warning: epic not found at {epic_desc_abs}", file=sys.stderr)
        else:
            epic_text = epic_desc_abs.read_text(encoding='utf-8')
            epic_text = update_child_row_in_epic(
                epic_text, epic_desc_abs, src_desc, dst_desc, target_status
            )
            epic_desc_abs.write_text(epic_text, encoding='utf-8')
            print(f"  Updated child entry in epic {epic_desc_abs.parent.name}/")

    print(f"Done. Status -> '{target_status}'.")


if __name__ == '__main__':
    main()
