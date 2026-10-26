# Exhaust: O2 sensor, cat delete, front pipe and upgrades

**System:** engine / exhaust
**Status:** planned

What the factory exhaust on this car is, which parts it uses (Mercedes and aftermarket), and which
changes are worth making. The car is no longer in the US, so removing the cat is allowed where it is
now. Part numbers come from EPC catalog 452 (190 E 2.3 USA, to 09/88, this car), group 49.030 sheet 2,
via the private parts catalog and elcats.ru (available on request). Prices and stock were checked on
2026-10-14 and are only a rough guide.

## Summary

- **Keep the O2 sensor in every option.** It sits in the front pipe *before* the cat. The CIS-E
  (KE-Jetronic) lambda loop needs it; removing the cat does not affect it.
- **Do first:** test the O2 sensor ([duty cycle test](../fuel-injection/mixture-adjustment.md)),
  fix any leak upstream of it, replace tired rubber mounts.
- **Cat delete:** cut out the cat and weld in a silencer box (quiet) or a straight pipe, keeping the
  sensor where it is. Cheapest and the most common route.
- **Cat-back:** OE-style mufflers are cheap and still made. For a sportier sound, keep the center
  resonator and change only the rear muffler.
- **Headers:** not worth it on this car (little gain, top end only, can lose low-end torque).
- **No dyno data** was found for any exhaust change on the M102 8V. All gains are owner impressions.

## The factory system (this car)

Front pipe with the catalytic converter built in → center muffler (resonator) → rear muffler.
The cat is not sold separately; it is part of the front pipe.

The EPC drawing (49.030 sheet 2) is in the private catalog, available on request.

### O2 sensor

- **Part:** `A 006 542 96 17` (49.030 pos 128), with heat shield `A 107 490 12 30` (pos 125,
  replaces `A 126 490 00 30`, discontinued). Mercedes now supplies **`A 009 542 45 17 26`**
  (about US$194, mbpartsgiant).
- **Type:** heated, 3 wires (two black, one white), thread M18 × 1.5, **22 mm** wrench.
- **Location:** screwed into the front pipe before the cat, in a tight gap between the pipe and the
  floor pan, under its heat shield. The wire goes through a rubber grommet into the cabin; the 3-pin
  plug is **under the passenger-side carpet, next to the tunnel** (BenzWorld,
  [reference](references/bw-190e-2-3-cat-o2-sensor/README.md)). Not yet checked on this car.
- **Not this one:** EPC 14.090 also lists `A 009 542 87 17` (sensor in the exhaust manifold, with
  bracket `A 124 545 94 40`). Its footnotes limit it to later engines; this car's engine number
  (checked against `.env`) is before that change. Confidence: medium-high.
- **Problems:** old sensors seize in the pipe; a dead sensor puts the injection in limp-home mode
  (duty cycle stuck at 50%). An air leak before the sensor makes it read lean, and the loop then runs
  the engine rich.

### Exhaust manifold

Most likely **`A 102 140 11 09`** (14.060 pos 5; replaces `A 102 140 03 09`), the cat-car manifold
without a sensor port, for engines before the change at serial 079459. Confidence: medium. ILCATS
also lists `A 102 140 39 09`, which elcats doesn't have and nothing explains. Check the casting
number on the car.

## Mercedes part numbers (49.030 sheet 2)

"→" means replaced by; the last number is the current one. MB status from mbpartsgiant.

| Pos | Part number | Qty | Part | Notes |
|---|---|---|---|---|
| 8 | `A 201 490 62 19` → **`A 201 490 97 19`** | 1 | Front pipe with catalytic converter | In stock, MSRP US$1,920 |
| 17 | `A 201 490 17 15` → `27 15` → **`A 201 490 06 01`** | 1 | Center muffler (with pipe) | Discontinued |
| 26 | `A 201 490 18 15` → `28 15` → **`A 201 490 07 01`** | 1 | Rear muffler (with pipe) | Discontinued |
| 32 | `A 107 490 01 41` → **`A 107 490 00 41`** | 1 | Clamp | MB now `A 000 490 08 41` |
| 35, 44 | **`N 304 017 00 8043`** | 1 + 2 | Hex bolt (clamp; front pipe to center pipe) | |
| 38 | `N 000 433 00 8406` | 2 | Washer | |
| 41 | `N 000 934 00 8013` | 1 | Nut | |
| 44 | `N 910 143 00 8017` → **`A 129 990 04 10`** | 4 | Bolt with washer, M8 × 55: front pipe to manifold | For cat pipes |
| 47, 83 | **`A 000 990 32 50`** | 2 + 2 | Nut: front pipe to center pipe / to bracket | |
| 59 | `A 126 492 04 81` | 1 | Seal ring: front pipe to center pipe | Discontinued (aftermarket below) |
| 74 | `A 124 492 04 41` or `A 124 492 03 41` | 1 | Bracket: front pipe to transmission | Catalog doesn't say which |
| 80 | `A 201 492 01 27` | 1 | U-bolt: front pipe to bracket | |
| 86 | `N 000 440 00 9103` | 6 | Washer | |
| 89 | **`N 304 017 00 8021`** | 2 | Hex bolt: bracket to transmission | |
| 92 | `N 002 093 01 6100` | 8 | Disc spring | |
| 95 | `A 121 155 01 81` | 6 | Rubber ring: bracket to transmission | No aftermarket found |
| 98 | `A 126 492 01 72` | 2 | Nut | |
| 104 | `A 201 490 00 37` | 1 | Front hanger assembly | |
| 107 | `A 201 492 01 16` | 1 | Hanger ring, center muffler | |
| 110 | `A 201 492 00 26` | 1 | Clamping piece, center muffler | |
| 113 | **`N 304 017 00 8016`** | 2 | Hex bolt | |
| 116 | `N 000 125 00 8418` | 2 | Washer | |
| 119 | `A 107 492 00 82` | 2 | Rubber ring, rear muffler | |
| 122 | `A 123 987 09 40` | 1 | Rubber stop | |
| 125 | **`A 107 490 12 30`** | 1 | O2 sensor heat shield | Discontinued |
| 128 | `A 006 542 96 17` → **`A 009 542 45 17 26`** | 1 | O2 sensor | |

Exhaust manifold gaskets (14.060): `A 102 142 14 80` ×3 and `A 102 142 15 80` ×1. No gasket is listed
between the front pipe and the manifold; check the joint on the car.

The Euro catalog 431 (190 E 2.3 cat cars, to 08/88) uses the same front pipe, O2 sensor, shield and
mufflers, so European aftermarket parts sold against these numbers fit this car.

## Aftermarket parts

From TecDoc-based listings (buycarparts.co.uk) unless noted. Many were out of stock on 2026-10-14;
order by number from any TecDoc shop. Confidence high unless noted.

### O2 sensor (`A 006 542 96 17`)

| Brand / number | Type | Notes |
|---|---|---|
| **Bosch 0 258 003 915** (US 13915) | Direct fit, 3 wires, ~350 mm | OE list includes `A 006 542 96 17` ([reference](references/buycarparts-bosch-0258003915/README.md)). Not Bosch 13144 (1989–93) |
| **NTK 93395** (OZA721-EE9) | Direct fit, 3 wires, 315 mm | ~£123, in stock |
| **Vemo V30-76-0044** | Direct fit, 3 wires, 320 mm | ~£42 ([reference](references/buycarparts-vemo-v30-76-0044/README.md)). Medium-high |
| Delphi ES10258 | Heated, 325 mm | Medium |
| Bosch 0 258 986 502, NTK 93111, Denso DOX-0115 | Universal 3-wire, no plug | Reuse the old plug |
| Bosch with W201 harness and grommet (rpm-depot) | Plug and play, lists 201.028 | €99, out of stock ([reference](references/rpm-depot-bosch-o2-sensor/README.md)) |

TecDoc groups this sensor with `A 009 542 41 17`. Compare the plug on the car before buying a
direct-fit sensor.

### Front pipe with cat (`A 201 490 97 19`)

Walker 18345 (~£352), Bosal 099-502, Eberspächer 23.279.60, MTS 04.3803, LRT 7402, HJS 96 13 3017
(ECE approved), Vegaz MK-903 ([reference](references/buycarparts-oen-2014909719/README.md)).
rpm-depot sells an ECE R103 replacement with pre-cats for €1,799
([reference](references/rpm-depot-m102-8v-cat/README.md)) and a stainless 200-cell sport cat pipe
for €1,199 ([reference](references/rpm-depot-bastuck-front-pipe/README.md)).

### Front pipe without cat

- **Euro non-cat front pipe `A 201 490 06 20`** (Euro EPC, LHD; MB MSRP ~US$352). Has a pre-muffler
  where the cat would be. Aftermarket: **Bosal 281-299** (~£136,
  [reference](references/buycarparts-bosal-281-299/README.md)), Veneporte ME50003, Hella
  8LB 366 021-711, Faurecia FS50003, Eberspächer 23.486.80, Walker 05299, Ernst 353076.
  **Most likely has no O2 sensor boss** (inferred: the EPC lists the sensor for cat cars only), so one
  must be welded in (M18 × 1.5). Fit on this US car is inferred, not confirmed. Medium confidence.
  Later Euro numbers: `A 201 490 34 20` (from ident A 611778) ([reference](references/elcats-15c-exhaust-49-180/README.md)).
- **Bastuck stainless front pipe** MB190/W201-P/2, €299 (rpm-depot), bolts to the stock manifold
  ([reference](references/rpm-depot-bastuck-front-pipe/README.md)). Check whether it has an O2
  sensor boss before buying.

### Center muffler (`A 201 490 06 01`)

Polmo 13.08 (~£61), MTS 01.53450, Vegaz MS-104, **Bosal 175-123** (~£111), Asmet 01.011, Veneporte
ME50004, Hella 8LC 366 025-201, Walker 14097. All aluminized steel
([reference](references/buycarparts-oen-2014900601/README.md)).

### Rear muffler (`A 201 490 07 01`)

**Bosal 175-297** (~£60), Polmo 13.59, Eberspächer 23.486.84, Ernst 353267, Vegaz MS-139; fitting
kit HJS 82 13 9017 ([reference](references/buycarparts-oen-2014900701/README.md)). Not
`A 201 490 09 01` (a later rear muffler).

### Hardware

| OE | Aftermarket | Confidence |
|---|---|---|
| `A 126 492 04 81` seal ring | Bosal 256-090, HJS 83 13 6445, Walker 86115, Ernst 498319 ([reference](references/buycarparts-oen-1264920481/README.md)) | High |
| `A 107 492 00 82` rubber ring, rear | Bosal 255-338, Walker 81217, Vaico V30-7306 (match the size) | Medium |
| `A 201 492 01 16` hanger ring | Febi 07365, Lemförder 12659 01, Bosal 255-123, Topran 400 228 | Medium-high |
| `A 123 987 09 40` rubber stop | Febi 15705, Lemförder 12783 01, Bosal 255-001 | High |
| `A 201 492 01 27` U-bolt | Bosal 251-087, Walker 82145 | Medium-high |
| `A 107 490 00 41` clamp | HJS 83 13 8805 (Ø55; measure first) | Medium |
| `A 102 142 14 80` manifold gasket ×3 | Elring 917.542, Reinz 71-25226-20 | High |
| `A 102 142 15 80` manifold gasket ×1 | Elring 917.559, Reinz 71-26564-10 | High |
| `A 121 155 01 81`, `A 107 490 12 30` | None found: buy MB / reuse the shield | — |

## Options

### Cat delete

- **How owners do it:**
  1. Cut the cat out of the stock front pipe and weld in a silencer box or a straight pipe. Keeps
     the sensor boss and flanges. Cheapest. A silencer box is "slightly bassier", quiet at speed
     (MBClub, [reference](references/mbclub-190e-aftermarket-cats/README.md)).
  2. Euro non-cat front pipe (above) with a welded sensor boss. One UK owner passed inspection twice
     with this.
  3. Custom stainless front pipe.
- **Effect:** owners report the same or slightly better running, a small mpg gain, a bit more noise.
  A 1.8 with a blocked cat ran clearly better after the delete. Confidence: low (impressions only).
- **Not recommended by anyone:** running without the O2 sensor (Euro non-lambda style). CIS-E then
  runs open loop at a fixed mixture.
- **Check first:** your country's inspection rules; some test against the car's original spec.

### Front pipe

Factory pipes last 20+ years. Replace only if rusted or cracked, or as part of the cat delete.
The manifold bolts differ: cat pipes use M8 × 55 (`A 129 990 04 10`), Euro non-cat pipes M8 × 60
(`N 304 017 00 8053`).

### Headers

- **Available:** TeZet stainless header for the M102 8V incl. 102.985, €949, no road approval
  ([reference](references/rpm-depot-tezet-header/README.md)). A Supersprint 4-2-1 was mentioned for
  racing only (low confidence).
- **Verdict:** owners on w201.com agree the gain on a stock 8V is marginal, top end only, and can
  cost low-end torque; a tuner building 180 PS 2.3s skipped headers
  ([reference](references/w201com-faecherkruemmer-8v/README.md)). BenzWorld: no ready-made header
  existed for years ([reference](references/bw-exhaust-for-2-3-8v/README.md)). **Not worth it** on
  an automatic street car. Confidence: medium-high.

### Cat-back

- **OE-style** (cheap, quiet): the Polmo / Bosal mufflers above.
- **Supersprint** stainless (T304), keeps the stock cat: center **840103**, rear "Oo76"
  **841006**, for the 2.3 8V; ~US$655 and ~US$1,019
  ([reference](references/supersprint-w201-8v-exhaust/README.md)).
- **Bastuck** stainless 8V system, €1,399–1,749 (rpm-depot).
- **Custom:** one owner of the same engine runs a 2.5" system with a Magnaflow resonator and muffler,
  sporty but not loud.
- **Sound:** removing the center resonator makes most of the extra noise
  ([reference](references/peachparts-190e-exhaust/README.md)). A straight pipe instead of the
  resonator gives a slight growl
  ([reference](references/bw-190e-new-cat-back/README.md)); deleting the rear muffler is raspy and
  loud. A Thrush Turbo rear was too loud for one owner
  ([reference](references/bw-190e-2-3-muffler/README.md)).

## Plan

1. Duty cycle test at X11. If the O2 sensor is dead or slow, replace it.
2. Look under the car: cat present? Sensor and plug? Leaks at the manifold and front pipe joint?
   Rubber mounts?
3. Decide: cat delete (cut and weld a silencer box) and/or new mufflers.

## Shopping list

- [ ] **O2 sensor:** Bosch 0 258 003 915 or NTK 93395 (or MB `A 009 542 45 17 26`). Compare the plug first.
- [ ] **Tool: O2 sensor wrench / socket, 22 mm** (7/8"), slotted for the wire.
- [ ] **Penetrating oil** for the sensor and the manifold nuts.
- [ ] **Manifold nuts** `A 000 990 32 50` ×9 (M8 × 1.25, copper-plated steel locking nut; wrench
      probably 12 mm, have 13 mm too) and washers `A 116 990 14 40` ×9, if the manifold or front pipe
      comes off. Fit new nuts with copper anti-seize on the studs. Not solid brass or copper: weaker,
      and they can loosen with heat and cause a leak ahead of the O2 sensor.
- [ ] **Seal ring** front pipe to center pipe: Bosal 256-090 (for `A 126 492 04 81`), if the joint is opened.
- [ ] **Rubber mounts** as needed: `A 107 492 00 82` ×2, `A 201 492 01 16`, `A 123 987 09 40`,
      `A 121 155 01 81` ×6.
- [ ] **For a cat delete:** silencer box or pipe section (Ø about 55 mm; measure), welding by an exhaust shop.
- [ ] **Mufflers** if replaced: center Bosal 175-123 / Polmo 13.08; rear Bosal 175-297 / Polmo 13.59
      (or Supersprint 840103 / 841006).
