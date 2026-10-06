# R16 / R16/1: EZL ignition reference resistor

**System:** ignition
**Status:** reference (value on this car not measured yet)

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
| R16/1 resistor | **Not listed in EPC 452** | Probably supplied as part of a harness |
| Resistance fitted | **Not measured yet** | |
| Location | **Not checked yet** | See below |

**Location (forum reports, not checked on this car):** taped to the wiring harness, wrapped in black
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
differ):

| Position | Resistance | "EZL-KAT" plug marking |
|---|---|---|
| 1 (A) | open, no pin | — |
| 2 (B) | 2.4 kΩ | |
| 3 (C) | 1.3 kΩ | |
| 4 (D) | 750 Ω | **S** (premium) |
| 5 (E) | 470 Ω | |
| 6 (F) | 220 Ω | **N** (regular) |
| 7 (G) | 0 Ω | |

Other points from the WIS document:

- Engines 102.96/98 with catalytic converter **from 09/89** have separate maps for automatic and
  manual transmissions, picked by special R16 plugs. This car was built before 09/88, so this may
  not apply.
- Plug position 7 is used for other signals on some engines (transmission overload protection on
  102.983/99 with automatic), so it must not be used there.
- Cars with the adjustable R16 plug must run on premium fuel. Best output and consumption come with
  premium.

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
- Parts data: EPC catalog 452, via the private parts catalog (available on request)
