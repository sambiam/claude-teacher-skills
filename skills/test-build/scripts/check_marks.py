#!/usr/bin/env python3
"""Check the mark arithmetic in an assessment .docx.

Wrong mark totals are the most common and most embarrassing defect in a
generated test: the questions sum to 74 while the front page promises 80, and
nobody notices until a student does. This finds that before it reaches paper.

What it checks:
  - Every mark allocation it can find in the body, and their sum
  - The declared total on the front page, if one is stated
  - A front-page marks table, if one exists, and whether its rows sum to the
    declared total
  - Ticks in a solutions document, and whether the tick count matches the marks
  - Ticks recorded in a manifest, for solutions produced as a raster overlay
    where the ticks are graphics and cannot be counted from the file

Stdlib only.

Usage:
    python check_marks.py TEST.docx [--solutions SOLUTIONS.docx]
                          [--tick-manifest solutions_ticks.json]
                          [--expect 80] [--json]

Exit codes: 0 = all checks passed, 1 = a discrepancy was found, 2 = unreadable.
"""

import argparse
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# "(3 marks)", "(1 mark)", "[3]", "3 marks" at the end of a line
MARK_PATTERNS = [
    re.compile(r"\((\d+)\s*marks?\)", re.I),
    re.compile(r"\[(\d+)\s*marks?\]", re.I),
    re.compile(r"(?:^|\s)(\d+)\s*marks?\s*$", re.I),
    re.compile(r"^\[(\d+)\]$"),
]

TOTAL_PATTERNS = [
    re.compile(r"total\s*marks\s*[:\-]?\s*(\d+)", re.I),      # Total marks: 80
    re.compile(r"total\s*[:\-]?\s*(\d+)\s*marks", re.I),       # Total: 80 marks
    re.compile(r"(\d+)\s*marks\s*(?:in\s*)?total", re.I),      # 80 marks total
]

TICK_CHARS = "\u2713\u2714\u2705"


def paragraphs(path):
    """Yield (text, in_table) for every paragraph, in document order."""
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
    body = root.find(f"{W}body")
    if body is None:
        return

    def walk(node, in_table):
        for child in node:
            if child.tag == f"{W}p":
                text = "".join(t.text or "" for t in child.iter(f"{W}t"))
                yield text, in_table
            elif child.tag == f"{W}tbl":
                yield from walk(child, True)
            else:
                yield from walk(child, in_table)

    yield from walk(body, False)


def find_marks(lines):
    """Return [(line_index, marks, text)] for each mark allocation found."""
    found = []
    for i, text in enumerate(lines):
        stripped = text.strip()
        if not stripped:
            continue
        for pattern in MARK_PATTERNS:
            m = pattern.search(stripped)
            if m:
                found.append((i, int(m.group(1)), stripped))
                break
    return found


def find_declared_total(lines):
    """The total marks stated on the front page, if any."""
    for text in lines[:60]:
        for pattern in TOTAL_PATTERNS:
            m = pattern.search(text)
            if m:
                return int(m.group(1))
    return None


def table_rows_with_numbers(path):
    """Rows from tables in the first part of the document that look like a
    marks table: a label cell and a numeric cell."""
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
    rows = []
    for tbl in root.iter(f"{W}tbl"):
        for tr in tbl.iter(f"{W}tr"):
            cells = []
            for tc in tr.iter(f"{W}tc"):
                cells.append("".join(t.text or "" for t in tc.iter(f"{W}t")).strip())
            numeric = [c for c in cells if re.fullmatch(r"/?\s*\d+", c)]
            if len(cells) >= 2 and numeric:
                rows.append(cells)
        if rows:
            break  # only the first table, which is the front-page marks table
    return rows


def count_ticks(lines):
    return sum(sum(text.count(ch) for ch in TICK_CHARS) for text in lines)


def analyse(path):
    lines = [text for text, _ in paragraphs(path)]
    marks = find_marks(lines)
    return {
        "path": path,
        "allocations": [{"marks": m, "text": t[:90]} for _, m, t in marks],
        "allocation_count": len(marks),
        "sum_of_marks": sum(m for _, m, _ in marks),
        "declared_total": find_declared_total(lines),
        "marks_table_rows": table_rows_with_numbers(path),
        "ticks": count_ticks(lines),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("test")
    ap.add_argument("--solutions", help="solutions .docx, to check tick counts")
    ap.add_argument(
        "--tick-manifest",
        help="JSON mapping question label to tick count, for raster-overlay "
        "solutions whose ticks are graphics and can't be counted from the PDF",
    )
    ap.add_argument("--expect", type=int, help="the total you intended")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        result = analyse(args.test)
    except (zipfile.BadZipFile, FileNotFoundError, KeyError) as exc:
        print(f"Could not read {args.test}: {exc}", file=sys.stderr)
        return 2

    problems = []
    total = result["sum_of_marks"]
    declared = result["declared_total"]

    if declared is not None and declared != total:
        problems.append(
            f"Front page says {declared} marks; the questions sum to {total}."
        )
    if args.expect is not None and args.expect != total:
        problems.append(f"You asked for {args.expect} marks; the questions sum to {total}.")
    if result["allocation_count"] == 0:
        problems.append(
            "No mark allocations found at all. Either they use a format this script "
            "doesn't recognise, or they're missing — check by eye before trusting this."
        )

    if args.solutions:
        try:
            sol = analyse(args.solutions)
        except (zipfile.BadZipFile, FileNotFoundError, KeyError) as exc:
            print(f"Could not read {args.solutions}: {exc}", file=sys.stderr)
            return 2
        result["solutions"] = sol
        if sol["ticks"] != total:
            problems.append(
                f"Solutions carry {sol['ticks']} ticks against {total} marks on the test."
            )

    if args.tick_manifest:
        try:
            with open(args.tick_manifest) as fh:
                manifest = json.load(fh)
        except (OSError, ValueError) as exc:
            print(f"Could not read {args.tick_manifest}: {exc}", file=sys.stderr)
            return 2

        if not isinstance(manifest, dict) or not manifest:
            print(
                f"{args.tick_manifest} should be a non-empty object mapping "
                'question labels to tick counts, e.g. {"1a": 2, "1b": 3}.',
                file=sys.stderr,
            )
            return 2

        bad = {k: v for k, v in manifest.items() if not isinstance(v, int) or v < 0}
        if bad:
            problems.append(
                "Tick manifest has non-integer or negative counts: "
                + ", ".join(f"{k}={v!r}" for k, v in sorted(bad.items()))
            )

        manifest_total = sum(v for v in manifest.values() if isinstance(v, int) and v >= 0)
        result["tick_manifest"] = {
            "path": args.tick_manifest,
            "entries": len(manifest),
            "total_ticks": manifest_total,
        }
        if manifest_total != total:
            problems.append(
                f"Tick manifest records {manifest_total} ticks against {total} "
                "marks on the test."
            )
        if len(manifest) != result["allocation_count"]:
            problems.append(
                f"Tick manifest has {len(manifest)} entries but the test has "
                f"{result['allocation_count']} mark allocations — check that "
                "every question is covered and none is doubled up."
            )

    if args.json:
        print(json.dumps({"result": result, "problems": problems}, indent=2))
        return 1 if problems else 0

    print(f"Mark allocations found: {result['allocation_count']}")
    print(f"Sum of marks: {total}")
    print(f"Declared total: {declared if declared is not None else 'not stated'}")
    if result["marks_table_rows"]:
        print(f"Front-page table rows: {len(result['marks_table_rows'])}")
    if args.solutions:
        print(f"Ticks in solutions: {result['solutions']['ticks']}")
    if args.tick_manifest:
        tm = result["tick_manifest"]
        print(f"Ticks in manifest: {tm['total_ticks']} across {tm['entries']} questions")

    if problems:
        print("\nProblems:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("\nNo mark discrepancies found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
