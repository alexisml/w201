# Factory specs

**Topic:** general reference
**Status:** reference

Factory values for this car (201.028, engine 102.985, USA, automatic 722.408, A/C), taken from
Mercedes-Benz manuals. They are the manufacturer's specs, not measurements on this car. Collected
2026-10-11.

Sources (scanned PDFs in the private archive, available on request):

- **SM 15:** service manual group 15, Electrical system, engine (ignition):
  [saved copy](../ignition/references/mb-service-manual-15-electrical-engine/README.md)
- **SM 20:** service manual group 20, Engine cooling system:
  [saved copy](../cooling/references/mb-service-manual-20-engine-cooling/README.md)
- **MM:** Mercedes-Benz of North America Maintenance Manual, MY 1981 on, Supplement 5 (March 1993):
  [saved copy](references/mbna-maintenance-manual-1981-1993/README.md)
- **Tempomatic:** service manual group 83, Tempomatic climate system:
  [saved copy](../climate-control/references/mbna-service-manual-tempomatic/README.md)
- **CB:** Mercedes-Benz of North America Service Manual, Chassis and Body, model 201 (1988):
  [saved copy](references/mbna-service-manual-chassis-body-1988/README.md)

The scans' text recognition is poor in places. Values marked *(text only)* were read from the
recognized text, not checked against the page image.

## Cooling

| Item | Value | Source |
|------|-------|--------|
| Coolant capacity | **9.5 L with A/C** (8.5 L without). The CB technical data table (00-020) gives 8.5 L for 201.028, probably the figure without A/C | SM 20, 20-010; MM; CB 00-020 |
| Antifreeze mix | 50 % (4.75 + 4.75 L) protects to −37 °C; 55 % (5.25 L antifreeze + 4.25 L water) to −45 °C; more than 55 % lowers protection | SM 20, 20-010 |
| Coolant change | at the latest every 3 years | SM 20, 20-010 |
| Thermostat | starts to open 87 °C, fully open 102 °C; fit with the ball valve at the highest point | SM 20, 20-005 |
| Thermostat housing | bolts 25 Nm; cap 10 Nm (alloy) or 8 Nm (plastic); plastic housing on model 201 from 01/1985 | SM 20, 20-115 |
| Pressure cap | code 120, opens at 1.2 bar (new 1.2 +0.1, used 1.2 −0.1) | SM 20, 20-430 |
| Leak test | system at 1.4 bar | SM 20, 20-017 |
| Drain plugs | radiator 1.5 Nm; engine block 30 Nm with a new seal | SM 20, 20-010 |
| Filling | open the cap only below 90 °C; close it at 60–70 °C with the heater on | SM 20, 20-010 |
| Fan switch | A/C cars: 3-pin "triple" switch H, red, 110 °C, also runs the 2-stage auxiliary fan via a double-contact relay. Cars without A/C: switch G, red, 100 °C. Details: [coolant sensors](../cooling/coolant-sensors.md#pos-98-wiring) | SM 20, 20-330 |
| Fan clutch | engaged above 98–102 °C, released below 93–98 °C, ignition on; constant positive at the solenoid, the switch closes the ground | SM 20, 20-330 |
| Fan | 430 mm, 5 blades (automatic, or A/C) *(text only)* | SM 20, 20-330 |
| Fan clutch pulley bolts | 10 Nm (hex socket) or 15 Nm (Torx, from 09/1985) *(text only)* | SM 20, 20-335 |
| A/C compressor cut-out | temperature switch 110 °C (item 23): closes to ground at about 110 °C coolant, A/C compressor off; opens at about 103 °C | Tempomatic 83-020 |
| Auxiliary fan | runs from the A/C pressure switch on the receiver-drier (on 20 bar, off 15 bar, via a pre-resistor: low speed) and, in parallel, from the 110 °C stage of the dual temperature switch on the engine (relay 20) | Tempomatic 83-020, 83-028 |
| A/C compressor pressure switch | on 2.6 bar, off 2.0 bar | Tempomatic 83-028 |

## Engine oil

| Item | Value | Source |
|------|-------|--------|
| Capacity | **5.0 L with filter** (engine 102 in model 201), gray dipstick | MM 0101.06 |
| Oil filter | spin-on, 20 Nm | MM 0101.06 |
| Drain plug | 25 Nm (another page of the same job gives 30 Nm for 102 engines other than 102.983; unresolved) | MM 0101.06 |

## Automatic transmission (722.4)

| Item | Value | Source |
|------|-------|--------|
| ATF capacity | 7.1 L full; 6.0 L at a fluid change (behind 102.98 engines); ATF from the MBNA approved list | MM 2702 |
| Fluid level | dipstick marks are for 80 °C fluid; at 20–30 °C the maximum level is **12 mm below the MIN mark** | MM 2710 |
| Fluid change | refill about 4 L with the engine off, then top up at idle | MM 2702 |
| Torques | pan drain plug and torque converter drain plug 14 Nm; pan bolts 8 Nm | MM 2702 |

## Ignition

| Item | Value | Source |
|------|-------|--------|
| Reference resistor R16/1 | 750 Ω for USA 102.985, 1987–1989 (this car has `A 000 540 24 81`). Details: [R16 note](../ignition/r16-reference-resistor.md) | SM 15, 15-515 |
| Ignition point | 8–12° BTDC at idle; 23–27° (without vacuum) / 39–43° (with) at 3200 rpm, EZL `007 545 47/48 32` | SM 15, 15-515 |
| Test conditions | coolant 75–90 °C; above 90–100 °C (by version) the EZL retards up to 5° as boiling protection | SM 15, 15-510 |
| Fuel | below the octane the engine was set for, retard 1–2° per RON, at most 6° | SM 15, 15-515 |
| Coolant sensor (2-pin, B11/2) | two NTC elements, one pin each: one for the fuel injection, one for the EZL; 320 Ω = 80 °C | SM 15, 15-510 |
| Ignition coil | primary 0.3–0.6 Ω | SM 15, 15-540 |
| Crankshaft position sensor | 660–1200 Ω | SM 15, 15-540 |
| Suppression resistors | distributor cap per terminal, rotor and plug connectors, about 1 kΩ each (700–1300 Ω) | SM 15, 15-510 / 15-540 |
| Spark plugs | tapered seat, 10–20 Nm (type and gap not given in these manuals) | MM 1580 |

## Brakes

| Item | Value | Source |
|------|-------|--------|
| Front discs | vented, 262 mm, 22 mm thick; machine to no less than 20 mm, wear limit 19.4 mm; runout max 0.12 mm | CB 42-220 |
| Front pads | floating caliper, 54 mm piston; pad 17.5 mm including 5.5 mm backing plate; replace at 3.5 mm lining | CB 42-160 |
| Rear discs | 258 mm, 9 mm thick; machine to no less than 7.6 mm, wear limit 7.3 mm; runout max 0.15 mm *(text only)* | CB 42-228 |
| Rear pads | replace at 2 mm lining *(text only)* | CB 42-160 |
| Torques | front caliper 115 Nm (new self-locking bolts); rear caliper 50 Nm *(text only)*; disc locating screw 10 Nm | CB 42-220, 42-228 |
| Brake fluid capacity | about 0.35 L | CB 00-020 |

## Wheels and tyres

| Item | Value | Source |
|------|-------|--------|
| Wheel bolts | 110 Nm *(text only)* | CB 40-110 |
| Tyre pressures, cold | partial load: front 1.8 bar (26 psi), rear 2.0 bar (29 psi); full load: front 2.0 bar (29 psi), rear 2.3 bar (33 psi). Label `201 584 05 39` | CB 40-106 |
| Warm tyres | may read up to 4 psi higher; don't let air out *(text only)* | CB, 1987 supplement |
| Standard wheel and tyre (1987) | 6J × 15 H2 ET 49 alloy, 185/65 R 15 87 H (winter 87 T M+S) *(text only)* | CB, 1987 supplement |

## Suspension and steering

| Item | Value | Source |
|------|-------|--------|
| Springs and dampers (201.028, 1987 supplement) | front spring `201 321 22 04` or `23 04`, front strut `201 320 14 30`; rear spring `201 324 25 04`, rear shock `201 326 08 00`. Spring and pad choice uses a points table: front 37 base (incl. automatic, climate control, SRS) + 2 sunroof + 2 ABS + 1 headlamp washers; rear 8 + 3 sunroof. Details in [suspension](../suspension-steering/suspension.md) | CB, 1987 supplement C32 |
| Front strut | top nut 60 Nm; lower bolts 100 Nm; clamp 75 Nm *(text only)* | CB 32-100 |
| Front wheel bearing | end play 0.01–0.02 mm; clamp nut screw 12 Nm *(text only)* | CB 33-300 |
| Power steering | about 0.6 L ATF (the 00-020 table says 1.0 L); relief valve 65 ± 5 bar; circulating pressure max 5 bar; cold level 6–8 mm below the mark | CB 46-130 |
| Steering wheel play | max 25 mm at the rim *(text only)* | CB 46-110 |
| Wheel alignment | not in this manual (it refers to job 40-320, not included) | — |

## Drivetrain and electrical

| Item | Value | Source |
|------|-------|--------|
| Rear axle | 1.1 L SAE 90 hypoid oil; ratio 3.27 (49:15) *(ratio text only)* | CB 00-020; 1987 supplement C35 |
| Fuel tank | 55 L, reserve 7.0 L | CB 00-020 |
| Battery | 12 V, 62 Ah | CB 00-020 |
| Alternator / starter | 14 V 70 A / 1.4 kW | CB 00-020 |
| Fuses | 1, 3, 6, 7, 8, 19, 20 = 16 A; 10 and 12 = 8 (16) A; others 8 A. Relays: R1 combination (turn signals, rear window heater, wipers), R2 power windows, R3 A/C, R4 overvoltage protection | CB, fuse box page |
| Blower fuse (1988) | moved from a 25 A fuse to a 30 A fuse in an extra holder (F15) *(text only)* | CB, 1988 supplement |
| Sunroof motor slip clutch | 4–5 Nm *(text only)* | CB 77-195 |

## Belts and other

| Item | Value | Source |
|------|-------|--------|
| Poly-V belt | 1980 mm with power steering and A/C; tensioner bolt 75 Nm (19 mm hex) or 80 Nm (17 mm, shouldered). Which belt drive this car has is not confirmed | MM 1351 |
| Older multi-belt drive | tension in kg on gauge `001 589 69 21 00`: A/C and power steering 50 new / 40–45 used; alternator–coolant pump 30 new / 20–25 used | MM 1350.05 |
| Oxygen sensor | 50–60 Nm with paste `000 989 88 51` | MM 1480 |

## Service intervals (USA)

| Item | Interval | Source |
|------|----------|--------|
| Maintenance service | every 15,000 mi / 24,000 km; additional work every 30,000 mi; at least every 2 years | MM |
| Engine oil and filter | at least once a year (year-round multigrade oil) | MM |
| Brake fluid | every year | MM |
| ATF change (no filter) | every 15,000 mi under severe use | MM |
| Coolant | at the latest every 3 years | SM 20 |
