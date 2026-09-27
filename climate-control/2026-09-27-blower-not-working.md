# 2026-09-27 — Blower fan not working

**Mileage:** 
**Topic:** climate-control
**Status:** open

## Background

- A while back, a diagnostic-socket blink-code reader showed a fault (owner recalls about 15 blinks)
  that pointed at the **feedback potentiometer**.
- The potentiometer was replaced with **`A 201 821 02 60`**. The reader now shows
  **1 blink = no fault stored**.
- The replacement's lever was slightly different from the original one. A plastic part was removed
  to make the swap, and it went in fine.
- In EPC catalog 452 this part is "resistor, air mixing flap control", 83.045 pos 41. It sits on the
  heater case next to element 38 (actuator (a) in the
  [vacuum actuators entry](2026-09-27-dashboard-removal-vacuum-actuators.md)), and the
  catalog part number matches what was bought.

## Symptom

The blower fan doesn't work.

- It had already stopped working **before** the dashboard came out. The dash is still out
  (not reinstalled yet), so the dash job is ruled out as the cause.
- The 4-speed blower switch was checked and seems to work fine.
- The blower appears to be fed **through the Tempmatik control unit** (owner's reading of the
  circuit).

## Tests done

- **Fuses:** checked many times, all fine.
- **Motor direct test:** removed the blower motor and connected it straight to the 12 V battery. It
  spun, but not very fast. So the motor isn't dead, but it may be weak (worn brushes, a dirty
  commutator or dry bearings), and that should be checked.
- **Tool:** bought a Mercedes *Buchsenkasten* (socket box / breakout box), **124 589 00 21 00**.
  Researched, not yet verified: it's a generic 126-pin box. It connects between a control unit and
  its harness through a **system-specific test cable (adapter)**, so every pin can be measured with
  the circuit live. The WIS / troubleshooting manual gives the expected volts or ohms per pin. Still
  came with test cable **201 589 09 63 00**, labelled **"Prüfkabel Tempmatik USA"**: the test cable
  for the Tempmatik climate control unit, US version. That's this car's system, so the box can
  test the climate control unit directly. Still needed: the WIS / troubleshooting pin-test table
  for Tempmatik USA.

## Parts involved and what tends to fail (EPC catalog 452)

Failure notes are general W201 and forum experience, not verified on this car.

| Part | Number | Catalog position | Prone to fail? / notes |
|------|--------|------------------|------------------------|
| Blower motor | `A 201 820 06 42` | 83.060 pos 32 | **Yes.** Brushes and commutator wear, bearings dry out. This car's motor spins slowly even straight from the battery |
| Blower motor plug (receptacle housing, contacts) | `A 008 545 08 28`, `A 001 545 44 26` | 83.060 pos 35, 38 | Corroded or burnt contacts from high current |
| Tempmatik operating unit (push-button unit; the catalog calls it the "Tempmatik operating unit") | `A 201 830 07 85` / `09 85` / `13 85` | 83.120 pos 5 | **Yes.** Internal relays and cracked solder joints are reported. Main suspect: the blower seems to be fed through it |
| Blower switch (4-speed, on the operating unit) | `A 201 820 17 10` | 83.120 pos 56 | Contacts wear. Checked on this car: seems fine |
| Blower series resistor (speed steps) | `A 201 821 04 60` (cap `A 201 821 00 33`) | 82.075 pos 32 | **Yes.** Its thermal fuse opens, killing the lower speeds; the top speed usually still works |
| Separate heater blower fuse box | `A 123 540 04 50` | 54.045 pos 45 | Corroded fuse clips. Fuses checked on this car: fine |
| Feedback potentiometer (air mixing flap) | `A 201 821 02 60` | 83.045 pos 41 | **Yes.** Already replaced on this car |
| Auxiliary water pump (recirculating pump) | `A 000 835 69/70/75 64` | 83.180 pos 140 | **Yes.** When it fails it can blow the shared fuse. Not the cause here (fuses fine) |
| Interior temperature sensor (roof rail) + its aspirator blower | `A 126 830 08/14 72`, `A 000 830 19 08` | 83.120 pos 77, 71 | Sensor or aspirator fan fails and gives the Tempmatik wrong readings |
| Heater case temperature sensor | `A 201 830 01 72` | 83.060 pos 71 | Tempmatik input |
| Evaporator temperature sensor | `A 201 830 06 72` | 83.060 pos 83 | Tempmatik / A/C input |

## Likely causes (ranked)

Based on the tests so far and forum reports (not verified on this car):

1. **Tempmatik control unit not powering the blower.** It could be a failed internal relay or a
   cracked solder joint. The unit may also be deliberately switching the blower off because of a
   condition it senses; the manual should say whether it ever holds the blower off. Test it with
   the socket box and the "Prüfkabel Tempmatik USA" cable against the service manual.
2. **Blower series resistor** open (its thermal fuse). Suspect it if the lower speeds are dead.
3. **Missing feed or ground** to the Tempmatik unit or the blower, including the ignition switch
   circuit that supplies it.
4. **Weak motor** that stalls under load. It spins slowly even straight from the battery.

## Diagnosis plan

General W201 checks, not yet verified on this car. Work from cheapest to hardest:

1. **Plugs.** The fault came before the dash job, but check that the connectors are clean and seated
   when reinstalling the dash.
2. ~~**Fuses.**~~ Done: all fine.
3. **Which speeds work.** If only the top speed works, the series resistor (or its thermal fuse) is
   the usual suspect, because the top speed bypasses it. If no speed works, go to steps 4 and 5.
4. **Voltage at the motor plug.** Ignition on, blower switch at max: is there 12 V across the motor
   plug?
   - 12 V present, motor still: the motor is bad (brushes, or seized; tapping the housing
     sometimes gets it going briefly).
   - No 12 V: trace back through the fuse, switch, resistor and wiring.
5. ~~**Motor direct test.**~~ Done: the motor spins, but slowly (see above).
6. **Motor health.** Measure the current the motor draws on the battery. Spin the fan by hand to feel
   for drag or grinding, and look at the brushes and commutator. A weak motor explains "slow", but
   not "not running at all" in the car, so step 4 still matters.
7. **Breakout box** (Tempmatik USA cable). Put it on the Tempmatik control unit plug. With the wiring
   diagram, check the feed, ground and blower output pins for each switch position.

## Fix

_(pending)_

## Notes

- The blink code only covers what the control unit monitors. A dead blower motor or blown fuse won't
  necessarily set a code, so a clean readout (1 blink) doesn't rule out a blower fault.

## Sources

Forum reports behind the ranked causes. Wayback has no copies, and the pages couldn't be saved
automatically, so they are **not archived** for now:

- [BenzWorld: w201 190e heater fan not working](https://www.benzworld.org/threads/w201-190e-heater-fan-not-working.1481423/) (Tempmatik can switch the blower off). **Not archived**
- [BenzWorld: 1993 W201 190e 2.6 climate control system fan control has no power](https://www.benzworld.org/threads/1993-w201-190e-2-6-climate-control-system-fan-control-has-no-power.3043488/). **Not archived**
- [BenzWorld: 1988 190e blower not working](https://www.benzworld.org/threads/1988-190e-blower-not-working.3036779/) (ignition switch; "2 relays in that control unit"). **Not archived**
- Parts data: EPC catalog 452, via the private parts catalog (available on request)
- Owner's physical copy of the Mercedes climate control service manual (Tempmatik tests)
