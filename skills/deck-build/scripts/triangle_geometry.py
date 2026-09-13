#!/usr/bin/env python3
"""Triangle geometry for labelled diagrams (trig SSDD sets, deck diagrams,
worksheet diagrams).

Every trig diagram needs the same handful of things worked out before a
single shape gets drawn: where the three vertices actually go, where a
mirrored second triangle sits for a shared-diagram panel or an ambiguous-case
pair, where a label can be dropped near a vertex or a side midpoint without
sitting on top of the triangle's own lines, where the tick-mark dashes for an
"these sides are equal" mark go, and where an angle bisector point sits for a
coloured angle badge. None of this is specific to a lesson or a question —
work it out once here rather than re-deriving it inline every time a diagram
is needed.

    import sys; sys.path.insert(0, '<skill>/scripts')
    from triangle_geometry import (triangle_sas, triangle_sss, mirror,
                                    label_anchors, tick_marks,
                                    angle_badge_point, interior_angles,
                                    side_lengths)

Conventions:

- Every vertex dict has keys 'A', 'B', 'C' plus (where the builder computed
  them) 'sides'. Side lengths follow the standard triangle-label convention:
  side a = BC is opposite vertex A, side b = AC is opposite vertex B, side
  c = AB is opposite vertex C. This is what makes cosine/sine-rule working
  line up with the labels on the diagram.
- All coordinates are plain (x, y) tuples in whatever unit the caller is
  drawing in (inches for pptxgenjs/python-pptx, cm, points — this module does
  no unit conversion) and no clamping to a slide or page is performed; place
  the returned points, then translate/scale the whole triangle to fit your
  canvas.
- Angles are always degrees in and out.
- Coordinates here are standard maths coordinates (y increases upward,
  angles increase anticlockwise). pptxgenjs and python-pptx both put y
  increasing *downward*. Either build in maths coordinates and flip once at
  the end (`y_slide = canvas_height - y_maths` for every point you draw), or
  negate every angle you pass in — don't mix the two conventions mid-diagram,
  or the triangle comes out mirrored vertically from what you expect.
"""

import math


def triangle_sas(p, theta_deg, q, origin=(0.0, 0.0), rotation_deg=0.0):
    """Place a triangle from two sides and the angle between them (the
    classic SAS trig setup: "two sides and the included angle").

    The included-angle vertex is 'A', placed at `origin`. The side of
    length `q` runs out along `rotation_deg`, landing on 'C'; the side of
    length `p` leaves 'A' at `rotation_deg + theta_deg`, landing on 'B'.
    So AB = c = p and AC = b = q, and the third side a = BC is found by the
    cosine rule, all consistent with the module's side-labelling convention.

    Returns {'A': (x,y), 'B': (x,y), 'C': (x,y), 'sides': {'a':.., 'b':.., 'c':..}}.
    """
    if p <= 0 or q <= 0:
        raise ValueError("side lengths must be positive")
    if not 0 < theta_deg < 180:
        raise ValueError("included angle must be strictly between 0 and 180 degrees")
    ax, ay = origin
    r0 = math.radians(rotation_deg)
    r1 = math.radians(rotation_deg + theta_deg)
    A = (ax, ay)
    C = (ax + q * math.cos(r0), ay + q * math.sin(r0))
    B = (ax + p * math.cos(r1), ay + p * math.sin(r1))
    return {'A': A, 'B': B, 'C': C, 'sides': side_lengths({'A': A, 'B': B, 'C': C})}


def triangle_sss(a, b, c, origin=(0.0, 0.0), rotation_deg=0.0, flip=False):
    """Place a triangle from its three side lengths (a = BC, b = AC, c = AB
    — the module's standard convention).

    Vertex 'B' sits at `origin`; vertex 'C' sits a distance `a` away along
    `rotation_deg`. `flip=True` places 'A' on the other side of BC, for a
    mirrored/reflected build without a separate call to `mirror`.

    Raises ValueError if the three lengths can't form a triangle.
    """
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("sides %r, %r, %r do not form a triangle" % (a, b, c))
    cos_B = (a * a + c * c - b * b) / (2 * a * c)
    cos_B = max(-1.0, min(1.0, cos_B))
    angle_B = math.acos(cos_B)
    if flip:
        angle_B = -angle_B
    bx, by = origin
    r0 = math.radians(rotation_deg)
    r1 = r0 + angle_B
    B = (bx, by)
    C = (bx + a * math.cos(r0), by + a * math.sin(r0))
    A = (bx + c * math.cos(r1), by + c * math.sin(r1))
    return {'A': A, 'B': B, 'C': C, 'sides': {'a': a, 'b': b, 'c': c}}


def centroid(vertices):
    """The centroid of a vertex dict's A/B/C points."""
    pts = [vertices[k] for k in ('A', 'B', 'C')]
    return (sum(p[0] for p in pts) / 3.0, sum(p[1] for p in pts) / 3.0)


def side_lengths(vertices):
    """Side lengths measured directly from vertex coordinates, keyed the
    standard way (a = BC opposite A, b = AC opposite B, c = AB opposite C).
    Use this after `mirror` or any manual transform to get fresh lengths,
    since a mirrored/rotated dict doesn't carry the original 'sides' key
    forward automatically unless you recompute it."""
    A, B, C = vertices['A'], vertices['B'], vertices['C']
    return {
        'a': math.dist(B, C),
        'b': math.dist(A, C),
        'c': math.dist(A, B),
    }


def interior_angles(vertices):
    """The three interior angles in degrees, computed directly from the
    vertex coordinates. Use this as the geometry QA check after rendering:
    compare against the angle the question states — a given obtuse angle
    that comes out under 90 here means a sign or offset error in the
    coordinate math, not a rendering issue."""
    def angle_at(v, o1, o2):
        a1 = (o1[0] - v[0], o1[1] - v[1])
        a2 = (o2[0] - v[0], o2[1] - v[1])
        dot = a1[0] * a2[0] + a1[1] * a2[1]
        n1, n2 = math.hypot(*a1), math.hypot(*a2)
        cos_a = max(-1.0, min(1.0, dot / (n1 * n2)))
        return math.degrees(math.acos(cos_a))
    A, B, C = vertices['A'], vertices['B'], vertices['C']
    return {
        'A': angle_at(A, B, C),
        'B': angle_at(B, A, C),
        'C': angle_at(C, A, B),
    }


def mirror(vertices, axis='vertical', translate=(0.0, 0.0)):
    """A mirrored/reflected copy of a triangle — a second congruent triangle
    for a shared-diagram SSDD panel, an ambiguous-case (SSA) pair, or a
    congruence proof.

    Reflects each vertex about the vertical or horizontal line through the
    triangle's own centroid (so the mirror lands exactly on the original —
    combine with `translate` to move it beside the original instead), then
    shifts by `translate`. `axis='vertical'` flips left-right (mirrors x);
    `axis='horizontal'` flips top-bottom (mirrors y).
    """
    if axis not in ('vertical', 'horizontal'):
        raise ValueError("axis must be 'vertical' or 'horizontal'")
    cx, cy = centroid(vertices)
    out = {}
    for k in ('A', 'B', 'C'):
        x, y = vertices[k]
        if axis == 'vertical':
            x = 2 * cx - x
        else:
            y = 2 * cy - y
        out[k] = (x + translate[0], y + translate[1])
    out['sides'] = dict(vertices.get('sides', side_lengths(vertices)))
    return out


def label_anchors(vertices, vertex_offset=0.25, side_offset=0.25):
    """Anchor points for vertex labels and side-midpoint labels, each pushed
    outward from the centroid so the label clears the triangle's own edges
    instead of sitting on top of them.

    Returns a dict with one entry per vertex ('A', 'B', 'C') and one per
    side, keyed by its two vertices in alphabetical order ('ab', 'ac', 'bc').
    `vertex_offset` and `side_offset` are distances in the same unit as the
    triangle's coordinates.
    """
    cx, cy = centroid(vertices)
    out = {}
    for k in ('A', 'B', 'C'):
        x, y = vertices[k]
        dx, dy = x - cx, y - cy
        d = math.hypot(dx, dy) or 1.0
        out[k] = (x + dx / d * vertex_offset, y + dy / d * vertex_offset)
    for pair in ('AB', 'AC', 'BC'):
        p1, p2 = vertices[pair[0]], vertices[pair[1]]
        mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
        dx, dy = mx - cx, my - cy
        d = math.hypot(dx, dy) or 1.0
        out[pair.lower()] = (mx + dx / d * side_offset, my + dy / d * side_offset)
    return out


def tick_marks(vertices, side, count=1, length=0.08, gap=0.05):
    """Endpoints for the short perpendicular dashes that mark a side as
    equal to another (or as carrying a given length).

    `side` is a two-letter vertex pair, e.g. `'AB'`. Returns a list of
    `count` (start, end) point pairs — 1 or 2 short segments, each
    perpendicular to the side, centred on its midpoint (`count=1`) or spaced
    either side of it (`count=2`, the standard "these two sides match, this
    pair matches separately" double-tick). `length` is each dash's own
    length; `gap` is the spacing between the two dashes when `count=2`.
    """
    if count not in (1, 2):
        raise ValueError("count must be 1 or 2")
    p1, p2 = vertices[side[0]], vertices[side[1]]
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    seg_len = math.hypot(dx, dy)
    ux, uy = dx / seg_len, dy / seg_len   # unit vector along the side
    px, py = -uy, ux                      # unit vector perpendicular to it
    mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
    if count == 1:
        centres = [(mx, my)]
    else:
        centres = [
            (mx - ux * gap / 2.0, my - uy * gap / 2.0),
            (mx + ux * gap / 2.0, my + uy * gap / 2.0),
        ]
    return [
        ((cx - px * length / 2.0, cy - py * length / 2.0),
         (cx + px * length / 2.0, cy + py * length / 2.0))
        for cx, cy in centres
    ]


def angle_badge_point(vertices, vertex, distance=0.3):
    """A point near `vertex`, along its internal angle bisector, for placing
    a coloured angle-value badge or label — close enough to read as
    labelling that angle, not the opposite side.

    `vertex` is 'A', 'B' or 'C'. `distance` is how far from the vertex, in
    the triangle's own coordinate unit, to place the point.
    """
    if vertex not in ('A', 'B', 'C'):
        raise ValueError("vertex must be 'A', 'B' or 'C'")
    others = [k for k in ('A', 'B', 'C') if k != vertex]
    v = vertices[vertex]
    dirs = []
    for k in others:
        p = vertices[k]
        dx, dy = p[0] - v[0], p[1] - v[1]
        d = math.hypot(dx, dy) or 1.0
        dirs.append((dx / d, dy / d))
    bx = sum(d[0] for d in dirs)
    by = sum(d[1] for d in dirs)
    bl = math.hypot(bx, by) or 1.0
    return (v[0] + bx / bl * distance, v[1] + by / bl * distance)


if __name__ == '__main__':
    # Self-check: a 3-4-5 right triangle built two ways should agree, and
    # its right angle should come out as 90 degrees regardless of how it
    # was built. This is the geometry-QA idea from the SKILL.md, run on the
    # module itself.
    t_sss = triangle_sss(5, 4, 3)   # a=BC=5 is the hypotenuse -> right angle at A
    angles = interior_angles(t_sss)
    assert abs(angles['A'] - 90.0) < 1e-6, angles

    t_sas = triangle_sas(p=3, theta_deg=90, q=4)  # AB=3, AC=4, angle A=90
    assert abs(interior_angles(t_sas)['A'] - 90.0) < 1e-6
    assert abs(t_sas['sides']['a'] - 5.0) < 1e-9   # BC via cosine rule = 5

    m = mirror(t_sss, axis='vertical')
    assert abs(side_lengths(m)['a'] - 5.0) < 1e-9   # mirroring preserves lengths

    anchors = label_anchors(t_sss)
    assert set(anchors) == {'A', 'B', 'C', 'ab', 'ac', 'bc'}

    ticks = tick_marks(t_sss, 'AB', count=2)
    assert len(ticks) == 2

    bp = angle_badge_point(t_sss, 'C', distance=0.3)
    assert math.hypot(bp[0] - t_sss['C'][0], bp[1] - t_sss['C'][1]) - 0.3 < 1e-6

    print('All checks passed.')
