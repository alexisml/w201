# Power antenna controller ideas

**System:** electrical
**Status:** untested ideas

> **These are untested ideas.** Each file in this folder is a design dump for one controller, not a
> finished or proven build. Nothing here has been built or run yet. The wiring comes from
> documentation and forum reports, and the firmware has not been compiled. Use them as a starting
> point, bench-test first, and check everything against your own parts.

The goal: make a cheap aftermarket 3-wire power antenna (ground, +12 V, trigger) behave like the
original Mercedes semi-automatic antenna with the dash switch (MAX / UP / AUTO / DOWN / OFF), using
off-the-shelf boards and no custom PCB. This is "option A" (the preferred option) in
[power-antenna.md](../power-antenna.md), which also has the original wiring and the sources.

## Ideas

| File | Controller | Outputs | Current sensing | Notes |
|---|---|---|---|---|
| [arduino-uno-profet-shield.md](arduino-uno-profet-shield.md) | Arduino Uno R3 + Infineon PROFET+2 12V shield | Automotive-grade smart high-side switches | Built into the switches | Preferred: protected outputs, fewer parts |
| [esp32-relay-board.md](esp32-relay-board.md) | ESP32 4-relay board (7–30 V input) | Relays | INA260 breakout | Cheaper; hobby-grade relays |

Everything below is common to all of them.

## How it works

The car still sends the original signals to the antenna plug: radio on (pin 5), and the two switch
lines (pins 4 and 1). The controller reads them and drives the aftermarket antenna with two
switched outputs:

| Motion | Output "feed" (antenna +12 V) | Output "trigger" |
|---|---|---|
| Up | on | on |
| Down | on | off |
| Stop / hold | off | (as it was) |

The aftermarket antenna needs its +12 V to move at all, so cutting it stops the mast where it is.
That's what makes the in-between heights possible.

**Position.** The antenna gives no position signal. The controller works it out:

- The controller measures the antenna's current on the feed, which shows when the motor is running.
- At the end of travel the motor stalls (the current jumps), or the antenna's own board cuts it
  (the current drops). Either way the controller knows the mast is fully up or fully down. It also
  cuts the power right away at a stall, which saves the gears.
- In between, it counts how long the motor has run, compared with the full travel time. It learns
  the travel time every time the mast goes from one end to the other.

**Behaviour** (with the radio on):

| Switch | Mast |
|---|---|
| Radio turns on, switch in AUTO | Goes to the "auto" height (default half) |
| UP (held) | Goes up while held, stops when released |
| MAX | Goes all the way up |
| DOWN (held) | Goes down while held, stops when released |
| OFF | Goes all the way down |
| Radio off / key off | Goes all the way down, then the controller switches itself off |

**Almost no standby drain.** The controller is off when the radio is off. Turning the radio on powers
it up through the radio's antenna wire. It then switches on a "hold" output that keeps it powered
from the permanent +12 V, so it can still lower the mast after the radio goes off. When the mast is
down it switches the hold output off and powers itself down.

## Control logic: truth table and Karnaugh maps

### Inputs

| Input | Car pin | 1 when |
|---|---|---|
| **R** | 5 (blue/white) | Radio on |
| **A** | 4 (blue/green) | Switch in AUTO, UP or MAX (and radio on) |
| **U** | 1 (blue/yellow) | Switch in UP or MAX (and radio on) |

Both switch lines are fed from the radio wire, and the second section only closes when the first
one does. So some combinations can't happen with working wiring:

- A = 1 or U = 1 needs R = 1.
- U = 1 needs A = 1.

Those combinations are **don't cares (X)** in the maps below, which makes the logic simpler.

### Truth table

| # | R | A | U | Switch / situation | Command |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Radio off (any switch position) | **DOWN**, then power off |
| 1 | 0 | 0 | 1 | impossible | X |
| 2 | 0 | 1 | 0 | impossible | X |
| 3 | 0 | 1 | 1 | impossible | X |
| 4 | 1 | 0 | 0 | OFF, or DOWN held | **DOWN** |
| 5 | 1 | 0 | 1 | impossible | X |
| 6 | 1 | 1 | 0 | AUTO | **AUTO** (hold, or go to the auto height) |
| 7 | 1 | 1 | 1 | UP held, or MAX | **UP** |

### Karnaugh maps

Rows are R; columns are A U in Gray-code order (00, 01, 11, 10).

**DOWN**

| R \ AU | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | **1** | X | X | X |
| 1 | **1** | X | 0 | 0 |

Group the left two columns (A = 0): cells 0, 1, 4, 5. **DOWN = ¬A**

**UP**

| R \ AU | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | X | X | X |
| 1 | 0 | X | **1** | 0 |

Group the middle two columns (U = 1): cells 1, 3, 5, 7. **UP = U**

**AUTO**

| R \ AU | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | X | X | X |
| 1 | 0 | X | 0 | **1** |

Group the right column (A = 1, U = 0): cells 2 and 6. **AUTO = A · ¬U**

### What this means

- The **direction doesn't depend on R** at all: ¬A means down, U means up, and A without U means
  AUTO. "Radio off" is just a case of ¬A.
- **R is still needed**, but only for events, not for direction:
  - R going on wakes the controller up and starts a move to the auto height.
  - R off, with the mast down, lets the controller power itself off.
- **Faults:** U = 1 with A = 0 would make UP and DOWN both true. That can only come from a wiring
  fault, so DOWN wins (it's the safe direction).
- **Today's "dumb" wiring** (trigger on pin 4) is the simplest version of this: trigger = A. So
  DOWN = ¬A (same as above), and UP = A, which covers both AUTO and UP. That's why AUTO now goes all
  the way up.

### AUTO: the part that needs memory

The maps decide **which way** to go, but AUTO alone doesn't say whether to move or hold. That depends
on what just happened:

| Event while in AUTO (A · ¬U) | Do |
|---|---|
| R just went on (radio switched on), or controller just woke up | Go to the auto height (if the position is unknown, first go down to find the bottom) |
| Just came from UP (U fell) | Hold where it is |
| Just came from DOWN or OFF (A rose) | Hold where it is (the original board can't tell DOWN from OFF either) |
| Moving to the auto height | Keep going until it's reached, then hold |

### Outputs

The command, the end stops and the position give the two outputs. T = mast at the top, B = mast at
the bottom (from the current: a stall, or the antenna's own board cutting the motor). G = a move to
the auto height is in progress, with gU = 1 if that move is upwards.

| Command | Feed (antenna +12 V) | Trigger |
|---|---|---|
| UP | ¬T | 1 |
| DOWN | ¬B | 0 |
| AUTO, holding | 0 | (as it was) |
| AUTO, moving to the auto height | G | gU |

Written out: **Feed = U·¬T + ¬A·¬B + A·¬U·G**, **Trigger = U + A·¬U·G·gU** (with ¬A taking priority if
U = 1 and A = 0). The firmware in each idea follows this: `!R` and `!A` go down, `A && U` goes up,
and AUTO goes to the auto height when R has just come on, and otherwise holds.

## Car side wiring (original 6-pin antenna plug)

Colours from the original W201/W124/W126 wiring. **Check them on your car with a multimeter.**

| Car pin | Colour | Signal | Goes to |
|---|---|---|---|
| 2 | red | +12 V permanent | Fuse → shield BAT+ |
| 5 | blue/white | Radio on | Optocoupler input 1 (R), and diode → regulator input |
| 4 | blue/green | Switch: AUTO, UP, MAX | Optocoupler input 2 (A) |
| 1 | blue/yellow | Switch: UP, MAX | Optocoupler input 3 (U) |
| 6 | brown | Ground | Ground bus |

Cars without the dash switch (or later 4-wire harnesses) only have R, +12 V and ground. Connect R to
**both** optocoupler inputs 1 and 2 (R and A) and leave U unconnected. The controller then acts as if
the switch were always in AUTO. (Leaving A unconnected would read as OFF, see the
[logic](#control-logic-truth-table-and-karnaugh-maps).)

## Bypass plug

Make a short adapter that connects car pin 2 → antenna +12 V, car pin 5 → antenna trigger, and
ground → ground. If the controller ever fails, plug this in and the antenna works the simple way
again (up with the radio, down without).

## Bench-test the antenna first

With the antenna on the bench and a 12 V supply, plus a multimeter in series with the +12 V wire:

1. +12 V and ground only: it should go down (or stay down). Note the idle current.
2. Add the trigger: it should go up. Time the full travel and note the **running current** and the
   **current when it hits the top**.
3. Remove the trigger: it should go down. Time it.
4. **Key test:** during travel, disconnect the +12 V. The mast must **stop where it is**. Reconnect
   it with the trigger on: it should carry on up; with the trigger off: it should go down. If the
   antenna doesn't behave like this, option A won't work with it.
5. Measure the current on the trigger wire too. It should be small (a signal, not motor current).

## Test the controller on the bench

Power the box from the bench supply instead of the car: use a switch for "radio on", and two more
switches for the A and U lines (or a real antenna switch). Check every row of the behaviour table.
Watch the serial monitor for current readings, then set `RUN_MA` and `STALL_MA`:

- `RUN_MA`: about halfway between the idle current and the running current.
- `STALL_MA`: about halfway between the running current and the stall current.

## Fit it in the car

Mount the box in the trunk near the antenna, away from water. Connect it to the car's antenna plug
(or splice into the harness with soldered, heat-shrunk joints), and the antenna to the box. Test
again with the real radio and switch.

## Open questions (all ideas)

- [ ] Does the aftermarket antenna stop when its +12 V is cut mid-travel? (Bench test step 4.)
- [ ] Running and stall current of the antenna, to set `RUN_MA` and `STALL_MA`.
- [ ] How much current the radio's antenna output can supply. It has to power the controller for
      about half a second at start-up, until the hold output switches on. If it's too weak, add a
      small 12 V relay driven by the radio wire to switch on the supply.
