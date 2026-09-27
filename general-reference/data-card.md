# Data card / VIN decode

Factory build data for this car, decoded from the VIN with the ILCATS parts catalog.

- **Source:** [ILCATS spare parts catalog](https://www.ilcats.ru/?language=en). Search with the VIN from `.env`.
- **Saved copy:** [references/ilcats-vin-decode/](references/ilcats-vin-decode/) (identifiers redacted)
- **Decoded:** 2026-09-27

The VIN, engine number, transmission serial, order number and body number live only in `.env`.

## Model

| Item | Value |
|------|-------|
| Model | 190 E 2.3 **USA** (201.028) |
| Model year | **1988** ("J" series, federal) |
| Production | before 09/88 |
| EPC catalog | **452** (190 E 2.3 USA, model years 87–88) |
| Engine | **M102.985** |
| Transmission | **722.408**, a 4-speed automatic (722.4 family, W4A 020). Option code 420 |
| Lights / wipers | Bosch / Bosch |

The site also lists the same data card under catalogs 14R, 15C, 15D, 15E and 431 (other markets and
model years). Only 452 matches this car's model year and ident range. **Use catalog 452 for parts lookups.** The full catalog 452 for this car (55 groups, 198 diagrams, 6,353 part
rows, with a part-number index) is kept in the private archive and is available on request.

## Why USA

The site lists the same data card under six catalogs, because it shows every catalog covering model
201.028. The market is decided by:

1. **Option code 491 "U.S. version"** on the car's own data card.
2. **US-format VIN** (`WDBDA28D…`, 17 characters with a check digit). A European 201.028 would
   read `WDB2010281…`.
3. **Serial within catalog 452's range** for 1988 US federal cars (it also fits the general
   catalog 431, so this alone isn't decisive).
4. The car has amber side markers in the front turn-signal corners.

Other things to check on the car: a speedometer in mph, US-size bumpers, a US emissions label
under the hood, and a third brake light.

## Paint & interior

| Field | Value on card | Notes |
|-------|---------------|-------|
| Paint | 77 (code list also shows **147**) | **147 = Arctic White.** Matches the car, which is white (owner confirmed) |
| Interior | 177 (code list shows **177A**) | **177 = MB-Tex, Medium Red** (1xx = MB-Tex vinyl, x77 = medium red). Matches the car's reddish interior (owner confirmed). Source: [SL Registry interior codes](https://www.sl-registry.com/decoder/interior-colors/) ([saved](references/slregistry-interior-codes/)) |

## Option codes

| Code | Description | On the car |
|------|-------------|------------|
| 240 | Outside temperature indicator | ✅ present |
| 286 | Luggage nets on front seat backrests | ❌ was removed from the car |
| 412 | Electric sliding roof with tilting device | ✅ present |
| 420 | Automatic transmission, 4-speed | ✅ present |
| 444 | Cruise control (Tempomat) and airbag | ✅ present |
| 467 | Central locking and instruments with English lettering *(ilcats says "electronic locking differential", see note)* | ✅ present |
| 491 | U.S. version | n/a (market code) |
| 506 | Outside mirrors left and right, heated; right one electrically adjustable (LHD) | ✅ present: both heated, right one electric |
| 519 | Rear audio system | ✅ present |
| 524 | Paintwork preservation | n/a (factory process) |
| 531 | Automatic antenna | ✅ present |
| 543 | Sun visors with make-up mirror, left and right | ✅ present |
| 575 | Center console for 2nd seat row | ✅ present |
| 586 | Behr air conditioning + electric windows front and rear (= 580 + 584) | ✅ present |
| 593 | Green heat-insulating glass all round, heated rear window, tinted strip on windshield | ✅ heated rear window. Tint can't be verified because the windows are not original |
| 600 | Headlamp cleaning system | ❌ was removed from the car |
| 639 | First-aid kit and warning triangle deleted | n/a (delete option) |
| 640 | 15-hole light alloy wheels | ✅ present |
| 808 | Model-year change code (AEJ 06/1/M/X) | n/a (production code) |
| 876 | Rear door contacts and lamp above rear window | ✅ present: reading lights front and rear |

**On the car**: ✅ present (owner confirmed), ❌ fitted at the factory, was removed from the car, ? not yet checked.

### Option code sources

The blank descriptions from ilcats were filled in from two Mercedes option code lists, using the
entry that was valid in 1988:

- *Mercedes Benz Option Codes (1960 and above)*, a BenzWorld attachment:
  [original](https://www.benzworld.org/attachments/mercedes-benz-option-codes-pdf.2627503/),
  [archived](https://web.archive.org/web/20231102014707/https://www.benzworld.org/attachments/mercedes-benz-option-codes-pdf.2627503/)
- *Mercedes-Benz Codes in German and English* (v2.5, 1999), a BenzWorld attachment:
  [original](https://www.benzworld.org/attachments/mercedes-option-codes-pdf.1870794/),
  [archived](https://web.archive.org/web/20240702050909/https://www.benzworld.org/attachments/mercedes-option-codes-pdf.1870794/)

**Note on 467:** ilcats describes it as "electronic locking differential", but the 1960+ list gives
467 (valid 1970–1993) as **central locking + instruments with English lettering**. That fits a
US car, whose gauges read in English (mph, "BRAKE" and so on). The car does have central locking and English instruments, which confirms this meaning.

**Note on 876:** ilcats uses the post-1997 meaning ("interior light assembly"). For 1964–1993, 876 is
"rear door contacts and lamp above rear window", which matches the rear reading light.
