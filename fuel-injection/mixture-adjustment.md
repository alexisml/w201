# Mixture adjustment: CIS-E (KE-Jetronic) duty cycle

**System:** fuel injection
**Status:** reference (not done on this car yet; no readings recorded)

How to check and set the idle mixture on the Bosch KE-Jetronic (CIS-E) system with a multimeter
that reads duty cycle. The control unit outputs a lambda "on/off ratio" at the X11 diagnostic
socket. A reading that keeps moving around 50% means the O2 sensor loop is in control and the
mechanical base mixture is centered.

Everything below is from forum posts, a YouTube comment and wiki articles (see
[References](#references)), **not verified on this car**. The factory WIS procedure for the M102
was not found online.

## On this car

| Item | Value | Source |
|---|---|---|
| Fuel injection | Bosch KE-Jetronic (CIS-E) with O2 sensor | General reference (README) |
| Market | USA (code 491) | Data card |
| Control unit type | **Not checked**: standard (70% at ignition on) or California (85%) | |
| Ignition-on reading | **Not measured yet** | |
| Idle reading, hot | **Not measured yet** | |
| 2500 rpm reading, hot | **Not measured yet** | |
| Mixture screw tamper plug | **Not checked** | |

## Tools

- Multimeter with a duty cycle (%) setting. An analog dwell meter or a voltmeter also works with
  a conversion (see [With a plain multimeter](#with-a-plain-multimeter-no-duty-cycle-setting)).
- 3 mm Allen key, long (a T-handle helps), for the mixture screw in the fuel distributor tower.
- Optional: 2 mm (or 1.5 mm) Allen for the EHA screw. See the warning below before touching it.

## Reading the meter

- **Socket:** X11 diagnostic socket on the left fender, in the fuel/ignition box. Pin 3 = lambda
  on/off signal (100 Hz since 1987), pin 2 = ground, pin 1 = rpm.
- **Mercedes counts the time the signal is low.** Most meters count time high. The YouTube comment
  and psfred put the red lead on pin 3 and black on pin 2 and read 70% with ignition on; Starwiki
  says to swap the leads on a normal meter. Practical check: with ignition on and engine off it
  should read **70%** (85% on California control units). If it reads 30% (or 15%), swap the leads
  or flip the meter's slope setting.
- **Lower % = richer, higher % = leaner.** All sources agree.
- **Fixed readings in steps of 10% are fault codes**, not mixture (factory table, quoted on
  PeachParts):

| Fixed reading | Meaning |
|---|---|
| 0% | Open circuit at pin 3, or too rich |
| 10% | Airflow sensor potentiometer |
| 20% | Full-load contact |
| 30% | Coolant temperature sensor |
| 40% | Airflow sensor potentiometer open |
| 50% | O2 sensor not working (or not warm yet) |
| 70% | No rpm (TD) signal |
| 80% | Altitude sensor |
| 100% | Too lean, O2 sensor shorted, or control unit |

- A **changing** reading means closed loop. That's the one used for adjustment.

### With a plain multimeter (no duty cycle setting)

Pin 3 carries a square wave that switches between about 0 V and battery voltage, 100 times a
second. On **DC volts** a multimeter shows the average of that wave, and the average gives the
duty cycle. This conversion is shown in the PeachParts "mixture settings and EHA current" thread
(2.9 V with a 13.2 V battery ≈ 77%).

1. Meter on DC volts (20 V range). Red lead on **pin 3**, black on **pin 2**.
2. Measure **battery voltage** at the same moment: about 12.4 V with the engine off, about
   13.8–14.2 V running. Use the real number, not a guess.
3. Mercedes duty cycle = **1 − (pin 3 voltage ÷ battery voltage)**.

| What you're checking | Duty cycle | Pin 3 volts, battery 12.4 V (engine off) | Pin 3 volts, battery 14.0 V (running) |
|---|---|---|---|
| Ignition on, standard unit | 70% | ~3.7 V | |
| Ignition on, California unit | 85% | ~1.9 V | |
| Warm-up / O2 sensor not working | 50% | | ~7.0 V |
| Target range when adjusting | 45–55% | | ~7.7–6.3 V |

- **Half of battery voltage = 50%.** That's the target.
- On volts the direction is reversed: **higher voltage = richer**, lower voltage = leaner.
- A digital meter will jump around because the signal is always moving. Watch the middle of the
  swing. An old analog (needle) meter averages more smoothly, if one is handy.
- If the reading sits at about 0 V or at full battery voltage, that's 100% or 0%: a fault or a
  wiring problem, not mixture.
- Not tried on this car yet. Check the 70% with ignition on first. If the reading isn't near 3.7 V,
  the conversion or the leads are wrong.

Another way is EHA current, using the mA range in series with the EHA. See
[Alternative methods](#alternative-methods-not-covered-in-detail).

## Procedure (YouTube comment by @ekaratd, adapted from psfred on PeachParts)

Full text of the comment: [comment.md](references/youtube-190mex-mixture-adjustment/comment.md).
Summary:

1. Remove the air cleaner. Open the X11 socket cover on the fender.
2. Meter on duty cycle, leads on pins 3 and 2 (see above).
3. Ignition on, engine off: about **70%**.
4. Start the engine. It reads **50%** until the O2 sensor warms up, then starts moving (it can drop
   to 30% or lower if rich). Idle until the coolant is at **80 °C**.
5. With the reading moving, put the 3 mm Allen into the mixture screw in the distributor tower.
   Press down **gently**, only until it engages. Pressing harder pushes the airflow sensor plate
   down and adds fuel (Starwiki: it can stall the engine).
6. **Clockwise = richer, counterclockwise = leaner.** Turn in small steps: 1/16 turn (comment,
   psfred), up to 1/4 turn (Starwiki). Release the key and wait about 10 s at idle for the reading
   to settle after each step.
7. Aim for the reading to swing around **50%** (45–55%). That puts EHA current near 0 mA, so the
   control unit has room to correct both ways.
8. Blip the throttle: the reading should briefly go **lower** (acceleration enrichment), then come
   back. If it goes higher, suspect the airflow sensor potentiometer or the throttle switch.
9. Check at **~2500 rpm** too. See the next section.

If the reading stays fixed at 50% and never moves: the O2 sensor is bad or unplugged. Its
connector is **under the floor mat in front of the passenger seat** (psfred; also an MBWorld 190E
thread). If it moves but can't be brought to 50%, something else is wrong (vacuum leak, EHA, sensor).

## Idle vs 2500 rpm, and the EHA screw

The comment says the 2500 rpm reading should be about 10% **lower** than at idle, and if not, to
adjust the screw in the EHA (2 mm Allen, CW richer, CCW leaner, 1/8 turn steps). **No other
source says this:**

- Starwiki: both readings near 50% and **within 10% of each other**, set with both screws.
- Brotherton (ImportCar 2001): EHA correction within 10% between idle and 2000 rpm. A difference
  points to **air leaks** (or, once, a bad EHA).
- A W124 video found readings way off because the EHA was leaking; after replacing it they sat at
  50%.

**The EHA screw is not a simple trim.** It sets the lower-chamber differential pressure in the
fuel distributor. A MB master technician (mbdoc, PeachParts) and Classic Jalopy set it with two
fuel pressure gauges: **0.4 bar** below system pressure with the EHA unplugged (Classic Jalopy:
~6.0 bar closed vs 6.4 bar open). Starwiki also says the screw is behind a cover on the **back**
of the EHA, so the EHA must be removed from the distributor to reach it (fuel will spill). The
comment itself ends by saying the EHA adjustment isn't required.

**Plan for this car:** set only the 3 mm mixture screw. Leave the EHA screw alone unless there are
fuel pressure gauges and a reason to think it was tampered with. If idle and 2500 rpm readings
differ a lot, look for vacuum leaks and EHA leaks first.

## Other checks before blaming the mixture

- **Vacuum leaks**, especially under the throttle body.
- **O2 sensor** working (the reading has to move). With a dead sensor neither the duty cycle nor
  the EHA current method works.
- **Coolant temperature sensor** (30% code), **airflow sensor potentiometer** (10% / 40% codes),
  **throttle / full-load switch** (20% code).
- **OVP relay**: a bad one kills EHA current, giving hard cold starts (ABS light on too).
- **EHA O-rings** (`243 021 00 41` per Starwiki) leak before the EHA itself fails: hard starting and
  wrong mixture.
- **Air in the fuel distributor**: bleed it before adjusting (INOVA video).

## Alternative methods (not covered in detail)

- **EHA current** with a mA meter in series with the EHA (test harness `102 589 04 63 00`, psfred).
  Should hover around **0 mA** (Brotherton), except on "early 190s" where it's positive only and
  centered on **8 mA**. Not known if a 1988 US 190E 2.3 counts as early.
- **CO meter** with the O2 sensor unplugged. No factory CO figure for the US 2.3 found; forum
  numbers (0.5–1.0%, or below 0.5% with cat) are unverified.

## Unknowns

- WIS job number for the M102 mixture adjustment: not found.
- US tamper plug over the mixture screw: described as a steel plug to drill out (Starwiki) or a
  pressed-in ball (forum snippet). Most US cars have had it removed already. Check on this car.
- Whether this car's control unit is a standard or California unit.

## References

- YouTube: Mercedes 190 mixture adjustment, 190mex, ~2014, and the comment by @ekaratd, ~2020:
  [video](https://www.youtube.com/watch?v=vzWADyvsFMs)
  · [comment](https://www.youtube.com/watch?v=vzWADyvsFMs&lc=Ugyj8NLf-tQQD4kwLXh4AaABAg)
  · [Wayback (video page only)](https://web.archive.org/web/20230330003704/https://www.youtube.com/watch?v=vzWADyvsFMs&list=PLPjD4SF-07HBhAF2i5QrkRIeHaUVDcRrm&index=93)
  · [comment text](references/youtube-190mex-mixture-adjustment/comment.md)
  · [reference](references/youtube-190mex-mixture-adjustment/README.md)
- Starwiki: CIS-E Fuel Adjustment, 2021: [original](https://starwiki.info/articles/cis-e_fuel_adjustment)
  · [Wayback (incomplete)](https://web.archive.org/web/20260608025221/https://starwiki.info/articles/cis-e_fuel_adjustment)
  · [reference](references/starwiki-cis-e-fuel-adjustment/README.md)
- Starwiki: Electro-Hydraulic Actuator Valve 000 070 39 62: [original](https://starwiki.info/parts/0000703962)
  · [Wayback](https://web.archive.org/web/20240530054251/https://starwiki.info/parts/0000703962)
  · [reference](references/starwiki-eha-valve/README.md)
- PeachParts: Setting up the EHA, 2003–2007: [original](https://www.peachparts.com/shopforum/tech-help/71584-setting-up-eha.html)
  · [Wayback](https://web.archive.org/web/20250327061928/http://www.peachparts.com/shopforum/tech-help/71584-setting-up-eha.html)
  · [reference](references/peachparts-setting-up-eha/README.md)
- Steve Brotherton: Evaluating Electronic Engine Controls, ImportCar 2001 (PeachParts wiki): [original](https://peachparts.com/wikka/EngineControls)
  · [Wayback](https://web.archive.org/web/20260125095744/http://www.peachparts.com/Wikka/EngineControls)
  · [reference](references/peachparts-brotherton-engine-controls/README.md)
- PeachParts: Mixture settings and EHA current, 2004–2007: [original](https://www.peachparts.com/shopforum/tech-help/99320-mixture-settings-eha-current.html)
  · [Wayback](https://web.archive.org/web/20260116221506/http://www.peachparts.com/shopforum/tech-help/99320-mixture-settings-eha-current.html)
  · [reference](references/peachparts-mixture-settings-eha-current/README.md)
- PeachParts: 88 560SL fuel injection, dmorrison's post with the fault table, 2005: [original](https://www.peachparts.com/shopforum/857443-post6.html)
  · [Wayback](https://web.archive.org/web/20220810164625/http://www.peachparts.com/shopforum/857443-post6.html)
  · [reference](references/peachparts-duty-cycle-fault-codes/README.md)
- PeachParts: Fuel mixture adjustment, 2014: [original](https://www.peachparts.com/shopforum/tech-help/362984-fuel-mixture-adjustment.html)
  · [Wayback](https://web.archive.org/web/20251214133600/http://www.peachparts.com/shopforum/tech-help/362984-fuel-mixture-adjustment.html)
  · [reference](references/peachparts-fuel-mixture-adjustment/README.md)
- PeachParts: duty cycle (70% standard / 85% California control unit): [original](https://www.peachparts.com/shopforum/tech-help/100052-duty-cycle.html)
  · **not archived** (no Wayback copy; the site blocks downloads)
- Classic Jalopy: KE Jetronic EHA Adjustment, 2019: [original](https://www.classicjalopy.com/2019/11/ke-jetronic-eha-adjustment/)
  · [Wayback](https://web.archive.org/web/20251215183227/https://www.classicjalopy.com/2019/11/ke-jetronic-eha-adjustment/)
  · [reference](references/classicjalopy-ke-eha-adjustment/README.md)
- MBWorld: oxygen sensor (190E, O2 connector location): [original](https://mbworld.org/forums/190e-w201/89165-oxygen-sensor.html)
  · [Wayback](https://web.archive.org/web/20110614025642/http://www.mbworld.org/forums/190e-w201/89165-oxygen-sensor.html)
- Videos (**not archived**, videos are not downloaded):
  - Mercedes Benz 260E fuel/air mixture; duty cycle 1987 (Tom Butchen, 2014): [video](https://www.youtube.com/watch?v=fafMXMVhWZ4)
  - Mercedes W124 M103 Adjusting Hertz Duty Cycle And Replacing EHA Valve (MyGermanCars And More, 2020): [video](https://www.youtube.com/watch?v=Ie0G2JSPr9I)
    · [Wayback (page only)](https://web.archive.org/web/20220916075932/https://www.youtube.com/watch?v=Ie0G2JSPr9I)
  - How to check duty cycle Mercedes 124 m103 (Lorain Furniture and Appliance): [video](https://www.youtube.com/watch?v=CFczSUyGjlk)
    · [Wayback (page only)](https://web.archive.org/web/20250720012615/https://www.youtube.com/watch?v=CFczSUyGjlk)
  - Bleeding Bosch K / KE / KE3 Jetronic, when to set mixture to 50% duty cycle (INOVA HIGHTECH, 2021): [video](https://www.youtube.com/watch?v=lDMlrzbsjbU)
