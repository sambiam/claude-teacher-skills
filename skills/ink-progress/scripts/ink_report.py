#!/usr/bin/env python3
"""Report which slides in a .pptx carry ink annotations.

A .pptx is a ZIP. Ink drawn with the Draw tab or with the slideshow pen is
stored as a separate InkML part (usually ppt/ink/inkN.xml, content type
application/inkml+xml). Each slide that carries ink references its ink part
through the slide's relationship file, and places it on the canvas with a
<p14:contentPart> element that supplies a bounding box.

This script reads all three of those and reports, per slide, whether ink is
present, how many strokes there are, and where on the slide they sit.

Stdlib only - no pip installs needed.

Usage:
    python ink_report.py DECK.pptx [--json] [--verbose]

Exit codes: 0 = ran fine, 2 = file unreadable or not a pptx.
"""

import argparse
import json
import posixpath
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

INKML_CONTENT_TYPE = "application/inkml+xml"

NS = {
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "p14": "http://schemas.microsoft.com/office/powerpoint/2010/main",
    "inkml": "http://www.w3.org/2003/InkML",
}

EMU_PER_INCH = 914400


def slide_sort_key(name):
    """slide10.xml must sort after slide9.xml, so sort numerically."""
    m = re.search(r"slide(\d+)\.xml$", name)
    return int(m.group(1)) if m else 0


def ink_parts_from_content_types(zf):
    """Return the set of part names (no leading slash) declared as InkML.

    Content types are authoritative: a part is ink because [Content_Types].xml
    says so, not because it happens to live under ppt/ink/. Both the Default
    (by extension) and Override (by part name) forms are handled.
    """
    ink_parts = set()
    ink_extensions = set()
    try:
        root = ET.fromstring(zf.read("[Content_Types].xml"))
    except KeyError:
        return ink_parts, ink_extensions

    for default in root.findall("ct:Default", NS):
        if default.get("ContentType") == INKML_CONTENT_TYPE:
            ink_extensions.add(default.get("Extension", "").lower())
    for override in root.findall("ct:Override", NS):
        if override.get("ContentType") == INKML_CONTENT_TYPE:
            ink_parts.add(override.get("PartName", "").lstrip("/"))

    if ink_extensions:
        for name in zf.namelist():
            ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
            if ext in ink_extensions:
                ink_parts.add(name)
    return ink_parts, ink_extensions


def resolve(base_part, target):
    """Resolve a relationship Target relative to the part that declares it."""
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(base_part), target))


def slide_rels(zf, slide_part):
    """Map rId -> resolved part name for one slide."""
    rels_part = posixpath.join(
        posixpath.dirname(slide_part), "_rels", posixpath.basename(slide_part) + ".rels"
    )
    out = {}
    try:
        root = ET.fromstring(zf.read(rels_part))
    except KeyError:
        return out
    for rel in root.findall("rel:Relationship", NS):
        if rel.get("TargetMode") == "External":
            continue
        out[rel.get("Id")] = resolve(slide_part, rel.get("Target", ""))
    return out


def content_part_boxes(zf, slide_part):
    """Return {rId: {x_in, y_in, w_in, h_in}} for each <p14:contentPart>.

    The element is normally wrapped in <mc:AlternateContent>, so search the
    whole tree by tag rather than by an expected path.
    """
    boxes = {}
    try:
        root = ET.fromstring(zf.read(slide_part))
    except KeyError:
        return boxes
    tag = "{%s}contentPart" % NS["p14"]
    rid_attr = "{%s}id" % NS["r"]
    for node in root.iter(tag):
        rid = node.get(rid_attr)
        if not rid:
            continue
        box = None
        for xfrm in node.iter("{%s}xfrm" % NS["p14"]):
            off = xfrm.find("a:off", NS)
            ext = xfrm.find("a:ext", NS)
            if off is not None and ext is not None:
                box = {
                    "x_in": round(int(off.get("x", 0)) / EMU_PER_INCH, 2),
                    "y_in": round(int(off.get("y", 0)) / EMU_PER_INCH, 2),
                    "w_in": round(int(ext.get("cx", 0)) / EMU_PER_INCH, 2),
                    "h_in": round(int(ext.get("cy", 0)) / EMU_PER_INCH, 2),
                }
            break
        boxes[rid] = box
    return boxes


def count_strokes(zf, ink_part):
    """One <trace> in InkML is one pen stroke (pen down to pen up)."""
    try:
        root = ET.fromstring(zf.read(ink_part))
    except (KeyError, ET.ParseError):
        return 0
    return sum(1 for _ in root.iter("{%s}trace" % NS["inkml"]))


def slide_order(zf):
    """Slides in presentation order, falling back to filename order.

    <p:sldIdLst> in presentation.xml is the real running order; slideN.xml
    numbering reflects creation order and can differ after reordering.
    """
    pres = "ppt/presentation.xml"
    try:
        root = ET.fromstring(zf.read(pres))
        rels = slide_rels(zf, pres)
    except KeyError:
        rels = {}
        root = None
    ordered = []
    if root is not None:
        lst = root.find("p:sldIdLst", NS)
        if lst is not None:
            for sld in lst.findall("p:sldId", NS):
                part = rels.get(sld.get("{%s}id" % NS["r"]))
                if part:
                    ordered.append(part)
    if ordered:
        return ordered
    return sorted(
        (n for n in zf.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
        key=slide_sort_key,
    )


def analyse(path):
    with zipfile.ZipFile(path) as zf:
        ink_parts, _ = ink_parts_from_content_types(zf)
        slides = slide_order(zf)
        results = []
        for position, slide_part in enumerate(slides, start=1):
            rels = slide_rels(zf, slide_part)
            boxes = content_part_boxes(zf, slide_part)
            found = []
            for rid, target in rels.items():
                if target in ink_parts:
                    found.append(
                        {
                            "part": target,
                            "strokes": count_strokes(zf, target),
                            "bounds_inches": boxes.get(rid),
                        }
                    )
            # Ink parts referenced by a contentPart but missing from content
            # types would be a malformed package; surface rather than hide it.
            orphan_rids = [
                rid for rid in boxes if rid in rels and rels[rid] not in ink_parts
            ]
            results.append(
                {
                    "position": position,
                    "slide_part": slide_part,
                    "has_ink": bool(found),
                    "stroke_count": sum(f["strokes"] for f in found),
                    "ink": found,
                    "unresolved_content_parts": orphan_rids,
                }
            )
    return results


def summarise(results):
    annotated = [r for r in results if r["has_ink"]]
    total = len(results)
    last = annotated[-1]["position"] if annotated else None
    return {
        "total_slides": total,
        "annotated_slides": [r["position"] for r in annotated],
        "last_annotated_slide": last,
        "slides_after_last_annotation": (total - last) if last else total,
        "total_strokes": sum(r["stroke_count"] for r in results),
        "ink_found": bool(annotated),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("deck")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--verbose", action="store_true", help="per-slide detail")
    args = ap.parse_args()

    try:
        results = analyse(args.deck)
    except (zipfile.BadZipFile, FileNotFoundError, IsADirectoryError) as exc:
        print(f"Could not read {args.deck}: {exc}", file=sys.stderr)
        return 2

    summary = summarise(results)

    if args.json:
        print(json.dumps({"summary": summary, "slides": results}, indent=2))
        return 0

    if not summary["ink_found"]:
        print(f"No ink found across {summary['total_slides']} slides.")
        print(
            "This means the deck was never annotated, the ink was discarded at the "
            "end of the slideshow, or annotation happened somewhere other than this file."
        )
        return 0

    print(f"Slides: {summary['total_slides']}")
    print(
        "Annotated: "
        + ", ".join(str(p) for p in summary["annotated_slides"])
        + f"  ({summary['total_strokes']} strokes total)"
    )
    print(f"Last annotated slide: {summary['last_annotated_slide']}")
    print(f"Slides after it: {summary['slides_after_last_annotation']}")

    if args.verbose:
        print()
        for r in results:
            if not r["has_ink"]:
                continue
            print(f"  slide {r['position']} ({r['slide_part']}): {r['stroke_count']} strokes")
            for f in r["ink"]:
                b = f["bounds_inches"]
                where = (
                    f"at {b['x_in']},{b['y_in']} in  size {b['w_in']}x{b['h_in']} in"
                    if b
                    else "position not recorded"
                )
                print(f"      {f['part']}: {f['strokes']} strokes, {where}")
            if r["unresolved_content_parts"]:
                print(f"      warning: content parts with no ink payload: {r['unresolved_content_parts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
