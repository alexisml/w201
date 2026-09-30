# Throttle pedal: dead zone, step and kickdown

**Mileage:** 
**Topic:** engine (throttle linkage)
**Status:** reference. Nothing is known to be wrong; this note is here just in case.

## What the pedal feels like

Observed by the owner:

- In the first part of the pedal travel the car barely speeds up.
- At about **20–30 %** of the travel there is a "step", and after it the engine responds.

## Is it normal?

**Mostly yes.** The dead zone is part of the design. A clear step or a bump that catches is worth a
quick look at the linkage, but it can also just be the point where the throttle starts opening quickly.

### How the linkage works (from the parts catalog, EPC 452, group 07.135)

The pedal cable does not pull on the throttle directly. On the engine it moves a **slotted gate
lever**: a lever with a curved slot, with a **roller** running in the slot. That lever works the
rod to the throttle housing. The curve of the slot sets how far the throttle opens for each bit of
pedal travel, so the response is not linear: the throttle opens little at first, then faster.

| Part | Number | Catalog position |
|------|--------|------------------|
| Slotted gate lever | `A 102 070 04 20` or `A 102 070 91 21` | 07.135 pos 26 |
| Roller | `A 180 072 03 93` | 07.135 pos 20 |
| Circlip, roller to control lever | `N 006 799 00 4001` | 07.135 pos 23 |
| Lever | `A 102 070 98 21` | 07.135 pos 14 |
| Bearing bracket, slotted gate | `A 102 070 85 24` | 07.135 pos 5 |
| Spring (on the linkage) | `A 102 993 09 10` | 07.135 pos 35 |
| Switch, "thrust cutoff" (closed-throttle / overrun fuel cut-off switch) | `A 002 545 68 14` | 07.135 pos 41 |
| Rod, control lever to throttle housing | `A 000 070 98 75` | 07.135 pos 47 |
| Spring (return spring at the throttle housing) | `A 102 993 23 10` | 07.015 pos 101 |
| Rod, cruise control lever to throttle housing | `A 102 070 40 75` | 54.750 pos 101 |

Pedal end (group 30.015):

| Part | Number | Catalog position |
|------|--------|------------------|
| Accelerator pedal | `A 126 300 05 04` | 30.015 pos 5 |
| Pedal lever | `A 201 300 07 25` | 30.015 pos 11 |
| Pedal lever bearing | `A 201 301 02 18` | 30.015 pos 14 |
| Pedal spring | `A 124 993 10 10` or `A 126 993 22 10` | 30.015 pos 29 |
| Pedal stop | `A 126 301 01 41` | 30.015 pos 32 |
| Kick-down switch | `A 001 545 63 14` or `A 001 545 78 14` | 30.015 pos 35 |
| Accelerator cable | `A 201 300 30 30` or `A 201 300 32 30` | 30.015 pos 38 |
| Cable guide with roller | `A 202 301 00 93` | 30.015 pos 39 |
| Rubber buffer, cable to firewall | `A 201 301 02 85` | 30.015 pos 41 |

The catalog lists several valid numbers for some positions. Read the number on the old part before
ordering.

### What the sources say (general info, not verified on this car)

- **The slack is built in.** A 190E owner on PeachParts saw a lot of linkage movement before the
  throttle opened and concluded it seems to be designed that way. Another owner tightened the cable
  until the slack was gone, and then found that the closed-throttle switch no longer closed.
  On an automatic he noticed the effect: with the switch closed, moving the selector from D to 3
  drops straight into 3rd; with it open, the gearbox seems to slip until the revs rise.
  ([PeachParts](https://www.peachparts.com/shopforum/tech-help/34196-190e-throttle-action.html))
- **Keep the switch click.** The throttle cable can be adjusted, but a click must be heard at the
  closed-throttle switch when the pedal is fully released. The engine management and the gearbox use
  it to know the pedal is up. Adjusting both the throttle cable and the kickdown / control pressure
  cable makes the car nicer to drive. (MBClub UK, W124 thread)
- **Cable free play.** About 1 mm of free play at the cable end (figure quoted on MBClub UK).
  A missing or broken return spring gives a limp, unresponsive pedal; the owner there named
  `102 993 09 10` (visible spring) and `102 993 23 10` (hard-to-reach spring under the air filter).
  (MBClub UK, 190E thread)
- **Aftermarket levers exist.** rpm-depot sells an upgraded slotted gate lever that makes the
  pedal-to-throttle ratio "more direct, sportier, and less comfort-oriented". The M102 version lists
  engine 102.985, but only for manual cars without ASR; the automatic version was on a waiting list
  when checked. Their note for the M103 version says that on an automatic the **control pressure
  cable must be readjusted** after fitting, which shows how closely the two are linked.
- **The control pressure cable** (722.4 automatic) tells the gearbox how far the pedal is pressed and
  sets the shift points. It should sit with slight tension. Screwing the white cable nut in slackens it
  and gives earlier shifts; unscrewing it tightens it and gives later shifts.
  ([Sun Valley Mercedes Transmissions](https://www.mercedesdismantlers.com/722.3and722.416_transmission_adjustments.html))
- **Dry linkage sticks.** Corroded ball joints and pivots at the valve cover can make the throttle
  stick, even wide open. Lubricate every 6–12 months; ATF is suggested as the lubricant.
  ([MercedesSource](https://mercedessource.com/problems/engine/throttle-linkages-binding))
- **Notchy pedal.** A W124 owner with a "notch" in the pedal found debris behind the pedal and asked
  about the worn square fitting that holds the pedal to its shaft. (BenzWorld)

### Our reading (not confirmed)

The step at 20–30 % is most likely the point where the roller reaches the steep part of the slot and
the throttle starts opening quickly. No source found names this exact step.

## Just in case: what to check

Only if the step gets worse, catches, or the throttle feels sticky.

1. **Watch the linkage.** Engine off. Someone presses the pedal slowly while you watch the slotted gate
   lever. If the step comes exactly when the throttle starts to move, it's the design. If it comes at
   another point, look for binding.
2. **Roller and slot.** Wear or a missing circlip lets the roller catch or jump.
3. **Ball joints and pivots.** Clean and lubricate them. Check for play.
4. **Springs.** Both return springs present and hooked on.
5. **Closed-throttle switch.** A click when the pedal is released. Don't adjust the slack away.
6. **Control pressure cable.** Slight tension, no binding. Too much tension adds pedal effort and
   moves the shift points.
7. **Cruise control actuator.** Its rod joins the same linkage and can drag.
8. **Pedal end.** The pedal lever bearing, the pedal stop, the kick-down switch and anything under
   the pedal (floor mat, debris).
9. **Kickdown.** See the next section.

## Kickdown

The kickdown switch has nothing to do with the step at 20–30 %. It only acts at the very end of the
pedal travel, when the pedal is pushed to the floor.

### Parts (EPC 452)

| Part | Number | Catalog position |
|------|--------|------------------|
| Kick-down switch, under the accelerator pedal | `A 001 545 63 14` or `A 001 545 78 14` | 30.015 pos 35 |
| Kickdown solenoid valve on the gearbox, magnet coil | `A 000 304 23 90` or `A 000 304 27 90` | 27.045 pos 130 / 205 |
| Kickdown solenoid valve, magnet frame | `A 000 304 22 90` or `A 000 304 28 90` | 27.045 pos 135 / 210 |

### How it works on the 722.4 (general info, not verified on this car)

- The 722.4 shifts hydraulically. The kickdown solenoid is one of its few electrical parts.
- **Two ways to get a downshift at full throttle:**
  - **Mechanical, through the control pressure cable.** Pressing hard pulls the cable and the gearbox
    shifts down on its own. One owner found his solenoid wire had been cut for years and the car still
    kicked down, up to about 55 mph.
  - **Electrical, through the switch and solenoid.** With the pedal on the floor, the switch powers the
    solenoid on the gearbox, which forces the downshift at higher speeds too (above about 55 mph in
    that owner's case). At low speed it can give a double downshift.
- **The circuit:** fuel pump relay → kick-down switch under the pedal → solenoid on the gearbox (at
  the rear, on the right). The switch gets its power through the fuel pump relay, so it is only live
  when the relay is on (engine running). One BenzWorld poster says the feed also goes through the A/C
  ("Klima") relay; not checked for this car.
- **The solenoid** is a coil sealed in epoxy. It rarely fails, and if it does it's open or shorted.
  A good one draws about **1 A at 12 V**, so about 12 Ω. (W126 thread; same design, not checked
  against the factory manual.)

### Expected behavior

- **Pedal feel (typical, not confirmed on this car):** the switch sits under the pedal and is only
  pressed in the last bit of travel, past full throttle, so it feels like a firmer spot right at the
  floor. It should not be felt anywhere in the middle of the travel.
- **On the road** (in D, at part throttle in a higher gear): floor it, and the gearbox drops one gear
  (two at low speed) straight away and holds it to higher revs. It should work at motorway speeds too.
- **When you lift off:** it shifts back up normally. It should never stay stuck in a low gear.

### Signs something is off

- **No downshift at all, at any speed**, plus very early upshifts (4th by 12–15 mph): points to the
  control pressure cable (loose, broken or badly adjusted), not the kickdown switch. The cable should
  just touch when the linkage is at idle. (190E 2.0 thread on BenzWorld)
- **Downshifts at low speed but not above about 55 mph:** the electrical side (switch, fuel pump
  relay, wiring, solenoid).
- **Stuck in a low gear, or won't upshift:** check for a switch stuck closed or constant power at the
  solenoid (our reading, not from a source).
- **A fuse blows under kickdown:** a shorted solenoid wire. One owner's wire was pinched between the
  gearbox pan and the case.

### How to check

1. **Pedal:** lift the carpet under the pedal. Check that the switch is there, the plug is on, and
   the pedal presses it at the bottom of its travel.
2. **Listen:** ignition on (engine running if the switch isn't live with the key alone). Someone
   presses the switch by hand or floors the pedal while another person under the car listens for a
   click at the solenoid on the gearbox.
3. **Voltage:** at the switch, the feed wire should have 12 V. The output wire to the solenoid should
   read 12 V only while the switch is pressed. Check the switch's fuse and the fuel pump relay if
   there's no feed.
4. **Solenoid:** unplugged, about 12 Ω across it. Check the wire along the gearbox for damage.
5. **Road test:** a downshift when floored at about 30 mph and again above about 55 mph.

## Sources

- **PeachParts forum: 190E Throttle action** (2002):
  <https://www.peachparts.com/shopforum/tech-help/34196-190e-throttle-action.html>
  ([Wayback](https://web.archive.org/web/20230514195833/http://www.peachparts.com/shopforum/tech-help/34196-190e-throttle-action.html),
  [saved copy](references/peachparts-190e-throttle-action/README.md)): designed-in slack, and the
  closed-throttle switch's effect on the automatic
- **MBClub UK: Throttle pedal unresponsive on 190E (Manual)** (2006):
  <https://forums.mbclub.co.uk/threads/throttle-pedal-unresponsive-on-190e-manual.27115/>
  ([Wayback](https://web.archive.org/web/20250515201658/https://forums.mbclub.co.uk/threads/throttle-pedal-unresponsive-on-190e-manual.27115/),
  [saved copy](references/mbclub-190e-throttle-unresponsive/README.md)): cable free play, the two
  springs and their part numbers
- **MBClub UK: W124 throttle travel** (2011):
  <https://forums.mbclub.co.uk/threads/w124-throttle-travel.119394/>
  ([Wayback](https://web.archive.org/web/20201027033512/https://forums.mbclub.co.uk/threads/w124-throttle-travel.119394/),
  [saved copy](references/mbclub-w124-throttle-travel/README.md)): adjust both cables, keep the switch click
- **rpm-depot: M102 upgraded throttle lever** (product page):
  <https://rpm-depot.de/en/product/m102-upgraded-throttle-lever-mercedes-w201-190e-1-8-2-0-2-3-w124-a1020700420/>
  ([saved copy](references/rpm-depot-m102-throttle-lever/README.md)). Wayback refuses the site.
- **rpm-depot: M103 Kulissenhebel** (product page, German):
  <https://rpm-depot.de/produkt/upgrade-gashebel-mercedes-w201-190e-2-6-w124-r107-r129-m103-kulissenhebel-a1030702821/>
  ([saved copy](references/rpm-depot-m103-kulissenhebel-de/README.md)): control pressure cable note
  for automatics. Wayback refuses the site.
- **Sun Valley Mercedes Transmissions: 722.3 and 722.416 series transmission adjustments**:
  <https://www.mercedesdismantlers.com/722.3and722.416_transmission_adjustments.html>
  ([Wayback](https://web.archive.org/web/20250713204217/http://mercedesdismantlers.com/722.3and722.416_transmission_adjustments.html),
  [saved copy](references/mercedesdismantlers-722-adjustments/README.md))
- **MercedesSource: Throttle Linkages Binding**:
  <https://mercedessource.com/problems/engine/throttle-linkages-binding>
  ([Wayback](https://web.archive.org/web/20220815140259/https://mercedessource.com/problems/engine/throttle-linkages-binding),
  [saved copy](references/mercedessource-throttle-linkage-binding/README.md))
- **BenzWorld: Throttle notch (accelerator pedal?)** (2021, W124 300E):
  <https://www.benzworld.org/threads/throttle-notch-accelerator-pedal.3080268/>
  ([saved copy](references/bw-throttle-notch/README.md)). No Wayback snapshot.
- **MBWorld: Adjust accelerator pedal?**:
  <https://mbworld.org/forums/mercedes-tech-talk/223760-adjust-accelerator-pedal.html>
  **not archived**: blocked by a bot check and not on Wayback. Search snippets say it describes a
  roller running along a flat part of a bracket for the first inch of pedal travel, but the page
  itself couldn't be read.
- **BenzWorld: How does the 722.4 kickdown work?** (2013):
  <https://www.benzworld.org/threads/how-does-the-722-4-kickdown-work.1716118/>
  ([saved copy](references/bw-722-4-kickdown-how/README.md)): mechanical kickdown up to about 55 mph,
  the solenoid above that. No Wayback snapshot.
- **BenzWorld: Kickdown diagnostic** (W126 section):
  <https://www.benzworld.org/threads/kickdown-diagnostic.1279657/>
  ([saved copy](references/bw-kickdown-diagnostic/README.md)): switch fed from the fuel pump relay,
  voltage test, solenoid draws about 1 A, pinched wire. No Wayback snapshot.
- **BenzWorld: 190E auto very early shift into top and no kickdown** (2016):
  <https://www.benzworld.org/threads/190e-auto-very-early-shift-into-top-and-no-kickdown.2552321/>
  ([saved copy](references/bw-190e-early-shift-no-kickdown/README.md)): control pressure cable
  symptoms, the three parts of the kickdown circuit. No Wayback snapshot.
- Parts: private parts catalog, EPC 452, groups 07.015, 07.135, 27.045, 30.015 and 54.750.
