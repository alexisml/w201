# 2026-09-28 — Central locking not working (pump silent)

**Mileage:** 
**Topic:** central-locking
**Status:** open

## Background

- The car has factory central locking: option code **467** on the
  [data card](../general-reference/data-card.md).
- The W201 system works on air pressure, not electric motors. A **bi-pressure pump** blows air to
  unlock and sucks it out to lock. Hoses carry the air to a rubber actuator (vacuum element) in each
  door, the rear lid (trunk) and the fuel filler flap. Switches in the front door locks, and the
  trunk lock, tell the pump which way to run (general W201 info, see the Pelican articles below).

## Symptom

- The central locking doesn't work, and the pump is **silent** when locking or unlocking.
- **Fuses:** all fuses in the fuse box are new.
- **Pump location (verified on this car):** under the rear seat. The catalog says "below rear seat,
  right" (80.045 pos 5), and Pelican shows it in a foam box under the passenger-side rear seat.
- **No water** under the rear seat (checked by the owner), so water damage is ruled out.

## Parts (EPC catalog 452)

From the private parts catalog, groups 80.045 (central locking mechanism) and 82.585 (central
locking wiring). The catalog lists several valid numbers for some positions without saying which
one this car has. Read the number on the old part before ordering.

### Pump

| Part | Number | Catalog position | Notes |
|------|--------|------------------|-------|
| Pump (bi-pressure pump) | **`A 124 800 21 48`** | 80.045 pos 5 | "With central locking mechanism control unit; below rear seat, right". Older pumps `A 124 800 06/07/13/14 48` lead to it through replacements |
| Pump, multi-contour backrest version | `A 124 800 28 48` | 80.045 pos 5 | Only for the orthopaedic (multi-contour) backrest |
| Distributor at the pump | `A 124 800 01 22` | 80.045 pos 8 | |
| Distributor | `A 124 800 02 22` | 80.045 pos 10 | |
| Pump caps, bottom and top | `A 201 800 01 35` | 80.045 pos 6 | |

### Actuators (vacuum elements)

| Where | Qty | Current numbers | Catalog position | Replaces |
|-------|-----|-----------------|------------------|----------|
| Front doors, left and right | 2 | `A 124 800 15 75`, `A 124 800 18 75`, `A 124 800 21 75` | 80.045 pos 11 | `000 800 85 75` → 15 75, `000 800 78 75` → 18 75, `000 800 94 75` → 21 75 |
| Rear doors, left and right | 2 | `A 124 800 17 75`, `A 124 800 20 75`, `A 124 800 23 75` | 80.045 pos 17 | |
| Rear lid (trunk) | 1 | `A 124 800 16 75`, `A 124 800 19 75`, `A 124 800 22 75` | 80.045 pos 26 | `000 800 77 75` → 16 75, `000 800 93 75` → 19 75, `000 800 86 75` → 22 75 |
| Fuel filler flap | 1 | `A 000 800 80 75`, `A 000 800 82 75`, `A 000 800 84 75`, `A 129 800 20 75` | 80.045 pos 32 | `000 800 91 75` → `129 800 20 75` |

### Small parts

| Part | Number | Catalog position |
|------|--------|------------------|
| Rod, front door element | `A 124 805 05 74` | 80.045 pos 35 |
| Rod, rear door element | `A 201 805 01 74` | 80.045 pos 38 |
| Rod, fuel flap element | `A 201 805 08 74` | 80.045 pos 41 |
| Lock (clip joining element and rod) | `A 201 800 10 74` | 80.045 pos 14, 29 |
| Hose, rear door elements | `A 117 078 05 81` | 80.045 pos 59 |
| Hose, fuel flap element (50 mm) | `A 007 997 61 82` | 80.045 pos 56 |
| Hose, fuel flap distributor to rear lid element (1050 mm) | `A 005 997 59 82` | 80.045 pos 62 |
| Distributor, fuel filler flap | `A 201 805 01 22` | 80.045 pos 71 |
| Branch-off fitting, main floor left | `A 117 078 00 45` | 80.045 pos 65 |
| Grommet, lines through rear panel | `A 107 997 29 81` | 80.045 pos 98 |
| Grommet, lines through front panel | `A 008 997 17 81` | 80.045 pos 104 |
| Rubber ring, rear doors | `A 201 987 02 41` | 80.045 pos 101 |

### Wiring

| Part | Number | Catalog position |
|------|--------|------------------|
| Cable harness, front doors to pump | **`A 201 540 30 34`** | 82.585 pos 5 |
| Pump connector (female) | `A 012 545 24 28` | 82.585 pos 17, 41 |
| Contacts for the pump connector | `A 003 545 26 26` | 82.585 pos 20, 44 |
| Cable harness, rear lid | `A 201 543 12 26` | 82.585 pos 23 |
| Plug pins, rear lid lock | `A 011 545 16 28` | 82.585 pos 26 |

The rear lid lock is wired to the pump too, so it can lock and unlock the whole car.
The trunk lock itself is `A 201 750 12 85` ("less key; used with central locking mechanism",
75.030 pos 8).

## Likely causes (ranked)

For a silent pump with good fuses and no water. General W201 and forum experience, not verified on
this car. Prices are rough estimates (2026-09-28), not checked against current listings.

| # | Suspect | Why it fails | Fix | Rough cost |
|---|---------|--------------|-----|------------|
| 1 | **Pump circuit board**: cracked solder joints, bad relay, or a burnt trace near the connector pins | 30+ years of heat and vibration. A stalled motor can burn the power trace | Open the pump, reflow the joints, repair the trace | DIY €0–10 · rebuild service €80–150 |
| 2 | **Pump motor worn** (brushes) | Age, and long running against old leaks | Fit a replacement motor, or buy a pump | Motor under €10–30 · aftermarket pump €120–250 · MB €400+ |
| 3 | **Broken wires in the door sleeve** (driver's side most often) | Flexing every time the door opens | Splice and solder, heat shrink | DIY €0–20 · shop 1–2 h |
| 4 | **Switch in the front door element** | Wear. The front element has an electrical plug (Pelican) | Replace the element | €40–100 aftermarket |
| 5 | **Fuse box clip or ground point** | Oxidation under a good fuse | Clean, bend the clip tight, redo the ground | €0–5 |
| 6 | **Pump connector pins** | Oxidation from age, loose pins | Contact cleaner, re-crimp | €0–20 |

Things that don't cause a silent pump, but often show up once it runs again:

- **Leaking actuators:** fuel flap and trunk most often, then the doors. The pump runs a long time,
  then stops.
- **Cracked hoses:** where they pass between the body and the doors.
- **Broken element-to-rod clips** (`A 201 800 10 74`): the element moves but the lock doesn't.
- **Worn door lock tumbler:** the key doesn't trigger the switch. It works from one door but not
  the other.
- **Sticking trunk lock.**

## Diagnosis plan

1. **Fuse box clips.** New fuses don't prove power. With a test light, check for 12 V on **both
   ends** of the central locking fuse.
2. **At the pump connector.** Lift the rear seat cushion: push in the two clips under the front
   edge and lift it up. Take the pump out of its foam box and unplug it. Then check:
   - constant 12 V to ground
   - the ground pin to the body (near 0 Ω)
   - the signal lines, while a helper turns the key to lock and to unlock (driver's door, then
     passenger's door, then the trunk)

   A w201.com thread describes a round 3-pin connector where the blue, green and yellow wires meet.
   Each wire carries either ground or +12 V, depending on the position of each lock. A w201-ev.de
   thread says remote keyless kits are spliced into the blue control wire at this connector, so
   look for a cut or spliced blue wire left by an old remote kit. Neither is verified on this car.
3. **Read the result:**

   | Power | Ground | Signal | Points to |
   |-------|--------|--------|-----------|
   | no | – | – | Fuse box clip, or the wiring from the fuse box to the pump |
   | yes | no | – | Bad ground point |
   | yes | yes | no | Door sleeve wires or door switch. If the trunk key works but the doors don't, it's the doors |
   | yes | yes | yes | The pump itself → step 4 |

4. **Pump repair before replacement.** Open the pump and look at the board under a magnifier for
   cracked joints and burnt traces. Reflow them. Apply 12 V straight to the motor; if it doesn't
   spin, fit a replacement motor (match the shaft and body size). Buy a new pump only if the board
   can't be saved.

## Fix vs. converting to electric locks

Researched, not verified. Most owners repair the air system, because the usual faults are a leak or
a pump solder job, and all actuators and pumps are still available. Aftermarket electric actuator
kits are cheap but need brackets and new wiring through the doors, handle the trunk and fuel flap
badly, and hurt originality. A popular middle path is to keep the air system and wire a remote
keyless module to the pump's lock and unlock inputs. Either way, the air system has to work first.

## Fix

_(pending)_

## Sources

### Replacing the parts (Pelican Parts, W201)

- [Pelican: vacuum supply pump replacement](https://www.pelicanparts.com/techarticles/Mercedes-190E/49-BODY-Replacing_Your_Vacuum_Supply_Pump/49-BODY-Replacing_Your_Vacuum_Supply_Pump.htm)
  ([Wayback](https://web.archive.org/web/20170926174437/http://www.pelicanparts.com/techarticles/Mercedes-190E/49-BODY-Replacing_Your_Vacuum_Supply_Pump/49-BODY-Replacing_Your_Vacuum_Supply_Pump.htm),
  [saved copy](references/pelican-190e-vacuum-supply-pump/README.md)): rear seat removal, the pump's foam box
- [Pelican: front door latch and vacuum element](https://www.pelicanparts.com/techarticles/Mercedes-190E/13-BODY-Front_Door_Latch_and_Vacuum_Element_Replacement/13-BODY-Front_Door_Latch_and_Vacuum_Element_Replacement.htm)
  ([Wayback](https://web.archive.org/web/20180225062804/http://www.pelicanparts.com/techarticles/Mercedes-190E/13-BODY-Front_Door_Latch_and_Vacuum_Element_Replacement/13-BODY-Front_Door_Latch_and_Vacuum_Element_Replacement.htm),
  [saved copy](references/pelican-190e-front-door-latch-vacuum-element/README.md))
- [Pelican: rear door vacuum element](https://www.pelicanparts.com/techarticles/Mercedes-190E/12-BODY-Central_Locking_Rear_Door_vacuum_element_replacement/12-BODY-Central_Locking_Rear_Door_vacuum_element_replacement.htm)
  ([Wayback](https://web.archive.org/web/20171023040630/http://www.pelicanparts.com/techarticles/Mercedes-190E/12-BODY-Central_Locking_Rear_Door_vacuum_element_replacement/12-BODY-Central_Locking_Rear_Door_vacuum_element_replacement.htm),
  [saved copy](references/pelican-190e-rear-door-vacuum-element/README.md))
- [Pelican: trunk vacuum actuator](https://www.pelicanparts.com/techarticles/Mercedes-190E/50-BODY-Replacing_Your_Trunk_Lock_Vacuum_Actuator/50-BODY-Replacing_Your_Trunk_Lock_Vacuum_Actuator.htm)
  ([Wayback](https://web.archive.org/web/20231106032115/https://www.pelicanparts.com/techarticles/Mercedes-190E/50-BODY-Replacing_Your_Trunk_Lock_Vacuum_Actuator/50-BODY-Replacing_Your_Trunk_Lock_Vacuum_Actuator.htm),
  [saved copy](references/pelican-190e-trunk-vacuum-actuator/README.md)): the reader comments cover worn lock switches

### Repairing the pump

Most of these are about other models' pumps (W140, A140, and so on). Those pumps are built the
same way, so the repair methods carry over, but the parts may not.

- [MBCA Seattle: Central Locking Vacuum Pump Repair](https://www.mbcaseattle.org/single-post/2016/07/18/central-locking-vacuum-pump-repair)
  ([Wayback](https://web.archive.org/web/20260314095836/https://www.mbcaseattle.org/single-post/2016/07/18/central-locking-vacuum-pump-repair),
  [saved copy](references/mbca-seattle-pump-repair/README.md)): worn brushes; motor swapped for a Mabuchi RS-545SH. Model not stated
- [BenzWorld: PSE Pump Post Mortem and Resurrection: FREE Repair!](https://www.benzworld.org/threads/diy-pse-pump-post-mortem-and-resurrection-free-repair.1585361/)
  ([Wayback, page 1 only](https://web.archive.org/web/20191212194111/https://www.benzworld.org/threads/diy-pse-pump-post-mortem-and-resurrection-free-repair.1585361/),
  [saved copy](references/bw-pse-pump-post-mortem/README.md)): W140 pump, worn brushes, motor swap
- [BenzWorld: Central locking pump/PSE pump rebuild](https://www.benzworld.org/threads/central-locking-pump-pse-pump-rebuild.1327873/)
  ([saved copy](references/bw-pse-pump-rebuild/README.md)): W140 owner; motor swapped and soldered back red to red, black to black
- [BenzWorld: Replaced PSE pump motor, still no power to it](https://www.benzworld.org/threads/replaced-pse-pump-motor-still-no-power-to-it.1537481/)
  ([Wayback](https://web.archive.org/web/20230325192936/https://www.benzworld.org/threads/replaced-pse-pump-motor-still-no-power-to-it.1537481/),
  [saved copy](references/bw-pse-motor-no-power/README.md)): W140; after a motor swap the pump still had no power. Reply: a stalled motor can burn the power trace on the board near the pins
- [Restore Your Mercedes: door lock pump repair](https://restoreyourmercedes.com/doorlockpumprepair.html)
  ([Wayback](https://web.archive.org/web/20241210023428/https://restoreyourmercedes.com/doorlockpumprepair.html),
  [saved copy](references/restoreyourmercedes-pump-repair/README.md)): W140 motor swap service, bench-tested
- [EEVblog: Mercedes A140 central lock pump control board repair](https://www.eevblog.com/forum/repair/mercedes-a140-central-lock-pump-control-board-repair/)
  ([Wayback](https://web.archive.org/web/20241210145508/https://www.eevblog.com/forum/repair/mercedes-a140-central-lock-pump-control-board-repair/),
  [saved copy](references/eevblog-a140-pump-board/README.md), text only)
- [BenzWorld: FYI...a fuel pump relay can be repaired!](https://benzworld.org/forums/w201-190-class/1208211-fyi-fuel-pump-relay-can-repaired.html)
  (now at <https://www.benzworld.org/threads/fyi-a-fuel-pump-relay-can-be-repaired.1208211/>)
  ([Wayback](https://web.archive.org/web/20140624172409/http://www.benzworld.org/forums/w201-190-class/1208211-fyi-fuel-pump-relay-can-repaired.html),
  [saved copy](references/bw-fuel-pump-relay-repair/README.md)): an 86 190E 2.3's fuel pump relay; a different part, but the same cracked-joint fix

### W201 forums (German)

- [w201-ev.de: Zentralverriegelung funktioniert nicht](https://w201-ev.de/forum/thread/5086-zentralverriegelung-funktioniert-nicht/)
  ([saved copy](references/w201ev-zv-funktioniert-nicht/README.md), text only): pump on the passenger side under the rear seat; remote kits spliced into the blue wire
- [w201.com: Zentralverriegelung spinnt](https://w201.com/index.php?thread%2F93210-zentralverriegelung-spinnt%2F=)
  ([saved copy](references/w201com-zv-spinnt/README.md)): round 3-pin connector (blue, green, yellow), ground or +12 V per lock position

### Replacement motors

- [Napol Performance: repair motor for W201/W126/W202/W210 pumps](https://napolperformance.com/mercedes-benz-w201-w126-w202-w210-central-locking-vacuum-air-pump-repair-motor-190-190e-190d-c-e-s-class-140-800-10-48.html)
  ([saved copy](references/napol-pump-repair-motor/README.md))
- [Hong Mei: central locking pump inner motor](http://www.hongmei.com.tw/shop/vacuum-pump-motors-parts/benz-central-locking-pump-inner-motor/)
  ([Wayback](https://web.archive.org/web/20210927163929/http://www.hongmei.com.tw/shop/vacuum-pump-motors-parts/benz-central-locking-pump-inner-motor/),
  [saved copy](references/hongmei-pump-inner-motor/README.md), text only)

### Parts data

- EPC catalog 452, from the private parts catalog (available on request): 80.045, 82.585, 72.030,
  73.030, 75.030
