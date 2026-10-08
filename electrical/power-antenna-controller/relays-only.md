# Power antenna controller idea: relays only, no microcontroller

**System:** electrical
**Status:** untested idea

> **Untested idea.** This is a design dump, not a finished or proven build. Nothing here has been
> built or run yet. The wiring comes from documentation and forum reports. Bench-test the antenna
> first (see the [README](README.md#bench-test-the-antenna-first)) and check everything against your
> own parts.

Two ordinary automotive relays and no programming. It gives everything the original switch did
except the automatic medium height when the radio comes on; an optional timer add-on brings that
back too. How the original behaves, the car wiring and the bench tests are in the
[README](README.md).

## The logic

The [Karnaugh maps](README.md#control-logic-truth-table-and-karnaugh-maps) give:

- **Trigger = U**: the antenna goes up only when the switch is in UP or MAX.
- **Feed = ¬A + U**: the antenna gets +12 V when the switch is in OFF or DOWN, when the radio is off
  (both are ¬A), or in UP/MAX (U). In AUTO (A without U) the feed is cut, so the mast stays where it
  is.

The end stops are left to the antenna's own board, as they are today, so no current sensing is
needed.

| Situation | A | U | Feed | Trigger | Mast |
|---|---|---|---|---|---|
| Radio off (key off) | 0 | 0 | on | off | All the way down |
| OFF | 0 | 0 | on | off | All the way down |
| DOWN held | 0 | 0 | on | off | Goes down while held |
| AUTO | 1 | 0 | **off** | off | Stays where it is |
| UP held | 1 | 1 | on | on | Goes up while held |
| MAX | 1 | 1 | on | on | All the way up |

Rocking the switch to UP or DOWN and letting go now moves the mast in steps and leaves it there,
like the original. **What's missing:** when the radio comes on in AUTO, the mast stays down (it was
lowered when the radio went off). Press UP or MAX to raise it, or add the
[timer](#optional-medium-height-when-the-radio-comes-on).

## Parts

| # | Part | What for | Example |
|---|---|---|---|
| 1 | **K1: changeover relay, 12 V** (5-pin: 30, 87, 87a, 85, 86) | Feed when A is off (normally-closed contact) | See [which relays](#which-relays) |
| 2 | **K2: relay, 12 V** | Feed when U is on (normally-open contact) | Same type as K1 |
| 3 | Perfboard, screw terminals, and mini ISO PCB sockets (if using mini ISO relays) | Holds everything; car and antenna wires go to screw terminals | See [building it on perfboard](#building-it-on-perfboard) |
| 4 | Inline blade fuse holder + 5 A fuse | Protects the +12 V permanent feed | Any automotive inline holder |
| 5 | D1: diode, 1 A or more | Stops +12 V from the timer add-on feeding back into the U switch line. Optional without the timer, **needed with it** (see [simulation](#simulation)) | 1N4007 |
| 6 | Waterproof box, wire | | See the [shopping list](#list) |

The relay coils are powered from the switch lines, which come from the radio's antenna output. A
typical mini relay coil draws about 150 mA, and up to two are on at once. **Measure what the radio's
antenna output can supply** before using it this way. If it's weak, use relays with lower-power
coils (the Omron G5LE draws 33 mA at 12 V, see [which relays](#which-relays)).

Use relays with a built-in suppression diode (and connect 85/86 the right way round), or add a diode
across each coil. Without it, the coil's switch-off spike goes back into the radio's output.

## Shopping list (cheap, US prices)

Rough US prices from listings seen on 2026-10-08 (eBay US, Amazon, Walmart, Digi-Key). They change,
and most parts come in packs, so one order leaves spares.

### Which relays

**Suggested build: on perfboard**, with one of two relay types (see [building it](#building-it-on-perfboard)):

- **Mini ISO relays in PCB sockets**: standard car relays that unplug for replacement.
- **Omron G5LE PCB relays**: small and cheap, with the lowest coil current; soldered in.

The relay coils are powered from the switch lines, so from the **radio's antenna output**. In UP or
MAX two coils are on at once (K1 and K2), and with the timer add-on K1, K3 and the timer module are on
together when the radio comes on. That's what decides between the two:

| | **Mini ISO relay + PCB socket** (suggested) | **Omron G5LE-1-E DC12** (suggested) |
|---|---|---|
| Relay | 12 V, 5-pin SPDT (changeover) mini ISO: generic "Bosch-style" 30/40 A, or TE Connectivity V23134 (40 A, built-in suppression diode, −40 to 125 °C) | 12 V SPDT PCB relay, 16 A |
| Coil current at 12 V | about 150 mA (80–90 Ω) | 33 mA |
| Mounting | Mini ISO PCB socket soldered to the perfboard (for example Durakool DZ85AB-5-PCB, 60 A); the relay plugs in | Soldered straight to the perfboard |
| Price | Generic relay about $2–3 each in packs (TE about $11–13); socket about €5 each (RS Components; US price not checked) | about $2.50 each (Digi-Key) |
| Use when | The radio output can supply about 300–400 mA | The radio output is weak, or you'd rather not load it |

The antenna motor draws a few amps, so both are well oversized for the contacts. Generic mini ISO
relays usually have **no** suppression diode and the Omron never has one: add a 1N4007 across each
coil (stripe/cathode to the + side, 85; other end to 86). The TE relay has it built in, so mind its
polarity.

Other ways to mount them, if perfboard isn't wanted:

- **Relays with pigtail sockets**, joined with WAGO connectors: no board at all (5-pack of relays
  with sockets about $9–14), but messier.
- **A ready-made waterproof relay/fuse box** (about $24–76): tidy, but they usually come with 4-pin
  relays wired to the normally-open contact only. K1 needs the normally-closed contact (87a), so it
  would need a 5-pin relay and an extra wire.

### List

| Qty | Part | Search for | Rough US price |
|---|---|---|---|
| 2 (3 with the timer) | Relays, see [above](#which-relays) | Mini ISO: "12V 5 pin SPDT mini relay 40A" · Omron: "G5LE-1-E DC12" | Mini ISO: about $2–3 each in packs · Omron: about $2.50 each |
| 2 (3 with the timer) | Mini ISO PCB sockets (mini ISO relays only) | "mini ISO relay PCB socket" (e.g. Durakool DZ85AB-5-PCB) | about €5 each (US price not checked) |
| 1 | Perfboard, about 10 × 7 cm or bigger | "perfboard" / "prototype PCB" | about $5 for a pack |
| 1 set | 5 mm PCB screw terminals (2- and 3-way), for the car and antenna wires | "5mm PCB screw terminal block" | about $5–8 for a pack |
| 1 | NE555 delay relay module, 12 V, 0–60 s (timer add-on) | "DC 12V NE555 0-60 seconds delay relay module" | about $2.30–3 (eBay US); more on Amazon |
| 1 | Diode assortment with 1N4007 and 1N5408 | "diode assortment kit 1N4007 1N5408 100pcs" | about $7 (Walmart) |
| 1 | Inline blade fuse holder + 5 A blade fuse | "inline blade fuse holder waterproof 5 pack" | about $10 for a 5-pack |
| 1 | Small waterproof box, with standoffs for the board | "IP65 ABS junction box" (about 120 × 80 × 60 mm or bigger) | about $7–11 |
| — | Wire (1 mm² / 18 AWG red and brown, 0.5 mm² / 20 AWG for signals), heat-shrink | | about $10, or what you have |

The timer module is the common 67 × 17 × 17 mm board: the relay pulls in at power-up and releases
after the set time ([reference](../references/grobotronics-ne555-delay-relay-module/README.md)).
Check the listing says the same.

**Rough total, from scratch:** about $45–60, timer included, with plenty left over. The parts
actually used cost about $25–35 (more with mini ISO sockets, less with the Omron relays).

### Building it on perfboard

![Perfboard layout guide: car screw terminals on the left, K1, K2, the timer module and K3 in a row, diodes D1 to D3, antenna screw terminals on the right, with colour-coded wires](images/2026-10-08-relays-only-perfboard.svg)

A placement and wiring guide, not to scale: mini ISO sockets are about 28 mm square, so with them
the board ends up roughly 13 × 9 cm; with Omron relays it's smaller. Check the footprint of the
sockets or relays you buy against the perfboard's 2.54 mm grid; mini ISO socket pins may need the
holes drilled out.

- **Power paths:** cheap perfboard copper is thin. Run the +12 V rail and the antenna feed (a few
  amps) with 1 mm² (18 AWG) wire soldered point to point on the back, not with solder bridges.
  Signal and coil connections can be thin wire.
- **Connections in and out:** 5 mm screw terminals for the car side (pins 2, 1, 4, 5, 6) and the
  antenna side (+12 V, trigger, ground), so nothing is soldered to the harness.
- **On the board:** the relays (or their sockets), a 1N4007 across each coil, D1, D2 and D3. The
  timer module can sit on standoffs next to it and connect with short wires to its screw terminals.
- **In the box:** mount the board on standoffs, add strain relief where the cables enter, and keep
  the box in a dry spot in the trunk. A conformal coating on the board helps against damp.

## Wiring

### Black-box view

What connects to what, with each part as a box. The dotted lines belong to the optional timer
add-on (timer module, K3, D2 and D3).

```mermaid
flowchart LR
    subgraph CAR["Car: original antenna plug"]
        C2["pin 2 · red<br/>+12 V permanent"]
        C1["pin 1 · blue/yellow<br/>U: UP / MAX"]
        C4["pin 4 · blue/green<br/>A: AUTO / UP / MAX"]
        C5["pin 5 · blue/white<br/>R: radio on"]
        C6["pin 6 · brown<br/>ground"]
    end

    subgraph BOX["Relay box"]
        F1["fuse 5 A"]
        K1["K1 changeover relay<br/>coil from A<br/>NC contact: +12 V → feed"]
        K2["K2 relay<br/>coil from U<br/>NO contact: +12 V → feed"]
        D1["diode D1"]
        TMR["timer module<br/>powered by R<br/>passes A while running"]
        K3["K3 relay<br/>NO contact: +12 V → X"]
        D23["diodes D2, D3<br/>X → feed, X → trigger"]
    end

    subgraph ANT["Aftermarket 3-wire antenna"]
        A12["+12 V (feed)"]
        ATR["trigger"]
        AG["ground"]
    end

    C2 --> F1
    F1 --> K1
    F1 --> K2
    F1 -.-> K3
    C4 -- "coil" --> K1
    C1 -- "coil" --> K2
    C1 --> D1
    C5 -.-> TMR
    C4 -.-> TMR
    TMR -. "coil" .-> K3
    K3 -.-> D23
    K1 --> A12
    K2 --> A12
    D1 --> ATR
    D23 -.-> A12
    D23 -.-> ATR
    C6 --> AG
```

### Circuit

![Relays-only schematic: car plug, fuse, relays K1 and K2, diode D1, optional timer with K3 and diodes D2 and D3, and the antenna](images/2026-10-08-relays-only-schematic.svg)

Relay pins use the usual automotive numbers: 85 and 86 are the coil, 30 is the common contact, 87 is
normally open and 87a is normally closed.

### Connection list (without the timer)

| From | To |
|---|---|
| Car pin 2 (+12 V permanent) | Fuse 5 A → K1 pin 87a **and** K2 pin 87 |
| Car pin 4 (A, blue/green) | K1 pin 85 (coil +) |
| Car pin 1 (U, blue/yellow) | K2 pin 85 (coil +) **and** D1 anode; D1 cathode → antenna trigger |
| K1 pin 30 **and** K2 pin 30 | Antenna +12 V (red) |
| K1 pin 86, K2 pin 86 | Ground |
| Car pin 6 (ground) | Ground bus and antenna ground |
| Car pin 5 (R, blue/white) | Not used (only by the timer add-on) |

How it reads:

- K1 is **closed when its coil is off**, so the antenna gets +12 V whenever A is off: radio off,
  OFF, or DOWN held. When A comes on (AUTO, UP, MAX), K1 opens.
- K2 closes when U is on (UP, MAX), so the antenna gets +12 V again for going up, even though K1 is
  open.
- The trigger comes straight from U, so the antenna only goes up in UP or MAX.

## Optional: medium height when the radio comes on

To raise the mast part way automatically when the radio comes on in AUTO, add a timer that drives
it up for a few seconds:

| # | Part | Example |
|---|---|---|
| 1 | 12 V one-shot timer: relay on for an adjustable time after it's powered (see [timer choices](#timer-choices-adjusted-with-a-screw)) **NE555 timer relay module** (trimmer screw; preferred, cheap). Finder 80.01 (dial) as a sturdier alternative |
| 2 | K3: relay, 12 V (5-pin) | Same type as K1 |
| 3 | 2 diodes, 3 A | 1N5408 |

- Power the timer from **car pin 5 (R)**, set to "relay on for T seconds after power-on".
- Its contact passes **car pin 4 (A)** to **K3's coil**. So K3 only pulls in if the switch is in
  AUTO (or higher) during those first seconds, not in OFF.
- K3's contact (87) is fed from the fused +12 V. Its output (30) goes through D2 to the antenna
  +12 V and through D3 to the antenna trigger. All three diodes are needed once the timer is fitted
  (checked in the [simulation](#simulation)):
  - **D2** stops K1's feed from reaching the trigger, which would send the mast up instead of down.
  - **D3** stops the U line from feeding the antenna motor through D1 and D2, which would load the
    radio's output with motor current.
  - **D1** stops the timer's +12 V from feeding back into the U line (and the switch and radio).
- The time T sets the height: about half the full travel time gives about half height. It goes
  wrong if the mast wasn't fully down when the radio came on; it then ends higher, up to the top.

This adds the timer module's own current (tens of mA) to the radio's output while the radio is on.

### Timer choices (adjusted with a screw)

**Preferred: the NE555 module**, as the cheap option. The Finder is the sturdier, more expensive
alternative. Both set the time, and so the height, with a screwdriver. Pick one whose mode is **"relay on for the
set time after power is applied, then off"** (also called interval, single pulse or one-shot).

| | **NE555 timer relay module** (preferred) | Finder 80.01 multifunction timer (alternative) |
|---|---|---|
| What it is | Small hobby board with a relay and a blue trimmer potentiometer | Industrial timer relay for a DIN rail, 17.5 mm wide |
| Adjusting | Turn the trimmer screw; usually about 0–25 s or 0–60 s | Rotary dials: one for the function, one for the time scale, one for the time |
| Mode to use | The common 0–60 s board does it by default: relay on at power-up, off after the set time (some other boards need a trigger pulse; check the listing) | **DI (interval)**: contact closes when powered, opens after the set time |
| Supply | 12 V DC | 12–240 V AC/DC |
| Contact | 1 changeover, about 10 A | 1 changeover, 16 A |
| Robustness | Bare board; needs the waterproof box | Industrial build, enclosed |
| Price | Cheap | More expensive |
| Notes | A multi-turn trimmer makes fine adjustment easier | Time scales from 0.1 s up to hours; use the shortest that covers the antenna's travel time |

How to set it: time the full travel from down to up on the bench, then set the timer to the fraction
you want (half the time for about half height). The height won't be exact: the motor runs a little
faster or slower with battery voltage, temperature and how stiff the mast is.

With the Finder, its 16 A contact could switch the antenna's +12 V directly. K3 is still needed,
because it's what makes the timer do nothing when the switch is in OFF.

## Simulation

The circuit was checked with a small logic-level simulation ([relays-only-sim.py](relays-only-sim.py)). It models the netlist
from the schematic: the fused +12 V rail, the three switch lines (driven by the radio and switch, or
left open), the relay coils and contacts, the diodes (one-way), the timer (closed for T seconds after
the radio comes on) and the antenna (moves only while its +12 V is on; up with the trigger, down
without; full travel 8 s). It also flags two wiring faults: +12 V **backfeeding** into a switch
line, and a switch line (the radio's output) being able to **feed the antenna motor**.

**Result with D1, D2, D3 and the timer (T = 4 s, about half height): all 12 scenarios pass.**

| Scenario | Expected | Simulated |
|---|---|---|
| Parked, radio off | down | down |
| Radio on in AUTO (timer raises it) | 50% | 50% |
| Rock UP 1 s, release | 62% | 62% |
| Rock DOWN 2 s, release | 25% | 25% |
| MAX | up | up |
| MAX, back to AUTO | stays up | stays up |
| OFF | down | down |
| OFF, back to AUTO | stays down | stays down |
| Radio off with the mast half up | down | down |
| Radio on in OFF (timer must not raise it) | down | down |
| Radio on in MAX | up | up |
| DOWN held while the timer runs | down | down |

**Every combination.** The car can be in three states: key off, key on with the radio off (or in a
mode that switches its antenna output off, like CD or AUX on some radios), and key on with the radio
on. With the 5 switch positions that's 15 states. On this car the radio stays on for a few seconds after the key is
turned off, so the simulation keeps the radio's output on for 3 s after every key-off.

| Check | Cases | Result |
|---|---|---|
| Every change from one state to another, held long enough to settle, starting with the mast down, half up and fully up | 675 | All settle where the design says; no wiring faults |
| Every sequence of three quick changes (1 s each, so the mast is mid-travel and the timer may still be running), then key off | 10,125 | The mast always ends fully down (it starts lowering when the radio switches off, a few seconds after the key); no wiring faults |

"Where the design says": with the radio off (any switch position, key on or off) the mast goes down;
in OFF or DOWN it goes down; in UP or MAX it goes up; in AUTO it rises by the timer's amount if the
radio has just come on, and otherwise stays where it is.

The same checks fail clearly when a diode is taken out: without D2, 576 of the 675 transitions end at
the wrong height; without D1 or D3, the wiring-fault check trips (75 and 168 cases).

**Taking one diode out (timer fitted):**

| Missing | What goes wrong |
|---|---|
| D1 | +12 V backfeeds into the U line (and so the switch and the radio) whenever K3 is on |
| D2 | K1's feed reaches the trigger through D3: the mast goes **up** in OFF, DOWN and with the radio off |
| D3 | The mast still moves right, but in UP and MAX the U line (radio output) can feed the antenna motor through D1 and D2 |

**Without the timer**, D1 can be left out (nothing else drives the trigger line); everything else
behaves the same, except that the mast stays down when the radio comes on in AUTO.

What the simulation doesn't cover: real currents and voltages, relay bounce and switching times,
the timer's accuracy, and whether the antenna really stops when its +12 V is cut (bench test step 4
in the README). It checks the wiring logic, not the parts.

The script is [relays-only-sim.py](relays-only-sim.py) (Python 3, no extra libraries):

```bash
python3 relays-only-sim.py
```

## Compared with the microcontroller ideas

| | Relays only | Relays + timer | Arduino / ESP32 |
|---|---|---|---|
| UP / DOWN in steps, MAX, OFF, down with radio off | Yes | Yes | Yes |
| Medium height when the radio comes on | No | Yes, by time | Yes, by time and current |
| Stops the motor as soon as it stalls | No (the antenna's own board does it, as today) | No | Yes |
| Learns the travel time | No | No | Yes |
| Programming | None | None (set a time) | Yes |
| Parts | 2 relays | + timer, relay, 2 diodes | Board, sensor/shield, optocouplers, supply |
| Standby drain | None added (same as today) | None added | Almost none |
| Load on the radio's antenna output | 1–2 relay coils | + timer module | Optocoupler inputs (a few mA) and the start-up current |

## Open questions (this idea)

- [ ] What the radio's antenna output can supply (for the relay coils). Simple test: with the radio
      on, connect one relay coil (85 to the output, 86 to ground), then two. The voltage on the output
      should stay close to the battery voltage and the relays should click firmly. If it sags, use
      option C relays.
- [ ] Bench test step 4 in the README: does the antenna stop when its +12 V is cut mid-travel? This
      idea depends on it as much as the others.

## References

- GRobotronics: Relay Module, 1 channel 12 V with adjustable delay time (NE555 delay relay module;
  how it behaves at power-up): [original](https://grobotronics.com/relay-module-1-channel-12v-with-adjustable-delay-time.html)
  · [Wayback](https://web.archive.org/web/20250813224724/https://grobotronics.com/relay-module-1-channel-12v-with-adjustable-delay-time.html)
  · [reference](../references/grobotronics-ne555-delay-relay-module/README.md)
