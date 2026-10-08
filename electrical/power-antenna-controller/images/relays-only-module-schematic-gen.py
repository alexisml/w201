"""Draw the relays-only schematic, module build (timer module's own relay, no K3), as a plain SVG (white background, works in GitHub light/dark).

Untested idea: the circuit from relays-only.md.
Run with: python3 relays-only-module-schematic-gen.py  (writes 2026-10-08-relays-only-module-schematic.svg)
"""

W, H = 1540, 775
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
line(CX1, Y12, 250, Y12); line(320, Y12, 685, Y12)
text(335, Y12 - 10, "+12 V (fused)", 13)
line(CX1, YG, 1380, YG)
ground(240, YG)
line(CX1, YU, 860, YU)      # U: to K2 coil and D1
line(CX1, YA, 330, YA)      # A: to K1 coil
line(CX1, YR, 920, YR)      # R: to the timer supply

def coil(x0, y0, p85, p86):
    rect(x0 + 20, y0 + 35, 18, 30, fill="#fff")
    poly((x0, p85), (x0 + 29, p85), (x0 + 29, y0 + 35))
    poly((x0, p86), (x0 + 29, p86), (x0 + 29, y0 + 65))
    text(x0 - 6, p85 - 6, "85", 12, "end"); text(x0 - 6, p86 - 6, "86", 12, "end")

# ---------------- K1: changeover, all three contacts used ----------------
RY = 270
x0, y0, w, h = 370, RY, 130, 100
rect(x0, y0, w, h)
cx = x0 + 65
K1 = dict(x0=x0, x1=x0 + w, cx=cx, p85=y0 + 25, p86=y0 + 75, top=y0, p87=y0 + 30, p87a=y0 + 70)
coil(x0, y0, K1["p85"], K1["p86"])
line(cx, y0, cx, y0 + 22); dot(cx, y0 + 24)                 # 30: common, from +12 V
for yy in (K1["p87"], K1["p87a"]):                           # contacts on the right
    line(x0 + w, yy, x0 + 104, yy)
    add(f'<circle cx="{x0+101}" cy="{yy}" r="3" fill="#fff" stroke="#000" stroke-width="2"/>')
line(cx, y0 + 24, x0 + 99, K1["p87a"] - 3)                    # blade resting on 87a (coil off)
line(x0 + 40, y0 + 50, x0 + 70, y0 + 44, dash=True, w=1.5)   # mechanical link
text(cx + 6, y0 - 6, "30", 12)
text(x0 + w + 6, K1["p87"] - 6, "87", 12); text(x0 + w + 6, K1["p87a"] - 6, "87a", 12)
text(cx, y0 + h + 20, "K1  (changeover)", 15, "middle", "bold")
text(cx, y0 + h + 38, "30–87a when A is off, 30–87 when A is on", 12, "middle")

# ---------------- K2: normally open ----------------
x0 = 620
rect(x0, y0, w, h)
cx2 = x0 + 65
K2 = dict(x0=x0, x1=x0 + w, cx=cx2, p85=y0 + 25, p86=y0 + 75, top=y0, p30=y0 + 50)
coil(x0, y0, K2["p85"], K2["p86"])
piv = (x0 + 100, K2["p30"]); line(x0 + w, K2["p30"], piv[0], K2["p30"]); dot(*piv)
line(cx2, y0, cx2, y0 + 22)
add(f'<circle cx="{cx2}" cy="{y0+24}" r="3" fill="#fff" stroke="#000" stroke-width="2"/>')
line(piv[0], piv[1], cx2 + 6, y0 + 40)
line(x0 + 40, y0 + 50, x0 + 82, y0 + 38, dash=True, w=1.5)
text(cx2 + 6, y0 - 6, "87", 12); text(x0 + w + 6, K2["p30"] - 6, "30", 12)
text(cx2, y0 + h + 20, "K2", 15, "middle", "bold")
text(cx2, y0 + h + 38, "closed when U is on", 12, "middle")

# +12 V to K1 30 and K2 87
line(cx, y0, cx, Y12); dot(cx, Y12)
line(cx2, y0, cx2, Y12)
# grounds (86)
for K, x86 in ((K1, 352), (K2, 602)):
    poly((K["x0"], K["p86"]), (x86, K["p86"]), (x86, YG)); dot(x86, YG)
# coils
poly((330, YA), (330, K1["p85"]), (K1["x0"], K1["p85"]))
poly((580, YU), (580, K2["p85"]), (K2["x0"], K2["p85"])); dot(580, YU)
# feed: K1 87a and K2 30
poly((K1["x1"], K1["p87a"]), (535, K1["p87a"]), (535, YFEED)); dot(535, YFEED)
poly((K2["x1"], K2["p30"]), (785, K2["p30"]), (785, YFEED)); dot(785, YFEED)

# U -> D1 -> trigger
line(860, YU, 860, 420)
diode_down(860, 420, 470, "D1")
line(860, 470, 860, YTRIG); dot(860, YTRIG)

# ---------------- timer add-on ----------------
rect(890, 225, 330, 310, dash=True, sw=1.5)
text(1210, 245, "optional timer add-on", 14, "end", style="italic")
TX0, TY0, TW, TH = 940, RY, 140, 100
rect(TX0, TY0, TW, TH)
text(TX0 + TW / 2, TY0 + 42, "timer module", 14, "middle", "bold")
text(TX0 + TW / 2, TY0 + 60, "NE555, own relay", 12, "middle")
text(TX0 + TW / 2, TY0 + 78, "time set by screw", 12, "middle")
tv, tg, tno = TY0 + 25, TY0 + 75, TY0 + 50
text(TX0 + 5, tv + 4, "+", 12); text(TX0 + 5, tg + 4, "−", 12)
text(TX0 - 6, tv - 6, "VCC", 11, "end"); text(TX0 - 6, tg - 6, "GND", 11, "end")
text(1010 + 6, TY0 - 6, "COM", 11); text(TX0 + TW + 6, tno - 6, "NO / NC*", 11)
poly((920, YR), (920, tv), (TX0, tv)); dot(920, YR)
poly((TX0, tg), (925, tg), (925, YG)); dot(925, YG)
# G: K1 87 -> timer COM
poly((K1["x1"], K1["p87"]), (515, K1["p87"]), (515, 240), (1010, 240), (1010, TY0))
text(700, 234, "G (+12 V only while A is on)", 12, weight="bold")
# timer output -> node X -> D2 (feed) and D3 (trigger)
XX = 1130
line(TX0 + TW, tno, XX, tno); dot(XX, tno); text(XX + 8, tno + 18, "X", 13, weight="bold")
line(XX, tno, XX, 420); diode_down(XX, 420, 470, "D2"); line(XX, 470, XX, YFEED); dot(XX, YFEED)
poly((XX, tno), (1175, tno), (1175, 420)); diode_down(1175, 420, 470, "D3"); line(1175, 470, 1175, YTRIG); dot(1175, YTRIG)

# ---------------- FEED / TRIG rails ----------------
line(535, YFEED, 1400, YFEED)
line(860, YTRIG, 1400, YTRIG)
text(1360, YFEED - 8, "FEED", 13, "end", "bold")
text(1360, YTRIG - 8, "TRIGGER", 13, "end", "bold")

# ---------------- antenna ----------------
AX0 = 1400
rect(AX0, 455, 125, 245)
text(AX0 + 62, 428, "Aftermarket", 15, "middle", "bold")
text(AX0 + 62, 446, "3-wire antenna", 15, "middle", "bold")
text(AX0 + 8, YFEED + 5, "+12 V", 13); text(AX0 + 8, YTRIG + 5, "trigger", 13); text(AX0 + 8, YG + 5, "ground", 13)
line(1380, YG, AX0, YG)

# ---------------- notes ----------------
text(240, 727, "Relays: JQC-3FF 12 V changeover (COM = 30, NO = 87, NC = 87a), or Omron G5LE / mini ISO; each coil needs a 1N4007 "
     "(stripe to 85). D1: 1N4007. D2, D3: 1N5408. Pin 5 (R) only feeds the timer.", 13)
text(240, 745, "* Timer output: NO on a one-shot module (relay on at power-up, off after T), NC on a delay-on module "
     "(relay off at power-up, on after T).", 13)
text(240, 763, "Untested idea: check the antenna and the radio output first (see the README).", 13, style="italic")

add("</svg>")
open("2026-10-08-relays-only-module-schematic.svg", "w").write("\n".join(out))
