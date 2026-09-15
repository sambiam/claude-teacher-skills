"""
label_debug_overlay.py -- draw dots and text at every label's recorded
fractional position, directly on top of the diagram PNG, so you can check
placement (no collisions with lines or other labels) BEFORE ever building a
docx or pptx. Iterating here is one Python call; iterating in the actual
document means a full render-and-inspect cycle each time.

Usage:
    python label_debug_overlay.py diagrams/my_prism.png
    -> writes diagrams/my_prism_debug.png

Requires the same-named .json manifest that Scene.save() writes alongside
the PNG.
"""
import sys, json
from PIL import Image, ImageDraw, ImageFont

def main(path):
    img = Image.open(path).convert('RGB')
    manifest = json.load(open(path.replace('.png', '.json')))
    d = ImageDraw.Draw(img)
    W, H = img.size
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    except Exception:
        font = ImageFont.load_default()
    for lab in manifest['labels']:
        x, y = lab['fx'] * W, lab['fy'] * H
        d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(255, 0, 0))
        d.text((x + 6, y - 9), lab['text'], fill=(0, 0, 200), font=font)
    out = path.replace('.png', '_debug.png')
    img.save(out)
    print(out)

if __name__ == '__main__':
    main(sys.argv[1])
