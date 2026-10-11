# Coolant sensors and thermovalves at the thermostat

**Mileage:** 
**Topic:** cooling (also fuel injection and fan control)
**Status:** reference. Parts on the car identified 2026-10-05, corrected 2026-10-10. The green injection sender first read 0 Ω, later 1.18–1.29 kΩ warm, so it is probably fine (see [Findings](#findings)).

Five parts (four temperature sensors and a thermovalve) thread into the cylinder head, next to the
thermostat housing. Each one seals with a sealing ring, `N 007 603 01 4100`. Part numbers come from
the parts catalog (EPC 452, group 01.065, cylinder head & gasket kit, positions 92 to 107).

Contents: [On this car](#on-this-car) · [Findings](#findings) · [Catalog](#catalog) ·
[Diagnostics](#diagnostics) · [Research notes](#research-notes) · [Sources](#sources)

---

## On this car

Markings read by the owner on 2026-10-10. The "identified as" column is matched against the catalog
below, not verified unless it says so.

| # | What the owner sees | Identified as | Confidence | Still to check |
|---|---------------------|---------------|------------|----------------|
| 1 | Thermo vacuum valve, `50AN6 F8T`, **2 connectors** | Pos 101 thermovalve, opens at 50 °C (`A 000 140 71 60` / `72 60`) | Medium: "50" fits the 50 °C valve; the rest of the marking is not decoded | Part number on the body; where its hoses go |
| 2 | Blue, 2 wires (green, brown), `905/26/1` | A/C cut-off sensor `A 008 542 45 17`; per the Tempomatic manual probably the 110 °C compressor cut-out switch (closes to ground at ~110 °C, opens ~103 °C) | High (the gauge sender is the 1-wire part, so this can't be it) | `905/26/1` is undecoded; may be a date code |
| 3 | Red, 2 pins, 3 wires, `100 95 - 5169`, "made in Italy" | Pos 98 fan switch, probably `A 006 545 40 24`; "made in Italy" suggests a non-Mercedes replacement (e.g. Facet/EPS, unconfirmed) | High on the function; medium on the number (no part number on the body, owner 2026-10-11; the match rests on the `100 95` marking) | Wiring (see [Pos 98 wiring](#pos-98-wiring)) |
| 4 | Black, 1 wire, `01/20/1` (approx.) | Pos 92 dash gauge sender (`A 005 542 10 17` / `26 17`) | Medium-high (owner's inference from the single wire) | Re-read the marking; confirm its wire goes to the dash gauge |
| 5 | Green, 2-pole, `5427717` | Pos 95 coolant sensor `A 006 542 77 17` (Bosch 0 280 130 044): **two NTC elements, one pin for the fuel injection and one for the EZL ignition** (SM 15, 15-510) | High: `5427717` is the tail of `006 542 77 17` | — |
| 6 | Round plug, 1 pin, unplugged, wired to the red switch's output pin (**not one of the 5**) | Unknown. Not the fan clutch: the clutch's own plug is connected elsewhere (see [Fan clutch circuit](#fan-clutch-circuit-2026-10-11)). Possibly the 20.015 switch, `A 006 545 37 24` (warning lamp, per a listing) | Low | Continuity to the clutch cable; what it should plug into |

**Corrected 2026-10-10:** the black sender has one wire, so it is the gauge sender (pos 92), not the
injection sender. The green `77 17` is the injection sender. An earlier version of this page said the
black `56 17` was on the car; that was wrong. `56 17` stays in the catalog only as another listed
option.

### To do

- **Transmission vacuum modulator (deferred by the owner, 2026-10-11):** check the capped upper port on
  intake runner #3, the modulator and its line for transmission fluid, the fluid level and colour,
  and how the transmission shifts. See [Thermovalve](#thermovalve-pos-101-vacuum), transmission vacuum
  port.
- **Thermovalve's disconnected hose:** identify where it belongs (in progress).
- **Fan switch (2026-10-11):** check how the round plug's wire meets the 2-pin plug (own wire or a
  crimp shared with another wire), then replace the 2-pin `100 95` switch with a 3-pin
  `A 006 545 42 24` and a new sealing ring `N 007 603 01 4100`. **Bought 2026-10-11: Facet 7.5637**
  (for `42 24`, about USD 37). On arrival: check 3 pins (one round), bench-test in hot water (which pair
  closes at about 100 °C, which at about 107 °C), then fit. Sealing ring still to buy. See
  [Pos 98 wiring](#pos-98-wiring).
- **Fan clutch doesn't engage when the red switch is jumped (2026-10-11):** find the relay that clicks,
  measure the clutch coil, and check for 12 V at the clutch plug while the switch is jumped. See
  [Fan clutch circuit](#fan-clutch-circuit-2026-10-11).

### Wire colours (factory diagrams)

From the wiring diagram for this exact model (Tempomatic manual, Fig. 83/5 "Wiring diagram, Tempmatic
climate control, model 201.028", model year 1987) and the ignition manual (group 15, 15-540). Mercedes
codes: sw black, bl blue, gn green, br brown, ws white, rt red. Sizes in mm². Compare with what is on
the car before trusting any of it: this car is a 1988 and parts have been changed.

| Part on the car | Factory item | Terminal | Wire | Goes to |
|---|---|---|---|---|
| Red fan switch (item 3; should be 3-pin) | S25/4, 100/110 °C switch | 1 | 0.75 **black/blue/green** | X48/2, circuit 15 (ignition +12 V): common feed |
| | | 2 | 0.75 **black/blue** (two wires) | X15 connector → fan clutch Y2 (100 °C stage); and double-contact relay K8 |
| | | 3 (round pin) | 0.75 **black/green** | auxiliary fan relay high K9, terminal 4 (110 °C stage) |
| Fan clutch | Y2 | feed / ground | 0.75 black from X15 / 0.75 **brown** to ground W11 | |
| Aux fan relay high | K9 | 4 / 5 | black/green from S25/4 / 0.75 brown to ground W3 (coil) | |
| Black 1-wire sender (item 4) | B13, coolant temperature gauge sensor | 1 pin | 0.75 **green** | electrical center F1 (U4), then 0.5 green to the gauge A1p1; body is ground |
| Blue sensor (item 2)? | S25/3, 110 °C compressor cut-out switch | 1 pin | 0.75 **brown/white** | A/C compressor control unit N6; body is ground |
| Green 2-pin sensor (item 5) | B11/2, coolant temperature sensor (EZL / CIS-E) | — | 4-pin version from 09/89 only: EZL signal 0.75 **green/black**, CIS-E signal 0.75 **green/red**, plus brown and brown/white grounds | ignition module N1/2 and CIS-E control unit N3. The 2-pin version on this car isn't drawn; its two wires are probably the green/black and green/red signal wires (unconfirmed) |
| Thermovalve (item 1) | — | — | no wires (vacuum only) | |

**Open points against the car:**

- The **blue sensor** has **green and brown** wires, but the factory compressor cut-out switch S25/3
  is a 1-pin part with a **brown/white** wire. Check whether the blue's "brown" is brown/white, and
  where its green goes. It may not be S25/3.
- The **black gauge sender** should have a **green** wire.
- The **loose round plug** should be **black/green**; the switch plug's single wire black/blue/green and
  its two wires black/blue.

### Wiring seen so far

**Item 3, red fan switch (pos 98).** 2 pins and 3 wires, all black with a blue stripe. One wire runs
to the round-plug 1-pin sensor (item 6). That fits a shared feed: one pin may carry two wires and the
other pin is the output. Unknown: which wire goes where; mark them before unplugging anything.

**Item 6, round-plug 1-pin sensor.** Just unplugged, wire intact, plug round and a different style
from the others; the sensor side is a **simple round single pin** (owner, 2026-10-11). A retailer listing gives `A 006 545 37 24` as a coolant **warning lamp** switch, not a
fan switch, so if this is that part it feeds a dash lamp, not the fans (see
[Research notes](#research-notes)). Not confirmed. Its wire is on the red switch's output pin; the
fan clutch has its own plug, connected elsewhere (2026-10-11), so this is not the clutch feed. Its
plug looks nothing like the clutch's 1-pin connector, so it is not an alternative factory clutch
feed either. Best lead: it is for the **third terminal of a 3-pin fan switch** (A/C cars), replaced at
some point by the 2-pin one on the car (see [Pos 98 wiring](#pos-98-wiring)). Unconfirmed. It carries
+12 V when the red switch closes, so keep it insulated and away from metal.

**Item 7, sensor on the replacement water pump (owner, 2026-10-11).** The water pump was replaced
(date not recorded); the new pump has a sensor with a flat-tab connector, and nothing is connected to
it. Not known whether the old pump had one; the EPC lists a temperature switch at the water pump
(20.015 pos 26). It is **not** for the loose round plug (item 6): that wire is on the red switch's
switched +12 V side, which would short a switch that closes to ground. Still to do: read its marking.

**Voltage readings at the red switch and the loose plug (owner, 2026-10-11).** Ignition on, engine
cold: the red switch's **single wire reads 12 V**, and its **two-wire pin reads 0.07 V**, including the
wire that goes to the unplugged round connector. Reading: the single wire is the **feed**
(switched +12 V). The two-wire pin is the **output side**, sitting near 0 V because it is pulled to
ground through a load (for example the fan clutch solenoid, which has a permanent earth per a UK report)
while the red switch is open. The round connector's wire is therefore on that output side, **not a
live 12 V feed**, so it is a second load branch or something fed from the same switch. Which device it
feeds is unknown. The red switch was **plugged in** for these readings. With the ignition off, the
loose wire to ground reads **OL (open)**. So the loose wire has no DC path to ground, and the load I
guessed (clutch solenoid) is **not** electrically connected to that node: either the other wire on
that pin goes somewhere else, or the clutch solenoid, its plug or its earth is open. Not yet checked:
where the other wire on that pin goes, and the resistance of the fan clutch solenoid at its own plug.

#### Fan clutch circuit (2026-10-11)

Owner checks on 2026-10-11, in order:

1. **Harness route.** The red switch's wires run in a bundle with a green wire that goes to a coolant
   sensor (connected, only a landmark). The round 1-pin plug's wire is in the same bundle.
2. **Clutch plug.** The fan clutch has its own **1-pin connector**, which is **plugged into another
   cable** that runs **below the intake manifold**. The plug looks original, no splices. So the loose
   round plug is **not** the clutch feed.
3. **Not wired on permanently.** Ignition off and on, the fan turns by hand with the same light drag,
   so the clutch is not fed all the time (a known bodge: a previous owner hot-wires the clutch on).
4. **Jumper test.** Ignition on, engine off, the red switch's plug terminals jumped: **clicks from the
   back of the engine bay** (a relay), but the **clutch did not engage**.

Reading (not confirmed): the red switch drives a **relay**, and the relay feeds the clutch through the
cable under the manifold. That fits the earlier OL reading: the switch output goes to the relay input,
not straight to the clutch. The control side works (it clicks); the fault is after it: the relay's
contacts or fuse, the wire under the manifold, or the clutch coil or its earth. A 1986 190E 2.3-16
owner on BenzWorld had the same 2-prong layout (one prong with one wire carrying 12 V, the other with
two wires) and replaced a "K-8 relay in the fuse panel"; on that car, jumping the plug made the clutch
lock ([BenzWorld, 2012](https://www.benzworld.org/threads/fan-clutch-relay-testing.1653488/),
[Wayback](https://web.archive.org/web/20261011152856/https://www.benzworld.org/threads/fan-clutch-relay-testing.1653488/),
[saved copy](references/bw-fan-clutch-relay-testing/README.md)).

Caution: on a 1986 190E 2.3 (US), jumping the red sensor turned on the **high-speed electric fans**, not
the clutch ([PeachParts, 2008](https://www.peachparts.com/shopforum/tech-help/220289-190e-location-sensor-electromagnetic-fan.html),
[saved copy](references/peachparts-190e-electromagnetic-fan-sensor/README.md)). So the relay that
clicked may be the **auxiliary fan relay**. Check whether the electric fans in front of the radiator
ran during the jump.

**Where the relay probably is.** Under the hood, in the **separate relay box just in front of the main
fuse box** (left side, near the firewall, which fits "behind the engine"). A BenzWorld poster places the
fan clutch relay there as "the silver relay", and another owner names it K-8 (same thread as above);
an '85 190E 2.3 owner traced a wire from the sensor bundle by the thermostat to "the black fuse/switch
box" in front of the main fuse box ([PeachParts, 2000](https://www.peachparts.com/shopforum/30842-post1.html),
[Wayback](https://web.archive.org/web/20210224173151/http://www.peachparts.com/shopforum/30842-post1.html),
[saved copy](references/peachparts-85-190e-aux-fan-advice/README.md)). A fuse-box guide lists the
auxiliary fan relays (K9, K8/1) in that same box ([fuseandrelay.com](https://fuseandrelay.com/mercedes/w201.html),
[Wayback](https://web.archive.org/web/20260617194939/https://fuseandrelay.com/mercedes/w201.html)). Not confirmed on this car. To find it: a helper jumps the switch while you
listen at the box, or feel the relays for the click. Relays may vary by year and options, so read the
label on the box cover.

**Next tests:**

1. Ignition off, clutch plug off: clutch side to the engine should read a few Ω (OL = open coil or lead).
2. Engine off, hands clear: +12 V from the battery through a 5–10 A fused jumper to the clutch side for
   1–2 s. The fan should lock.
3. Helper jumps the red switch, ignition on: measure the harness side of the clutch plug to ground.
   12 V = relay and wiring OK, fault is the clutch or its earth. 0 V = relay, its fuse, or the wire
   under the manifold.
4. Swap the clicking relay with an identical one in the box, if there is one.

**Item 2, blue A/C cut-off sensor.** Green and brown wires. Brown is the usual Mercedes ground
colour, so brown is probably the return and green the signal to the A/C control unit, which fits a
2-pin temperature-dependent resistor. Not verified against a diagram.

**Item 1, thermo vacuum valve.** 2 connectors, so a plain two-port valve (open or closed), not a
three-port changeover valve. Probably the fuel-vapour purge valve's vacuum switch; see
[Thermovalve](#thermovalve-pos-101-vacuum). Its colour (red = 50 °C, yellow = 70 °C) is not recorded.

### Findings

**Green injection sender, first reading: 0 Ω (2026-10-10).** Plugs removed, each pin to the engine
body, meter on the 2 kΩ range: 0 Ω cold and hot. At the time this looked like a shorted sender.

**Green injection sender, second reading: 1.29 kΩ and 1.18 kΩ (2026-10-11).** Factory manual (group 15, 15-510): each pin is a separate NTC element (one for the injection, one for the ignition), so a small difference between pins is expected. Engine on for about 5
minutes, warm to the touch, one value per pin (assumed pin to body). Against the
[resistance table](#resistance-table): 1.18 kΩ is 40 °C, 1.29 kΩ is about 38 °C, and a sender warm to
the touch after 5 minutes is plausible at that temperature. Both pins are close (about 9 % apart,
about 3 °C). **So the sender works; the first 0 Ω reading was most likely a measurement error**, for
example the meter not on resistance, or a bad contact. The "sender very likely bad" conclusion is
withdrawn.

- Status: **sender OK, not suspect** (pending a cold reading).
- Still worth a check: the exact coolant temperature at the time of the reading (an infrared
  thermometer on the thermostat housing), and one cold reading on the 20 kΩ range, which should be
  about 2.5 kΩ at 20 °C.
- The small pin-to-pin difference may be normal for a dual-element sender or a contact effect; a
  large gap, or a difference that doesn't follow temperature, would not be.
- Don't replace it on this evidence.

---

## Catalog

### Sensors and thermovalves

| Pos | Part | Function | Part numbers | Sealing ring |
|-----|------|----------|--------------|--------------|
| 92 | Sender unit | Dash water temperature gauge. On this car: the black 1-wire sender (number to check) | `A 005 542 10 17`, `A 005 542 26 17` | `N 007 603 01 4100` |
| 95 | Sender unit | KE-Jetronic injection (coolant temp); the `77 17` is listed "for California" | `A 006 542 56 17`; also listed: **`A 006 542 77 17` (on this car)**, `A 008 542 32 17` | `N 007 603 01 4100` |
| 95 (alt.) | Temperature sensor | A/C "off" emergency switch, cuts the A/C at 130 °C; in the hole next to the injection sender | **`A 008 542 45 17` (on this car)** | `N 007 603 01 4100` |
| 98 | Temperature switch | Fan coupling (dual switch, see [Pos 98 wiring](#pos-98-wiring)). On this car, probably `40 24` | `A 006 545 15 24`, `A 006 545 40 24`, `A 006 545 42 24`, `A 006 545 91 24` | `N 007 603 01 4100` |
| 101 | Thermovalve (vacuum) | Opens at 50 °C, on cylinder head | `A 000 140 71 60`, `A 000 140 72 60` | `N 007 603 01 4100` |
| 101 | Thermovalve (vacuum) | Opens at 70 °C | `A 000 140 80 60`, `A 001 140 62 60` | `N 007 603 01 4100` |

The catalog lists the sealing ring at pos 107 with qty 3, so it may not count the thermovalve. Buy
one per part you remove.

### Related parts

| Catalog ref | Part | Part numbers | Note |
|-------------|------|--------------|------|
| 01.065 pos 104 | Screw plug | `N 007 604 01 4110` | Plugs an unused sensor hole |
| 20.015 pos 26 | Temperature switch | `A 006 545 37 24`, `A 006 545 90 24` | At the water pump / thermostat housing; ring `N 007 603 01 4100` (pos 29) |

The engine harness has a plug for a "temperature switch, 100 degs", probably the 20.015 switch. Not
checked.

### Sealing ring `N 007 603 01 4100`

A plain flat DIN 7603 sealing washer, 14 mm inside diameter, so any generic DIN 7603 ring of the
same size works; the original isn't needed.

- **Size:** several references give an 18 mm outside diameter, and most give 1.5 mm thickness (a few
  say 2 mm). **Target: 14 × 18 × 1.5 mm.** Material not confirmed (the old ones look like copper).
- Related Mercedes rings of the same series are 14 × 20 × 1.5 mm (`N 007 603 01 4106` copper,
  `01 4104` aluminium).
- Generic match: copper ring 14 × 18 × 1.5 DIN 7603 A
  ([eHorst](https://ehorst.de/en/Kupferdichtring-14x18x1-5-DIN-7603-A-1123879.html),
  [saved copy](references/ehorst-copper-ring-14x18/README.md)).
- An assortment of DIN 7603 form A (flat, solid) copper rings works too, if it includes 14 × 18 × 1.5
  (owner's idea, 2026-10-11). Avoid form C (filled/crush) rings for these sensors. Aluminium form A
  rings also work: Mercedes lists an aluminium ring in the same series (`N 007 603 01 4104`, 14 × 20),
  and they suit the aluminium head. Use them once; don't reuse.
- Measure an old ring before buying. Use a new ring every time; copper rings can be reused after
  annealing.

### Pos 95: `56 17` vs `77 17`

The catalog only labels `A 006 542 77 17` "for California" and gives no other reason. The green
`77 17` is Bosch 0 280 130 044
([EuroSport Tuning](https://eurosporttuning.com/temperature-sensor-0-280-130-044/),
[saved copy](references/eurosporttuning-bosch-0280130044/README.md)) and is sold for many models
([FCP Euro](https://www.fcpeuro.com/products/mercedes-engine-coolant-temperature-sensor-mer-0065427717),
[saved copy](references/fcpeuro-0065427717/README.md)), so it may have become the general
replacement. `56 17` is the black version
([BenzWorld](https://www.benzworld.org/threads/the-engine-temperature-sensors.3084442/),
[saved copy](references/bw-engine-temperature-sensors/README.md)); it is not the one on this car.

The temperature curve is probably the **same** for all of them: the factory test page for the
EZL/CIS-E sensor (B11/2) says the 4-pin sensor's resistances are identical to the 2-pin sensor's, and
a W126 owner found the same table in the 190E manual
([BenzWorld](https://www.benzworld.org/threads/coolant-temperature-sensors-tests-readings-locations-and-more.2795522/),
[saved copy](references/bw-coolant-sensors-tests-readings/README.md)).

### Pos 98 wiring

The switch on the car shows 2 pins and 3 wires. A 201.028 owner reports that the M102 switch holds
two switches: the lower temperature (about 100–105 °C) engages the fan clutch, the higher (about
110 °C) turns on the auxiliary electric fan, both switching +12 V
([PeachParts](https://www.peachparts.com/shopforum/568571-post4.html),
[saved copy](references/peachparts-190e-dual-temp-switch/README.md)). That needs a shared feed
plus two outputs, so 3 wires can be stock if two share one terminal. Check for factory crimps inside
the original boot versus splices or taps. The switch body has no part number (owner, 2026-10-11), only
`100 95` and "made in Italy". Retailer listings
for the probable `40 24` (Febi 02948) show 2 connectors and 95 / 100 °C switch points, which does not
match the two-stage story, so the wiring is **unresolved**.

**Factory manual, job 20-330 "Solenoid fan coupling"** (service manual group 20, for 201 with 102.961
and 102.985; [saved copy](references/mb-service-manual-20-engine-cooling/README.md)):

- Two switch versions in the sensor box on the cylinder head: **G**, red, **100 °C**, for the fan
  coupling; **H**, red, **110 °C**, for the fan coupling **and the 2-stage auxiliary fan**, fitted to
  cars **with air conditioning or automatic climate control**. H is called the "triple temperature switch".
- Function: the fan engages only with the ignition on and coolant above 98–102 °C, and releases below
  93–98 °C. **A constant positive is at the solenoid body; the temperature switch engages the minus
  (ground).** So the switch is on the ground side, not the +12 V side as assumed elsewhere on this page.
- On cars with automatic air conditioning, the fan coupling and the electric auxiliary fan are engaged
  by a **double-contact relay activated by the triple temperature switch (H)**.

What this means here: this car has A/C (it has the A/C cut-off sensor), so per the factory manual it
**should have the 3-pin 110 °C switch H**, not the 2-pin 100 °C G type that is fitted (owner agrees,
2026-10-11). The loose round plug fits H's third pin. The manual does not give H's part number; the catalog's pos 98 options
include `42 24`, and listings for it disagree (100/110 vs 95/107 °C), so confirm the number for an A/C
car before buying. Also, with the switch on the ground side, the earlier readings may mean something
else: the single wire's 12 V may come **through** the clutch coil or a relay coil, and the 0.07 V pin
may be ground. Not yet re-tested.

**Lead (2026-10-11): the car may need a 3-pin switch.** A 1992 190E 2.3 owner quotes the service
manual: M102 engines **with A/C** used a **3-pin** switch (fan clutch at 110 °C), engines without A/C a
**2-pin** 100 °C switch, and the two are not interchangeable; on A/C cars a "double-contact relay
which is activated by the triple temperature switch" also runs the auxiliary fan whenever the clutch
is engaged ([PeachParts, 2015](https://www.peachparts.com/shopforum/tech-help/364526-1992-190e-2-3-temp-fan-switch-sensor-questions.html),
[Wayback](https://web.archive.org/web/20170521002233/http://www.peachparts.com/shopforum/tech-help/364526-1992-190e-2-3-temp-fan-switch-sensor-questions.html),
[saved copy](references/peachparts-1992-190e-temp-fan-switch-questions/README.md)). Another owner
sorts the 3-pin parts: `A 006 545 42 24` (red) and `45 24` (green) are **dual thermoswitches** (two
circuits), `91 24` is a switch plus a gauge thermistor, `61 24` is grey
([PeachParts, 2018](https://www.peachparts.com/shopforum/3819151-post6.html), from the thread
[3 pin coolant temperature sensor questions](https://www.peachparts.com/shopforum/tech-help/393527-3-pin-coolant-temperature-sensor-questions.html)
([Wayback](https://web.archive.org/web/20200120034841/http://www.peachparts.com/shopforum/tech-help/393527-3-pin-coolant-temperature-sensor-questions.html)),
[saved copy](references/peachparts-3-pin-coolant-temp-sensor-post6/README.md)); in the same thread
a poster says that on his car the first circuit runs the fan at high speed and the second cuts the
A/C (one opinion, not checked). A retailer lists
`42 24` with a 3-connection plug and 95 / 107 °C switch points (not archived).

This car is a US car **with A/C**, but has a 2-pin `100 95` switch (the non-A/C type, probably `40 24`
or a copy). So the original was probably a 3-pin switch, and the **loose round plug (item 6) may be
for its third terminal**, left unplugged when a 2-pin switch was fitted. It would also fit the relay
clicking. On this car the gauge has its own sender, so the gauge-thermistor `91 24` is the less likely
original; `42 24` fits better. The owner compared photos of `42 24` (2026-10-11): its third pin has
the **same shape** as the loose round plug. Strong lead, not yet confirmed by a diagram or a fitted part.

Replacements for `42 24` (retailer listings, 2026-10-11, not archived): **Mahle/Behr TSW 34D** (same
company; AutohausAZ lists it as "3 Pin Red; 100/110 Degree C", one other seller shows a grey TSW 35
under the same number), **Febi 07017** (3 connectors, 95 / 107 °C), **Vemo V30-99-2259** (3 connectors,
round plug, M14×1.5, 95 / 107 °C; Vemo cross-references it to Mahle TSW 34D), **Facet 7.5637**
(same part as EPS 1.850.637 and KW 550 637; M14×1.5, 22 mm hex, two stages 100/95 and 107/102 °C,
W201 1982–93; made in Italy; pin count not confirmed from a listing). Listings disagree on
the switch points (100/110 vs 95/107 °C). The owner can't open the plug boot, so the bridging check is
by continuity only. Before fitting a 3-pin switch, check which terminal
the round plug's wire is really on (a factory double crimp in the 2-pin plug, or a separate wire), so
the new switch's third contact can't short the switched +12 V.

---

## Diagnostics

Ranking and tests are general M102 / KE-Jetronic knowledge plus forum reports. Only the pos 95
resistance values are factory data; other numbers are expectations, not specs.

### General rules

- **Check the connectors first.** Brittle plugs and corroded pins cause many of these symptoms.
- **Label wires before unplugging.** Several wires on this car are the same colour (black with a blue
  stripe), so colour alone won't tell them apart.
- **Pick the meter range to match.** A 2 kΩ range overranges on a cold sender (2.5 kΩ); use 20 kΩ.
- **Resistance tests are done with the plug off**, and the sensor measured at two temperatures: cold,
  then warm (hot engine, or the sensor in heated water with a thermometer).
- **Replace pos 95 and 98 first** if doing it preventively: they are the likeliest to fail.

### Quick reference

| Part | Risk | Symptom | Test (details linked) |
|------|------|---------|-----------------------|
| [Injection sender, pos 95 (green)](#injection-sender-pos-95-green) | High | Hard cold start, stumbling warm-up, rich or lean mixture | Pin to body: 2.5 kΩ at 20 °C, 325 Ω at 80 °C |
| [Fan switch, pos 98 (red)](#fan-switch-pos-98-red) | High | Fan clutch never engages, overheating in traffic | Open cold; closes near 100 °C |
| [Gauge sender, pos 92 (black)](#gauge-sender-pos-92-black) | Medium | Gauge reads low, high, or jumps | Resistance falls steadily as it warms |
| [Thermovalve, pos 101 (vacuum)](#thermovalve-pos-101-vacuum) | Low–medium (owner has a fuel smell) | Fuel smell (canister not purged); vacuum leak if cracked | Blocked cold, passes vacuum above 50 °C |
| [A/C cut-off sensor (blue)](#ac-cut-off-sensor-blue) | Low | A/C cuts out early or never | A few kΩ cold, falling when warm |
| [Round-plug 1-pin switch](#round-plug-1-pin-switch-unplugged) | Unknown | Warning lamp (if `37 24`) | Read the number first |

### Injection sender, pos 95 (green)

Probably `A 006 542 77 17`. Often one pin dies while the other still works.

1. Unplug it. Engine cold, meter on **20 kΩ**.
2. Meter lead on the sensor body (ground), the other on each pin in turn.
3. Both pins must read the same and match the [resistance table](#resistance-table). Pin to pin reads wrong.
4. Bad: zero, open, or a big mismatch. On the car, a first reading of 0 Ω was later followed by
   1.18–1.29 kΩ warm (see [Findings](#findings)), so confirm the meter mode and contact before
   judging.

Basis: factory table and BenzWorld
([saved copy](references/bw-coolant-sensors-tests-readings/README.md),
[saved copy](references/bw-engine-temperature-sensors/README.md)).

#### Resistance table

Factory values from the test page 07.3-121/31, for the fuel injection / ignition coolant sensor
(pos 95). Measure one pin against the sensor body. The page says the 2-pin and 4-pin sensors share
these values ([saved copy](references/bw-coolant-sensors-tests-readings/README.md)).

| Coolant °C | -20 | -10 | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
|------------|-----|-----|---|----|----|----|----|----|----|----|----|----|
| Resistance | 15.7 kΩ | 9.2 kΩ | 5.9 kΩ | 3.7 kΩ | 2.5 kΩ | 1.7 kΩ | 1.18 kΩ | 840 Ω | 600 Ω | 435 Ω | 325 Ω | 247 Ω |

### Fan switch, pos 98 (red)

Probably `A 006 545 40 24` (Febi 02948: 2 connectors, on at 100 °C, off at 95 °C; not confirmed on
the car).

**A. Switch alone (removed from the engine)**

1. Cold, pin to pin and each pin to body: should read **open**, not 0 Ω. On the car (2026-10-11): the
   unplugged sensor reads **OL (open)** cold, as expected. Not yet done: the hot-water test.
2. In heated water with a thermometer: should close near 100 °C and open again near 95 °C.

**B. Circuit on the car (switch unplugged)**

1. Ignition on. Find which plug terminal has 12 V and which goes to the clutch (3 wires; one may be
   shared). The feed is fuse 10 per a UK report.
2. **If both terminals read 12 V, do not jump them.**
3. Jump the 2 plug terminals for 1–2 s with a fused wire. The fan clutch should lock up (the blades
   no longer spin freely by hand).
4. Engine off is safest; keep hands clear of the blades.

Meaning: if the clutch engages, the circuit is fine and the switch is the suspect. If nothing
happens, the fault is in the wiring, fuse or clutch.

On the car (2026-10-11): a relay clicks, the clutch does not engage. The switch probably drives a relay
rather than the clutch itself; see [Fan clutch circuit](#fan-clutch-circuit-2026-10-11).

Basis: [MBClub](https://forums.mbclub.co.uk/threads/w124-230-ce-viscous-fan-not-working.155536/)
([saved copy](references/mbclub-w124-viscous-fan/README.md)), PeachParts.

### Gauge sender, pos 92 (black)

The black 1-wire sender on this car (probably). No factory resistance table found; the injection
sender table is not for this part.

1. Measure the wire pin to the body: resistance should fall steadily as the engine warms.
2. Quick check: ignition on, unplug its wire; the dash gauge should drop to cold.
3. Touching the wire to ground briefly should swing the gauge toward hot (a moment only).
4. Compare the gauge with an infrared thermometer on the thermostat housing.

Basis: general, not sourced.

### Thermovalve, pos 101 (vacuum)

**Factory manual (ignition, group 15, job 15-543 "Testing ignition advance in warm-up phase (only
TSZ)", engine 102.961 basic version; [saved copy](../ignition/references/mb-service-manual-15-electrical-engine/README.md)).**
The only factory description of a coolant thermovalve in the manuals we have:

- **Purpose:** extra ignition advance while the engine warms up: 8–12° crank angle through the
  distributor's vacuum unit, on top of the centrifugal advance, up to about 60 °C coolant.
- **Layout (diagram):** intake manifold → restrictor (1) → check valve (2) → distributor vacuum unit.
  The thermovalve (3), screwed into the coolant, has **two ports**: one goes to a side port of the check
  valve (2) (that hose end is marked white), the other to a port on the **throttle housing**.
- **Function:** below about 60 °C the valve is closed, so full manifold vacuum is held at the vacuum
  unit (the check valve keeps it there even when accelerating) → more advance. Above about 60 °C the
  valve opens and bleeds the vacuum to the throttle housing port, so the extra advance stops at idle.
  The restrictor keeps the other vacuum users from leaking through this circuit at idle.
- **Test:** engine at about 80 °C, idle, timing light on. Pull the **white/red** line at the
  thermovalve: timing must not change. Plug the thermovalve port: timing should advance about 8–12°.
  If not, check the restrictor, the check valve and the vacuum unit for leaks. The valve must pass air
  above about 60 °C.

**What it means for this car (not confirmed):** the manual's version is the earlier TSZ engine
(102.961) with a vacuum unit on the distributor. This car has the EZL (102.985), whose ignition point
table also lists values with and without vacuum, so the EZL takes a vacuum signal; the EPC lists a
thermovalve line to "the ignition distributor (branch fitting) and the throttle housing" and a
thermovalve-to-throttle-housing pipe (460–500 mm). So this car's thermovalve is **probably the same
warm-up advance valve, feeding the EZL's vacuum line instead of a distributor**, and **not** the
charcoal canister purge valve assumed below from forum posts. The owner's report that a valve hose
goes to the EZL fits this. The **disconnected 40–50 cm hose** then most likely runs from the thermovalve
to a nipple on the **throttle housing**. With it open, the warm engine has a small vacuum leak through
the restrictor and the EZL may see the wrong vacuum. Its marking `50` would mean it opens at 50 °C, not
the manual's 60 °C (a different version). The fuel smell is then probably unrelated to this valve.


**What it is.** A temperature-controlled on/off valve for the vacuum line to the **fuel-vapour purge
(charcoal canister regeneration) valve**. Below 50 °C it is **closed**; above 50 °C it passes vacuum.
So the cold state is closed, as sources agree
([PeachParts, posts #2 and #3](https://www.peachparts.com/shopforum/tech-help/38251-what-sensor.html),
[saved copy](references/peachparts-thermovalve-what-sensor/README.md)). Colour tells the temperature:
**red = 50 °C** (`A 000 140 71 60`, `72 60`; EPC still lists `71 60 67`), **yellow = 70 °C**
(`A 000 140 80 60`) ([PeachParts, 2012](https://www.peachparts.com/shopforum/2994299-post1.html),
[saved copy](references/peachparts-thermovacuum-valve-question/README.md)). A yellow valve is a
different part and should not replace a red one.

Item 1 on the car has **2 connectors**, matching the "2 prongs" valve in those posts. The valve is
for the "regeneration system", sits close to the fan switch on the front of the head, and the two
pipes are not alike: the upright one goes to the regeneration valve
([Mercedes-190.co.uk](https://mercedes-190.co.uk/thermo-valve-t54251.html),
[saved copy](references/mercedes190uk-thermo-valve/README.md)). A broken valve is also often
repaired with a tube and glue, per that thread.

**Colour and temperature codes (owner search, 2026-10-11)**

| Code | Opens at | Part number | Source |
|------|----------|-------------|--------|
| Red | 50 °C | `A 000 140 71 60`, `71 60 67` (both seen red by the owner) | PeachParts |
| Yellow | 70 °C (from Aug 1984 on some models) | `A 000 140 80 60` (seen yellow) | PeachParts |
| Black | 40 °C | no number on the store page; listed for 190E 1985–1993 among many models | [EPS Parts](https://epsparts.com/products/new-genuine-mercedes-thermo-thermal-vacuum-valve-color-code-black-40-c-104-f) ([Wayback](https://web.archive.org/web/20260122134121/https://epsparts.com/products/new-genuine-mercedes-thermo-thermal-vacuum-valve-color-code-black-40-c-104-f), [saved copy](references/epsparts-thermo-vacuum-valve-black-40c/README.md)) |
| Black with a white ring | unknown | `A 001 140 62 60` (seen by the owner) | owner |
| Blue | 17 °C | `A 000 140 34 60` | a German eBay listing, not archived |
| unknown | 50 °C (listing) | `A 000 140 72 60`: no listing or photo found, only as an interchange claim | eBay.de sellers |

The EPS listing says the colour code is on the **2 hose fittings**, so "black" on the car may mean
the fittings, not the body. The car's valve is black but its marking says `50AN6`; if the "50" is
the temperature, a black 40 °C valve would not match. Photograph both fittings and the body.

The valve's job also depends on the model: a PeachParts thread on a 380SL says the valves on the
intake manifold control **acceleration enrichment** below 50 °C coolant (70 °C from August 1984)
([PeachParts, 2008](https://www.peachparts.com/shopforum/2050260-post1.html),
[saved copy](references/peachparts-thermovacuum-valve-temperature-color/README.md)), while the
300E posts describe the purge function. What the valve does on this M102 is **not confirmed**.

**Hose routing, from the EPC (catalog 452, group 14.120 "Vacuum system", checked 2026-10-11).** The
catalog lists these lines at the thermovalve; none has a usage restriction, so I can't tell which
variants this car has:

| Pos | Part number | Line | Length |
|-----|-------------|------|--------|
| 14 | `A 000 158 89 35` | thermovalve to the ignition distributor (the branch fitting) and the throttle housing | 500 mm |
| 17 | `A 117 997 09 82` | hose, thermovalve to throttle housing | 40 mm |
| 50 | `A 000 158 88 35` / `A 000 158 93 35` | pipe, thermovalve to throttle housing | 460 / 500 mm |
| 35 / 47 | `A 117 078 05 81` / `A 001 158 01 35` | thermovalve to the **regeneration (purge) valve** | 770 mm |
| 71 | `A 000 158 96 35` | exhaust gas recirculation valve to thermovalve | 760 mm |

The EZL's own vacuum line is a different pipe, pos 65 `A 000 158 14 35` (900 mm), from the intake
manifold branch fitting (pos 59) to the ignition control box. So the EPC does **not** put the EZL line
on the thermovalve. The owner's first report (an EZL hose "not from the thermovalve") fits this; a
later report that the valve's hose goes to the EZL (2026-10-11) conflicts with it and is not
resolved: trace the hoses.

What this says about the car: the **regeneration valve** and the **activated charcoal reservoir** are in
the US catalog 452, so the purge system is fitted. The owner's short hose (about 40–50 cm, broken
end, disconnected) matches the 460–500 mm pipe from the **thermovalve to the throttle housing**
(pos 14 / 50). Look for a **nipple on the throttle housing with no hose**. That would also fit the
PeachParts description of the valve passing vacuum above idle to the purge valve. Not yet confirmed
on the car. Don't plug the open hose until the matching fitting is found.

**Hose colour (2026-10-11).** The owner's disconnected hose looks white with a black stripe (old and
yellowed). No factory colour chart for this circuit was found. Leads: on a US 190E, a light hose with a
red stripe is described as the thermovalve's vacuum input (BenzWorld, below). A search summary
pointed to a JustAnswer Q&A describing a black line with a white tracer near the throttle housing, but
the owner read the page (2026-10-11) and found nothing useful, so that lead is dropped. The hose's
length (40–50 cm) still matches the EPC thermovalve-to-throttle-housing pipe (460–500 mm). A dealer vacuum diagram for the
1985–88 190E 2.3 8V was posted on BenzWorld, but its image is gone
([BenzWorld, 2011](https://www.benzworld.org/threads/mercedes-190e-85-88-vacuum-line-diagram-pic.1581206/),
[Wayback, 2018, text only](https://web.archive.org/web/20180201055554/http://www.benzworld.org/forums/w201-190-class/1581206-mercedes-190e-85-88-vacuum-line.html);
the diagram image is **not archived**).

**More forum references (found 2026-10-11, text only; their photos are dead Photobucket links).**
- A 190E owner with a red 50 °C thermovalve asks where the lines go; a Bentley post is said to carry a
  W201 vacuum diagram ([BenzWorld, w201 vacuum diagrams all](https://www.benzworld.org/threads/w201-vacuum-diagrams-all.1508353/),
  [Wayback](https://web.archive.org/web/20261011150131/https://www.benzworld.org/threads/w201-vacuum-diagrams-all.1508353/),
  [stub](references/bw-w201-vacuum-diagrams-all/README.md)).
- The vacuum diagrams in the W201 CD manual are under group 14, "Intake and exhaust, manifolds,
  emission control", and a dealer diagram for the 190E 2.3 8V 1984–88 was posted, now a dead image
  ([BenzWorld, 86 190e EPC vacuum line diagrams](https://www.benzworld.org/threads/help-advice-86-190e-epc-vacuum-line-diagrams.1575248/),
  [Wayback](https://web.archive.org/web/20261011150131/https://www.benzworld.org/threads/help-advice-86-190e-epc-vacuum-line-diagrams.1575248/),
  [stub](references/bw-86-190e-epc-vacuum-line-diagrams/README.md)).
- On a US 190E, a reply describes the thermo-vacuum valve as on top, brass, with a **light hose with a
  red stripe as the vacuum input** and its other side going to the **EGR valve**, and says high NOx
  can come from "either of two temp/vac valves" ([BenzWorld, ICV and vacuum hose](https://www.benzworld.org/threads/how-to-identify-idle-speed-control-valve-amp-vacuum-hose.1535441/),
  **not archived**, [stub](references/bw-idle-speed-control-valve-vacuum-hose/README.md)). That matches the EPC's EGR line to a thermovalve
  (pos 71), so this car may have **a second, EGR thermovalve** besides the purge one, which is not
  confirmed.

**Transmission vacuum port (owner, 2026-10-11).** The owner found a capped port on the intake
manifold. A PeachParts thread on a 190E 2.3 concludes that the port on the **upper side of intake
runner #3** is the **transmission vacuum modulator** line (modulator on the driver's side of the
transmission, one hose only, vacuum with the engine running), and that the ports on the **underside**
of the manifold (under the airflow meter, on the throttle housing) go to the thermo-vacuum valve and
the charcoal canister. That owner's transmission "shifts like a new one" once the line was attached
([PeachParts, 2005](https://www.peachparts.com/shopforum/tech-help/113311-190e-vacuum-hose-question-w-pic.html),
[saved copy](references/peachparts-190e-vacuum-hose-question/README.md)). The EPC agrees there is an
automatic-transmission vacuum connection on the manifold: group 14.030 pos 152 `A 117 078 02 81`
(hose, "automatic transmission vacuum connection to intake manifold") and pos 143 `A 000 998 07 23`
(protective cap, "to plug vacuum connection to automatic transmission"). This car has the 4-speed
automatic 722.408, so that port should normally carry a hose to the modulator, not a cap. The owner
says the cap is on a plug, and thinks the transmission line is connected at the "bottom one"; which
port is capped, and whether the modulator line is connected, is **not yet confirmed**. Check: a
capped upper port on runner #3 plus a modulator with no vacuum would explain harsh or late shifts
(unconfirmed). Update 2026-10-11: the cap is on the **upper side** of runner #3 (the transmission
port) and is **not a factory cap**; whether the modulator line is connected at the transmission end is
unknown, and the owner has not checked how the transmission shifts. A non-factory cap may mean someone
closed the port on purpose (for example because the modulator diaphragm leaked fluid into the line),
so check the modulator and the line for transmission fluid before reconnecting. Also, one owner there advises capping an open nipple until the valve is replaced,
to avoid a leak.

The owner's earlier 2001 PeachParts reference (a 1991 190E 2.3 where the valve's other line ran to a
check valve on the driver's inner fender, a 70 °C valve `001 141 62 60`, "for emission control system")
([PeachParts, 2001](https://www.peachparts.com/shopforum/tech-help/23366-91-190e-2-3-part-id.html),
[saved copy](references/peachparts-91-190e-2-3-part-id/README.md)) is a later model year than this
car (1988 US) and may be routed differently.

Caveats: all of this is forum knowledge, mostly from 6-cylinder cars (300E, M103). **Not confirmed** for
the 1988 US M102 on this car: the hose routing on the car itself (the EPC shows the purge parts are listed for this catalog). The
`50AN6 F8T` marking is undecoded. The owner says the valve is **black, definitely not yellow**
(2026-10-11), so it is not the 70 °C part; but the red = 50 °C colour rule may not hold for it (old
or later valves may be black, or it may be stained). Go by the number and the bench test, not the
colour.

**Symptom.** A stuck-closed valve means the canister never purges. A moderator says the only
noticeable effect would probably be a fuel smell (an unpurged canister may leak raw fuel).
The owner **does have a fuel smell** (2026-10-11). That fits, but it is not evidence: a fuel smell
has many other causes (see below), so test the valve and check the others before blaming it.

**Other fuel-smell checks (general, not sourced):** hoses to the canister and purge valve (cracked,
loose, wrong way round); fuel filler cap seal and tank breather; fuel lines and hose clamps near the
fuel distributor and warm-up regulator; injector seals; fuel accumulator leaks; the charcoal
canister saturated with fuel. Look and smell with the engine cold, then hot.

**A. Bench test (valve removed, or hoses off)**

1. Cold (below about 30 °C), blow gently through one port. Expect it **blocked**.
2. Put the valve's metal tip in water with a thermometer and heat slowly.
3. Retest above 50 °C (say 55–60 °C). Expect air to **pass**.
4. Let it cool and retest. It should block again, with a few degrees of hysteresis.

**B. On the car**

1. Put a hand vacuum pump or gauge on the line.
2. Cold engine: the valve should block vacuum. Warm engine (above 50 °C): vacuum should reach the
   purge valve, but only above idle (the purge valve is fed by throttle position).

**Faulty if:** it passes air cold, stays blocked hot, switches at a very different temperature, or the
body is cracked and leaks.

Before pulling hoses, label or photograph them, and pull by hand without prying the nipples. The
two pipes are fitted differently, so note which is which. Basis: forum posts above (single-source
statements, not factory data).

### A/C cut-off sensor (blue)

`A 008 542 45 17`, green and brown wires.

**Factory manual (Tempomatic, group 83, 83-020 and 83-040; [saved copy](../climate-control/references/mbna-service-manual-tempomatic/README.md)):**
on model 201 with engine 102, a **temperature switch 110 °C (item 23) cuts the A/C compressor** to
protect the engine from overheating. It **closes to ground at about 110 °C**, signalling the compressor
cut-out control unit (141), and **opens again at about 103 °C**. The manual's test: engine running, A/C
on, pull its connector and connect it to ground; the compressor must switch off at once. The manual
calls it a 1-pin connector; the blue part here has 2 wires (green, brown), so whether the blue part is
item 23 is **likely but not confirmed** (the EPC describes it as an A/C "off" switch at 130 °C). If it
is, it is an **on/off switch, not a resistor**: open when cold. The resistance test below then only
needs to show open when cold and closed when hot.

Earlier assumption (before the manual): a temperature-dependent resistor. Kept below for reference.

**A. Sensor itself (plug off, ignition off)**

1. Engine cold, **20 kΩ** range, one lead on each of the 2 pins. Expect a few kΩ (roughly 2–3 kΩ at
   20 °C, like the injection sender; unconfirmed).
2. Each pin to the engine body. Both open: floating 2-pin part, brown is ground at the control unit.
   One pin 0 Ω to the body: it is grounded at the sensor; note which.
3. Warm it and repeat step 1. The value should fall smoothly, to a few hundred Ω around 80 °C.
4. Bad: 0 Ω, open, or no change with temperature. If you only ever see 0 or open and nothing in
   between, it is a switch after all.

**B. Harness side (plug off, ignition on)**

1. Green to ground: a low voltage, not 12 V.
2. Brown to the engine body: about 0 Ω.
3. If either fails, the wiring is at fault, not the sensor.

Basis: BenzWorld (the same part, blue 2-pin, runs the aux fan on W126;
[saved copy](references/bw-coolant-sensors-tests-readings/README.md)); curve not confirmed.

### Round-plug 1-pin switch (unplugged)

**Factory manual (Tempomatic, 83-020 and 83-036):** on engine 102 from model year 85, the switch at the
cylinder head (item 16) is a dual switch: **100 °C for the electromagnetic fan clutch and 110 °C for the
auxiliary fan**. The auxiliary fan stage drives auxiliary fan relay (20) and works in parallel with the
A/C pressure switch on the receiver-drier (on 20 bar, off 15 bar). The A/C test procedure says: "pull
the 1-pin connector from temperature switch (16) and connect it to ground, so that the auxiliary fan
runs". So the **loose round 1-pin plug is very likely the auxiliary fan stage of switch 16**, left
unplugged when the 2-pin switch was fitted.

**Wiring diagram for this exact model (Tempomatic manual, Fig. 83/5 "Wiring diagram, Tempmatic climate
control, model 201.028", model year 1987):** the 100/110 °C switch is **S25/4**, with 3 terminals:

| S25/4 terminal | Wire (0.75 mm²) | Goes to | Job |
|---|---|---|---|
| 1 | **black/blue/green** (sw/bl/gn) | X48/2, circuit 15 (switched +12 V) | Common feed |
| 2 | **black/blue** (sw/bl), two wires | X15 "connector, engine fan / 100 °C temp switch" → fan clutch Y2; and the double-contact relay K8 | 100 °C stage: +12 V to the clutch |
| 3 (round pin) | **black/green** (sw/gn) | auxiliary fan relay, high (K9), terminal 4 | 110 °C stage: +12 V to the K9 coil |

The fan clutch Y2 is grounded through a brown wire to W11. So on this car the switch **switches +12 V**
(this matches the owner's readings: 12 V on the single wire, the two-wire terminal is the output). The
"connect to ground" tests in the manual's A/C chapter are for the 1-pin switches of other engines and
years; **don't ground the round plug**, it would do nothing. The connector the clutch plugs into
(under the intake manifold) is probably X15.

**Test (owner, not yet done):** check the loose round plug's wire is black/green. Ignition on, engine
off: with a fused jumper (5 A), connect the round plug's terminal to the switch plug's single
black/blue/green wire (+12 V) for a few seconds. K9 should click and the auxiliary fan should run on
high. If not: K9 (its coil is between terminal 4, black/green, and terminal 5, brown to ground W3), its
fuse, or the fan.

**Fan clutch, from the same diagram:** jumping terminals 1 and 2 sends +12 V through X15 to the clutch.
The relay K8 clicked but the clutch didn't engage (2026-10-11), so check that path: X15 connector, the
clutch coil, and its brown ground to W11.

Earlier notes:

If it is `A 006 545 37 24`, a fault only affects a dash warning lamp, not the fans.

1. Read the number on the body first.
2. Switch cold, pin to body: expect open.
3. Ignition on: check whether the loose plug's wire has 12 V or goes to a dash lamp circuit.
4. Don't rejoin the wire until its job is known.

Basis: retailer listing
([FACET 7.4042](https://www.mbpartsgiant.com/oem-mercedes_benz-190e-temperature_sender)); not
confirmed on the car.

---

## Research notes

### Part-number lookup (2026-10-10, retailer listings, medium confidence, not archived)

- The red switch marking `100 95` matches Febi 02948, which cross-references OE `A 006 545 40 24` and
  is listed with **2 connectors and switch points 95 and 100 °C**
  ([VEMO V30-99-2255](https://www.onlinecarparts.co.uk/vemo-2293711.html),
  [AZ Motor Factors, Febi 02948](https://azmotorfactors.co.uk/product/temperature-switch-radiator-fan-02948)).
  So item 3 is very likely `40 24`. `95` is the switch-off temperature of the 100 °C stage.
- `A 006 545 37 24` is listed as a **coolant warning lamp switch**, not a fan switch (FACET 7.4042,
  [listing](https://www.mbpartsgiant.com/oem-mercedes_benz-190e-temperature_sender), 1982–1993
  models). This changes the earlier guess that the round-plug switch feeds the auxiliary fan.
- A forum post warns that dealer and supplier cross-references for these switches are often wrong, so
  go by the number on the body ([PeachParts](https://www.peachparts.com/shopforum/912616-post5.html)).

### Wiring diagram search (2026-10-10, not found)

No W201 fan wiring diagram located; forum reports only, and they disagree.

- On a UK 1991 190E 2.0 (M102.962, no A/C), the clutch solenoid has a permanent earth and +12 V from
  fuse 10 switched through the temperature switch, whose third wire serves the temperature gauge
  ([MBClub](https://forums.mbclub.co.uk/threads/91-190e-fan-clutch-wiring-diagram-wanted.69649),
  **not archived**). The Haynes manual is said to show the reverse.
- A lead: a diagram folder at `autolib.diakom.ru/CAR/Mercedes-Benz/1991/190E/SYSTEM WIRING DIAGRAMS/`,
  linked from that thread. The site no longer resolves; a Wayback copy hasn't been checked
  (archive.org rate-limited the check).
- The car is a 1988 US model with A/C (EPC 452), so the circuit may differ from that UK car (aux fan relay, 2 outputs).
- Another 1991 UK 190E 2.0 owner (no A/C) says his wiring diagram shows a "dual contact relay" that
  energises when the temperature switch closes, but he could not find it
  ([MBClub](https://forums.mbclub.co.uk/threads/w201-190e-magnetic-fan-clutch-relay.69544/),
  [Wayback](https://web.archive.org/web/20250116111816/https://forums.mbclub.co.uk/threads/w201-190e-magnetic-fan-clutch-relay.69544/)).
  On this car a relay does click when the switch is jumped (2026-10-11).

### Diagram colour codes

Mercedes diagrams print `size sw/bl`: base colour, then stripe, with the size in mm². German codes:
sw black, bl blue, rt red, gn green, ge yellow, br brown (ground), gr grey, ws white, vi violet,
or orange, rs pink. English WIS uses BK, BU, RD, GN, YE, BR, GY, WH, VT, OG, PK (check the legend).

---

## Sources

- Parts catalog, EPC 452: groups 01.065 (cylinder head & gasket kit) and 20.015 (water pump).
- Mercedes-Benz service manual, group 20 "Engine cooling system" (jobs 20-005 to 20-445, incl. 20-330
  solenoid fan coupling): [saved copy](references/mb-service-manual-20-engine-cooling/README.md)
- Mercedes-Benz of North America Maintenance Manual, 1981 on (Supplement 5, March 1993):
  [saved copy](../general-reference/references/mbna-maintenance-manual-1981-1993/README.md)
- [The engine temperature sensors](https://www.benzworld.org/threads/the-engine-temperature-sensors.3084442/)
  (BenzWorld, 2021): [saved copy](references/bw-engine-temperature-sensors/README.md)
- [Coolant Temperature Sensors, Tests, Readings, Locations, and More](https://www.benzworld.org/threads/coolant-temperature-sensors-tests-readings-locations-and-more.2795522/)
  (BenzWorld, 2017, with the factory test page): [saved copy](references/bw-coolant-sensors-tests-readings/README.md)
- [What sensor is this? (thermo-vacuum valve)](https://www.peachparts.com/shopforum/tech-help/38251-what-sensor.html)
  (PeachParts, 2002): [saved copy](references/peachparts-thermovalve-what-sensor/README.md)
- [Thermovacuum Valve Question?](https://www.peachparts.com/shopforum/2994299-post1.html)
  (PeachParts, 2012): [saved copy](references/peachparts-thermovacuum-valve-question/README.md)
- [Thermo valve](https://mercedes-190.co.uk/thermo-valve-t54251.html)
  (Mercedes-190.co.uk): [saved copy](references/mercedes190uk-thermo-valve/README.md)
- ['91 190E 2.3 part id?](https://www.peachparts.com/shopforum/tech-help/23366-91-190e-2-3-part-id.html)
  (PeachParts, 2001): [saved copy](references/peachparts-91-190e-2-3-part-id/README.md)
- [87 190E 2.3 overheating in traffic, post #4](https://www.peachparts.com/shopforum/568571-post4.html)
  (PeachParts, 2004): [saved copy](references/peachparts-190e-dual-temp-switch/README.md)
- [W124 230 CE viscous fan not working](https://forums.mbclub.co.uk/threads/w124-230-ce-viscous-fan-not-working.155536/)
  (MBClub UK, 2013): [saved copy](references/mbclub-w124-viscous-fan/README.md)
- [FCP Euro, 0065427717](https://www.fcpeuro.com/products/mercedes-engine-coolant-temperature-sensor-mer-0065427717):
  [saved copy](references/fcpeuro-0065427717/README.md)
- [EuroSport Tuning, Bosch 0 280 130 044](https://eurosporttuning.com/temperature-sensor-0-280-130-044/):
  [saved copy](references/eurosporttuning-bosch-0280130044/README.md)
- [Fan Clutch Relay testing](https://www.benzworld.org/threads/fan-clutch-relay-testing.1653488/)
  (BenzWorld, 2012): [saved copy](references/bw-fan-clutch-relay-testing/README.md)
- [ENGINE FAN](https://www.peachparts.com/shopforum/tech-help/16399-engine-fan.html)
  (PeachParts, 2001–2003): [saved copy](references/peachparts-engine-fan-16399/README.md)
- [190e location of sensor for electromagnetic fan](https://www.peachparts.com/shopforum/tech-help/220289-190e-location-sensor-electromagnetic-fan.html)
  (PeachParts, 2008): [saved copy](references/peachparts-190e-electromagnetic-fan-sensor/README.md)
- [Valve train noise / fan problem, post #2](https://www.peachparts.com/shopforum/1548016-post2.html)
  (PeachParts, 2007): [saved copy](references/peachparts-valve-train-noise-fan-post2/README.md)
- [Aux. Fan advice requested](https://www.peachparts.com/shopforum/30842-post1.html)
  (PeachParts, 2000): [saved copy](references/peachparts-85-190e-aux-fan-advice/README.md)
- [W201 fuse box and relay diagram](https://fuseandrelay.com/mercedes/w201.html):
  [Wayback](https://web.archive.org/web/20260617194939/https://fuseandrelay.com/mercedes/w201.html)
- [eHorst, copper ring 14 × 18 × 1.5 DIN 7603 A](https://ehorst.de/en/Kupferdichtring-14x18x1-5-DIN-7603-A-1123879.html):
  [saved copy](references/ehorst-copper-ring-14x18/README.md)
