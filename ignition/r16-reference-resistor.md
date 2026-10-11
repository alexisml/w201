# R16 / R16/1: EZL ignition reference resistor

**System:** ignition
**Status:** reference. Fitted: R16/1 `24 81`, 750 Ω, the factory value for this car (owner, 2026-10-11)

A resistor plugged into the EZL ignition module's wiring tells the module which ignition timing map
to use. Mercedes made two kinds:

- **R16, resistance trimming plug:** an adjustable plug with 7 positions, so the owner could set the
  timing for premium ("S") or regular ("N") fuel. Euro and other markets.
- **R16/1, reference resistor:** a single fixed resistor. US cars like this one got this kind.

## On this car

| Item | Value | Source |
|---|---|---|
| Ignition control unit (EZL) | `A 007 545 47 32` or `A 007 545 48 32` | EPC 452, 54.255 pos 5 |
| EZL cable harness | `A 201 540 87 10` | EPC 452, 54.255 pos 14 |
| R16/1 resistor | **`A 000 540 24 81`, 750 Ω** (marked "24 81" on the part). Matches the factory spec for USA 102.985, 1987–1989: fixed reference resistor 750 Ω (job 15-515, table below). Not listed in EPC 452 | Owner, 2026-10-11; service manual group 15 |
| Location | **Below the air filter.** Located from the factory manual and seen on the car by the owner | Owner, 2026-10-11; service manual group 15 |

**Found 2026-10-11:** below the air filter (owner). The sealed 2-wire part by the battery
([battery frame entry](../body/2026-10-11-battery-frame-replacement.md#found-near-the-battery-sealed-2-wire-part-unidentified))
is therefore probably something else; still unidentified.

**Factory manual (group 15, job 15-510, engines 102.96/98):** two kinds are fitted: a variable
resistance trimming plug (R16) or a fixed reference resistor (R16/1). Model 201 fixed values listed
there: `000 540 22 81` 220 Ω, `25 81` 1300 Ω, `26 81` 2400 Ω. Test at the ignition control module,
sensor connector contact 3 to ground. Its ignition-timing table (15-515) notes a safety retardation
of 6° and an entry for an open circuit in the trimming plug
([saved copy](references/mb-service-manual-15-electrical-engine/README.md)).

**Factory value for this car (job 15-515, table "Engine 102.983/102.985, USA"):**

| Engine | Model year | Ignition control module | Reference resistor | Ignition point °CKA BTDC (without / with vacuum) |
|---|---|---|---|---|
| 102.985 | 1987/1988 | `005 545 30 32`, `005 545 32 32` | 750 Ω | 25–29 / 39–43 at 3200 rpm; 8–12 at idle |
| 102.985 | 1989 | `007 545 47 32`, `007 545 48 32` (may also be fitted before 08/88) | 750 Ω | 23–27 / 39–43 at 3200 rpm; 8–12 at idle |
| 102.985 | 1991 | `010 545 59 32`, `010 545 60 32` | 1.3 kΩ manual, 2.4 kΩ automatic | 22–26 / 39–43 at 3200 rpm; 8–12 at idle |

The EPC lists `007 545 47 32` / `48 32` for this car, so **750 Ω is correct**. The same table's note says
an open circuit in the resistor makes the module apply a safety retardation of 6°.

**Fuel (job 15-515, footnote):** normal-compression engines need at least 98 RON (88 MON),
low-compression engines at least 92 RON (82 MON); below that, retard 1–2° per RON, at most 6°. The
US 750 Ω setting was made for US premium (91 AKI, roughly 95 RON). In Uruguay, 95 and 97 RON are at
or above that, so **no change is needed**. More advance (470 or 220 Ω) is not a factory setting for
this engine, there is no knock sensor, and forum posts report little gain on the low-compression US
engine. Recommendation (2026-10-11): keep `24 81`.

**Correction (2026-10-11):** an earlier version of this page said the owner measured OL at EZL
contact 3. The owner never measured R16 or the EZL, so that reading is withdrawn. Nothing suggests
the resistor or its wiring is faulty.

**Location (forum reports, earlier):** taped to the wiring harness, wrapped in black
tape. One BenzWorld post says: remove the battery and the plastic cover behind it, and look on the
fire wall. The EZL module sits on the left wheelhouse panel (EPC 54.255).

## How to measure it (WIS 15-0020)

Measure at the EZL control unit, between the **sensor connector, contact 3, and ground**. The
module reads the resistance between the trimming plug and ground.

## Part numbers and values (WIS 15-0020, model 201)

Fixed R16/1 reference resistors:

| Resistance | Part number |
|---|---|
| 220 Ω | `A 000 540 22 81` |
| 470 Ω | `A 000 540 23 81` |
| 750 Ω | `A 000 540 24 81` |
| 1300 Ω | `A 000 540 25 81` |
| 2400 Ω | `A 000 540 26 81` |

Adjustable R16 plug positions (same resistor network in every plug; only the printed markings
differ; WIS 15-0020 table). **S** = premium ("Super"), **N** = regular ("Normal"). The same
letter sits on a different resistance depending on the plug, so a resistance alone doesn't say which fuel it is for:

| Pin | Resistance | "EZL-ECE" | "EZL-KAT" | "EZL" (102.983 Std., 103.980 Std., 117.968 Std.) | "EZ-ECE-S" (102.983 RÜF) | "EZL-KAT MECHANISCH" | "EZL-KAT AUTOMATISCH" |
|---|---|---|---|---|---|---|---|
| A | open, no pin | **S** | 1 | 1 | 1 | – | – |
| B | 2.4 kΩ | 2 | 2 | 2 | **S** | – | **S** |
| C | 1.3 kΩ | **N** | 3 | 3 | **N** | **S** | – |
| D | 750 Ω | 4 | **S** | 4 | 4 | 4 | 4 |
| E | 470 Ω | 5 | 5 | 5 | 5 | **N** | **N** |
| F | 220 Ω | 6 | **N** | 6 | 6 | 6 | 6 |
| G | 0 Ω | 7 | 7 | 7 | 7 | – | – |

Other points from the WIS document:

- Engines 102.96/98 with catalytic converter **from 09/89** have separate maps for automatic and
  manual transmissions, picked by special R16 plugs. This car was built before 09/88, so this may
  not apply.
- Plug position 7 is used for other signals on some engines (transmission overload protection on
  102.983/99 with automatic), so it must not be used there.
- Cars with the adjustable R16 plug must run on premium fuel. Best output and consumption come with
  premium.

## Which fuel goes with which resistance

Mercedes gives RON numbers for a plug position in only one place found so far: factory job 15-520
(German), for engine **117.968 Std.** (V8, 220 kW) with the white "EZL" plug, premium fuel only, 2°
crank angle later per plug step
([saved copy](references/mb-15-520-ezl-plug-fuel/README.md)):

| Position | Resistance (WIS table) | Fuel |
|---|---|---|
| 1 | open | Leaded premium (98 RON) or unleaded "Super Plus" (98 RON) |
| 3 | 1.3 kΩ | Unleaded premium (95 RON) |

The same job, for the other plugs (letters only, no RON):

- **"EZL-ECE"** (white, "RÜF" cars: prepared for a catalytic converter but sold without one):
  S = leaded/unleaded premium, N = leaded/unleaded regular. Workshop position 2 (2.4 kΩ) = 3° later than S, for poor premium.
- **"EZL-KAT"** (green, catalytic converter, unleaded only): S (750 Ω) = unleaded premium, N
  (220 Ω) = unleaded regular. Workshop positions: 5 (470 Ω) = 3° later than S, for poor unleaded
  premium; 7 (0 Ω) = 3° later than N, for poor unleaded regular.
- **US and Australian cars** got a fixed R16/1 instead of the plug. No fuel is named for it.

So lower resistance does not always mean more advance: on the EZL-KAT plug, 470 Ω is later than
750 Ω, and 0 Ω later than 220 Ω.

**Inferred, not stated by Mercedes:** German pump grades of that time were about 98 RON for leaded
"Super", 95 RON for unleaded "Super" and 91 RON for "Normal". One W124 wiki page says the KAT
setting was retarded for unleaded 95 RON compared to the original 98 RON tuning (not checked;
[saved copy](references/mb124-abgleichstecker-ezl-ke/README.md)).

**For this car:** the fitted 750 Ω is the EZL-KAT "S" (unleaded premium) value, and job 15-515
lists 750 Ω for the US 102.985. 95 and 97 RON are fine; keep it.

## Forum findings (not verified on this car)

- **Retard per resistance**, from the 1986 190E 2.3-16 Introduction to Service Manual, quoted on
  PeachParts: no resistor = no retard, 2.4 kΩ = 2°, 1.3 kΩ = 4°, 750 Ω = 6° (US 2.3-16 standard),
  470 Ω = 8°, 220 Ω = 10°, 0 Ω = 12°. That's for the 16V engine. Another poster's manual listing
  didn't follow this order, so treat it with care.
- **Removing it is not a "free power upgrade"** (MBWorld). The EZL reads an open circuit as a fault
  and uses the most retarded curve, the same as a short. R16 has no effect at idle; the changes
  show mostly above ~3000 rpm under load. On the poster's M102, 1300 Ω and 2400 Ω gave the same
  result.
- **On the US 2.3 8V, R16 picks the manual or automatic map, and removing it sets an error**
  (BenzWorld, two posts by the same member). One member found 2.4 kΩ (`26 81`) resistors in two
  cars.
- **US compression ratio was lower** (MBWorld post, not checked): 190E 2.3 at 8.0:1 for the US
  market, 9.1:1 elsewhere. More advance on a lower-compression US engine gains little.

## Before changing anything

Measure and record the original value first. Don't remove the resistor. If you ever try another
value, use one of the values above (1% resistors), check for pinging under load on a hot day, and
check the timing with a timing light.

## References

- WIS 15-0020, EZL resistance trimming plug: [original](http://www.w124performance.com/docs/mb/other/EZL_trim_function.pdf)
  · [Wayback](https://web.archive.org/web/20240714103352/http://www.w124performance.com/docs/mb/other/EZL_trim_function.pdf)
  · [reference](references/wis-ezl-trim-plug/README.md)
- PeachParts: Reference Resistor (R16/1) for EZL Ignition, 2001: [original](https://www.peachparts.com/shopforum/tech-help/23791-reference-resistor-r16-1-ezl-ignition-1986-2-3-16v-no-resistor-=-no-retard.html)
  · [Wayback](https://web.archive.org/web/20200930182025/http://www.peachparts.com/shopforum/tech-help/23791-reference-resistor-r16-1-ezl-ignition-1986-2-3-16v-no-resistor-%3D-no-retard.html)
  · [reference](references/peachparts-r16-reference-resistor/README.md)
- MBWorld: M102 & M103 "free power upgrade" (R16 modification), 2003: [original](https://mbworld.org/forums/190e-w201/42714-m102-m103-free-power-uprade-r16-modification-must-read.html)
  · [Wayback](https://web.archive.org/web/20150908165025/http://mbworld.org/forums/190e-w201/42714-m102-m103-free-power-uprade-r16-modification-must-read.html)
  · [reference](references/mbworld-r16-free-power/README.md)
- BenzWorld: R16 Resistor Revisited, page 2, 2011: [original](https://benzworld.org/forums/w201-190-class/1572759-r16-resistor-revisited-2.html)
  · [Wayback](https://web.archive.org/web/20140228143310/http://www.benzworld.org/forums/w201-190-class/1572759-r16-resistor-revisited-2.html)
  · [reference](references/bw-r16-resistor-revisited/README.md)
- Mercedes-Benz job 15-520, adapting the ignition point to the fuel with the EZL plug (German): [original](http://www.gehner.de/560sel/images/ezl_anpassung_an_spritqualitaet_mit_stecker.pdf)
  · [Wayback](https://web.archive.org/web/20261011200059/http://www.gehner.de/560sel/images/ezl_anpassung_an_spritqualitaet_mit_stecker.pdf)
  · [reference](references/mb-15-520-ezl-plug-fuel/README.md)
- W124-Archiv wiki: Abgleichstecker EZL / KE, 2007 (German): [original](https://archiv.mb124.de/index.php?title=Abgleichstecker_EZL_/_KE)
  · [Wayback](https://web.archive.org/web/20261011200121/https://archiv.mb124.de/index.php?title=Abgleichstecker_EZL_%2F_KE)
  · [reference](references/mb124-abgleichstecker-ezl-ke/README.md)
- Parts data: EPC catalog 452, via the private parts catalog (available on request)
