"""Logic-level simulation of the relays-only antenna circuit (with the optional timer add-on).

Untested idea: this checks the wiring logic of relays-only.md, not real parts.
Run with: python3 relays-only-sim.py  (Python 3, no extra libraries)

Two builds, netlists taken from the schematics in images/:

Module build (2026-10-08-relays-only-module-schematic.svg), the timer module's own relay:
  K1 (changeover, coil from A): 30 = B12 (fused +12 V); 87a (A off) -> FEED; 87 (A on) -> G
  K2 (coil from U): 87 = B12, 30 -> FEED
  Timer module (powered from R): its own relay connects G -> X for T seconds after power-up
    (COM-NO on a one-shot board, COM-NC on a delay-on board)

Discrete build (2026-10-08-relays-only-discrete-schematic.svg), a separate relay K3:
  K1 (coil from A): 87a = B12, 30 -> FEED      K2 (coil from U): 87 = B12, 30 -> FEED
  Timer module (powered from R): its relay passes A to K3's coil for T seconds after power-up
  K3: 87 = B12, 30 -> X

Both: X -D2-> FEED ; X -D3-> TRIG ; U -D1-> TRIG
  Antenna: FEED (+12 V), TRIG (trigger), ground.
The switch lines R, A, U are driven by the radio/switch (high) or open (not driven).
A node is "high" if a +12 V source reaches it through closed contacts (both ways) or diodes
(anode -> cathode only). Backfeed = a switch line ends up high while the switch isn't driving it.
"""

TRAVEL = 8.0      # s, full travel time of the antenna
TIMER_T = 4.0     # s, timer setting (about half height)
DT = 0.1
BUILD = "module"  # "module" or "discrete"; set by run()

def contacts(k1_on, k2_on, k3_on, timer_closed):
    """Closed contacts (both ways) for the current relay states."""
    e = []
    if not k1_on: e.append(("B12", "FEED"))              # K1: +12 V to the feed while A is off
    elif BUILD == "module": e.append(("B12", "G"))       # K1 30-87 (A on): gate for the timer
    if k2_on: e.append(("B12", "FEED"))                  # K2 87-30
    if BUILD == "module":
        if timer_closed: e.append(("G", "X"))            # timer module's own relay
    else:
        if timer_closed: e.append(("A", "K3COIL"))       # timer passes A to K3's coil
        if k3_on: e.append(("B12", "X"))                 # K3 87-30
    return e

def solve(drive, k1_on, k2_on, k3_on, timer_closed, diodes):
    """Return the set of high nodes. drive: dict of driven lines {'R','A','U'} -> bool."""
    edges_bi = contacts(k1_on, k2_on, k3_on, timer_closed)   # closed contacts, both ways
    edges_uni = []     # diodes: anode -> cathode
    if "D1" in diodes: edges_uni.append(("U", "TRIG"))
    else:              edges_bi.append(("U", "TRIG"))     # diode replaced by a wire
    if "D2" in diodes: edges_uni.append(("X", "FEED"))
    else:              edges_bi.append(("X", "FEED"))
    if "D3" in diodes: edges_uni.append(("X", "TRIG"))
    else:              edges_bi.append(("X", "TRIG"))
    high = {"B12"} | {k for k, v in drive.items() if v}
    changed = True
    while changed:
        changed = False
        for a, b in edges_bi:
            if (a in high) != (b in high):
                high |= {a, b}; changed = True
        for a, b in edges_uni:
            if a in high and b not in high:
                high.add(b); changed = True
    return high

def reach_from(src, k1_on, k2_on, k3_on, timer_closed, diodes):
    """Nodes reachable from one switch line alone (the +12 V rail is ignored)."""
    edges_bi = [e for e in contacts(k1_on, k2_on, k3_on, timer_closed) if "B12" not in e]
    edges_uni = []
    (edges_uni if "D1" in diodes else edges_bi).append(("U", "TRIG"))
    (edges_uni if "D2" in diodes else edges_bi).append(("X", "FEED"))
    (edges_uni if "D3" in diodes else edges_bi).append(("X", "TRIG"))
    seen = {src}; ch = True
    while ch:
        ch = False
        for a, b in edges_bi:
            if (a in seen) != (b in seen): seen |= {a, b}; ch = True
        for a, b in edges_uni:
            if a in seen and b not in seen: seen.add(b); ch = True
    return seen

def lines_for(radio_on, sw):
    """Switch position -> which lines the radio/switch drives."""
    if not radio_on:
        return {"R": False, "A": False, "U": False}
    return {"R": True,
            "A": sw in ("AUTO", "UP", "MAX"),
            "U": sw in ("UP", "MAX")}

def run(script, diodes=("D1", "D2", "D3"), with_timer=True, pos0=0.0, build=None):
    """script: list of (seconds, radio_on, switch). Returns (final pos, problems, trace)."""
    global BUILD
    if build: BUILD = build
    pos = pos0
    radio_prev = False
    t_power = None
    problems = []
    trace = []
    # relay coil states settle iteratively each step (coil inputs depend on solved nodes)
    k1 = k2 = k3 = False
    t = 0.0
    for dur, radio_on, sw in script:
        steps = int(round(dur / DT))
        for _ in range(steps):
            if radio_on and not radio_prev:
                t_power = t
            if not radio_on:
                t_power = None
            radio_prev = radio_on
            timer_closed = with_timer and t_power is not None and (t - t_power) < TIMER_T
            drive = lines_for(radio_on, sw)
            for _ in range(5):                      # let relays settle
                high = solve(drive, k1, k2, k3, timer_closed, diodes)
                n1, n2, n3 = "A" in high, "U" in high, "K3COIL" in high
                if (n1, n2, n3) == (k1, k2, k3):
                    break
                k1, k2, k3 = n1, n2, n3
            for line in ("R", "A", "U"):
                if line in high and not drive[line]:
                    problems.append(f"t={t:.1f}s {sw}: backfeed into {line}")
                if drive[line]:
                    if "FEED" in reach_from(line, k1, k2, k3, timer_closed, diodes):
                        problems.append(f"t={t:.1f}s {sw}: {line} (radio output) can feed the antenna motor")
            feed, trig = "FEED" in high, "TRIG" in high
            if feed:
                pos += (DT / TRAVEL) * (1 if trig else -1)
                pos = min(1.0, max(0.0, pos))
            trace.append((round(t, 1), radio_on, sw, feed, trig, round(pos, 3)))
            t += DT
    return pos, problems, trace

def pct(p): return f"{p*100:.0f}%"

SCENARIOS = [
    # name, script, expected final height (None = check by rule), start height
    ("Parked, radio off",                      [(3, False, "AUTO")], 0.0, 0.0),
    ("Radio on in AUTO (timer raises it)",     [(10, True, "AUTO")], TIMER_T / TRAVEL, 0.0),
    ("Rock UP 1 s, release",                   [(10, True, "AUTO"), (1, True, "UP"), (3, True, "AUTO")], TIMER_T / TRAVEL + 1 / TRAVEL, 0.0),
    ("Rock DOWN 2 s, release",                 [(10, True, "AUTO"), (2, True, "DOWN"), (3, True, "AUTO")], TIMER_T / TRAVEL - 2 / TRAVEL, 0.0),
    ("MAX",                                    [(10, True, "AUTO"), (10, True, "MAX")], 1.0, 0.0),
    ("MAX, back to AUTO (stays up)",           [(10, True, "MAX"), (5, True, "AUTO")], 1.0, 0.0),
    ("OFF lowers it",                          [(10, True, "MAX"), (10, True, "OFF")], 0.0, 0.0),
    ("OFF back to AUTO (stays down)",          [(10, True, "OFF"), (5, True, "AUTO")], 0.0, 0.0),
    ("Radio off with mast half up",            [(10, True, "AUTO"), (10, False, "AUTO")], 0.0, 0.0),
    ("Radio on in OFF (timer must not raise)", [(10, True, "OFF")], 0.0, 0.0),
    ("Radio on in MAX",                        [(10, True, "MAX")], 1.0, 0.0),
    ("DOWN held during the timer",             [(1, True, "AUTO"), (5, True, "DOWN"), (3, True, "AUTO")], 0.0, 0.0),
]

def main():
    print("=== Full circuit (D1, D2, D3, timer) ===")
    allok = True
    rows = []
    for name, script, exp, p0 in SCENARIOS:
        pos, probs, _ = run(script, pos0=p0)
        ok = abs(pos - exp) < 0.02 and not probs
        allok &= ok
        rows.append((name, pct(exp), pct(pos), "OK" if ok else "FAIL", "; ".join(probs[:2])))
    for r in rows:
        print(" | ".join(r))
    print("ALL OK" if allok else "SOME FAILED")

    print("\n=== Without the timer ===")
    for name, script, exp, p0 in SCENARIOS:
        pos, probs, _ = run(script, with_timer=False, pos0=p0)
        print(f"{name} | final {pct(pos)} | {'; '.join(probs[:1]) or 'no backfeed'}")

    for missing in ("D1", "D2", "D3"):
        ds = tuple(d for d in ("D1", "D2", "D3") if d != missing)
        print(f"\n=== Timer fitted, {missing} replaced by a wire ===")
        for name, script, exp, p0 in SCENARIOS:
            pos, probs, _ = run(script, diodes=ds, pos0=p0)
            bad = abs(pos - exp) >= 0.02 or probs
            if bad:
                print(f"{name} | expected {pct(exp)} got {pct(pos)} | {'; '.join(sorted(set(p.split(': ',1)[1] for p in probs))) or ''}")

    print("\n=== Trace: radio on in AUTO, rock UP, rock DOWN, OFF, radio off ===")
    script = [(6, True, "AUTO"), (1, True, "UP"), (2, True, "AUTO"), (2, True, "DOWN"), (2, True, "AUTO"),
              (10, True, "OFF"), (2, False, "OFF")]
    _, _, tr = run(script)
    last = None
    for t, r, sw, f, tg, p in tr:
        key = (r, sw, f, tg)
        if key != last:
            print(f"t={t:5.1f}s radio={'on ' if r else 'off'} switch={sw:4} feed={'on ' if f else 'off'} trigger={'on ' if tg else 'off'} mast={pct(p)}")
            last = key
    print(f"end   mast={pct(tr[-1][5])}")


# ---------------- exhaustive check: car state x switch, every transition ----------------
CAR_STATES = [("key off", False), ("key on, radio off", False), ("key on, radio on", True)]
KEY_OFF_DELAY = 3.0   # s: on this car the radio stays on for a few seconds after the key is turned off
# "radio on" here means the radio's antenna output is on (some radios switch it off in CD/AUX mode,
# which is the same as "radio off" for the antenna). With the key off the radio is off.
SWITCHES = ["OFF", "DOWN", "AUTO", "UP", "MAX"]
STATES = [(c, out, sw) for c, out in CAR_STATES for sw in SWITCHES]

def spec(p, prev_out, out, sw):
    """Where the mast should settle (held long enough), from the design."""
    if not out:
        return 0.0
    if sw in ("OFF", "DOWN"):
        return 0.0
    if sw in ("UP", "MAX"):
        return 1.0
    if not prev_out:                     # radio just came on in AUTO: timer raises it by T
        return min(1.0, p + TIMER_T / TRAVEL)
    return p                             # AUTO otherwise holds

def exhaustive():
    LONG = 15.0
    fails, faults, n = [], [], 0
    for p0 in (0.0, 0.5, 1.0):
        for a in STATES:
            for b in STATES:
                n += 1
                script = [(LONG, a[1], a[2])]
                if a[1] and b[0] == "key off":          # radio keeps running briefly after key off
                    script.append((KEY_OFF_DELAY, True, b[2]))
                script.append((LONG, b[1], b[2]))
                pos, probs, _ = run(script, pos0=p0)
                pa = spec(p0, False, a[1], a[2])
                exp = spec(pa, a[1], b[1], b[2])
                if abs(pos - exp) > 0.02:
                    fails.append((p0, a, b, exp, pos))
                if probs:
                    faults.append((p0, a, b, probs[0]))
    print(f"Long transitions (radio stays on {KEY_OFF_DELAY:.0f} s after key off): {n} checked, {len(fails)} wrong height, {len(faults)} wiring faults")
    for f in fails[:10]:
        print("  WRONG", f)
    for f in faults[:10]:
        print("  FAULT", f)

    # fast sequences: three states, 1 s each (timer still running, mast mid-travel),
    # then the car is switched off for 15 s: the mast must end down, with no faults.
    n2, bad2 = 0, []
    for p0 in (0.0, 0.5, 1.0):
        for a in STATES:
            for b in STATES:
                for c in STATES:
                    n2 += 1
                    script = []
                    prev_on = False
                    for st in (a, b, c):
                        if prev_on and st[0] == "key off":
                            script.append((min(1.0, KEY_OFF_DELAY), True, st[2]))
                        script.append((1.0, st[1], st[2]))
                        prev_on = st[1]
                    if prev_on:                               # key off at the end
                        script.append((KEY_OFF_DELAY, True, c[2]))
                    script.append((LONG, False, c[2]))
                    pos, probs, _ = run(script, pos0=p0)
                    if probs or pos > 0.001:
                        bad2.append((p0, a, b, c, pos, probs[:1]))
    print(f"Fast sequences then key off (radio stays on {KEY_OFF_DELAY:.0f} s after key off): {n2} checked, {len(bad2)} problems")
    for f in bad2[:10]:
        print("  BAD", f)

for b in ("module", "discrete"):
    BUILD = b
    print(f"\n################ {b.upper()} BUILD ################")
    main()
    exhaustive()
