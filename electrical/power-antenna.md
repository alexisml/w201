# Power antenna: original wiring, aftermarket unit, and a controller to bring back the switch

**System:** electrical
**Status:** reference; controller planned

The car has the factory automatic antenna option (code 531). The original antenna has been replaced
by an aftermarket 3-wire unit. It works, but in the simplest way: up when it gets a signal, down when
the signal goes away. The dash switch still works, but only as on/off: OFF lowers the mast, AUTO
raises it all the way. This note records how the original
worked, how the aftermarket unit works, and a plan for a small controller that makes the 3-wire
unit behave like the original.

## On this car

| Item | Value | Source |
|---|---|---|
| Option | **531, automatic antenna**: present | [Data card](../general-reference/data-card.md) |
| Antenna fitted now | **Aftermarket 3-wire unit** (ground, +12 V, trigger). Works: up with a signal, down without | Owner |
| Make / model of the aftermarket unit | Not recorded yet | |
| Which car wires it's connected to | Trigger probably on **pin 4 (blue/green)**, the switch's AUTO/UP/MAX line. Not checked yet | Owner |
| Dash switch | In use, but only on/off: **OFF** lowers the mast, **AUTO** raises it all the way (no medium height) | Owner |
| Location | Rear left, front corner of the trunk, bracket on the wheelhouse | EPC 82.345; 1990 US 190E wiring diagram listing |

With the trigger on pin 4, the antenna follows the switch's first section. Pin 4 is live in AUTO, UP
and MAX, so the mast goes all the way up in any of them, and all the way down in OFF, DOWN or with the
radio off. Holding DOWN should lower it, and letting go should send it all the way up again (expected,
not tried). The second switch section (pin 1) and the radio line (pin 5) aren't used.

### Parts (EPC 452)

| Part | Part number | EPC |
|---|---|---|
| Automatic antenna, rear mounted | `A 124 820 01 75` or `A 124 820 17 75` | 82.345 pos 56 |
| Telescopic mast (Hirschmann) | `B66828037` | 82.345 pos 59 |
| Antenna switch (dash rocker) | `A 002 820 98 10` | 82.045 pos 8 |
| Antenna cable | `A 124 820 12 15` | 82.345 pos 5 |
| Connector housing, automatic antenna (harness side) | `A 011 545 51 28` | 82.345 pos 11 |
| Female contacts, 2.5 mm | `A 002 545 99 26` | 82.345 pos 14 |
| Seal, antenna to fender / upper / lower | `A 201 827 01 98` / `04 98` / `05 98` | 82.345 pos 29, 32 |
| Bracket, automatic antenna | `A 201 820 35 14`, `36 14`, `A 201 827 18 14` (variants) | 82.345 pos 68 |

The `A 124 …` part numbers show that the W201 uses the W124 antenna. Older W124s also had the extra
"half-up" wires (blue/yellow and blue/green) for the dash switch.

## How the original works

### Switch positions

The switch is a rocker with 5 positions: two latched, one rest position in the middle, and two
momentary ones next to it.

| Position | Kind | What the mast does (radio on) |
|---|---|---|
| **MAX** | latched | Goes up all the way |
| **UP** | momentary (rock, don't latch) | Goes up while held, then stays |
| **AUTO** (middle, rest) | rest | When the radio comes on, goes to **medium height** |
| **DOWN** | momentary | Goes down while held, then stays |
| **OFF** | latched | Goes down all the way and stays down, even with the radio on |

With the radio off or the key in position 0, the mast always goes all the way down. The switch only
works with the radio on and the key in position 1 or 2.

Sources: the 190 E 2.3 owner's manual (read through a search summary only, see References) and
forum posts about R107, W126 and W123 cars, which all describe the same switch. **Not tried on this
car yet.**

### Wiring (6-pin antenna plug)

The original antenna takes 6 pins (pin 3 not used). The colours come from a factory W126 diagram and
from a 560SL (R107) owner's measurements. The two match. **Not checked on this W201 yet.**

| Antenna pin | Colour | Function | Comes from |
|---|---|---|---|
| 1 | **blue/yellow** (BU/YE) | "Up" command | Dash switch, 2nd section: live in UP and MAX |
| 2 | **red** (RD; RD/WT on the W126) | +12 V at all times (terminal 30) | Fuse; the trunk lamp is fed from the same circuit |
| 3 | — | not used | |
| 4 | **blue/green** (BU/GN) | "Enable / auto" | Dash switch, 1st section: live in AUTO, UP and MAX |
| 5 | **blue/white** (BU/WH) | Radio on | Radio's antenna output, direct |
| 6 | **brown** (BR) | Ground (terminal 31) | Ground point in the trunk |

The radio's antenna output (a single **blue** wire) feeds both pin 5 directly and the dash switch.
The switch passes that +12 V on to pin 4 and pin 1 depending on its position:

| Switch | Pin 5 (radio) | Pin 4 (BU/GN) | Pin 1 (BU/YE) | Result |
|---|---|---|---|---|
| any, radio off | 0 | 0 | 0 | All the way down |
| OFF | 12 V | 0 | 0 | All the way down |
| DOWN (held) | 12 V | 0 | 0 | Goes down while held |
| AUTO | 12 V | 12 V | 0 | Medium height when the radio comes on; otherwise stays where it is |
| UP (held) | 12 V | 12 V | 12 V | Goes up while held |
| MAX | 12 V | 12 V | 12 V | All the way up |

DOWN looks the same as OFF on the wires, and UP looks the same as MAX. The difference is only how
long the signal lasts: a momentary position is let go, a latched one stays. The board inside the
antenna stops the motor where it is when the signal goes back to AUTO.

**Later cars:** around 1990–1992 the switch was dropped. Those antennas have a 4-wire plug: blue
(radio command), two red/yellow (+12 V, one passes on to the trunk lamp) and brown (ground). That
was reported on a 1992 W124 and fits the 1993 190E "red, blue, brown" description.

**Even older cars** (W123/early W126) used a relay-type antenna with a cam contact that stopped the
mast at about 30 cm in the middle position. That's where the "medium height" idea comes from.

## How the aftermarket 3-wire unit works

| Wire | Function |
|---|---|
| +12 V "constant" | Powers the motor and the board. Must be there for anything to move |
| Trigger | +12 V: goes up all the way. No voltage: goes down all the way |
| Ground | |

A board inside senses the end of travel and stops the motor. Tested by forum members on a
Hirschmann-type unit (not tested on ours):

- With the constant cut, the trigger does nothing. **Cutting the constant stops the mast where it
  is.**
- When the constant comes back with no trigger, the mast goes down.
- With trigger + constant, the mast goes up.

That's what makes a controller possible: switching the constant and the trigger separately gives
**up**, **down** and **stop**.

## What others have built

No one online seems to have built exactly this (an Arduino or ESP that reads the original switch and
drives a 3-wire antenna). There are close pieces:

- **Arduino Nano Every driving the antenna motor directly** (Arduino forum, Germany, 2020, a
  Hirschmann Auta 6000 with a dead board). The radio's control wire powers the Nano. A 1-channel
  relay latches its own power on, so it can finish retracting after the radio goes off. A 2-channel
  relay module reverses the motor, and an ACS712-type 5 A current-sense board detects the stall at
  each end. Forum advice: wire the two relays as a proper H-bridge, put flyback diodes on the motor,
  use a step-down regulator against voltage spikes, and clamp the input with a zener. Schematic
  saved. This is the closest to our plan.
- **Replacement Hirschmann control board, Eagle CAD files** (BenzWorld, richy1025, 2013–2015, W124
  300D). A 3-pin board (ground, +12 V, radio signal) that drops into the antenna housing. It uses an
  NE555, two relays and a 0.5–1 Ω current-sense resistor that stops the motor at the end of travel,
  with a delay so the start-up current doesn't trip it. The schematic, layout, Gerbers, parts list
  and test steps were posted. It has no switch inputs, but it shows how the original boards sense the
  end stops.
- **Original boards are swappable modules** (same BenzWorld thread, mclare, 2009–2011). The
  semi-automatic (switch, 5/6-pin) and fully automatic (3-pin) Hirschmann units share the housing and
  motor. The control board slides out, and the motor connects with two plug-in wires (red and green).
  He converted units both ways by swapping boards. Members also report the boards keep driving the
  stalled motor for about 2 to 8 seconds at each end, which wears the gears.
- **Motor polarity** (Jaguar tech page, Sean Straw, 2005, Auta 6000EL): red + / green − = up,
  red − / green + = down. The board is described as an "overload module".
- **W201, US switch** (W201 club forum, 2014): the switch was fitted to US cars for the "half up"
  position. Its place is the third rocker above the center vents, lit by light guides from the
  instrument cluster. One member rewired it as a 3-way selector on the remote line (off / normal /
  always up on terminal 15). The club has a PDF "Funktion Antennenschalter US-Version bis MJ 91"
  (switch function, US version to model year 1991), members only; not read.

I found no teardown of the original 5/6-pin board with the switch logic, and nothing on the radio
side. The radio only gives a +12 V antenna output.

### Three ways to do it

**Preferred: option A**, built from off-the-shelf boards (an Arduino Uno with Infineon's automotive-grade PROFET+2 switch shield; an ESP32 relay board as a cheaper alternative). No custom PCB.

| Option | What | For | Against |
|---|---|---|---|
| **A. Drive the aftermarket unit's wires** (plan below; **preferred**) | Switch its constant and trigger with 2 relays | Unit stays sealed and its own end stop works | Position estimated from motor run time and current, not measured directly; depends on the unit stopping when the constant is cut (test first) |
| **B. Drive the motor directly** (Arduino forum way) | Open the unit, remove its board, H-bridge + current sense | Full control: real stall detection, any height, soft stops | Needs opening the unit; more electronics in the trunk; we own the end-stop logic |
| **C. Original semi-automatic board** | Find a used 5/6-pin Hirschmann board and fit it to a compatible Hirschmann mechanism | Exactly original behaviour, no code | Only if the aftermarket unit is a Hirschmann clone; used boards are old and failing |

## Controller plan: make the 3-wire unit work like the original

A small box between the car harness and the aftermarket antenna. It reads the original signals
(radio, switch pins 4 and 1) and drives the antenna's constant and trigger wires.

```
car harness (original 6-pin plug)            controller                 aftermarket antenna
  pin 2  RD     +12 V permanent  ───────►  power + K1 (relay) ─────►  +12 V constant
  pin 5  BU/WH  radio on         ───────►  input R
  pin 4  BU/GN  switch auto/up   ───────►  input A
  pin 1  BU/YE  switch up/max    ───────►  input U             K2 ─►  trigger
  pin 6  BR     ground           ───────►  ground  ──────────────────► ground
```

### Outputs

| Motion | K1 (constant) | K2 (trigger) |
|---|---|---|
| Up | on | on |
| Down | on | off |
| Stop / hold | off | (keep as it was) |
| Idle (mast down, radio off) | off | off |

### Behaviour

| Inputs | Switch | Controller does |
|---|---|---|
| R = 0 | radio off | Goes all the way down, then sleeps |
| R goes on, A = 1, U = 0 | AUTO | Moves to the "auto" height (setting, e.g. half) |
| R = 1, A = 1, U = 1 | UP held / MAX | Goes up while the input is there (MAX holds it, so it reaches the top) |
| R = 1, A = 0 | DOWN held / OFF | Goes down while the input is there (OFF holds it, so it goes all the way) |
| R = 1, A = 1, U = 0, after a manual move | AUTO (released) | Holds where it is |
| A comes back on (DOWN released, or OFF → AUTO), radio on | AUTO | Holds where it is. The two look the same on the wires, so the original board can't tell them apart either. Toggling the radio goes back to the auto height |
| U = 1 with A = 0 | not possible with a working switch | Treat as a fault: hold |

### Knowing where the mast is

The 3-wire unit gives no position feedback. Two options:

1. **Timing.** Measure the full-up and full-down times once. Track the position by how long the motor
   ran. Reset it to zero after each full retract (run "down" for the full time plus a margin).
2. **Current sensing** (better). A shunt on the constant line shows when the motor runs and when the
   unit's own board stops it at the end of travel. That gives real end points and lets the
   controller measure travel times itself.

### Build

Untested build ideas, one file per controller, with parts lists, wiring and firmware:
[power-antenna-controller/](power-antenna-controller/README.md).

### Keep it reversible

- Plug into the car harness's original connector (housing `A 011 545 51 28`) instead of cutting it.
  The mating plug from the old antenna, or a scrap one, gives a clean adapter.
- Make a **bypass plug** that wires constant to pin 2 and trigger to pin 5. If the controller fails,
  the antenna goes back to the "dumb" behaviour it has today.

### Test on the bench first

1. Measure the aftermarket unit's full-up and full-down times, and its current running and stalled.
2. Check that cutting the constant mid-travel really stops it. Check that restoring the constant
   with the trigger on carries on going up, and with the trigger off goes down.
3. Check that the unit's board doesn't mind being powered on and off often.

## To check on the car

- [ ] Make and model of the aftermarket antenna, and its wire colours.
- [ ] Confirm which car wires it's connected to now (trigger probably pin 4 blue/green; pin 2
      red, pin 6 brown).
- [ ] The original 6-pin plug: still there? Colours as in the table above?
- [ ] Measure pins 5, 4 and 1 with the radio on, in each switch position.
- [ ] The radio fitted: does it have an antenna output, and does it drop out in CD/AUX mode?
- [ ] Fuse number and rating for the antenna (+12 V permanent).
- [ ] Where the switch is and what it looks like.

## References

- PeachParts: Antenna operation ins & outs, 2003–2007 (pages 1–2; the 560SL pinout, the 3-wire unit
  tests and a factory relay-type schematic): [original](https://www.peachparts.com/shopforum/car-audio-multimedia/70719-antenna-operation-ins-outs.html)
  · [Wayback (page 1 only)](https://web.archive.org/web/20230209105930/http://www.peachparts.com/shopforum/car-audio-multimedia/70719-antenna-operation-ins-outs.html)
  · [reference](references/peachparts-antenna-operation/README.md)
- BenzWorld: auto antenna wiring diagram, 2005–2006 (W126 factory diagram of the switch and
  6-pin plug): [original](https://www.benzworld.org/threads/auto-antenna-wiring-diagram.1182554/)
  · [reference](references/bw-auto-antenna-wiring-diagram/README.md)
- BenzWorld: Power Antenna - Dash Switch, 2012 (switch positions; replacement antennas lose the
  height control): [original](https://www.benzworld.org/threads/power-antenna-dash-switch.1660531/)
  · [reference](references/bw-power-antenna-dash-switch/README.md)
- BenzWorld: What does the "ANT." switch do?, 2003 (switch positions, W123): [original](https://www.benzworld.org/threads/what-does-the-ant-switch-do.714675/)
  · [Wayback](https://web.archive.org/web/20230329171054/https://www.benzworld.org/threads/what-does-the-ant-switch-do.714675/)
  · [reference](references/bw-ant-switch/README.md)
- BenzWorld: Antenna wiring, 2017 (later 4-wire W124 antenna): [original](https://www.benzworld.org/threads/antenna-wiring.2823410/)
  · [reference](references/bw-antenna-wiring-w124/README.md)
- Portal Diagnostov: Power Antenna wiring diagram, Mercedes-Benz 190E 1990 (list of parts only; the
  diagram itself needs a login): [original](https://portal-diagnostov.com/en/2020/05/01/power-antenna-mercedes-benz-190e-1990-system-wiring-diagrams/)
  · [reference](references/portal-diagnostov-190e-1990-power-antenna/README.md)
- Mercedes-Benz 190 E 2.3 owner's manual, antenna switch (page 48 on ManualsLib): [original](https://www.manualslib.com/manual/1658926/Mercedes-Benz-190-E-2-3.html?page=48)
  · **not archived** (Cloudflare check, no Wayback copy). Read only through a search summary; check
  against a paper owner's manual.
- BenzWorld: Hirschmann Antenna Rebuild and Control Change, 2009–2024 (5 pages; board swaps,
  richy1025's replacement board files): [original](https://www.benzworld.org/threads/hirschmann-antenna-rebuild-and-control-change.1432845/)
  · [Wayback](https://web.archive.org/web/20261007195021/https://www.benzworld.org/threads/hirschmann-antenna-rebuild-and-control-change.1432845/)
  · [reference](references/bw-hirschmann-rebuild-control-change/README.md)
- Arduino forum: Automatische Versenkantenne mit Arduino steuern, 2020: [original](https://forum.arduino.cc/t/automatische-versenkantenne-mit-arduino-steuern/636315)
  · [Wayback](https://web.archive.org/web/20260203105841/https://forum.arduino.cc/t/automatische-versenkantenne-mit-arduino-steuern/636315/)
  · [reference](references/arduino-forum-versenkantenne/README.md)
- Sean's Jaguar Tech Pages: Repairing the Hirschmann Auta 6000EL Electric Aerial, 2005: [original](http://jaguar.professional.org/aerial/)
  · [Wayback](https://web.archive.org/web/20200218105318/http://jaguar.professional.org/aerial/)
  · [reference](references/jaguar-hirschmann-6000el-repair/README.md)
- W201 club forum (w201-ev.de): Antennenschalter, 2014: [original](https://w201-ev.de/forum/thread/27784-antennenschalter/)
  · [Wayback](https://web.archive.org/web/20261007195936/https://w201-ev.de/forum/thread/27784-antennenschalter/)
  · [reference](references/w201-ev-antennenschalter/README.md). The linked PDF "Funktion
  Antennenschalter US-Version bis MJ 91" is members only: **not archived**.
- Parts data: EPC catalog 452, 82.345 and 82.045, via the private parts catalog (available on request)
