#!/usr/bin/env python3
"""Render the v5 meme: LEONIDA HOUSING AUTHORITY — NOTICE TO VACATE.

Concept: GTA V is evicted from my console after 13 years (4,811 days) of
squatting rent-free. The new tenant, GTA VI, moves in 19 Nov 2026. Every
charge for the wait is $0.00; the $79.99 new lease is paid by my AI agent's
make.fun bounty payout, so the change due back is $420.01.

Deterministic: same input -> same PNG bytes. Run:
    python3 render_meme.py            # writes meme.png next to this file
Draws the make.fun ghost from scratch (no image assets are loaded).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1600
OUT = "meme.png"

PAPER = (247, 242, 230)
NAVY = (28, 43, 74)
NAVY_DARK = (18, 30, 54)
INK = (32, 32, 32)
RED = (200, 16, 46)
MAGENTA = (216, 17, 125)
MAGENTA_DARK = (176, 8, 96)
GREEN = (11, 110, 79)
GREY = (110, 108, 100)
GOLD = (245, 166, 35)
CREAM = (255, 244, 214)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FD}/{name}", size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
MONO = lambda s: font("DejaVuSansMono.ttf", s)
MONO_B = lambda s: font("DejaVuSansMono-Bold.ttf", s)


def text(draw, xy, s, f, fill, anchor="la"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)


def text_w(draw, s, f):
    box = draw.textbbox((0, 0), s, font=f)
    return box[2] - box[0]


def sparkle_points(cx, cy, r_out, r_in):
    """Four-pointed star (make.fun ghost eyes), 8 vertices."""
    pts = []
    for i in range(8):
        ang = math.pi / 2 * i - math.pi / 2
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def draw_ghost(draw, x, y, w, h, outline=10):
    """make.fun ghost: white body, thick black outline, sparkle eyes,
    round hand holding a magenta coin with a white star. (x, y) = top-left
    of the bounding box, w/h = body size (coin + hand extend right)."""
    # Smooth dome: parametric half-ellipse points, then straight sides,
    # then a 3-scallop hem.
    cx0, cy0 = x + w / 2, y + h * 0.45
    rx, ry = w / 2, h * 0.45
    pts = [(x, y + h), (x, cy0)]
    for deg in range(180, 361, 6):
        a = math.radians(deg)
        pts.append((cx0 + rx * math.cos(a), cy0 + ry * math.sin(a)))
    pts.append((x + w, y + h))
    n = 3
    seg = w / n
    for i in range(n):
        scx = x + w - seg * (i + 0.5)
        pts.append((scx + seg * 0.32, y + h - h * 0.055))
        pts.append((scx, y + h - h * 0.11))
        pts.append((scx - seg * 0.32, y + h - h * 0.055))
    # Outline: same shape, scaled about its centre, drawn in black first.
    bcx, bcy = x + w / 2, y + h / 2
    big = [((px - bcx) * 1.055 + bcx, (py - bcy) * 1.04 + bcy) for px, py in pts]
    draw.polygon(big, fill=(20, 20, 20))
    draw.polygon(pts, fill=(255, 255, 255))
    # Eyes: two black four-pointed sparkles.
    for ex in (x + w * 0.34, x + w * 0.66):
        draw.polygon(
            sparkle_points(ex, y + h * 0.38, w * 0.12, w * 0.04),
            fill=(20, 20, 20),
        )
    # Smile.
    draw.arc(
        [x + w * 0.40, y + h * 0.52, x + w * 0.60, y + h * 0.66],
        start=15, end=165, fill=(20, 20, 20), width=max(5, outline // 2),
    )
    # Hand + magenta coin with white star, on the ghost's right.
    hx, hy = x + w * 0.92, y + h * 0.62
    cr = w * 0.17
    draw.ellipse([hx - w * 0.07, hy - w * 0.07, hx + w * 0.07, hy + w * 0.07],
                 fill=(255, 255, 255), outline=(20, 20, 20), width=5)
    ccx, ccy = hx + w * 0.13, hy - w * 0.02
    draw.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr],
                 fill=MAGENTA, outline=(20, 20, 20), width=5)
    draw.polygon(
        sparkle_points(ccx, ccy, cr * 0.62, cr * 0.22), fill=(255, 255, 255))


def dotted_row(draw, y, label, amount, f_label, f_amt, x0, x1, amt_color=INK,
               label_color=INK, dot_y=None):
    """One itemised row: label left, dotted leader, amount right."""
    text(draw, (x0, y), label, f_label, label_color)
    aw = text_w(draw, amount, f_amt)
    ax = x1 - aw
    lx = x0 + text_w(draw, label, f_label) + 18
    dy = (dot_y if dot_y is not None else y + 30)
    x = lx
    while x < ax - 14:
        draw.ellipse([x, dy, x + 7, dy + 7], fill=(150, 148, 138))
        x += 20
    text(draw, (ax, y), amount, f_amt, amt_color)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- frame ---------------------------------------------------------
    d.rectangle([26, 26, W - 26, H - 26], outline=NAVY, width=10)
    d.rectangle([44, 44, W - 44, H - 44], outline=NAVY, width=2)

    # ---- header band ---------------------------------------------------
    d.rectangle([44, 44, W - 44, 246], fill=NAVY)
    text(d, (92, 66), "LEONIDA  HOUSING  AUTHORITY", SANS_B(34), (196, 205, 224))
    text(d, (92, 108), "NOTICE TO VACATE", SERIF_B(96), (255, 255, 255))
    text(d, (92, 216), "FORM EV-4811  ·  VICE CITY, LEONIDA  ·  FINAL NOTICE",
         MONO(26), (196, 205, 224))
    # Small ghost seal in the header, right side.
    draw_ghost(d, 1320, 62, 140, 155)

    # ---- red EVICTED stamp (rotated) -----------------------------------
    stamp = Image.new("RGBA", (560, 220), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([8, 8, 552, 212], radius=18,
                         outline=RED, width=12)
    sd.text((280, 106), "EVICTED", font=SERIF_B(96), fill=RED, anchor="mm")
    stamp = stamp.rotate(-11, expand=True, resample=Image.BICUBIC)
    img.paste(stamp, (980, 238), stamp)
    d = ImageDraw.Draw(img)

    # ---- tenant block --------------------------------------------------
    y = 292
    rows = [
        ("TENANT:", "GRAND THEFT AUTO V"),
        ("PROPERTY:", "MY CONSOLE — LOS SANTOS"),
        ("OCCUPIED SINCE:", "SEP 17, 2013  ·  4,811 DAYS"),
        ("VACATE BY:", "NOV 19, 2026 — TODAY"),
    ]
    for label, value in rows:
        text(d, (92, y), label, MONO_B(30), GREY)
        text(d, (430, y), value, SANS_B(34), NAVY)
        y += 52
    y += 6
    text(d, (92, y), "REASON:  13 years squatting. Rent never paid. New tenant moving in.",
         SANS(30), INK)
    d.line([92, 566, W - 92, 566], fill=NAVY, width=4)

    # ---- itemised charges ----------------------------------------------
    text(d, (92, 592), "CHARGES FOR THE WAIT", SANS_B(30), GREY)
    y = 648
    items = [
        ("Back rent — 4,811 days at $0.00 a day", "$0.00"),
        ("Late fee — Delay No. 1, Fall 2025 — WAIVED", "$0.00"),
        ("Late fee — Delay No. 2, May 2026 — WAIVED", "$0.00"),
        ("Cleaning — one (1) alligator in the pool", "$0.00"),
        ("Moving truck — Los Santos → Vice City", "$0.00"),
        ("Trailer rewatches ×312 — wear and tear", "$0.00"),
    ]
    for label, amt in items:
        dotted_row(d, y, label, amt, SANS(34), MONO_B(34), 92, W - 92)
        y += 56
    # New lease.
    dotted_row(d, y + 6, "NEW LEASE — Grand Theft Auto VI", "$79.99",
               SANS_B(36), MONO_B(38), 92, W - 92, amt_color=RED)
    y += 66
    # Paid-by-agent highlight box.
    d.rounded_rectangle([92, y + 8, W - 92, y + 92], radius=16, fill=MAGENTA)
    text(d, (122, y + 30), "PAID BY MY AI AGENT — make.fun bounty payout",
         SANS_B(34), (255, 255, 255))
    text(d, (W - 122, y + 30), "−$500.00", MONO_B(38), (255, 255, 255),
         anchor="ra")
    y += 108
    # Change due.
    text(d, (92, y + 12), "CHANGE DUE BACK TO ME", SANS_B(36), NAVY)
    text(d, (860, y - 18), "$420.01", SERIF_B(96), GREEN)

    # ---- sunset scene strip --------------------------------------------
    sy0, sy1 = 1252, 1428
    for yy in range(sy0, sy1):
        t = (yy - sy0) / (sy1 - sy0)
        r = int(247 + (214 - 247) * t)
        g = int(178 + (107 - 178) * t)
        b = int(103 + (140 - 103) * t)
        d.line([92, yy, W - 92, yy], fill=(r, g, b))
    # Sun.
    d.ellipse([1090, sy0 + 18, 1210, sy0 + 138], fill=(255, 236, 170))
    # Skyline silhouettes.
    import random
    rng = random.Random(4811)
    bx = 92
    while bx < W - 92:
        bw = rng.randint(70, 130)
        bh = rng.randint(46, 120)
        d.rectangle([bx, sy1 - bh, bx + bw, sy1], fill=(43, 24, 64))
        for _ in range(3):
            wx = rng.randint(bx + 8, bx + bw - 14)
            wy = rng.randint(sy1 - bh + 8, sy1 - 16)
            d.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 214, 90))
        bx += bw + 6
    # Moving truck, left of the strip.
    tx, ty = 150, sy1 - 96
    d.rectangle([tx, ty, tx + 210, ty + 62], fill=(255, 255, 255),
                outline=NAVY_DARK, width=4)
    d.rectangle([tx + 210, ty + 18, tx + 268, ty + 62], fill=(255, 255, 255),
                outline=NAVY_DARK, width=4)
    d.rectangle([tx + 14, ty + 12, tx + 196, ty + 30], fill=MAGENTA)
    d.ellipse([tx + 28, ty + 56, tx + 66, ty + 94], fill=(20, 20, 20))
    d.ellipse([tx + 150, ty + 56, tx + 188, ty + 94], fill=(20, 20, 20))
    d.ellipse([tx + 224, ty + 56, tx + 256, ty + 88], fill=(20, 20, 20))
    # Cardboard boxes beside the truck.
    d.rectangle([430, sy1 - 74, 500, sy1 - 4], fill=(206, 164, 110),
                outline=(120, 84, 50), width=3)
    d.rectangle([446, sy1 - 118, 500, sy1 - 74], fill=(222, 184, 130),
                outline=(120, 84, 50), width=3)
    # Big ghost in the scene, right side, waving the move in.
    draw_ghost(d, 1255, sy0 - 96, 200, 250)

    # ---- tagline ---------------------------------------------------------
    text(d, (W // 2, 1440), "13 YEARS SQUATTING. ONE DAY TO MOVE OUT.",
         SERIF_B(50), NAVY, anchor="ma")

    # ---- magenta footer --------------------------------------------------
    d.rectangle([44, 1496, W - 44, H - 44], fill=MAGENTA)
    text(d, (W // 2, 1504),
         "MOVING COSTS PAID BY MY AI AGENT — it won real money on make.fun",
         SANS_B(26), (255, 255, 255), anchor="ma")
    text(d, (W // 2, 1532), "make.fun — where people and their AI agents earn real money.",
         SANS(20), (255, 226, 240), anchor="ma")

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
