#!/usr/bin/env python3
"""Find the exemplar material for a new assessment.

Replaces the old workflow of uploading exemplars by hand: point this at the
topic folder and the template folder and it reports what's already there,
pairing each test with its solutions so you can see what's missing before you
start rather than halfway through.

Classification is by filename and folder, so it's a starting map rather than
the truth. Open the files it finds before relying on them.

Stdlib only.

Usage:
    python find_test_sources.py TOPIC_FOLDER [--templates TEMPLATE_FOLDER] [--json]
"""

import argparse
import datetime as dt
import json
import os
import re
import sys

DOC_EXT = {".docx", ".doc", ".pdf", ".odt"}

SOLUTION_HINTS = ("solution", "answer", "worked", "marking", "key", "ms")
PRACTICE_HINTS = ("practice", "revision", "mock", "trial", "sample")
TEST_HINTS = ("test", "exam", "assessment", "quiz", "task")
SKIP_HINTS = ("~$", ".tmp")

YEAR = re.compile(r"(20\d{2})")


def classify(name):
    low = name.lower()
    is_solution = any(h in low for h in SOLUTION_HINTS)
    is_practice = any(h in low for h in PRACTICE_HINTS)
    is_test = any(h in low for h in TEST_HINTS)
    if is_solution:
        return "practice solutions" if is_practice else "solutions"
    if is_practice:
        return "practice test"
    if is_test:
        return "test"
    return "other"


def scan(folder):
    items = []
    for root, _dirs, files in os.walk(folder):
        for f in files:
            if any(h in f for h in SKIP_HINTS) or f.startswith("."):
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext not in DOC_EXT:
                continue
            path = os.path.join(root, f)
            year_match = YEAR.search(f)
            items.append(
                {
                    "path": path,
                    "name": f,
                    "kind": classify(f),
                    "year": int(year_match.group(1)) if year_match else None,
                    "modified": dt.datetime.fromtimestamp(
                        os.path.getmtime(path)
                    ).strftime("%Y-%m-%d"),
                    "size_kb": round(os.path.getsize(path) / 1024, 1),
                }
            )
    items.sort(key=lambda i: (i["year"] or 0, i["modified"]), reverse=True)
    return items


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("topic_folder")
    ap.add_argument("--templates", help="folder holding the assessment template")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.topic_folder):
        print(f"Not a folder: {args.topic_folder}", file=sys.stderr)
        return 2

    found = scan(args.topic_folder)
    templates = scan(args.templates) if args.templates and os.path.isdir(args.templates) else []

    by_kind = {}
    for item in found:
        by_kind.setdefault(item["kind"], []).append(item)

    missing = [k for k in ("test", "solutions", "practice test", "practice solutions")
               if k not in by_kind]

    if args.json:
        print(json.dumps({"found": found, "templates": templates, "missing": missing}, indent=2))
        return 0

    if not found:
        print(f"No assessment documents found under {args.topic_folder}.")
    for kind in ("test", "solutions", "practice test", "practice solutions", "other"):
        if kind not in by_kind:
            continue
        print(f"\n{kind.upper()}")
        for item in by_kind[kind]:
            year = item["year"] or item["modified"][:4]
            print(f"  [{year}] {item['name']}  ({item['size_kb']} KB)")
            print(f"         {item['path']}")

    if templates:
        print("\nTEMPLATES")
        for item in templates:
            print(f"  {item['name']}\n         {item['path']}")
    elif args.templates:
        print(f"\nNo template found in {args.templates}")

    if missing:
        print("\nNot present: " + ", ".join(missing))
        print("Build on what exists; flag the gaps rather than assuming they were never needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
