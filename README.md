# Mercedes-Benz 190 E 2.3 (W201) — Logbook

A *bitácora* (logbook) of fixes, findings, measurements and lessons learned while
keeping my Mercedes-Benz 190 E 2.3 8V alive and healthy.

---

## The car

### Confirmed facts

These are verified for **this specific car**.

| Item          | Value                                  | Source |
|---------------|----------------------------------------|--------|
| Chassis       | W201                                   | |
| Model         | 190 E 2.3                              | |
| Model variant | **201.028**                            | |
| Engine        | **M102.985**, 2.3 L, 8 valves          | Engine number prefix |

The VIN and engine number are in `.env` (git-ignored, never committed). See `.env.example`.

### From the factory data card

Decoded from the VIN. Details in [general-reference/data-card.md](general-reference/data-card.md).

| Item          | Value |
|---------------|-------|
| Market        | **USA**: code 491 "U.S. version", US-format VIN, amber side markers |
| Model year    | **1988**, built before 09/88 |
| EPC catalog   | **452** (use this one for parts lookups) |
| Transmission  | **722.408**, 4-speed automatic (722.4 / W4A 020), code 420 |
| Paint         | **White**: code 147, Arctic White (the owner confirms the car is white) |
| Interior      | **MB-Tex, Medium Red** (code 177) |
| Options present | Outside temp display (240), electric sunroof (412), 4-speed automatic (420), cruise control + airbag (444), central locking + English instruments (467), heated mirrors with electric right mirror (506), rear audio (519), power antenna (531), vanity mirrors (543), rear center console (575), Behr A/C + electric windows front/rear (586), heated rear window (593), 15-hole alloys (640), front and rear reading lights (876) |
| Options no longer fitted | Headlamp cleaning (600) and seatback luggage nets (286), both removed from the car |
| Options not verifiable | Green tinted glass (part of 593); the windows are not original |

### To be confirmed

Fill these in as they get verified (VIN plate, engine stamping, service book).

| Item                          | Value | Source |
|-------------------------------|-------|--------|
| Current mileage               |       |        |

### General reference (not yet verified on this car)

Typical specs for the 201.028 / M102.985. Treat as a starting point, not gospel —
always check against the data card and factory service manual.

- **Engine:** 2299 cc inline-4, SOHC, 8 valves
- **Fuel injection:** Bosch KE-Jetronic (CIS-E)
- **Ignition:** EZL electronic ignition
- **Timing drive:** single-row timing chain
- **Power:** ~130–136 PS depending on year/market and catalyst
- **Production:** mid-1980s to 1993

---

## Repo structure

No code here — just Markdown notes and images, organized by topic folder.
Each topic folder holds its own entries plus an `images/` subfolder for photos,
diagrams and scans referenced by those entries.

```
.
├── README.md                 # car overview + index
├── CLAUDE.md                 # repo rules (links, private data)
├── .env.example              # template for VIN / engine number (.env is git-ignored)
├── general-reference/        # whole-car info: data card, specs, manuals
├── art/                      # posters, drawings, blueprints
├── climate-control/          # heating, ventilation, A/C, vacuum actuators
│   ├── YYYY-MM-DD-short-title.md
│   ├── images/
│   └── references/           # source info per link (full copies on request)
├── central-locking/          # pneumatic central locking: pump, actuators, lines
├── engine/
├── fuel-injection/
├── ignition/
├── cooling/
├── electrical/
├── transmission/
├── suspension-steering/
├── brakes/
├── body/
├── interior/
└── specs/                    # torque values, fluids, capacities, part numbers
```

Folders get created as needed — only add a topic when there's something to put in it.

### Conventions

- **File names:** `YYYY-MM-DD-short-title.md` for dated entries; plain `topic-name.md`
  for reference notes that aren't tied to a date.
- **Images:** stored in the topic's `images/` folder, named `YYYY-MM-DD-description.jpg`,
  and referenced with relative paths: `![Vacuum lines](images/2026-09-27-vacuum-lines.jpg)`.
- **Links:** every link gets a saved copy. Full copies of other people's work are kept in a
  private archive and are **available on request**. Only fair-use material (our notes and photos,
  facts, short quotes, links) is published here. Full rule in [CLAUDE.md](CLAUDE.md).
- **Index:** every new entry gets a row in the [Log index](#log-index) below.

### Log entry template

```markdown
# YYYY-MM-DD — Short title

**Mileage:** 
**System:** engine / fuel / ignition / cooling / electrical / suspension / brakes / body / interior
**Status:** open | fixed | monitoring

## Symptom
What was observed.

## Diagnosis
Tests done, measurements, findings.

## Fix
What was done. Parts used (with part numbers), tools, torque values.

## Cost
Parts / labor.

## Notes
Lessons learned, follow-ups, references.
```

---

## Log index

| Date | Title | Topic | Status |
|------|-------|-------|--------|
| 2026-09-27 | [Data card / VIN decode](general-reference/data-card.md) | general-reference | done |
| 2026-09-27 | [Dashboard removal & broken HVAC vacuum actuators](climate-control/2026-09-27-dashboard-removal-vacuum-actuators.md) | climate-control | open |
| 2026-09-27 | [Blower fan not working](climate-control/2026-09-27-blower-not-working.md) | climate-control | open |
| 2026-09-28 | [Central locking not working (pump silent)](central-locking/2026-09-28-central-locking-not-working.md) | central-locking | open |
| 2026-09-29 | [Throttle pedal: dead zone, step and kickdown](engine/throttle-pedal.md) | engine | reference |
| 2026-10-01 | [Interior restoration: door panels, carpets](interior/interior-restoration.md) | interior | planned |

---

## Resources

- [Parts suppliers](general-reference/parts-suppliers.md): stores worth checking for W201 parts
- [To buy: aesthetic parts](general-reference/to-buy-aesthetic.md): cosmetic parts to replace, with part numbers
- Mercedes-Benz WIS / EPC (factory service info and parts catalog)
- Bosch KE-Jetronic technical documentation
- Community forums: BenzWorld (W201 section), PeachParts (MBWorld), w201.com
