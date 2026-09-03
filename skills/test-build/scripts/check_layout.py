#!/usr/bin/env python3
"""Render an assessment and report what the printed pages actually look like.

Mark arithmetic is checked by check_marks.py. This checks the other half —
the half that gets noticed the moment a teacher opens the file:

  - How many pages it really is (the source never tells you)
  - Whether the last page is blank or nearly blank, which is what a stray
    trailing "[2 marks]" line produces
  - Where content stops on each page, so a page holding one short question
    stands out
  - Whether a solutions document paginates identically to its student paper,
    which it must, or the solutions stop lining up with the questions

Usage:
    python check_layout.py STUDENT.docx [--solutions SOLUTIONS.docx]
                           [--max-pages 4] [--json]

Needs libreoffice and pdftoppm. Pillow is used if present for the ink
measurements; without it you still get page counts.

IMPORTANT: LibreOffice silently drops every Word equation unless the
`libreoffice-math` package is installed — the pages render with blank working
spaces and nothing warns you. This script checks for it and says so.

Exit codes: 0 = clean, 1 = a problem was found, 2 = could not render.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile


def have(cmd):
    return shutil.which(cmd) is not None


def math_component_installed():
    """LibreOffice needs libreoffice-math to render OMML. Without it the
    equations vanish from the PDF and the paper looks empty where the
    mathematics should be."""
    try:
        out = subprocess.run(['dpkg', '-l'], capture_output=True, text=True,
                             timeout=30).stdout
        return 'libreoffice-math' in out
    except Exception:
        return None  # unknown platform; don't claim either way


def to_pdf(docx_path, outdir):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf',
                    docx_path, '--outdir', outdir],
                   capture_output=True, timeout=300)
    base = os.path.splitext(os.path.basename(docx_path))[0] + '.pdf'
    pdf = os.path.join(outdir, base)
    return pdf if os.path.exists(pdf) else None


def page_profile(pdf, dpi=50):
    """For each page return the fraction of the page height at which content
    stops. 0.0 means a blank page; 0.95 means a full one."""
    subprocess.run(['pdftoppm', '-r', str(dpi), '-png', pdf,
                    os.path.join(os.path.dirname(pdf), 'pg')],
                   capture_output=True, timeout=300)
    pages = sorted(f for f in os.listdir(os.path.dirname(pdf))
                   if f.startswith('pg') and f.endswith('.png'))
    try:
        from PIL import Image
    except ImportError:
        return [None] * len(pages)
    out = []
    for name in pages:
        im = Image.open(os.path.join(os.path.dirname(pdf), name)).convert('L')
        w, h = im.size
        px = im.load()
        # ignore the footer band, where the page number always sits
        limit = int(h * 0.94)
        # the lowest row containing ink tells you where content stops
        last = 0
        for y in range(limit - 1, -1, -1):
            if any(px[x, y] < 200 for x in range(0, w, 2)):
                last = y
                break
        out.append(round(last / h, 3))
    return out


def report(docx, max_pages, solutions=None):
    problems, notes = [], []
    tmp = tempfile.mkdtemp()

    mc = math_component_installed()
    if mc is False:
        problems.append(
            'libreoffice-math is not installed, so this render drops every '
            'Word equation — install it (apt-get install -y libreoffice-math) '
            'and re-run, or the blank working spaces you see are an artefact.')

    student_pdf = to_pdf(docx, os.path.join(tmp, 'student'))
    if not student_pdf:
        print('Could not render %s' % docx, file=sys.stderr)
        return 2, {}

    sp = page_profile(student_pdf)
    result = {'pages': len(sp), 'content_ends_at': sp}

    if max_pages and len(sp) > max_pages:
        problems.append('%d pages, limit is %d.' % (len(sp), max_pages))

    for i, frac in enumerate(sp, 1):
        if frac is None:
            continue
        if frac < 0.05:
            problems.append('Page %d is blank.' % i)
        elif i == len(sp) and frac < 0.35:
            problems.append(
                'Page %d holds almost nothing (content stops %d%% down). A '
                'trailing marks line or a single short question is stranded '
                'there — rebalance the working-space heights so the last page '
                'is genuinely used, or pull it back onto the previous page.'
                % (i, frac * 100))
        elif frac < 0.55 and i != len(sp):
            notes.append('Page %d is only %d%% full.' % (i, frac * 100))

    if solutions:
        sol_pdf = to_pdf(solutions, os.path.join(tmp, 'solutions'))
        if not sol_pdf:
            problems.append('Could not render the solutions document.')
        else:
            qp = page_profile(sol_pdf)
            result['solution_pages'] = len(qp)
            if len(qp) != len(sp):
                problems.append(
                    'Solutions are %d pages, student paper is %d. They must '
                    'match, or the solutions stop lining up with the '
                    'questions. Any answer written outside a fixed-height box '
                    'causes this.' % (len(qp), len(sp)))

    shutil.rmtree(tmp, ignore_errors=True)
    return (1 if problems else 0), dict(result, problems=problems, notes=notes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('--solutions')
    ap.add_argument('--max-pages', type=int, default=0)
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()

    for tool in ('soffice', 'pdftoppm'):
        if not have(tool):
            print('%s not found; cannot check layout.' % tool, file=sys.stderr)
            return 2

    code, res = report(a.docx, a.max_pages, a.solutions)
    if a.json:
        print(json.dumps(res, indent=2))
        return code

    print('Pages: %d' % res.get('pages', 0))
    if 'solution_pages' in res:
        print('Solutions pages: %d' % res['solution_pages'])
    ends = res.get('content_ends_at') or []
    if ends and ends[0] is not None:
        print('Content ends at: ' + ', '.join(
            'p%d %d%%' % (i, f * 100) for i, f in enumerate(ends, 1)))
    for n in res.get('notes', []):
        print('  note: ' + n)
    if res.get('problems'):
        print('\nProblems:')
        for p in res['problems']:
            print('  - ' + p)
    else:
        print('\nNo layout problems found.')
    return code


if __name__ == '__main__':
    sys.exit(main())
