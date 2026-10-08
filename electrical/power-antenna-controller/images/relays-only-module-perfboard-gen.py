"""Draw the relays-only perfboard layout guide, module build (not to scale), as an SVG.

Untested idea: a placement and wiring guide for relays-only.md, not a measured layout.
Run with: python3 relays-only-module-perfboard-gen.py  (writes 2026-10-08-relays-only-module-perfboard.svg)
"""

W, H = 1100, 880
out = []
def add(s): out.append(s)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def text(x, y, s, size=14, anchor="start", weight="normal", color="#000", style="normal"):
    add(f'<text x="{x}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" '
        f'text-anchor="{anchor}" font-weight="{weight}" font-style="{style}" fill="{color}">{esc(s)}</text>')
def wire(pts, color, w=3):
    p = " ".join(f"{x},{y}" for x, y in pts)
    add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round"/>')
def dot(x, y, color="#000"):
    add(f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/>')
def rect(x, y, w, h, fill="#fff", stroke="#000", sw=2, rx=0, dash=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'
        + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')
def pad(x, y):
    add(f'<circle cx="{x}" cy="{y}" r="6" fill="#fff" stroke="#000" stroke-width="2"/>')
def diode(x, y1, y2, label, color="#000", up=False):
    """Vertical diode between y1 (top) and y2 (bottom). Points down unless up=True."""
    mid = (y1 + y2) / 2
    if not up:
        add(f'<polygon points="{x-9},{mid-8} {x+9},{mid-8} {x},{mid+8}" fill="{color}"/>')
        add(f'<line x1="{x-10}" y1="{mid+8}" x2="{x+10}" y2="{mid+8}" stroke="{color}" stroke-width="3"/>')
    else:
        add(f'<polygon points="{x-9},{mid+8} {x+9},{mid+8} {x},{mid-8}" fill="{color}"/>')
        add(f'<line x1="{x-10}" y1="{mid-8}" x2="{x+10}" y2="{mid-8}" stroke="{color}" stroke-width="3"/>')
    text(x + 13, mid + 5, label, 12)

RED, BLACK, ORANGE, BLUE = "#d01010", "#000000", "#e07000", "#0055cc"
GREEN, PURPLE, GREY, TEAL = "#1f8f2f", "#8a2be2", "#777777", "#008b8b"
BROWN = "#8b4513"   # node X (timer output): must NOT touch the feed
GOLD = "#c89400"    # node G (K1 pin 87)

# lanes / rails (y)
Y12, YU, YA, YR = 90, 125, 150, 175
YFEED, YTRIG, YG = 430, 495, 590

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add(f'<rect width="{W}" height="{H}" fill="#fff"/>')

# board with a dot grid
BX0, BY0, BX1, BY1 = 60, 50, 1020, 650
add('<defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse">'
    '<circle cx="10" cy="10" r="1.6" fill="#c9a96b"/></pattern></defs>')
rect(BX0, BY0, BX1 - BX0, BY1 - BY0, fill="#f6ecd4", stroke="#8a6d3b", sw=2, rx=8)
add(f'<rect x="{BX0}" y="{BY0}" width="{BX1-BX0}" height="{BY1-BY0}" fill="url(#g)"/>')
text(BX0 + 10, BY0 - 12, "Module build: perfboard, top view (placement and wiring guide, not to scale)", 15, weight="bold")

# ---------- car screw terminals (left) ----------
rect(BX0 + 5, Y12 - 20, 55, (YR - Y12) + 40, fill="#2a6fdb", stroke="#123d7a")
rect(BX0 + 5, YG - 20, 55, 40, fill="#2a6fdb", stroke="#123d7a")
for y, lbl in ((Y12, "2"), (YU, "1"), (YA, "4"), (YR, "5"), (YG, "6")):
    pad(BX0 + 45, y)
    text(BX0 + 22, y + 5, lbl, 13, "middle", "bold", "#fff")
text(BX0 - 5, YG + 45, "CAR", 13, "start", "bold")
text(BX0 - 5, YG + 62, "screw terminals", 11)
TX = BX0 + 45

# ---------- antenna screw terminals (right) ----------
AX = BX1 - 45
rect(BX1 - 60, YFEED - 20, 55, (YG - YFEED) + 40, fill="#2a6fdb", stroke="#123d7a")
for y, lbl in ((YFEED, "+12"), (YTRIG, "TRG"), (YG, "GND")):
    pad(AX, y)
    text(BX1 - 18, y + 5, lbl, 11, "middle", "bold", "#fff")
text(BX1 - 62, YG + 45, "ANTENNA", 13, "start", "bold")
text(BX1 - 62, YG + 62, "screw terminals", 11)

# ---------- relays ----------
def relay(x0, name, pins):
    """pins: dict name -> (dx, dy, label, label_anchor) relative to the box."""
    y0, w, h = 210, 150, 150
    rect(x0, y0, w, h, fill="#fdfdfd", stroke="#333", sw=2, rx=6)
    text(x0 + 100, y0 + 140, name, 18, "middle", "bold")
    text(x0 + w / 2, y0 + h + 16, "JQC-3FF 12 V changeover", 11, "middle", color="#555")
    text(x0 + w / 2, y0 + h + 30, "(or Omron G5LE / mini ISO)", 11, "middle", color="#555")
    p = {}
    for k, (dx, dy, lbl, anc) in pins.items():
        p[k] = (x0 + dx, y0 + dy)
        pad(*p[k])
        text(p[k][0] + (10 if anc == "start" else -10), p[k][1] + 5, lbl, 12, anc)
    # coil diode across 85 (cathode) and 86 (anode), on the board next to the relay
    ddx = x0 + 45
    wire([p["p85"], (ddx, p["p85"][1]), (ddx, p["p85"][1] + 20)], GREY, 2)
    wire([p["p86"], (ddx, p["p86"][1]), (ddx, p["p86"][1] - 20)], GREY, 2)
    diode(ddx, p["p85"][1] + 20, p["p86"][1] - 20, "", GREY, up=True)
    return p

COIL = {"p85": (15, 35, "85", "start"), "p86": (15, 115, "86", "start")}
K1 = relay(230, "K1", {**COIL, "c": (75, 15, "30 COM", "start"), "p87": (135, 45, "87 NO", "end"), "p87a": (135, 105, "87a NC", "end")})
K2 = relay(450, "K2", {**COIL, "c": (75, 15, "87 NO", "start"), "p30": (135, 75, "30 COM", "end")})

# timer module (sits on standoffs; short wires to these pads)
TMX0, TMY0, TMW, TMH = 690, 210, 130, 150
rect(TMX0, TMY0, TMW, TMH, fill="#eaf4ff", stroke="#333", sw=2, rx=6, dash="7 5")
text(TMX0 + 80, TMY0 + 100, "timer", 16, "middle", "bold")
text(TMX0 + 80, TMY0 + 116, "module", 12, "middle")
text(TMX0 + 80, TMY0 + 132, "(on standoffs)", 11, "middle", color="#555")
TV, TG, TC, TN = (TMX0 + 15, TMY0 + 35), (TMX0 + 15, TMY0 + 115), (TMX0 + TMW / 2, TMY0 + 15), (TMX0 + TMW - 15, TMY0 + 75)
for (x, y), lbl, anc, dx in ((TV, "VCC", "start", 10), (TG, "GND", "start", 10), (TC, "COM", "start", 10)):
    pad(x, y); text(x + dx, y + 5, lbl, 11, anc)
pad(*TN); text(TN[0], TN[1] - 12, "NO/NC", 11, "middle")

# ---------- wires ----------
# +12 V (fused outside the box) -> K1 30 and K2 87
wire([(TX, Y12), (K2["c"][0], Y12), K2["c"]], RED, 5)
wire([(K1["c"][0], Y12), K1["c"]], RED, 5); dot(K1["c"][0], Y12, RED)
# ground bus
wire([(TX, YG), (AX, YG)], BLACK, 5)
for K in (K1, K2):
    xg = K["p86"][0] - 25
    wire([K["p86"], (xg, K["p86"][1]), (xg, YG)], BLACK, 3); dot(xg, YG)
wire([TG, (TG[0] - 25, TG[1]), (TG[0] - 25, YG)], BLACK, 3); dot(TG[0] - 25, YG)
# feed: K1 87a, K2 30, D2 -> antenna +12
xf1, xf2 = K1["p87a"][0] + 30, K2["p30"][0] + 20
wire([K1["p87a"], (xf1, K1["p87a"][1]), (xf1, YFEED)], ORANGE, 5); dot(xf1, YFEED, ORANGE)
wire([K2["p30"], (xf2, K2["p30"][1]), (xf2, YFEED)], ORANGE, 5); dot(xf2, YFEED, ORANGE)
wire([(xf1, YFEED), (AX, YFEED)], ORANGE, 5)
# A: car 4 -> K1 85
xa = K1["p85"][0] - 45
wire([(TX, YA), (xa, YA), (xa, K1["p85"][1]), K1["p85"]], GREEN, 3)
# U: car 1 -> K2 85 and D1
xu = K2["p85"][0] - 45
xd1 = 634
wire([(TX, YU), (xd1, YU), (xd1, 380)], PURPLE, 3)
wire([(xu, YU), (xu, K2["p85"][1]), K2["p85"]], PURPLE, 3); dot(xu, YU, PURPLE)
diode(xd1, 380, 420, "D1", PURPLE)
wire([(xd1, 420), (xd1, YTRIG)], BLUE, 3); dot(xd1, YTRIG, BLUE)
# R: car 5 -> timer VCC
xr = TV[0] - 20
wire([(TX, YR), (xr, YR), (xr, TV[1]), TV], GREY, 3)
# G: K1 87 -> timer COM (+12 V only while A is on)
YGATE = 195
wire([K1["p87"], (K1["p87"][0] + 22, K1["p87"][1]), (K1["p87"][0] + 22, YGATE), (TC[0], YGATE), TC], GOLD, 4)
text(480, YGATE - 6, "G", 13, weight="bold")
# timer output -> X -> D2 (feed) and D3 (trigger)
XX = TN[0] + 35
wire([TN, (XX, TN[1])], BROWN, 4); dot(XX, TN[1], BROWN)
text(XX + 6, TN[1] - 8, "X", 13, weight="bold")
wire([(XX, TN[1]), (XX, 380)], BROWN, 4); diode(XX, 380, 420, "D2", BROWN); wire([(XX, 420), (XX, YFEED)], ORANGE, 4); dot(XX, YFEED, ORANGE)
xd3 = XX + 45
wire([(XX, TN[1]), (xd3, TN[1]), (xd3, 450)], BROWN, 3)
diode(xd3, 450, 480, "D3", BLUE)
wire([(xd3, 480), (xd3, YTRIG)], BLUE, 3); dot(xd3, YTRIG, BLUE)
# trigger line to the antenna
wire([(xd1, YTRIG), (AX, YTRIG)], BLUE, 3)

# ---------- legend ----------
LX, LY = 70, 700
legend = [(RED, 5, "+12 V permanent (car pin 2, through the 5 A inline fuse outside the box)"),
          (BLACK, 5, "ground"),
          (ORANGE, 5, "antenna feed (+12 V to the antenna)"),
          (BLUE, 3, "antenna trigger"),
          (GREEN, 3, "A: AUTO/UP/MAX (car pin 4)"),
          (PURPLE, 3, "U: UP/MAX (car pin 1)"),
          (GREY, 3, "R: radio on (car pin 5); coil diodes"),
          (GOLD, 4, "G: K1 pin 87 to timer COM (+12 V only while A is on)"),
          (BROWN, 4, "X: timer output (NO or NC) to D2 and D3; crosses the feed without touching it")]
for i, (c, w, lbl) in enumerate(legend):
    col, row = i % 2, i // 2
    x, y = LX + col * 480, LY + row * 26
    add(f'<line x1="{x}" y1="{y}" x2="{x+40}" y2="{y}" stroke="{c}" stroke-width="{w}"/>')
    text(x + 50, y + 5, lbl, 13)
text(LX, LY + 138, "Thick lines (+12 V, ground, feed): 1 mm² / 18 AWG wire on the back of the board. Dots are joints; "
     "lines that cross without a dot don't touch (insulated wire).", 12, style="italic")
text(LX, LY + 156, "Grey diode next to each relay: 1N4007 across the coil, stripe to 85. The timer, the G wire, D2 and D3 are the optional add-on. Untested idea.", 12, style="italic")

add("</svg>")
open("2026-10-08-relays-only-module-perfboard.svg", "w").write("\n".join(out))
