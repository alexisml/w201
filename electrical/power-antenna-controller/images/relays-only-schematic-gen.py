"""Draw the relays-only schematic as a plain SVG (white background, works in GitHub light/dark).

Untested idea: the circuit from relays-only.md.
Run with: python3 relays-only-schematic-gen.py  (writes 2026-10-08-relays-only-schematic.svg)
"""

W, H = 1540, 760
out = []
def add(s): out.append(s)
def line(x1, y1, x2, y2, dash=False, w=2):
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="{w}"'
        + (' stroke-dasharray="6 5"' if dash else '') + '/>')
def poly(*pts):  # polyline wire
    p = " ".join(f"{x},{y}" for x, y in pts)
    add(f'<polyline points="{p}" fill="none" stroke="#000" stroke-width="2"/>')
def rect(x, y, w, h, dash=False, fill="none", sw=2):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#000" stroke-width="{sw}"'
        + (' stroke-dasharray="8 6"' if dash else '') + '/>')
def dot(x, y):
    add(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#000"/>')
def text(x, y, s, size=15, anchor="start", weight="normal", style="normal"):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    add(f'<text x="{x}" y="{y}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" '
        f'text-anchor="{anchor}" font-weight="{weight}" font-style="{style}" fill="#000">{s}</text>')
def diode_down(x, y1, y2, label):
    """Diode pointing down (anode at top), body between y1 and y2."""
    line(x, y1, x, y1 + 8)
    add(f'<polygon points="{x-11},{y1+8} {x+11},{y1+8} {x},{y2-8}" fill="#000"/>')
    line(x - 12, y2 - 8, x + 12, y2 - 8, w=3)
    line(x, y2 - 8, x, y2)
    text(x + 16, (y1 + y2) / 2 + 5, label, 14)
def fuse(x1, x2, y, label):
    rect(x1, y - 9, x2 - x1, 18, fill="#fff")
    line(x1, y, x2, y, w=1)
    text((x1 + x2) / 2, y - 16, label, 14, "middle")
def ground(x, y):
    line(x, y, x, y + 12)
    line(x - 14, y + 12, x + 14, y + 12); line(x - 9, y + 18, x + 9, y + 18); line(x - 4, y + 24, x + 4, y + 24)

# rail heights
Y12, YU, YA, YR = 70, 130, 165, 200
YFEED, YTRIG, YG = 500, 565, 670

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>')

# ---------------- car plug ----------------
CX0, CX1 = 20, 215
rect(CX0, 30, CX1 - CX0, 670)
text((CX0 + CX1) / 2, 22, "Car: original antenna plug", 15, "middle", "bold")
for y, pin, name in ((Y12, "2", "+12 V permanent (red)"), (YU, "1", "U: UP / MAX (blue/yellow)"),
                     (YA, "4", "A: AUTO / UP / MAX (blue/green)"), (YR, "5", "R: radio on (blue/white)"),
                     (YG, "6", "ground (brown)")):
    text(CX1 - 8, y + 5, name, 12, "end")
    text(CX1 + 6, y - 6, pin, 13, weight="bold")

# ---------------- rails ----------------
fuse(250, 320, Y12, "F1  5 A")
line(CX1, Y12, 250, Y12); line(320, Y12, 1200, Y12)
text(335, Y12 - 10, "+12 V (fused)", 13)
line(CX1, YG, 1380, YG)
ground(240, YG)
line(CX1, YU, 860, YU)      # U: to D1
line(CX1, YA, 1010, YA)     # A: to the timer COM
line(CX1, YR, 920, YR)      # R: to the timer supply

# ---------------- relay drawing ----------------
def relay(x0, y0, name, contact, sub):
    w, h = 130, 100
    rect(x0, y0, w, h)
    cx = x0 + 65
    # coil between 85 and 86
    p85, p86 = y0 + 25, y0 + 75
    rect(x0 + 20, y0 + 35, 18, 30, fill="#fff")
    poly((x0, p85), (x0 + 29, p85), (x0 + 29, y0 + 35))
    poly((x0, p86), (x0 + 29, p86), (x0 + 29, y0 + 65))
    # switch: COM (30) on the right, contact at the top
    p30 = y0 + 50
    piv = (x0 + 100, p30)
    line(x0 + w, p30, piv[0], p30)
    dot(*piv)
    line(cx, y0, cx, y0 + 22)
    add(f'<circle cx="{cx}" cy="{y0+24}" r="3" fill="#fff" stroke="#000" stroke-width="2"/>')
    if contact == "NC":
        line(piv[0], piv[1], cx + 2, y0 + 27)
    else:
        line(piv[0], piv[1], cx + 6, y0 + 40)
    line(x0 + 40, y0 + 50, x0 + 82, y0 + 38, dash=True, w=1.5)  # mechanical link
    text(x0 - 6, p85 - 6, "85", 12, "end"); text(x0 - 6, p86 - 6, "86", 12, "end")
    text(cx + 6, y0 - 6, "87a" if contact == "NC" else "87", 12)
    text(x0 + w + 6, p30 - 6, "30", 12)
    text(cx, y0 + h + 20, name, 15, "middle", "bold")
    text(cx, y0 + h + 38, sub, 12, "middle")
    return dict(x0=x0, x1=x0 + w, cx=cx, p85=p85, p86=p86, p30=p30, top=y0)

RY = 270
K1 = relay(370, RY, "K1  (changeover)", "NC", "closed when A is off")
K2 = relay(620, RY, "K2", "NO", "closed when U is on")

def wire_relay_common(K, x86, x30, to_feed=True, rail_dot=True):
    line(K["cx"], K["top"], K["cx"], Y12)
    if rail_dot: dot(K["cx"], Y12)
    poly((K["x0"], K["p86"]), (x86, K["p86"]), (x86, YG)); dot(x86, YG)
    if to_feed:
        poly((K["x1"], K["p30"]), (x30, K["p30"]), (x30, YFEED)); dot(x30, YFEED)

wire_relay_common(K1, 352, 535)
wire_relay_common(K2, 602, 785)
# coils
poly((330, YA), (330, K1["p85"]), (K1["x0"], K1["p85"])); dot(330, YA)
poly((580, YU), (580, K2["p85"]), (K2["x0"], K2["p85"])); dot(580, YU)

# U -> D1 -> trigger
line(860, YU, 860, 420)
diode_down(860, 420, 470, "D1")
line(860, 470, 860, YTRIG); dot(860, YTRIG)

# ---------------- timer add-on ----------------
rect(890, 235, 470, 300, dash=True, sw=1.5)
text(1350, 255, "optional timer add-on", 14, "end", style="italic")
TX0, TY0, TW, TH = 940, RY, 140, 100
rect(TX0, TY0, TW, TH)
text(TX0 + TW / 2, TY0 + 42, "one-shot timer", 14, "middle", "bold")
text(TX0 + TW / 2, TY0 + 60, "NE555 module", 12, "middle")
text(TX0 + TW / 2, TY0 + 78, "time set by screw", 12, "middle")
tv, tg, tno = TY0 + 25, TY0 + 75, TY0 + 50
text(TX0 + 5, tv + 4, "+", 12); text(TX0 + 5, tg + 4, "−", 12)
text(TX0 - 6, tv - 6, "VCC", 11, "end"); text(TX0 - 6, tg - 6, "GND", 11, "end")
text(1010 + 6, TY0 - 6, "COM", 11); text(TX0 + TW + 6, tno - 6, "NO", 11)
poly((920, YR), (920, tv), (TX0, tv)); dot(920, YR)
poly((TX0, tg), (925, tg), (925, YG)); dot(925, YG)
line(1010, YA, 1010, TY0)

K3 = relay(1135, RY, "K3", "NO", "closed while the timer runs")
poly((TX0 + TW, tno), (1110, tno), (1110, K3["p85"]), (K3["x0"], K3["p85"]))
wire_relay_common(K3, 1120, None, to_feed=False, rail_dot=False)
# K3 30 -> node X -> D2 (feed) and D3 (trigger)
XX = 1290
line(K3["x1"], K3["p30"], XX, K3["p30"]); dot(XX, K3["p30"]); text(XX + 6, K3["p30"] - 8, "X", 13, weight="bold")
line(XX, K3["p30"], XX, 420); diode_down(XX, 420, 470, "D2"); line(XX, 470, XX, YFEED); dot(XX, YFEED)
poly((XX, K3["p30"]), (1335, K3["p30"]), (1335, 420)); diode_down(1335, 420, 470, "D3"); line(1335, 470, 1335, YTRIG); dot(1335, YTRIG)

# ---------------- FEED / TRIG rails ----------------
line(535, YFEED, 1400, YFEED)
line(860, YTRIG, 1400, YTRIG)
text(1240, YFEED - 8, "FEED", 13, "end", "bold")
text(1240, YTRIG - 8, "TRIGGER", 13, "end", "bold")

# ---------------- antenna ----------------
AX0 = 1400
rect(AX0, 455, 125, 245)
text(AX0 + 62, 428, "Aftermarket", 15, "middle", "bold")
text(AX0 + 62, 446, "3-wire antenna", 15, "middle", "bold")
text(AX0 + 8, YFEED + 5, "+12 V", 13); text(AX0 + 8, YTRIG + 5, "trigger", 13); text(AX0 + 8, YG + 5, "ground", 13)
line(1380, YG, AX0, YG)

# ---------------- notes ----------------
text(240, 735, "Relays: Bosch-style 12 V mini relays with a built-in suppression diode (85 = +, 86 = −). "
     "D1: 1N4007. D2, D3: 1N5408. Car pin 5 (R) is only used by the timer add-on.", 13)
text(240, 755, "Untested idea: check the antenna and the radio output first (see the README).", 13, style="italic")

add("</svg>")
open("2026-10-08-relays-only-schematic.svg", "w").write("\n".join(out))
