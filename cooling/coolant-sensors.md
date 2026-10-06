# Coolant sensors and thermovalves at the thermostat

**Mileage:** 
**Topic:** cooling (also fuel injection and fan control)
**Status:** reference. Sensors on the car identified 2026-10-05; nothing is known to be wrong.

Four temperature sensors and the thermovalves thread into the cylinder head, next to the
thermostat housing. Each one seals with a sealing ring, `N 007 603 01 4100`. Part numbers come from
the parts catalog (EPC 452, group 01.065, cylinder head & gasket kit, positions 92 to 107).

## On this car

Confirmed by the owner:

- **Pos 95, fuel injection sender:** the **black** `A 006 542 56 17`.
- **Pos 95 alternative, A/C cut-off sensor:** `A 008 542 45 17`, in its own hole next to the black
  sender. The catalog lists it as an alternative at the same position, but the car has both.
- **Pos 98, fan coupling switch:** `A 006 545 15 24` or `A 006 545 40 24` (**to check**: read the
  number on the hex body). It has 2 pins with 3 wires going out (see [Pos 98 wiring](#pos-98-wiring-to-check)).

## Sensors and thermovalves

| Pos | Part | Function | Part numbers | Sealing ring |
|-----|------|----------|--------------|--------------|
| 92 | Sender unit | Dash water temperature gauge | `A 005 542 10 17`, `A 005 542 26 17` | `N 007 603 01 4100` |
| 95 | Sender unit (black) | KE-Jetronic injection (coolant temp); the green `77 17` is listed "for California" | **`A 006 542 56 17` (on this car)**; also listed: `A 006 542 77 17`, `A 008 542 32 17` | `N 007 603 01 4100` |
| 95 (alt.) | Temperature sensor | A/C "off" emergency switch, cuts the A/C at 130 °C; in the hole next to the black sender | **`A 008 542 45 17` (on this car)** | `N 007 603 01 4100` |
| 98 | Temperature switch | Fan coupling (dual switch, see wiring note). On this car: `15 24` or `40 24`, to check | `A 006 545 15 24`, `A 006 545 40 24`, `A 006 545 42 24`, `A 006 545 91 24` | `N 007 603 01 4100` |
| 101 | Thermovalve (vacuum) | Opens at 50 °C, on cylinder head | `A 000 140 71 60`, `A 000 140 72 60` | `N 007 603 01 4100` |
| 101 | Thermovalve (vacuum) | Opens at 70 °C | `A 000 140 80 60`, `A 001 140 62 60` | `N 007 603 01 4100` |

The catalog lists the sealing ring at pos 107 with qty 3, so it may not count the thermovalve. Buy
one per part you remove.

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
- Measure an old ring before buying. Use a new ring every time; copper rings can be reused after
  annealing.

### Pos 95: `56 17` vs `77 17` (unconfirmed)

The catalog only labels `A 006 542 77 17` "for California" and gives no other reason. The green
`77 17` is Bosch 0 280 130 044
([EuroSport Tuning](https://eurosporttuning.com/temperature-sensor-0-280-130-044/),
[saved copy](references/eurosporttuning-bosch-0280130044/README.md)) and is sold for many models
([FCP Euro](https://www.fcpeuro.com/products/mercedes-engine-coolant-temperature-sensor-mer-0065427717),
[saved copy](references/fcpeuro-0065427717/README.md)), so it may have become the general
replacement. `56 17` is the black version, the one on this car
([BenzWorld](https://www.benzworld.org/threads/the-engine-temperature-sensors.3084442/),
[saved copy](references/bw-engine-temperature-sensors/README.md)).

The temperature curve is probably the **same** for all of them: the factory test page for the
EZL/CIS-E sensor (B11/2) says the 4-pin sensor's resistances are identical to the 2-pin sensor's, and
a W126 owner found the same table in the 190E manual
([BenzWorld](https://www.benzworld.org/threads/coolant-temperature-sensors-tests-readings-locations-and-more.2795522/),
[saved copy](references/bw-coolant-sensors-tests-readings/README.md)). The table is below, under
[Resistance table](#resistance-table-ezlcis-e-sensor-b112).

### Pos 98 wiring (to check)

The switch on the car shows 2 pins and 3 wires. A 201.028 owner reports that the M102 switch holds
two switches: the lower temperature (about 100–105 °C) engages the fan clutch, the higher (about
110 °C) turns on the auxiliary electric fan, both switching +12 V
([PeachParts](https://www.peachparts.com/shopforum/568571-post4.html),
[saved copy](references/peachparts-190e-dual-temp-switch/README.md)). That needs a shared feed
plus two outputs, so 3 wires can be stock if two share one terminal. Check for factory crimps inside
the original boot versus splices or taps, and read the number on the switch body.

## Related parts

| Catalog ref | Part | Part numbers | Note |
|-------------|------|--------------|------|
| 01.065 pos 104 | Screw plug | `N 007 604 01 4110` | Plugs an unused sensor hole |
| 20.015 pos 26 | Temperature switch | `A 006 545 37 24`, `A 006 545 90 24` | At the water pump / thermostat housing; ring `N 007 603 01 4100` (pos 29) |

The engine harness has a plug for a "temperature switch, 100 degs", probably the 20.015 switch
running the auxiliary fan. Not checked.

## Failure risk and quick tests

Pos 95 and 98 are the ones most likely to fail; replace those first if doing it preventively.
Ranking and tests are general M102 / KE-Jetronic knowledge plus forum reports; only the pos 95
resistance values are factory data.

| Pos | Part | Risk | Typical symptoms | Quick test | Basis |
|-----|------|------|------------------|------------|-------|
| 95 | KE-Jetronic sender (black `56 17`) | High | Hard cold start, stumbling warm-up, rich or lean mixture; often one pin dies, the other still works | Unplug. One meter lead on the sensor body (ground), the other on each pin in turn: both pins must read the same and match the [resistance table](#resistance-table-ezlcis-e-sensor-b112) (2.5 kΩ at 20 °C, 325 Ω at 80 °C). Pin to pin reads wrong. Zero, open, or a big mismatch = bad | Factory table and BenzWorld ([saved copy](references/bw-coolant-sensors-tests-readings/README.md), [saved copy](references/bw-engine-temperature-sensors/README.md)) |
| 98 | Fan coupling switch (dual) | High | Fan clutch never engages, overheating in traffic; or auxiliary fan never runs | Engine hot: bridge the switch terminals; clutch or aux fan should engage. Or ohmmeter on the removed switch in heated water: closes near 100–105 °C and 110 °C. Identify the terminals first | [MBClub](https://forums.mbclub.co.uk/threads/w124-230-ce-viscous-fan-not-working.155536/) ([saved copy](references/mbclub-w124-viscous-fan/README.md)), PeachParts |
| 92 | Temp gauge sender | Medium | Gauge reads low, high, or jumps | Measure sender to ground: resistance should fall steadily as the engine warms. Compare the gauge with an IR thermometer on the thermostat housing | General, not sourced |
| 101 | Thermovalves (vacuum) | Medium | Sticking or cracked valve, vacuum leak; affects ignition advance / EGR | Cold engine: blow through, should be closed. Hot (above 50 / 70 °C): should pass air. A hand vacuum pump makes it exact | General, not sourced |
| 95 alt. | A/C cut-off sensor `45 17` | Low | Rarely noticed: A/C cuts out early or never cuts out | Probably a temperature-dependent resistor, not an on/off switch: the A/C control unit reads it and cuts the A/C near 130 °C, so there is no "resting state". Unplug and measure across the 2 pins: a few kΩ cold, falling smoothly to a few hundred Ω warm. 0 Ω or open = bad. Only 0 or open and nothing between = it is a switch after all. No chart found for this part; likely close to the table below | BenzWorld (the same part, blue 2-pin, runs the aux fan on W126; [saved copy](references/bw-coolant-sensors-tests-readings/README.md)); curve not confirmed |

Check the connectors before replacing anything: brittle plugs and corroded pins cause many of these
symptoms.

### Resistance table (EZL/CIS-E sensor B11/2)

Factory values from the test page 07.3-121/31, for the fuel injection / ignition coolant sensor
(pos 95). Measure one pin against the sensor body. The page says the 2-pin and 4-pin sensors share
these values ([saved copy](references/bw-coolant-sensors-tests-readings/README.md)).

| Coolant °C | -20 | -10 | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
|------------|-----|-----|---|----|----|----|----|----|----|----|----|----|
| Resistance | 15.7 kΩ | 9.2 kΩ | 5.9 kΩ | 3.7 kΩ | 2.5 kΩ | 1.7 kΩ | 1.18 kΩ | 840 Ω | 600 Ω | 435 Ω | 325 Ω | 247 Ω |

## Sources

- Parts catalog, EPC 452: groups 01.065 (cylinder head & gasket kit) and 20.015 (water pump).
- [The engine temperature sensors](https://www.benzworld.org/threads/the-engine-temperature-sensors.3084442/)
  (BenzWorld, 2021): [saved copy](references/bw-engine-temperature-sensors/README.md)
- [Coolant Temperature Sensors, Tests, Readings, Locations, and More](https://www.benzworld.org/threads/coolant-temperature-sensors-tests-readings-locations-and-more.2795522/)
  (BenzWorld, 2017, with the factory test page): [saved copy](references/bw-coolant-sensors-tests-readings/README.md)
- [87 190E 2.3 overheating in traffic, post #4](https://www.peachparts.com/shopforum/568571-post4.html)
  (PeachParts, 2004): [saved copy](references/peachparts-190e-dual-temp-switch/README.md)
- [W124 230 CE viscous fan not working](https://forums.mbclub.co.uk/threads/w124-230-ce-viscous-fan-not-working.155536/)
  (MBClub UK, 2013): [saved copy](references/mbclub-w124-viscous-fan/README.md)
- [FCP Euro, 0065427717](https://www.fcpeuro.com/products/mercedes-engine-coolant-temperature-sensor-mer-0065427717):
  [saved copy](references/fcpeuro-0065427717/README.md)
- [EuroSport Tuning, Bosch 0 280 130 044](https://eurosporttuning.com/temperature-sensor-0-280-130-044/):
  [saved copy](references/eurosporttuning-bosch-0280130044/README.md)
- [eHorst, copper ring 14 × 18 × 1.5 DIN 7603 A](https://ehorst.de/en/Kupferdichtring-14x18x1-5-DIN-7603-A-1123879.html):
  [saved copy](references/ehorst-copper-ring-14x18/README.md)
