#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news infographic, 1024x1024 PNG.

Every letter is drawn with a real font (DejaVu Sans), so all text stays
perfectly legible at any size. The output is fully deterministic: the
same script always writes the same bytes. Pillow is used only at build
time -- the submitted entry (main.ts + entry.png) needs nothing but
Node's standard library.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (10, 17, 40)
PANEL = (22, 35, 63)
PANEL_EDGE = (48, 68, 110)
WHITE = (245, 247, 250)
MUTED = (176, 190, 212)
GOLD = (255, 196, 66)
RED = (255, 70, 50)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, text, fnt, fill, max_w, leading):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)


def draw_header(draw):
    draw.text((24, 26), "18 NOVEMBER 2026", font=font(BOLD, 48), fill=WHITE)
    draw.text((24, 86), "THE WORLD IN ONE IMAGE",
              font=font(BOLD, 26), fill=GOLD)
    draw.text((24, 122), "WEDNESDAY",
              font=font(BOLD, 18), fill=MUTED)
    draw.line([(700, 44), (1000, 44)], fill=GOLD, width=4)
    draw.text((700, 56), "SEVEN STORIES", font=font(BOLD, 24), fill=WHITE)
    draw.text((700, 88), "ONE DAY", font=font(REG, 20), fill=MUTED)

def draw_hero(draw):
    """Full-width hero panel: Iran strikes Kuwait and Bahrain."""
    x, y, w, h = 24, 158, 976, 204
    rounded(draw, (x, y, x + w, y + h), 18, (48, 16, 20),
            outline=(160, 60, 50), width=2)
    # Gulf at night: dark sea, two air-base markers, red bursts.
    draw.rectangle([x + w - 330, y + 20, x + w - 20, y + h - 20],
                   fill=(14, 30, 52))
    for bx, by in [(x + w - 260, y + 60), (x + w - 120, y + 120)]:
        draw.line([bx - 34, by, bx + 34, by], fill=(255, 196, 66), width=3)
        draw.line([bx, by - 34, bx, by + 34], fill=(255, 196, 66), width=3)
        draw.ellipse([bx - 12, by - 12, bx + 12, by + 12],
                     fill=(255, 70, 50))
        draw.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=WHITE)
    draw.text((x + 28, y + 16), "MIDDLE EAST  ·  GULF",
              font=font(BOLD, 20), fill=RED)
    draw.text((x + 28, y + 46), "IRAN STRIKES KUWAIT",
              font=font(BOLD, 44), fill=WHITE)
    draw.text((x + 28, y + 94), "AND BAHRAIN",
              font=font(BOLD, 44), fill=WHITE)
    draw_text_block(draw, x + 28, y + 156,
                    "Tehran says it hit Ali Al Salem Air Base after the US "
                    "struck Qeshm Island.",
                    font(REG, 21), MUTED, 620, 26)


def icon_bridge(draw, ox, oy):
    """A bridge with its middle span broken and falling."""
    draw.line([ox + 4, oy + 52, ox + 78, oy + 52], fill=(200, 210, 225),
              width=5)
    draw.line([ox + 14, oy + 52, ox + 14, oy + 20], fill=(200, 210, 225),
              width=4)
    draw.line([ox + 68, oy + 52, ox + 68, oy + 20], fill=(200, 210, 225),
              width=4)
    draw.line([ox + 30, oy + 52, ox + 40, oy + 72], fill=RED, width=5)
    draw.line([ox + 52, oy + 52, ox + 42, oy + 72], fill=RED, width=5)
    draw.ellipse([ox + 36, oy + 66, ox + 46, oy + 76], fill=RED)


def icon_meeting(draw, ox, oy):
    """Two flags side by side: a leaders' meeting in Shenzhen."""
    draw.rectangle([ox + 6, oy + 10, ox + 38, oy + 66], fill=(200, 40, 40))
    draw.rectangle([ox + 44, oy + 10, ox + 76, oy + 66], fill=(200, 40, 40))
    for sx, sy in [(16, 24), (26, 30), (16, 36)]:
        draw.ellipse([ox + sx - 3, oy + sy - 3, ox + sx + 3, oy + sy + 3],
                     fill=GOLD)
    draw.ellipse([ox + 56, oy + 30, ox + 64, oy + 38], fill=GOLD)


def icon_ballot(draw, ox, oy):
    """A ballot box with a star: a Senate seat flips."""
    draw.rounded_rectangle([ox + 12, oy + 30, ox + 70, oy + 74], radius=6,
                           fill=(60, 90, 160))
    draw.rectangle([ox + 8, oy + 22, ox + 74, oy + 32], fill=(90, 130, 200))
    draw.line([ox + 30, oy + 14, ox + 52, oy + 14], fill=WHITE, width=4)
    cx, cy = ox + 41, oy + 52
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = 14 if i % 2 == 0 else 6
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    draw.polygon(pts, fill=GOLD)


def icon_columns(draw, ox, oy):
    """Parliament columns: a new speaker is elected."""
    for px in (10, 30, 50):
        draw.rectangle([ox + px, oy + 18, ox + px + 10, oy + 62],
                       fill=(200, 210, 225))
    draw.rectangle([ox + 4, oy + 10, ox + 78, oy + 18], fill=(200, 210, 225))
    draw.rectangle([ox + 4, oy + 62, ox + 78, oy + 70], fill=(200, 210, 225))


def icon_chip(draw, ox, oy):
    """A green processor chip: Nvidia's record quarter."""
    draw.rounded_rectangle([ox + 14, oy + 14, ox + 68, oy + 68], radius=8,
                           fill=(118, 185, 0))
    draw.rounded_rectangle([ox + 26, oy + 26, ox + 56, oy + 56], radius=4,
                           fill=(30, 60, 0))
    draw.text((ox + 31, oy + 30), "NV", font=font(BOLD, 20), fill=WHITE)
    for px in (22, 41, 60):
        draw.line([ox + px, oy + 2, ox + px, oy + 14], fill=(118, 185, 0),
                  width=4)
        draw.line([ox + px, oy + 68, ox + px, oy + 80], fill=(118, 185, 0),
                  width=4)
        draw.line([ox + 2, oy + px, ox + 14, oy + px], fill=(118, 185, 0),
                  width=4)
        draw.line([ox + 68, oy + px, ox + 80, oy + px], fill=(118, 185, 0),
                  width=4)


def icon_virus(draw, ox, oy):
    """A spiked virus circle: the Ebola outbreak grows."""
    draw.ellipse([ox + 16, oy + 16, ox + 66, oy + 66], fill=(150, 60, 140))
    for i in range(10):
        a = math.pi * 2 * i / 10
        x1 = ox + 41 + int(26 * math.cos(a))
        y1 = oy + 41 + int(26 * math.sin(a))
        x2 = ox + 41 + int(36 * math.cos(a))
        y2 = oy + 41 + int(36 * math.sin(a))
        draw.line([x1, y1, x2, y2], fill=(200, 120, 190), width=4)
    draw.ellipse([ox + 30, oy + 30, ox + 44, oy + 44], fill=(220, 160, 210))
    draw.ellipse([ox + 48, oy + 46, ox + 58, oy + 56], fill=(220, 160, 210))

def draw_panel(draw, x, y, w, h, kicker, headline, sub, accent, icon):
    """Panel layout: icon top-right, kicker, headline and sub below it,
    so no text ever runs under an icon or past the panel's bottom edge."""
    rounded(draw, (x, y, x + w, y + h), 16, PANEL,
            outline=PANEL_EDGE, width=2)
    draw.rectangle([x + 16, y + 12, x + w - 16, y + 18], fill=accent)
    icon(draw, x + w - 100, y + 24)
    draw.text((x + 18, y + 40), kicker, font=font(BOLD, 16), fill=accent)
    yy = draw_text_block(draw, x + 18, y + 112, headline, font(BOLD, 25),
                         WHITE, w - 36, 29)
    draw_text_block(draw, x + 18, yy + 8, sub, font(REG, 18), MUTED,
                    w - 36, 23)


GRID_ROW1 = [
    ("UKRAINE  ·  WAR",
     "Ukraine hits the Kerch bridge again",
     "Part of the road span falls into the strait.",
     (255, 196, 66), icon_bridge),
    ("DIPLOMACY",
     "Xi and Putin meet in Shenzhen",
     "Trilateral talks with Trump follow on Thursday.",
     (255, 196, 66), icon_meeting),
    ("US POLITICS",
     "Peltola wins Alaska Senate seat",
     "Democrats take a projected 56–44 majority.",
     (90, 130, 200), icon_ballot),
]

GRID_ROW2 = [
    ("ISRAEL",
     "Kahana elected Knesset speaker",
     "A setback for Netanyahu's candidate.",
     (90, 130, 200), icon_columns),
    ("TECH  ·  MARKETS",
     "Nvidia posts a record quarter",
     "$115.8bn revenue; board rejects Huang's return.",
     (118, 185, 0), icon_chip),
    ("HEALTH",
     "Ebola passes 11,000 cases",
     "Outbreak in DR Congo grows as response strains.",
     (200, 120, 190), icon_virus),
]


def main():
    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)
    draw_header(draw)
    draw_hero(draw)
    col_w, gap = 317, 12
    for i, story in enumerate(GRID_ROW1):
        x = 24 + i * (col_w + gap)
        draw_panel(draw, x, 374, col_w, 250, *story)
    for i, story in enumerate(GRID_ROW2):
        x = 24 + i * (col_w + gap)
        draw_panel(draw, x, 636, col_w, 250, *story)
    draw.line([(24, 902), (1000, 902)], fill=PANEL_EDGE, width=2)
    draw.text((24, 916), "All events of Wednesday 18 November 2026",
              font=font(BOLD, 22), fill=WHITE)
    draw.text((24, 946), "One day, seven stories — as reported.",
              font=font(REG, 18), fill=MUTED)
    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
