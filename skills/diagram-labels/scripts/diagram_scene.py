"""
diagram_scene.py -- draw geometry-only diagrams and record where their labels
belong, as fractional (0-1) coordinates within the image.

Why fractional coordinates: the overlay step (see references/docx-overlay.md
and references/pptx-overlay.md) places the diagram image at whatever size and
position the target document needs, then computes each label's absolute
position as `image_position + fraction * image_size`. Because the fraction is
computed here from the plot's own axis limits -- not from pixels, not from
guessed offsets -- it stays exact no matter how the image is later resized or
where it lands on the page.

Typical use for a new shape:

    from diagram_scene import Scene, extrude, bbox_for_prism, polygon_centroid, outward_normal_for_edge

    cross = [(0,0), (8,0), (8,4), (0,4)]   # a rectangle cross-section, cm
    length = 6
    xlim, ylim = bbox_for_prism(cross, length, pad=1.6)
    sc = Scene(xlim=xlim, ylim=ylim, px_width=900)
    front, back, dx, dy = extrude(sc, cross, length)

    cen = polygon_centroid(front)
    mid = ((front[0][0]+front[1][0])/2, front[0][1])
    sc.add_label('8 cm', mid, outward_normal_for_edge(front[0], front[1], cen))

    sc.save('diagrams/my_prism.png')   # also writes diagrams/my_prism.json

Draw every diagram THIS way -- geometry only, no text baked into the pixels.
Then use scripts/label_debug_overlay.py to sanity-check label placement
before ever touching Word or PowerPoint, and only then follow
references/docx-overlay.md or references/pptx-overlay.md to place the real,
editable labels in the target document.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math, json

ANGLE_DEG = 35        # default oblique angle for prism extrusion, degrees
FORESHORTEN = 0.5      # foreshortening factor along that angle (cavalier-style)
DPI = 150


def _depth_vec(length, angle_deg=ANGLE_DEG):
    a = math.radians(angle_deg)
    return length * FORESHORTEN * math.cos(a), length * FORESHORTEN * math.sin(a)


class Scene:
    """A drawing canvas with a FIXED data coordinate system (xlim/ylim set
    once, axes filling the whole figure with no autoscale padding), so a
    label's fractional position is exact regardless of final image size.

    Work in real-world units (cm, etc.) as the data coordinates -- it makes
    every geometry call below read as the actual measurements of the shape.
    """
    def __init__(self, xlim, ylim, px_width=900):
        self.xlim = xlim
        self.ylim = ylim
        xr = xlim[1] - xlim[0]
        yr = ylim[1] - ylim[0]
        self.px_width = px_width
        self.px_height = int(round(px_width * (yr / xr)))
        self.fig = plt.figure(figsize=(px_width / DPI, self.px_height / DPI), dpi=DPI)
        self.ax = self.fig.add_axes([0, 0, 1, 1])   # no margin -- axes == whole figure
        self.ax.set_xlim(*xlim)
        self.ax.set_ylim(*ylim)
        self.ax.set_aspect('equal')                  # safe only because figsize already
        self.ax.axis('off')                           # matches xlim/ylim's aspect ratio
        self.labels = []   # each: {text, fx, fy, align}

    def line(self, p1, p2, dashed=False, lw=2.0, color='black'):
        style = (0, (5, 4)) if dashed else '-'
        self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], linestyle=style, lw=lw,
                     color=color, solid_capstyle='round')

    def polyline(self, pts, dashed=False, lw=2.0, color='black'):
        """One continuous line through every point -- use this (not repeated
        `line` calls) for anything that should dash as a single run, e.g. an
        arc. A dash pattern restarted on every tiny segment renders as solid."""
        style = (0, (5, 4)) if dashed else '-'
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        self.ax.plot(xs, ys, linestyle=style, lw=lw, color=color, solid_capstyle='round')

    def polygon(self, pts, dashed=False, lw=2.0, color='black'):
        n = len(pts)
        for i in range(n):
            self.line(pts[i], pts[(i + 1) % n], dashed=dashed, lw=lw, color=color)

    def right_angle_mark(self, corner, d1, d2, size=0.35):
        """d1, d2: direction vectors (need not be unit) from corner along the two edges."""
        def norm(v):
            m = math.hypot(*v)
            return (v[0] / m, v[1] / m) if m else (0, 0)
        u1, u2 = norm(d1), norm(d2)
        p1 = (corner[0] + u1[0] * size, corner[1] + u1[1] * size)
        p2 = (p1[0] + u2[0] * size, p1[1] + u2[1] * size)
        p3 = (corner[0] + u2[0] * size, corner[1] + u2[1] * size)
        self.line(p1, p2, lw=1.3); self.line(p2, p3, lw=1.3)

    def add_label(self, text, point, normal, offset=0.55):
        """Record a label at `point`, pushed outward along `normal` by `offset`
        data units. `normal` need not be a unit vector. This does NOT draw
        anything on the image -- it only records the fractional position for
        the overlay step, which is the whole point: the diagram stays a clean
        geometry-only image with no text baked in.

        Call this for EVERY label before `save()`. Check the result with
        scripts/label_debug_overlay.py -- collisions with lines or other
        labels are much cheaper to catch here than after building a docx/pptx.
        """
        m = math.hypot(*normal)
        nx, ny = (normal[0] / m, normal[1] / m) if m else (0, 1)
        x = point[0] + nx * offset
        y = point[1] + ny * offset
        fx = (x - self.xlim[0]) / (self.xlim[1] - self.xlim[0])
        fy = 1 - (y - self.ylim[0]) / (self.ylim[1] - self.ylim[0])   # flip: image y is top-down
        if nx > 0.4: align = 'left'          # pushed mostly right -> anchor its left edge at the point
        elif nx < -0.4: align = 'right'      # pushed mostly left -> anchor its right edge at the point
        else: align = 'center'
        self.labels.append({'text': text, 'fx': round(fx, 4), 'fy': round(fy, 4), 'align': align})

    def save(self, path):
        """Writes the PNG plus a same-named .json manifest (image size + labels).
        The overlay step and the debug tool both read that manifest."""
        self.fig.savefig(path, dpi=DPI)
        plt.close(self.fig)
        manifest = {'image': path, 'px_width': self.px_width, 'px_height': self.px_height,
                    'labels': self.labels}
        with open(path.replace('.png', '.json'), 'w') as f:
            json.dump(manifest, f, indent=2)
        return manifest


def polygon_centroid(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return (sum(xs) / len(xs), sum(ys) / len(ys))


def outward_normal_for_edge(p1, p2, centroid):
    """A normal to edge p1->p2 pointing away from `centroid` -- the natural
    default direction to push a side label. For a label that ends up
    colliding with another line anyway (common on the edge of a shape facing
    the same direction as the extrusion), override with an explicit direction
    and a bigger offset rather than fighting this heuristic -- see
    references/label-placement.md."""
    ex, ey = p2[0] - p1[0], p2[1] - p1[1]
    n1 = (-ey, ex); n2 = (ey, -ex)
    mid = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    d1 = (mid[0] + n1[0] - centroid[0]) ** 2 + (mid[1] + n1[1] - centroid[1]) ** 2
    d2 = (mid[0] + n2[0] - centroid[0]) ** 2 + (mid[1] + n2[1] - centroid[1]) ** 2
    return n1 if d1 > d2 else n2


def bbox_for_prism(cross, length, origin=(0, 0), pad=1.6, extra_top=0.0,
                    extra_right=0.0, angle_deg=None):
    """Compute a Scene's xlim/ylim for an extruded prism BEFORE drawing it,
    so the axes exactly fit the shape (front face + extruded back face) with
    a fixed padding margin -- avoids the wasted whitespace that comes from
    guessing generous limits up front."""
    ox, oy = origin
    front = [(x + ox, y + oy) for x, y in cross]
    dx, dy = _depth_vec(length, angle_deg) if angle_deg is not None else _depth_vec(length)
    back = [(x + dx, y + dy) for x, y in front]
    xs = [p[0] for p in front + back]; ys = [p[1] for p in front + back]
    return (min(xs) - pad, max(xs) + pad + extra_right), (min(ys) - pad, max(ys) + pad + extra_top)


def extrude(sc, cross_pts, length, origin=(0, 0), connectors=True, angle_deg=None):
    """Draw an extruded prism from a 2D cross-section polygon (list of (x,y),
    convex or concave -- concave works fine since this only draws outlines,
    never a filled polygon). Front face solid, back face dashed (hidden),
    depth connectors solid. Returns (front_pts, back_pts, dx, dy) in data
    coordinates for you to compute label positions from.

    If the cross-section has an edge whose own slope is close to ANGLE_DEG,
    that edge's front and back copies will nearly overlap on screen -- pass a
    different `angle_deg` for that one diagram rather than fighting it."""
    ox, oy = origin
    front = [(x + ox, y + oy) for x, y in cross_pts]
    dx, dy = _depth_vec(length, angle_deg) if angle_deg is not None else _depth_vec(length)
    back = [(x + dx, y + dy) for x, y in front]
    sc.polygon(front, dashed=False, lw=2.2)
    sc.polygon(back, dashed=True, lw=1.6)
    if connectors:
        for f, b in zip(front, back):
            sc.line(f, b, dashed=False, lw=2.2)
    return front, back, dx, dy


def draw_cylinder(sc, radius, height, origin=(0, 0)):
    """Upright cylinder: two ellipses (rx=radius, ry=radius*0.32, the standard
    textbook squash) joined by tangent verticals. The bottom ellipse's near
    arc (visible, below its own centre) is solid; its far arc (behind the
    body) is dashed. Returns a dict of useful reference points (top_center,
    bot_center, left, right, top_left, top_right, radius, ry) for placing
    radius/diameter/height labels and helper lines."""
    cx, cy = origin
    ry = radius * 0.32
    top_cy = cy + height
    t = np.linspace(0, 2 * math.pi, 100)

    def ellipse_pts(cyc):
        return [(cx + radius * math.cos(a), cyc + ry * math.sin(a)) for a in t]

    top = ellipse_pts(top_cy)
    bot = ellipse_pts(cy)
    sc.polyline(top, dashed=False, lw=2.0)
    near_arc, far_arc = [], []
    for i, a in enumerate(t):
        (near_arc if math.sin(a) < 0 else far_arc).append(bot[i])
    sc.polyline(near_arc, dashed=False, lw=2.0)
    sc.polyline(far_arc, dashed=True, lw=1.6)
    left_top = (cx - radius, top_cy); left_bot = (cx - radius, cy)
    right_top = (cx + radius, top_cy); right_bot = (cx + radius, cy)
    sc.line(left_top, left_bot, dashed=False, lw=2.0)
    sc.line(right_top, right_bot, dashed=False, lw=2.0)
    return {'top_center': (cx, top_cy), 'bot_center': (cx, cy), 'radius': radius, 'ry': ry,
            'left': (cx - radius, cy), 'right': (cx + radius, cy),
            'top_left': left_top, 'top_right': right_top}
