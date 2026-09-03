#!/usr/bin/env python3
"""Word equation objects and assessment layout primitives.

Every run that builds a maths paper needs the same two things: real Word
equation objects (OMML), because plain-text `x^2` and `a/b` are not acceptable
on a printed test, and fixed-height working grids, because a solutions document
only stays aligned with its student paper if nothing can reflow.

python-docx does not do either. Rather than rediscovering the OOXML each time,
import this.

    import sys; sys.path.insert(0, '<skill>/scripts')
    from docx_math import mr, frac, sup, delim, omath, add_math, grid, slot

Requires python-docx and lxml.

## Building equations

Every equation is a list of "kids" appended to an `oMath` element:

    add_math(p, [mr('3x-9=23')])                       # 3x − 9 = 23
    add_math(p, [frac([mr('y+5')], [mr('4')]), mr('=-3')])   # (y+5)/4 = −3
    add_math(p, [mr('2x'), delim([mr('x+4')]), mr('+3'), sup('x', '2')])
    add_math(p, [mr('6'), delim([mr('h-7')])])         # 6(h − 7)

## Two rendering traps, both silent

A math run that is *only* `=` or that *ends* in `=` renders as an inverted
question mark in LibreOffice — so a continuation line written as
`mr('=5x+8')` looks fine in Word and broken in the PDF you actually ship.
Put the `=` in an ordinary Word run instead; `eq_run(p)` does this.

An unbalanced fragment inside a delimiter — `delim([mr('4k-')])`, because you
wanted a blank after the minus — breaks the same way. Close the bracket with
ordinary text runs and keep the math fragments whole.
"""

from docx.shared import Pt, Emu
from lxml import etree

M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


# --------------------------------------------------------------- equations
def _math_fonts(rPr):
    f = etree.SubElement(rPr, '{%s}rFonts' % W)
    f.set('{%s}ascii' % W, 'Cambria Math')
    f.set('{%s}hAnsi' % W, 'Cambria Math')


def mr(text):
    """A literal run of mathematics: `mr('3x-9=23')`."""
    r = etree.Element('{%s}r' % M)
    _math_fonts(etree.SubElement(r, '{%s}rPr' % W))
    t = etree.SubElement(r, '{%s}t' % M)
    t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return r


def _ctrl(tag):
    p = etree.Element('{%s}%sPr' % (M, tag))
    rPr = etree.SubElement(etree.SubElement(p, '{%s}ctrlPr' % M), '{%s}rPr' % W)
    _math_fonts(rPr)
    etree.SubElement(rPr, '{%s}i' % W)
    return p


def delim(kids):
    """Brackets round a group: `delim([mr('x+4')])` → (x + 4)."""
    d = etree.Element('{%s}d' % M)
    d.append(_ctrl('d'))
    e = etree.SubElement(d, '{%s}e' % M)
    for k in kids:
        e.append(k)
    return d


def frac(num, den):
    """A vertical fraction with a real bar."""
    f = etree.Element('{%s}f' % M)
    f.append(_ctrl('f'))
    n = etree.SubElement(f, '{%s}num' % M)
    for k in num:
        n.append(k)
    d = etree.SubElement(f, '{%s}den' % M)
    for k in den:
        d.append(k)
    return f


def sup(base, exponent):
    """A raised exponent: `sup('x', '2')` → x²."""
    s = etree.Element('{%s}sSup' % M)
    s.append(_ctrl('sSup'))
    etree.SubElement(s, '{%s}e' % M).append(mr(base))
    etree.SubElement(s, '{%s}sup' % M).append(mr(exponent))
    return s


def omath(kids):
    o = etree.Element('{%s}oMath' % M)
    for k in kids:
        o.append(k)
    return o


def add_math(paragraph, kids, color=None):
    """Append an equation to a paragraph. `color` is a hex string like C00000,
    used to set solutions in red without touching the student paper."""
    o = omath(kids)
    if color:
        for rPr in o.iter('{%s}rPr' % W):
            etree.SubElement(rPr, '{%s}color' % W).set('{%s}val' % W, color)
    paragraph._p.append(o)
    return o


def eq_run(paragraph, font=None, size_pt=12, color=None):
    """An `=` as an ordinary Word run, for continuation lines.

    Starting a math element with `=` renders as `¿` outside Word, so
    `= 5x + 8` must be written as this run followed by `add_math(p, [...])`.
    """
    r = paragraph.add_run('=  ')
    if font:
        r.font.name = font
    r.font.size = Pt(size_pt)
    if color:
        r.font.color.rgb = color
    return r


# ------------------------------------------------------------------ layout
def set_widths(tbl, widths_dxa, indent_dxa=340):
    """Fix a table's column widths in DXA. Percentage widths break grid
    alignment between the student paper and its solutions."""
    tbl.autofit = False
    tblPr = tbl._tbl.tblPr
    for el in tblPr.findall('{%s}tblW' % W):
        tblPr.remove(el)
    w = etree.SubElement(tblPr, '{%s}tblW' % W)
    w.set('{%s}w' % W, str(sum(widths_dxa)))
    w.set('{%s}type' % W, 'dxa')
    ind = etree.SubElement(tblPr, '{%s}tblInd' % W)
    ind.set('{%s}w' % W, str(indent_dxa))
    ind.set('{%s}type' % W, 'dxa')
    for row in tbl.rows:
        for i, c in enumerate(row.cells):
            c.width = Emu(int(widths_dxa[i] * 914400 / 1440))


def fix_height(row, points):
    """Pin a row to an exact height. This is what keeps the two documents on
    identical pagination: typing solutions into a grid must not grow it."""
    trPr = row._tr.get_or_add_trPr()
    h = etree.SubElement(trPr, '{%s}trHeight' % W)
    h.set('{%s}val' % W, str(int(points * 20)))
    h.set('{%s}hRule' % W, 'exact')


def grid(doc, cols, rows, height_pt, usable_dxa=10545, indent_dxa=680):
    """A bordered working space: fixed height, no row splitting, and kept with
    whatever follows so a box is never orphaned from its marks line."""
    t = doc.add_table(rows=rows, cols=cols)
    t.style = 'Table Grid'
    w = int((usable_dxa - indent_dxa) / cols)
    set_widths(t, [w] * cols, indent_dxa)
    for r in t.rows:
        fix_height(r, height_pt)
        etree.SubElement(r._tr.get_or_add_trPr(), '{%s}cantSplit' % W)
        for c in r.cells:
            pf = c.paragraphs[0].paragraph_format
            pf.space_after = Pt(0)
            pf.space_before = Pt(0)
            pf.line_spacing = 1.0
            pf.keep_with_next = True
    return t


def slot(doc, height_pt, usable_dxa=10545, indent_dxa=1400):
    """An invisible fixed-height strip.

    Some answers have nowhere to live — the student writes into a blank in the
    question line itself, or circles an option. Writing those answers as an
    extra paragraph in the solutions makes the two documents paginate
    differently, which is exactly the drift the whole fixed-height scheme
    exists to prevent. Reserve the space in both documents instead, and leave
    it empty on the student paper.
    """
    t = grid(doc, 1, 1, height_pt, usable_dxa, indent_dxa)
    tcPr = t.cell(0, 0)._tc.get_or_add_tcPr()
    bd = etree.SubElement(tcPr, '{%s}tcBorders' % W)
    for edge in ('top', 'left', 'bottom', 'right'):
        etree.SubElement(bd, '{%s}%s' % (W, edge)).set('{%s}val' % W, 'nil')
    return t


def clear_body(doc):
    """Strip a document's content but keep its section setup, header
    reference, margins, styles and numbering — the basis of building a new
    paper from a real one rather than approximating its look."""
    body = doc.element.body
    for child in list(body):
        if child.tag != '{%s}sectPr' % W:
            body.remove(child)
    return doc
