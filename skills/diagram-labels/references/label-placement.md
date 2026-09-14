# Placing labels without collisions

`Scene.add_label`'s default (push outward from the shape's centroid) gets
most labels right the first time, but not all of them — and a label sitting
on top of a line, or two labels overlapping each other, is worse than no
diagram at all for a printed worksheet. Always run
`scripts/label_debug_overlay.py` on every new diagram and look at it before
building it into a document. These are the collision patterns actually seen
building diagrams this way, and what fixed each one.

## The centroid-outward push can point straight at other geometry

For a prism, the extrusion direction is a fixed diagonal (up and to the
right, by default). An edge whose outward normal happens to point in roughly
that same direction gets pushed *into* the extruded back face and its
connector lines instead of into clear space — this hit a triangular prism's
hypotenuse directly. Fix: for that specific label, override the direction
and use a bigger offset, or better, move the label onto the corresponding
*back-face* edge instead (that copy of the line sits out in open space,
beyond the whole silhouette).

## A cross-section edge can coincide with the extrusion angle

If a diagram's own geometry has an edge sloped at close to `ANGLE_DEG`
(35° by default), that edge's front and back copies land almost on top of
each other on screen — this happened with a pentagon "house" roof edge at
~37°. It reads as a confusing doubled line, and any label near it collides
with two lines at once. Fix: pass a different `angle_deg` to `extrude()`
(and to `bbox_for_prism()`, so the bounding box still fits) for that one
diagram — there's no need to keep every diagram at the same angle.

## Two labels can land close together even when neither is "wrong"

A radius label pushed up and a diameter label pushed down from the same
horizontal reference line can still end up visually close if the shape is
small relative to the label text. Same for a height label and a distractor
length on adjacent parallel edges. The fix is usually just to increase one
label's `offset`, or move one of the two to a different, less crowded edge
of the same shape (e.g. a diameter distractor reads just as well placed
below a cylinder as beside it).

## An interior label can sit too close to the edge it's near

A label meant to sit inside a shape's face (e.g. an "Area = ..." callout on
a triangular prism's front face) needs a real interior anchor point, not
just a small offset from the shape's centroid — a centroid-relative push can
still land right on a diagonal edge for a lopsided shape. Pick an explicit
interior point by eye (e.g. a point clearly inside the smaller sub-triangle
of a right triangle) rather than trusting the general heuristic here.

## General approach

None of the above needs to be anticipated in advance — draw the diagram,
render the debug overlay, look at it, and fix what's actually wrong. This
loop is cheap (one Python call) compared to catching the same problem after
the labels are built into a docx or pptx.
