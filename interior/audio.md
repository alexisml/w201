# Audio: current setup and upgrade plan

**System:** interior / electrical
**Status:** planned

The factory radio and speakers are gone. This note records what is in the car now, what the W201
offers for mounting, and a plan to improve the sound in three budget tiers.

## Current setup

Verified by the owner.

| Item | Fitted | Notes |
|------|--------|-------|
| Head unit | **BOSS Audio Systems BVCP9700A** | Specs below |
| Front speakers | **Infinity Reference REF-4032cfx** (2), 4" coaxial | In the stock dash corner mounts |
| Rear speakers | **Infinity Reference REF-4032cfx** (2), 4" coaxial | In the stock mounts in the rear parcel shelf, below the rear window |
| Fader | **Deleted** | The stock front/rear fader is gone |
| Amplifier, sub, DSP | None | |

From the data card: option **519** (rear audio) and **531** (power antenna). See
[power antenna](../electrical/power-antenna.md). The disconnected "Bell Atlantic" wires in the trunk
(see [README](../README.md#aftermarket-equipment)) could be reused, but what they carry is not measured.

### Head unit: BOSS BVCP9700A

From the owner's manual (39 pages; spec page p. 36, audio settings p. 25, wiring pp. 28–30) unless
noted. BOSS now lists only the **BVCP9700A-C**
([product page](https://www.bossaudio.com/products/791489129558) ([archive](https://web.archive.org/web/20251010062525/https://bossaudio.com/products/791489129558))); its manual link opens the
BVCP9700A manual ([PDF](https://images.salsify.com/image/upload/s--1dxs8W49--/b7z7dm3kmvaqlrfivqhu.pdf) ([archive](https://web.archive.org/web/20250928171231/http://images.salsify.com/image/upload/s--1dxs8W49--/b7z7dm3kmvaqlrfivqhu.pdf), [saved copy](references/boss-bvcp9700a-manual/README.md))).

| Item | Value |
|------|-------|
| Size | Double DIN, 3.80 × 6.71 × 3.56" (H × W × D); 7" 1024×600 screen (double DIN and 7" confirmed by the owner on the car) |
| Built-in amp | "Max Power 85 W × 4". **No RMS figure** given. Speaker load **4–8 Ω**; the manual warns against 1–3 Ω speakers and bridging |
| Pre-outs | **3 pairs, 4 V**: front (full range), rear (full range), sub (mono, own LPF, ignores the fader) |
| Sub output | LPF 50 / 80 / 120 / 160 Hz; level +1 to +14 dB |
| High-pass filter | **None** in the manual (one retailer listing for the -C claims one; not confirmed) |
| EQ | 10 bands ±6 dB (32 Hz–16 kHz), 5 presets, loudness |
| Time alignment | None |
| Balance / fader | Both (so the deleted stock fader isn't missed) |
| Internal amp | Can be **switched off** in the settings (useful with an external amp) |
| Remote output | **Blue/White**, +12 V, 500 mA (use a relay for several amps) |
| Antenna output | **Blue**, +12 V, 500 mA max |
| Other wires | Red ACC, Yellow constant +12 V, Black ground, Orange illumination, Violet/White reverse; 15 A fuse |
| Speaker wires | Front right Gray / Gray-Black, rear right Purple / Purple-Black; White and Green are the left pairs |
| Phone | Wired CarPlay and Android Auto; Bluetooth 4.2 (HFP, A2DP, AVRCP, PBAP); SWC input (interface not included) |

What it means for the plan:

- **Good:** 4 V pre-outs on three pairs, a sub output with its own low-pass, and a switchable
  internal amp. Any amp or DSP in the tiers below connects by RCA.
- **Missing:** no high-pass for the main speakers and no time alignment. Without an external DSP or
  an inline filter, the 4" speakers keep getting full-range bass.
- **Impedance:** the Infinitys (3 Ω) sit just below the head unit's 4–8 Ω rating. Common practice
  with Infinity's 3 Ω design, but an external amp takes that load off the head unit.

### Speakers: Infinity REF-4032cfx

Infinity's own pages are gone (HTTP 410). Specs from a HARMAN Reference-series spec sheet
([PDF, hosted by a Norwegian dealer](https://bilradiospes.no/media/multicase/documents/infinity/h%c3%b8yttalere/infinity%20reference%20spesifikasjoner.pdf) ([saved copy](references/infinity-reference-spec-sheet/README.md))).

| Spec | Value |
|------|-------|
| Size | 4" (100 mm) coaxial |
| Power | 35 W RMS, 105 W peak |
| Sensitivity | 92 dB @ 2.83 V |
| Frequency response | 75 Hz – 21 kHz |
| Impedance | **3.0 Ω** nominal |
| Tweeter | Edge-driven textile (retailers say 1/2" or 1": conflict) |
| Mounting depth | 1-7/8" (retailers: [Sonic Electronix](https://www.sonicelectronix.com/viewitem.php?id=198893) (**not archived**), [OnlineCarStereo](https://www.onlinecarstereo.com/CarAudio/p_51208_Infinity_Reference_REF-4032CFX.aspx) ([archive](https://web.archive.org/web/20260118114217/https://www.onlinecarstereo.com/CarAudio/p_51208_Infinity_Reference_REF-4032CFX.aspx))) |
| Cutout | 3-5/8" or 3-11/16" (retailers disagree) |

The 3 Ω rating matters: any amp driving them should be **2 Ω stable**. Amps rated 4 Ω minimum
(for example the Kicker KEY200.4) run them out of spec (see below). Their low end stops around 75 Hz, so a high-pass
near 80 Hz costs them nothing.

## What the car offers

Researched, **not verified on this car**. Forum reports unless noted.

### Speaker locations

- **Front dash corners:** 4" (10 cm) is about the maximum. Owners break off the mounting tabs and
  press-fit or silicone the speaker in; the factory grille refits. Only low-profile tweeters fit. No
  published mounting depth: **measure before buying front speakers.**
  ([PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/20531-190e-front-speaker-dash-installation.html) ([archive](https://web.archive.org/web/20200221165129/http://www.peachparts.com/shopforum/car-audio-multimedia/20531-190e-front-speaker-dash-installation.html)),
  [Crutchfield fit guide](https://www.crutchfield.com/carsystems/Mercedesbenz-190E-Stereos-and-Speakers.html) ([archive](https://web.archive.org/web/20251006004004/https://www.crutchfield.com/carsystems/Mercedesbenz-190E-Stereos-and-Speakers.html)))
- **Rear parcel shelf:** stock size is reported differently (4–4.5", 5.25"). A 6.5" round fits
  without cutting metal if the deck-board holes are trimmed; 6×9 needs some metal trimming or a riser
  ([PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/12246-190e-speaker-sizes.html) ([archive](https://web.archive.org/web/20210517105535/https://www.peachparts.com/shopforum/car-audio-multimedia/12246-190e-speaker-sizes.html)),
  [PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/28856-6-5-sony-xplods-fit-perfectly-190-a.html) ([saved copy](references/pp-sony-xplod-6-5-fit-190/README.md))).
  Ours hold 4" speakers.
- **Doors:** door speakers appear in threads about 1990–93 cars, not 1988 US cars. Probably absent on
  ours ([BenzWorld](https://www.benzworld.org/threads/190e-six-speaker-system-door-speakers-not-working.506164/) ([partial archive](https://web.archive.org/web/20170815100802/http://www.benzworld.org/forums/w201-190-class/506164-190e-six-speaker-system-door-speakers.html))).

### Subwoofer locations

| Location | What's known | Verdict |
|----------|--------------|---------|
| **Under the rear seat cushion** | Cushion unclips at the front edge and lifts out. A factory hole under the passenger-side rear seat is reported, used to route wires under the carpet ([BenzWorld](https://www.benzworld.org/threads/running-wires-to-trunk.1282917/) (**not archived**)). **No W201 build with a sub here was found**, and no measurements. One unconfirmed claim of a fuel sender access plate under the bench: check before cutting anything | Possible; **measure first** |
| **Rear parcel shelf, free air** | Best documented W201 build: with the first-aid-kit carrier removed, the hole in the metal shelf fits an oval (about 13×8") bass driver. MDF sub-shelf under the carpet, invisible and reversible. Done in a 190 E 2.6 ([MBClub](https://forums.mbclub.co.uk/threads/thinking-of-sub-amp-combos.74466/), [partial archive, page 1 of 3](https://web.archive.org/web/20250116020821/https://forums.mbclub.co.uk/threads/thinking-of-sub-amp-combos.74466/)) | **Strong option**, needs a free-air (IB) driver and sealed trunk-to-cabin gaps |
| **Trunk box** | The fuel tank stands upright behind the rear backrest, so the seat doesn't fold and there's no pass-through except the first-aid pocket and grommets. One owner found trunk bass "isn't very crisp" ([BenzWorld](https://www.benzworld.org/threads/where-to-put-a-sub-in-a-190e-help.1307263/) (**not archived**), [PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/122012-sub-190e.html) ([saved copy](references/pp-sub-in-190e/README.md))) | Works, loses output |
| **Spare wheel well** | No W201 build found | Possible, untested |

**Seat cavity to measure** (when the cushion is out): depth from floor to cushion frame, width,
length, any access plates, wiring (seat heat, harness), floor shape.

### Mockup sizes for a fit test

Cut cardboard boxes to these outside sizes and try them in the cavity with the cushion back on.

**Powered slim subs** (amp built in, low tier). W × D × H from the makers unless noted. Add about
**40–50 mm at the connector end** for plugs and the wire bend (estimate: no maker publishes it).

| Model | Driver | mm | inches | Price | Source |
|-------|--------|----|--------|-------|--------|
| Pioneer TS-WX140DA | 8" | 200 × 280 × 70 | 7.9 × 11.0 × 2.76 | ~$280 | [Pioneer USA](https://usa.pioneer/products/ts-wx140da) ([archive](https://web.archive.org/web/20260112225315/https://usa.pioneer/products/ts-wx140da)) |
| Alpine PWE-S8 | 8", 120 W | 230 × 341 × 71 | 9-1/16 × 13-7/16 × 2-13/16 | $245–400 | [Alpine](https://www.alpine-usa.com/product/pwe-s8) ([archive](https://web.archive.org/web/20260607114249/https://www.alpine-usa.com/product/pwe-s8)) |
| JBL BassPro SL2 | 8" | 250 × 344 × 71 | 9-7/8 × 13-9/16 × 2-13/16 | ~$380, often out of stock | [JBL](https://mm.jbl.com/car-subwoofers/SUBBPSL2.html) ([saved copy](references/jbl-basspro-sl2/README.md)) |
| JBL BassPro Nano | 6×8" | 195 × 260 × 75 | 7-11/16 × 10-1/4 × 2-15/16 | ~$230, often out of stock | [JBL](https://support.jbl.com/gb/en/car-marine/car-speakers/car-speakers-subwoofers/SUBBPNANO-.html) ([saved copy](references/jbl-basspro-nano/README.md)) |
| Kicker Hideaway HS8 | 8", 150 W | 238 × 352 × 79 | 9-3/8 × 13-7/8 × 3-1/8 | ~$330 | [Kicker](https://www.kicker.com/hideaway) ([archive](https://web.archive.org/web/20260610065341/https://www.kicker.com/Hideaway)) |
| Kicker Hideaway HS10 | 10", 180 W | 249 × 356 × 81 | 9-7/8 × 14 × 3-1/8 | $320–400 | [Kicker](https://www.kicker.com/hideaway-hs10) ([archive](https://web.archive.org/web/20260413182912/https://www.kicker.com/hideaway-hs10)) |
| Rockford PS-8 | 8", 150 W | 238 × 365 × 83 | 9.4 × 14.4 × 3.3 | $350–390 | [Rockford](https://rockfordfosgate.com/products/details/ps-8) ([archive](https://web.archive.org/web/20260418080615/https://rockfordfosgate.com/products/details/ps-8/)) |

**Found for sale in Uruguay** (Mercado Libre UY, seen by the owner 2026-10-23; UY prices not
recorded yet). Mercado Libre UY needs a login to browse, so specs come from makers and other
retailers.

| Model | Driver / amp | mm (W × D × H) | Notes | Source |
|-------|--------------|----------------|-------|--------|
| **Helix U 10A** | 10", 180 W RMS (class AB) | 245 × 345 × **78** | RCA in 0.3–4 V (matches the head unit's 4 V pre-outs) + high-level in; LPF 50–150 Hz 24 dB/oct; subsonic 16 Hz; phase 0–180°; wired level remote; 25 A fuse; diecast aluminium. The **U 8A** (8") is listed with the same box size | [Audiotec Fischer](https://www.audiotec-fischer.de/en/helix/subwoofers/u-10a) ([archive](https://web.archive.org/web/20260308024540/https://www.audiotec-fischer.de/en/helix/subwoofers/u-10a)) |
| **JBL SW68A-MS** | 6×8", 100 W RMS | 290 × 210 × **70** | LPF 50–150 Hz, bass boost +12 dB, subsonic 20 Hz, level remote, 15 A fuse. The older SW68A-S sheet says 80 W, 290 × 210 × 72 | [Magazine Luiza](https://www.magazineluiza.com.br/produto/p/db17ed5j21/te/smsa/) ([saved copy](references/magalu-jbl-sw68a-ms/README.md)) (retailer), [JBL SW68A-S sheet](https://support.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw2a6648bd/pdfs/58033016_Spec%20sheet%20JBLSW68A.pdf) ([saved copy](references/jbl-sw68a-spec-sheet/README.md)) |
| **JBL SW8A-MS** | 8" + 2 passive radiators; sub 200 W RMS at 2 Ω **plus 2 × 100 W at 2 Ω full-range channels** | 345 × 245.5 × **74.6** | The two extra channels could power the front Infinitys (2 Ω rated, so the 3 Ω load is fine). **Not confirmed:** whether those channels have a high-pass. 35 A fuse, RCA in. Specs from Brazilian retailers only; JBL's support page lists none. Made since 2022 | [JBL support](https://support.jbl.com/sg/en/car-marine/car-speakers/car-speakers-subwoofers/58033017.html) ([archive](https://web.archive.org/web/20250324105009/https://support.jbl.com/sg/en/car-marine/car-speakers/car-speakers-subwoofers/58033017.html)), [Mercado Livre BR](https://www.mercadolivre.com.br/caixa-amplificada-jbl-sw8a-ms-slim-sub-8pol-200wrms-3-canais-cor-preto/p/MLB27447712) (**not archived**) |
| AIWA AW-10US | 10", 120 W RMS | 261 × 345 × **69** | USD 149 at aiwa.com.uy, **out of stock** 2026-10-23; remote included | [AIWA Uruguay](https://aiwa.com.uy/catalogo/subwoofer-activo-para-auto-120w-rms-aiwa-bajo-asiento-caja-aluminio-slim-10-pulgadas-aw-10us_AW-10US_AW-10US) ([archive](https://web.archive.org/web/20260711044902/https://aiwa.com.uy/catalogo/subwoofer-activo-para-auto-120w-rms-aiwa-bajo-asiento-caja-aluminio-slim-10-pulgadas-aw-10us_AW-10US_AW-10US)) |
| Pioneer TS-WX010A | 17 × 8 cm, 50 W | 230 × 116 × **70** | Footwell size, very small; LPF 50–125 Hz, phase. Seen via Tiendamia (import) at USD 199 | [Pioneer Latin America](https://pioneer-latin.com/producto/ts-wx010a/) ([archive](https://web.archive.org/web/20250327091558/https://pioneer-latin.com/producto/ts-wx010a/)) |

Conflicts: retailers list the HS8 as up to 386 mm long and the HS10 up to 368 mm (probably with the
control panel); the Alpine as 75 mm tall. Use the longer figure for the mockup.

**Passive shallow drivers in a sealed box** (mid tier, needs the amp). The box sizes below are
**our estimates**, not maker figures: 12 mm (1/2") plywood, driver firing up, minimum recommended
volume, internal height = mounting depth + rear clearance (6 mm for the JL, which JL specifies;
12 mm for the others, a rule of thumb). The cone and surround stick up above the box by the
"lip" figure.

| Driver | Mount depth | Lip | Cutout | Sealed volume | Box outside (W × D × H incl. lip) | Source |
|--------|-------------|-----|--------|---------------|------------------------------------|--------|
| Kicker CompRT 8 | 67 mm | 19 mm | Ø 177 mm | 5.7–28 L | **325 × 325 × 122 mm** at 7 L | Kicker drawing 48CWRT8-CSD |
| Rockford P3SD2-8 | 67.5 mm | not published (~20) | Ø 181 mm | 7 L (5.7–20) | **325 × 325 × ~124 mm** at 7 L | [Rockford](https://rockfordfosgate.com/products/details/p3sd2-8) ([archive](https://web.archive.org/web/20260518154349/https://rockfordfosgate.com/products/details/p3sd2-8/)) |
| Kicker L7T 8 (square) | 70 mm | 24 mm | 188 mm square | 5.7–21 L | **325 × 325 × 130 mm** at 7 L | Kicker drawing 46L7T8-CSD |
| JL Audio 10TW3-D4 | 83 mm | not published (~25) | Ø 244 mm | 14.2 L (14–21) | **425 × 425 × ~138 mm** at 14 L | [Audio Intensity](https://audiointensity.com/products/jl-audio-10tw3-d4) ([archive](https://web.archive.org/web/20260817142456/https://audiointensity.com/products/jl-audio-10tw3-d4)) |
| Rockford P3SD4-10 | 89 mm | not published | Ø 230 mm | 14 L (11–28) | **440 × 440 × ~145 mm** at 14 L | [Rockford](https://rockfordfosgate.com/products/details/p3sd4-10) ([archive](https://web.archive.org/web/20260415170236/https://rockfordfosgate.com/products/details/p3sd4-10/)) |
| Kicker L7T 10 (square) | 95 mm | 27 mm | 237 mm square | 11–28 L | **355 × 345 × 158 mm** at 11.3 L | Kicker drawing 46L7T10-CSD |

The volume can be traded between footprint and height: a longer, narrower box works as long as the
inside area stays about the same (7 L at 79 mm inside height ≈ 885 cm², for example 26 × 34 cm
inside). The JL 8" TW3 doesn't exist; prefab shallow enclosures (Rockford P3S-1X8, JL CS110TG-TW3,
Kicker L7T 10 loaded) are tall wedges for behind truck seats and don't lie flat.

**Takeaway:** powered units need about **70–85 mm** of height; a passive 8" needs about
**120–130 mm**, a passive 10" about **140–160 mm**. If the cavity is under about 120 mm, the
powered route (or the parcel shelf for a passive sub) is the only fit.

## Why each upgrade helps

1. **Sub + high-pass on the 4" speakers.** The 4" speakers can't make real bass; trying is where
   most distortion comes from. High-pass them at about 80–100 Hz and let a sub play below. Below
   about 80 Hz bass is non-directional, so the sub's location doesn't hurt the stereo image.
2. **DSP.** The front speakers fire up at the windshield from the dash corners and the driver sits
   off-center. Time alignment centers the stage; per-channel EQ tames windshield and cavity peaks;
   crossovers set the high-pass and low-pass.
3. **Amplifier.** Head-unit amps make far less real power than the box says. The Infinitys take
   35 W RMS; an amp at about 50 W gives clean peaks, not just more volume.
4. **Sound deadening.** Our speakers aren't in the doors, so the priorities shift:
   - Rear parcel shelf (it's the rear speakers' baffle and a sub's, if mounted there): 50–60%
     butyl coverage, seal around the speakers.
   - Dash pods: foam gasket to the grille, stop buzzes.
   - Floor, tunnel, rear wheel arches, trunk floor and around the tail lights: about 25–30% butyl
     to stop panel resonance, then closed-cell foam (CCF) over it; mass-loaded vinyl (MLV) on the
     floor only in the high tier.
   - Forum reports: deadening the rear bulkhead and the holes by the rear wheel arches cut most rear
     road noise ([BenzWorld](https://www.benzworld.org/threads/dynamat-project.1238120/) (**not archived**),
     [BenzWorld](https://www.benzworld.org/threads/soundproofing-with-dynamat.1712601/) (**not archived**),
     [BenzWorld](https://www.benzworld.org/threads/stereo-in-190e-rattle.1187777/) ([archive](https://web.archive.org/web/20180625034210/http://www.benzworld.org/forums/w201-190-class/1187777-stereo-190e-rattle.html))).

## Upgrade tiers

Prices are USD street prices from undated retailer listings (checked 2026-10-23). Check before
buying. Product sources in [Product sources](#product-sources).

### Low: about $450

Keep the head unit's amp. Add bass and fix rattles.

| Part | Price |
|------|-------|
| Powered slim sub: **Rockford PS-8** (8", 3.3" tall, built-in amp) or **JBL BassPro Nano** (6×8", 74.6 mm tall, 100 W) | $200–390 |
| 8 AWG OFC power kit (enough for a powered sub) | ~$40 |
| Kilmat 80 mil butyl, 36 ft² (parcel shelf, dash pods, trunk floor) | ~$80 |
| Optional: DIY high-pass capacitors on the four speakers (see [Filters](#filters-high-pass-for-the-4-speakers)) | ~$50 |
| **Total** | **≈ $320–560** |

Feed the powered sub from the head unit's sub pre-out (LPF at 80 Hz). The head unit has **no
high-pass** for the main speakers, so they still get full-range bass.

### Mid: about $1,100

Amp + DSP + passive slim sub. The Infinitys stay.

| Part | Price |
|------|-------|
| **Dayton Audio DSP-408** (4 in / 8 out, 10-band PEQ per output, 0–8.1 ms delay) | ~$170 |
| **Rockford R2-750X5** (4×100 W + 1×350 W at 2 Ω) | ~$490 |
| **Rockford P3SD4-10** (10", 3.5" mounting depth, 0.4–1.0 ft³ sealed) + DIY box | ~$270 |
| Kilmat 80 mil, 36 ft² | ~$80 |
| 4 AWG OFC kit, 120 A fuse | ~$100 |
| **Total** | **≈ $1,100** |

Infinitys on channels 1–4 at 2 Ω-stable power, sub on channel 5. Two boxes (DSP + amp) instead of one.

### High: about $1,900 (up to $3,600)

One-box DSP-amp, front components, better sub, full deadening.

| Part | Price |
|------|-------|
| **Audison Prima AP4.9 bit** (4×130 W at 2 Ω, 9-channel DSP, sub pre-out) | ~$700 |
| **Kicker KEY500.1** mono amp for the sub (300 W at 2 Ω) | ~$280 |
| **Kicker L7T 10** (3.75" mounting depth) + box, or **JL 10TW3-D4** (3.25–3.5") | $300–600 |
| **Alpine S2-S40C** 4" components in the dash corners (tweeter depth not published: measure) | ~$150 |
| Resonix CLD ×2 + CCF | ~$220 |
| 4 AWG OFC kit | ~$100 |
| **Total** | **≈ $1,750–2,050** |

No-limits variant (≈ $3,600): **Helix V EIGHT DSP MK2** (8×120 W at 2 Ω, 10-channel DSP), **Focal
ES 100 KE** components run active, Morel 402 coaxials in the rear, JL 10TW3-D4, Dynamat + CCF + MLV,
4 AWG and a "Big 3" upgrade. The **AudioControl D-5.1300** (4×200 W + 500 W at 2 Ω, ~$950) is a
cheaper one-box option, but its 4 channels + sub leave the rear speakers passive.

## US options under $300 each

To import to Uruguay. US street prices checked 2026-10-23 from dealer listings (Pioneer, Best
Buy, Worldwide Stereo, Sound of Tri-State, Car Toys, Parts Express); many listings are undated and
Crutchfield/Amazon couldn't be read, so check before buying.

### Slim powered subs

| Model | mm (W × D × H) | Amp | Price | Notes | Source |
|-------|----------------|-----|-------|-------|--------|
| **Pioneer TS-WX140DA** | 280 × 200 × 70 | 50 W RMS (170 max) | $280 list | 8×5.25". Wired remote with gain, LPF, phase, bass mode. RCA + high-level in. Out of stock at one dealer | [Pioneer USA](https://usa.pioneer/products/ts-wx140da) ([archive](https://web.archive.org/web/20260112225315/https://usa.pioneer/products/ts-wx140da)) |
| **Alpine PWE-S8** | 340 × 230 × 70–75 | 120 W RMS | $245 (Best Buy marketplace) – $400 | 8" quad-coil. Price conflict between sellers | [Best Buy](https://www.bestbuy.com/site/9597106.p) ([saved copy](references/bestbuy-alpine-pwe-s8/README.md)) |
| JBL BassPro Nano | 260 × 195 × 75 | 100 W RMS | $230 | 6×8", bass remote. Often out of stock | [Sound of Tri-State](https://www.soundoftristate.com/jbl-subbpnanoam) ([archive](https://web.archive.org/web/20261026120205/https://www.soundoftristate.com/jbl-subbpnanoam)) |
| JBL BassPro SL2 | 344 × 250 × 71–73 | 125 W RMS | $308 new, $250 refurbished | 8", remote. Just over budget new | [Worldwide Stereo](https://www.worldwidestereo.com/products/jbl-basspro-sl2-self-powered-8-low-profile-underseat-vehicle-subwoofer-system) ([archive](https://web.archive.org/web/20261026115854/https://www.worldwidestereo.com/products/jbl-basspro-sl2-self-powered-8-low-profile-underseat-vehicle-subwoofer-system)) |
| Pioneer TS-WX010A | 230 × 116 × 70 | small | $130–200 | Footwell size, least bass | [Pioneer USA](https://usa.pioneer/products/ts-wx010a) ([archive](https://web.archive.org/web/20260521164252/https://usa.pioneer/products/ts-wx010a)) |

Over budget or too big: Kicker HS8 ($330, ~80 mm tall), Rockford PS-8 ($350+, 83–86 mm). Helix U 10A
and the JBL SW8A-MS / SW68A-MS aren't sold in the US (the Helix is about €289 in the EU).

### Filters: high-pass for the 4" speakers

The head unit can't high-pass the main speakers. Three ways to do it, cheapest first:

1. **DIY series capacitors** (passive, 6 dB/oct). C = 1 / (2π · f · R): for 80 Hz at 3 Ω about
   **663 µF**, made from 3 × 220 µF 100 V non-polarized caps in parallel (Parts Express, about $4
   each; 12 caps for 4 speakers ≈ $50) ([Parts Express](https://parts-express.com/220uF-100V-Non-Polarized-Capacitor-027-368) ([archive](https://web.archive.org/web/20250929202021/https://www.parts-express.com/220uF-100V-Non-Polarized-Capacitor-027-368))).
   Approximate: the speaker's impedance rises near resonance, so the real cutoff moves.
   **Store-bought bass blockers don't work here:** they cut far too high (Metra BB99 is 400 Hz at
   4 Ω, about 535 Hz at 3 Ω; PAC BB-1PR 300 Hz) ([Metra](https://www.metraonline.com/part/BB99) ([saved copy](references/metra-bb99/README.md))).
2. **A 4-channel amp with a built-in high-pass** (12 dB/oct, adjustable). Also gives real power.
   The best value step.
3. **A DSP** (any slope, plus time alignment and EQ). The full fix.

### Compact 4-channel amps (2 Ω stable, adjustable high-pass)

| Model | RMS × 4 at 4 Ω / 2 Ω | HPF | Size (W × H × D mm) | Price | Source |
|-------|----------------------|-----|---------------------|-------|--------|
| **Pioneer GM-DX874** | 100 / 150 (1 Ω stable) | 40–500 Hz | 264 × 60 × 200 | $220 | [Car Toys](https://www.cartoys.com/products/pioneer-gm-dx874) ([archive](https://web.archive.org/web/20261026120001/https://www.cartoys.com/products/pioneer-gm-dx874)) |
| **JL Audio JD400/4** | 75 / 100 | variable | not found | $280–300 | [Sound of Tri-State](https://www.soundoftristate.com/jl-audio-jd400-4) ([archive](https://web.archive.org/web/20261026115650/https://www.soundoftristate.com/jl-audio-jd400-4)) |
| Rockford R2-300X4 | 50 / 75 | 50–250 Hz | 257 × 49 × 173 | $280–310 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-prime-r2-300x4) ([archive](https://web.archive.org/web/20261026120346/https://www.soundoftristate.com/rockford-fosgate-prime-r2-300x4)) |
| Kicker CXA360.4 | 65 / 90 | 50–200 Hz | 171 × 60 × 317 (class A/B, big) | $173–230 | [Worldwide Stereo](https://worldwidestereo.com/products/kicker-cxa360-4-4-channel-90-watt-class-a-b-amplifier) ([archive](https://web.archive.org/web/20250428195854/https://www.worldwidestereo.com/products/kicker-cxa360-4-4-channel-90-watt-class-a-b-amplifier)) |
| Sony XM-S400D | 45 / 45 | **fixed 120 Hz** (a bit high) | very small | $150 | [Car Toys](https://cartoys.com/products/sony-xm-s400d) ([archive](https://web.archive.org/web/20240808162905/https://cartoys.com/products/sony-xm-s400d)) |

Avoid: Rockford PBR300X4 (4 Ω only, discontinued). Discontinued: Kenwood X302-4, JBL Club A754.

**Kicker KEY200.4** (~$240, suggested by Gemini 2026-10-26): a 4 × 50 W amp with a built-in DSP
that tunes itself with the included microphone: auto time alignment (defeatable), auto 40-band EQ,
24 dB/oct high-pass at 60 / 80 / 120 Hz (or full range). Very small: 187 × 70 × 43 mm, fits behind
the dash or under a seat. Not bridgeable, no sub channel (the powered sub stays on the head unit's
sub pre-out). Specs from Kicker and the owner's manual
([Kicker](https://www.kicker.com/key-smart-amplifier),
[Crutchfield FAQ](https://www.crutchfield.com/learn/kicker-47key200-4-compact-4-channel-amplifier-faq.html), **not archived yet**).

- **Catch:** rated **4 Ω minimum per channel**; the Infinitys are 3 Ω. Each channel sees about 25%
  more current than rated. At normal volume it will most likely work (the BOSS is also rated 4 Ω and
  drives them), but at high volume it can run hot and hit protection, and it is outside the spec
  (warranty).
- **Reviews (2026-10-27, owner forums and one dealer test, mostly trucks with stock speakers):** the
  auto setup with the included mic is widely praised; "massive" improvement over stock is common;
  small, runs cool, fits behind a head unit. Complaints: auto-EQ results vary (some found it harsh
  and preferred EQ off, which keeps the time alignment), less punch than a full-size amp, little
  manual control, fixed bi-amp crossover, a few defective units (limiter / protect mode, replaced
  under warranty). DIYMA verdict: decent for simple systems like this one, not for complex builds.
  Sources: [BestCarAudio test](https://www.bestcaraudio.com/test-drive-review-kicker-key200-4-smart-amplifier/),
  [DIYMA](https://www.diymobileaudio.com/threads/is-the-kicker-key-200-4-with-dsp-pretty-decent.471902/),
  [Bronco6G "disappointing"](https://www.bronco6g.com/forum/threads/kicker-key-200-4-amp-disappointing.89851/),
  [Maverick impressions](https://www.mavericktruckclub.com/forum/threads/kicker-key-200-4-installed-impressions.29344/),
  [Tacoma World](https://www.tacomaworld.com/threads/problems-after-kicker-key-200-4.709503/)
  (**not archived yet**).
- **No higher-end KEY:** the 4-channel KEY line is only the KEY200.4 (plus the KEY500.1 mono sub amp).
  Amps with mic auto-tune are rare: besides the KEY200.4, only the Alpine PXE-C80-88 DSP amp (~$1,000)
  and the Alpine OPTIM6 processor (~$500, needs a separate amp) were found
  ([Sonic Electronix guide, 2026-08](https://learn.sonicelectronix.com/top-4-budget-car-audio-dsps-with-auto-eq-calibration/),
  **not archived yet**).
- **Ways around the 4 Ω minimum** (our reasoning, not from Kicker):
  1. **1 Ω series resistor per speaker** so the amp sees about 4 Ω. Use a 1 Ω, 25 W aluminium-housed
     resistor (Dale RH-25 style, a few dollars each), bolted to metal. At the amp's full 50 W it
     dissipates about 12.5 W; with music, a few watts. Costs: about 2.5 dB less level (voltage
     divider 3 : 4) and a weaker grip on the speaker (damping factor about 3), so the response follows
     the speaker's impedance curve a little. The 80 Hz high-pass removes most of the bass where that
     matters, and the KEY's auto-EQ measures the result and corrects the rest. Cheapest fix.
  2. **4 Ω speakers instead of the Infinitys** (at least the fronts). Many 4" coaxials are 4 Ω
     (Kicker, Rockford, Alpine; check each); a Kicker 4" with a Kicker amp is a natural pair. Fully in
     spec, no lost level; costs a new pair or two.
  3. **Front and rear in series per side** (about 6 Ω per channel, 2 channels used). In spec, but front
     and rear then share the same delay and EQ, which defeats most of the time alignment. Not
     recommended.
  4. **Run it at 3 Ω anyway.** About 25% below the minimum: likely fine at normal volume, may hit
     protection when hot and loud, outside the warranty.
- **Versus GM-DX874 + DSP-408 (~$390):** about $150 cheaper, one small box, no laptop tuning. Less
  control: tuning is automatic only (no manual per-channel EQ or delays), and less power headroom.
- **Fit for this car:** the auto time alignment is exactly what the dash-corner speakers need. A good
  choice if the 3 Ω risk is acceptable; the Pioneer + Dayton route is the in-spec one.

### Middle ground: one-box DSP amp, 2 Ω stable

**Stetsom HL400.4 DSPlayer** (Brazilian brand, common in South America, so likely sold in Uruguay;
no UY price checked yet). Researched 2026-10-27 from Stetsom's page and the user manual
([Stetsom](https://stetsom.com.br/en/produto/hl400-4-dsplayer/),
[manual PDF](https://stetsom.com.br/manual/manual_dsplayer.pdf), **not archived yet**).

- 4 × 100 W RMS at **2 Ω** (13.8 V), 4 × 70 W at 4 Ω: the 3 Ω Infinitys are in spec.
- DSP set from a phone app ("car mode"): **EQ, crossover, level, phase, delay** (time alignment)
  and balance. Delay range, EQ bands and filter slopes are not stated in the manual.
- RCA and high-level inputs, an RCA **DSP output** (can feed the powered sub), remote in/out.
  Also a Bluetooth / USB / FM player built in (not needed here).
- Very small: 50 × 125 × 139 mm, 0.5 kg. 25 A fuse, 4–6 mm² power cable.
- **Sold in the US:** $109.99 at Stetsom's US store (2026-10-27), also on Amazon US
  ([Stetsom US store](https://stetsomstore.com/products/stetsom-hl400-4-dsplayer-amplifier-dsp-player-radio-bt-fm),
  [Amazon](https://www.amazon.com/Stetsom-DSPlayer-400x4-Amplifier-Compatible/dp/B0F1G9Y3KK), **not archived yet**).
- **Reviews (thin, 2026-10-27):** no independent sound tests found; mostly Brazilian YouTube videos.
  Praised for features per price and the app. Complaints: units that stopped powering on (one owner
  voided the warranty by opening it to check the internal fuse), Bluetooth quieter than RCA, one
  "don't recommend" video that still calls it good value. Stetsom is a big, established Brazilian
  brand known more for loud bass amps than for sound-quality tuning. No mic auto-tune: tuning is by
  hand in the app.
  ([returned-unit video](https://www.youtube.com/watch?v=hdEO5ssPs3g),
  [power test video](https://www.youtube.com/watch?v=kCwX2CQMYyI), **not archived yet**)
- **Check:** its RCA input sensitivity is 250 mV – 1 V; the BOSS pre-outs go up to 4 V. Keep the gain
  at minimum, or use the high-level (speaker wire) inputs, which take 1.5 V, to avoid clipping the input.

### Amps seen on Mercado Libre UY (owner, 2026-10-27)

| Model | Type | Power | Filters | Size (mm) | Fit here | Source |
|-------|------|-------|---------|-----------|----------|--------|
| **Stetsom HL400.4** (2 Ω, plain, not DSPlayer) | 4 ch | 4 × 100 W at 2 Ω, 4 × 60 W at 4 Ω (13.8 V) | CH1–2: flat / HPF 90 Hz / LPF 90 Hz (fixed). CH3–4: flat / HPF 90 Hz / LPF 30–75 Hz + bass boost. Slope not stated | 50 × 125 × 124 | **Good**: 3 Ω in spec, HPF close to 80 Hz, tiny. No time alignment. RCA input 200 mV sensitivity: keep gain low, or use the 1.5 V "FIO" (wire) input | [Stetsom](https://stetsom.com.br/en/produto/hl400-4-2-ohms/), [manual PDF](https://stetsom.com.br/manual/manual_hl400.4.pdf) (**not archived yet**) |
| **Pioneer GM-DX874** | 4 ch | 4 × 100 W at 4 Ω, 4 × 150 W at 2 Ω | HPF 40–500 Hz, 12 dB/oct | 264 × 60 × 200 | **Good**: 3 Ω in spec, adjustable HPF. No time alignment | (see table above) |
| JBL GTO-501EZ | **mono** sub amp | 500 W at 2 Ω, 350 W at 4 Ω | LPF 40–280 Hz, 12 dB/oct, bass boost | 246 × 66 × 213 | Only for a **passive** sub; not needed with a powered sub. Discontinued in the US | [JBL support](https://support.harmanaudio.com/product-registration/GTO-501EZ_.html) (**not archived yet**) |
| Pioneer GM-D8601 | **mono** sub amp | 300 W at 4 Ω, 500 W at 2 Ω, 800 W at 1 Ω | LPF 40–240 Hz, 12 dB/oct, bass boost remote | ~270 × 60 × 200 | Only for a **passive** sub. Replaced by GM-D8701 | [Pioneer India](https://pioneer-india.in/buy/car-entertainment-car-amplifiers-mono/gm-d8601/) (**not archived yet**) |

### Getting amp + DSP in one box from the region

The owner found only plain amps on Mercado Libre UY (2026-10-27). Seen elsewhere (search results,
not checked on the listings themselves):

- **Stetsom HL400.4 DSPlayer**: Magazine Luiza Brazil about R$ 354; eBay Spain about €115; listed on
  Mercado Libre Argentina. Cheap enough to bring from Brazil or Argentina, or ask a UY Stetsom
  seller to order it.
- **Taramps Pro 2.4 BT**: a separate small DSP processor (EQ, crossover, **delay**, limiter, Bluetooth
  app, 4 RCA outputs), listed on Mercado Libre Mexico. Pairs with a plain HL400.4 if the DSPlayer
  can't be found. Specs not checked against Taramps.
- Plain 4-channel amps with fixed 90 Hz filters and no DSP, for reference: Taramps TS 400x4
  (4 × 100 W at 2 Ω), Stetsom IR400.4.

### US all-in-one DSP amps rated for 2 Ω (researched 2026-10-27)

Requirement: built-in DSP with per-channel delay, adjustable high-pass, EQ, and **2 Ω stable** (for
the 3 Ω Infinitys). **Nothing current and confirmed was found new in the US under $500.** Rockford has
no DSP amps (the DSR1 is a processor only); the JBL MS-A1004 shows no delay; the Kicker KEY200.4 is
4 Ω minimum.

| Model | RMS × 4 at 4 Ω / 2 Ω | DSP | Tuning | Size (mm) | US price | Source |
|-------|----------------------|-----|--------|-----------|----------|--------|
| **Audison Prima AP4.9bit** | 70 / 130 | 9-ch DSP, 0–15 ms delay per channel, spare outputs for a sub | PC (bit Tune) | ~198 × 134 × 46 (unverified) | $800 new; ~$540–600 open box / eBay | [Sound of Tri-State](https://www.soundoftristate.com/ap49bit), [Creative Audio](https://creativeaudio.net/ap4-9-bit-uvg/) |
| **Musway M4 Nano** | 55 / 95 | 8-ch DSP; delay very likely, not shown on the page; 4 RCA outputs | PC, or app with BTA-HD dongle | **150 × 45 × 95** | $700 (order only) | [OnlineCarStereo](https://www.onlinecarstereo.com/CarAudio/p_98517_Musway_M4%20Nano.aspx) |
| **AudioControl D-4.800** | 125 / 200 | Delay per route, 30-band EQ, sub pre-outs, RCA in up to 8 V | PC/Mac, optional BT | ~226 × 203 × 53 | $829 | [AudioControl](https://audiocontrol.com/products/d-4-800-high-power-4-channel-dsp-matrix-amplifier-accubass) |
| LinksWell LWAMP-0400-04 | 100 at 4 Ω; **2 Ω not confirmed** | 31-band EQ, app; **delay not confirmed** | App | — | $380 | [Quadratec](https://www.quadratec.com/p/linkswell/dsp-amplifier/4-channel-lwamp.0400.04) |
| JL Audio VX400/4i | 75 / 100 | Full DSP, 0.01 ms delay steps | PC (TüN) | 229 × 168 × 54 | $1,200+ | [Worldwide Stereo](https://worldwidestereo.com/products/jl-audio-vx400-4i-100-watts-x-4-at-2-ohms-4-channel-amplifier-w-dsp) |

Not in the US or discontinued: Helix M FOUR DSP (discontinued), Sony XM-GS6DSP (discontinued, front
not 2 Ω), Blam DSP 4.120 (UK, £570), Hifonics JUNO4DSP (EU, €329, delay unconfirmed), Pioneer
DEQ-2000A (Japan/Australia), Zapco ST-4X DSP III (EU, €594). All links above **not archived yet**.

**Conclusion:** for one box rated for 3 Ω, the imported Stetsom HL400.4 DSPlayer is by far the best
value. In the US the realistic choices are an open-box Audison AP4.9bit (~$550–600) or the Musway
M4 Nano ($700, smallest).

### US two-box setups: DSP processor + 2 Ω amp (researched 2026-10-27)

Owner preference: a DSP that tunes itself with a microphone (nice to have, not required).

**DSP processors**

| Model | Mic auto-tune | Inputs | Outputs | Size (mm) | US price | Source |
|-------|---------------|--------|---------|-----------|----------|--------|
| **Alpine PXE-C60-60 (OPTIM6)** | **Yes**: AutoEQ 2.0 sets EQ, time alignment and levels with a phone mic (iPhone X+ or Android) or the optional KTX-CSP1 mic kit | 6 RCA (max level not published), 6 high-level up to 27–30 V, BT, USB | 6 RCA, 4 V | 145 × 151 × 42.5 | $500 (launched at $400) | [Alpine](https://alpine-usa.com/product/pxe-c60-60-optim6-sound-processor), [Alpine press](https://www.alpine-usa.com/company/press/2023/alpine-now-shipping-the-optimtm6-6-channel-sound-processor-with-automatic-sound-tuning) |
| miniDSP C-DSP 8x12 DL | **Yes**: Dirac Live (best correction); needs a laptop; UMIK-1 mic bundle | 6 RCA (2 or 4 V), high-level, digital | 12 | 41 × 205 × 122 | $890–940 | [miniDSP](https://www.minidsp.com/products/car-audio-dsp/cdsp-8x12-dl) |
| **DS18 DSP4.8BTM** | No (manual, app) | 4 RCA up to **4 V** | 8, 3.5 V | — | $195–235 | [DS18](https://ds18.com/products/ds18-dsp4-8btm-4-channel-in-and-8-channel-out-digital-sound-processor-with-bluetooth-water-resistant) |
| Dayton DSP-408 | No (manual) | 4 RCA, **max 3.2 V** (1% THD point; sources differ on the sign). The BOSS can send 4 V near full volume: leave headroom, add an inline RCA attenuator, or feed the **speaker-level inputs** (≥ 8 V) from the BOSS speaker outputs instead | 8 | — | $165 | (see DSP table below) |
| Rockford DSR1 | No | 4 RCA up to 4 V, high-level | 8 | ~130 × 103 × 32 | $420 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-dsr1) |

No mic auto-tune: AudioControl DM-608/810, JL TwK-88, JL FiX-82 (its "auto" uses a test tone to undo
factory EQ, no mic), Helix DSP Mini MK2 (unclear). Any manual DSP can be measured with a UMIK-1 mic and
REW (free PC software): REW calculates the EQ, then it is typed in by hand (semi-automatic).

**Compact 4-channel amps, 2 Ω stable**

| Amp | RMS × 4 at 4 Ω / 2 Ω | Size (mm) | US price | Source |
|-----|----------------------|-----------|----------|--------|
| **Alpine KTA-450** | 50 / 45–50 | **181 × 89 × 36** (smallest) | $230–300 | [Abt](https://www.abt.com/Alpine-4-Channel-Power-Pack-Amplifier-With-PowerStack-KTA450/p/131270.html) |
| **AudioControl EPICFOUR** | 100 / 200 (far more than needed: set gains carefully) | 239 × 155 × 51 | $160–200 | [AudioControl](https://audiocontrol.com/products/epicfour-4-channel-amplifier-800w-rms) |
| JL Audio JD400/4 | 75 / 100 | ~242 × 53 × 180 | $300 new, $210 refurbished | [Sound of Tri-State](https://www.soundoftristate.com/jl-audio-jd400-4) |

**Combos**

| Combo | ≈ Total | Auto-tune | Notes |
|-------|---------|-----------|-------|
| **Alpine PXE-C60-60 + Alpine KTA-450** | $730–800 | **Yes** (phone mic) | Both small, one brand. 6 inputs take front, rear and sub |
| Alpine PXE-C60-60 + AudioControl EPICFOUR | ~$700 | **Yes** | Cheapest true auto-tune |
| **DS18 DSP4.8BTM + EPICFOUR** (+ UMIK-1 mic for REW) | $395–435 (+ mic) | Semi | 4 V inputs match the BOSS. Only 4 inputs: feed the sub from a DSP output |
| Dayton DSP-408 + EPICFOUR (+ UMIK-1) | ~$365 (+ mic) | Semi | Watch the 3.2 V input limit |

All links in this section **not archived yet**.

### Three ways to do amp + high-pass + time alignment

| Option | Boxes | Time alignment | 3 Ω in spec | Power × 4 | Tuning | ≈ Cost |
|--------|-------|----------------|-------------|-----------|--------|--------|
| Kicker KEY200.4 | 1 | Auto (mic) | **No** (4 Ω min) | 50 W | Automatic, easy | $240 US |
| **Stetsom HL400.4 DSPlayer** | 1 | Manual (app) | Yes | 100 W at 2 Ω | App | check UY |
| Pioneer GM-DX874 + Dayton DSP-408 | 2 | Manual (PC/app) | Yes | 150 W at 2 Ω | Most control | $390 US |
| Pioneer GM-DX874 alone | 1 | **None** | Yes | 150 W at 2 Ω | Knobs only | $220 US |
| Stetsom HL400.4 (plain) | 1 | **None** | Yes | 100 W at 2 Ω | Switches, HPF fixed 90 Hz | check UY |

### DSP

| Model | What | Price | Source |
|-------|------|-------|--------|
| **Dayton Audio DSP-408** | Processor only: 4 in / 8 out RCA, crossovers, 10-band PEQ per output, 0–8.1 ms delay, PC/app tuning | $165–180 | [Parts Express](https://www.parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500) ([archive](https://web.archive.org/web/20260623143611/https://www.parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500)) |
| Rockford DSR1 | Processor only, 8 ch | $350–420 (over budget) | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-dsr1) ([archive](https://web.archive.org/web/20261026120327/https://www.soundoftristate.com/rockford-fosgate-dsr1)) |
| JBL MS-A1004 | 4 × 100 W DSP amp, 2 Ω | $550+ (over budget) | [JBL](https://support.jbl.com/product-registration/MS-A1004_.html) ([archive](https://web.archive.org/web/20250615183518/https://support.jbl.com/us/en/car-marine/car-electronics/car-electronics-amplifiers/car-electronics-amplifiers-4-channel/MS-A1004_.html)) |

No 2 Ω-stable 4-channel DSP amp with time alignment was found new for $300 or less. The cheap DSP
route is a **DSP-408 + one of the amps above**.

### US packages

| Package | Parts | ≈ Cost | What it fixes |
|---------|-------|--------|---------------|
| **A. Sub only** | TS-WX140DA or PWE-S8 + 8 AWG kit (+ DIY caps $50) | $290–380 | Real bass; caps take bass off the 4" speakers |
| **B. Sub + amp** | A + GM-DX874 (HPF at 80 Hz on all 4 speakers) + 8 AWG kit for both (one shared power run, distribution block) | $520–560 | Bass, clean power, proper high-pass |
| **C. Sub + amp + DSP** | B + DSP-408 between head unit and amp (sub fed from a DSP output) | $690–740 | All of the above + time alignment and per-speaker EQ |

B → C is an add-on later: the DSP slots in between the head unit and the amp without changing anything
else. Switch the head unit's internal amp off once an external amp drives the speakers.

## Option: replace the head unit instead of adding a DSP

Researched 2026-10-23, not verified on this car. A better head unit with **time alignment +
high-pass + sub low-pass** does everything the DSP-408 would do here. Its built-in amp stays weak
(14–22 W RMS), but with the bass sent to a sub that can be enough (see below).

US street prices from dealer listings; no Uruguay prices found (Mercado Libre UY needs a login).

| Unit | Amp RMS × 4 (CTA-2006) | Time alignment | HPF / sub LPF | Pre-outs | Wireless CP / AA | US price | Source |
|------|------------------------|----------------|---------------|----------|------------------|----------|--------|
| **Sony XAV-AX6000** | **20 W**, rated 4 Ω | Yes, per speaker in 1 cm steps, seat presets | Yes, front + rear, adjustable slope / yes | 3 pairs, 5 V | Both | ~$600 | [Sony help guide](https://helpguide.sony.net/ev/xav-ax60/v1/en/contents/TP1000661292.html) ([archive](https://web.archive.org/web/20250811165830/https://helpguide.sony.net/ev/xav-ax60/v1/en/contents/TP1000661292.html)), [Sonic Electronix](https://www.sonicelectronix.com/viewitem.php?id=197726) (**not archived**) |
| **Sony XAV-AX4000** | **20 W**, rated 4–8 Ω | Same as AX6000 | Same | 3 pairs (2 V or 5 V: sources conflict) | CarPlay wireless only; AA both | $400–600 | [Sony help guide specs](https://helpguide.sony.net/ev/xav-ax40/v1/en/contents/TP1000661344.html) ([archive](https://web.archive.org/web/20240813063750/https://helpguide.sony.net/ev/xav-ax40/v1/en/contents/TP1000661344.html)) |
| **Kenwood DMX5710S** | ~22 W (unverified) | Yes | Yes / yes | 2.5 V | Both | $380–460 | [Electronic Express](https://electronicexpress.com/catalog/567115/kenwood-dmx5710-6-8-in-digital-multimedia-bluetooth-receiver-with-apple-carplay-and-android-auto) ([archive](https://web.archive.org/web/20250306112213/https://www.electronicexpress.com/catalog/567115/kenwood-dmx5710-6-8-in-digital-multimedia-bluetooth-receiver-with-apple-carplay-and-android-auto)) |
| **Pioneer DMH-W3050NEX** | 14 W | Yes, presets + custom | 25–250 Hz, 6–24 dB/oct (forum, not manual) / yes; 3-way network mode | 3 pairs, 4 V | Both | $470–530 | [Team IU](https://teamiu.com/products/pioneer-dmh-w3050nex-digital-multimedia-receiver) ([archive](https://web.archive.org/web/20250207200721/https://teamiu.com/products/pioneer-dmh-w3050nex-digital-multimedia-receiver)), [Pioneer network mode](https://usa.pioneer/blogs/tech-tips/better-sound-staging-with-time-alignment-network-mode) ([archive](https://web.archive.org/web/20250911085949/https://usa.pioneer/blogs/tech-tips/better-sound-staging-with-time-alignment-network-mode)) |
| Pioneer DMH-W4660NEX | 14 W | Yes | Same as W3050NEX | 3 pairs, 4 V | Both | $500–600 | [Car Toys](https://www.cartoys.com/pioneer-dmh-w4660nex) ([archive](https://web.archive.org/web/20230207150838/https://www.cartoys.com/pioneer-dmh-w4660nex)) |
| Alpine iLX-507 | 18 W | 6-channel time correction | Yes / yes; 13-band parametric EQ per channel | 3 pairs, 4 V | Both | ~$650 | [Worldwide Stereo](https://www.worldwidestereo.com/products/alpine-ilx-507-7-hi-res-digital-multimedia-receiver) ([archive](https://web.archive.org/web/20250905161200/https://www.worldwidestereo.com/products/alpine-ilx-507-7-hi-res-digital-multimedia-receiver)) |
| Alpine iLX-W670 | 16 W | 6-channel time correction | Yes / yes | 3 pairs, 4 V | **Wired only** | $280–350 | [Alpine](https://alpine-usa.com/product/ilxw670s-alpine-7-inch-ultra-shallow-multimedia-receiver) ([archive](https://web.archive.org/web/20260206223859/https://www.alpine-usa.com/product/ilxw670s-alpine-7-inch-ultra-shallow-multimedia-receiver)), [spec sheet](https://content.abt.com/documents/175113/alpine-car-video-ILX-W670-spec-sheet.pdf) ([saved copy](references/alpine-ilx-w670-spec-sheet/README.md)) |
| JVC KW-M785BW | ~22 W (unverified) | Yes | Yes / yes | 3 pairs | Both | $370–480, stock patchy | [Crutchfield](https://www.crutchfield.ca/p_105KWM785B/JVC-KW-M785BW.html) ([archive](https://web.archive.org/web/20230603185111/https://www.crutchfield.ca/p_105KWM785B/JVC-KW-M785BW.html)) |

Over budget: Kenwood Excelon DMX958XR / DMX908S ($800–1,000; 22 W, 5 V, 3-way), Sony XAV-AX8500
($800–900), Pioneer DMH-WT7600NEX (~$1,300). Kenwood DMX4707S is superseded and wired-only.

All are rated 4 Ω; the Infinitys are 3 Ω. Common and usually fine, but the amp runs warmer and may
hit protection at high volume.

### Is a head unit's 20 W enough? (estimate)

- The "92 dB" is at 2.83 V, which into 3 Ω is about 2.7 W, so about 90 dB at 1 W / 1 m.
- 20 W per speaker: about 103 dB at 1 m. Four speakers in a small cabin: roughly **104–106 dB
  peaks** at the seat, **90–95 dB clean average** for music. CTA ratings are at 14.4 V, so expect
  about 1 dB less in practice.
- An external 4 × 50 W amp adds about 4 dB of headroom, but the speakers' 35 W rating caps the useful
  gain near 2.4 dB.
- **Verdict:** 20–22 W + an 80 Hz high-pass + a powered sub is enough for normal-to-loud listening.
  The high-pass matters more than the watts. An external amp buys cleaner peaks at high volume:
  optional, not needed.

### Head unit packages

| Package | Parts | ≈ US cost |
|---------|-------|-----------|
| **D. New head unit + sub** | Sony XAV-AX4000/AX6000 (or Kenwood DMX5710S) + powered slim sub + 8 AWG kit | $700–950 |
| **E. D + amp later** | D + Pioneer GM-DX874 when more headroom is wanted | +$220 |

Compared to C (BOSS + DSP-408 + amp + sub, ≈ $700): about the same money, fewer boxes, easy on-screen
tuning, wireless CarPlay and a better unit overall, but less tuning depth than the DSP-408 and less
power until an amp is added. Selling the BOSS offsets part of the cost.

**Decision input (owner, 2026-10-26):** a wireless Android Auto dongle is already in use, so wireless
phone support is no reason to replace the BOSS. That favours keeping it and going **B → C**
(amp with high-pass + sub now, DSP-408 when ready).

## Plan in progress (2026-10-27): local amp + DS18 DSP

Budget ceiling for amp + DSP: about $300–400. Leading idea: a 2 Ω-stable 4-channel amp bought in
Uruguay (for example the plain **Stetsom HL400.4**) + a **DS18 DSP4.8BTM** from eBay or the US.

**DS18 DSP4.8BTM, what people say** (thin: retailer reviews, no independent tests found,
2026-10-27): mostly positive; easy to learn for a first DSP; no dongle, Bluetooth built in; app runs
in landscape only; no volume knob (users got used to it); EQ points can't be dragged on the graph.
Specs: 4 RCA in up to 4 V (matches the BOSS), 8 out, time alignment 0–18.95 ms (entered as 0–6500 mm),
8-band parametric EQ per output plus input EQ (15 or 28 bands: sources differ), crossovers 6–48 dB/oct,
limiter, presets. App "DS18 DSP" for Android 7+ and iOS 13+; no desktop software (the iPad app is
"not verified" on macOS)
([Crutchfield reviews](https://www.crutchfield.com/p_408DSP48BT/Reviews/DS18-DSP4-8BTM.html),
[DS18](https://ds18.com/products/ds18-dsp4-8btm-4-channel-in-and-8-channel-out-digital-sound-processor-with-bluetooth),
[App Store](https://apps.apple.com/app/id1625944939), **not archived yet**).

**Wiring**

- BOSS front and rear RCA pre-outs → DSP inputs 1–4. BOSS sub pre-out → powered sub directly
  (keep its 80 Hz LPF there). Switch the BOSS internal amp off.
- DSP outputs 1–4 → amp → the four Infinitys. Outputs 5–8 spare.
- Amp crossover switches to **flat**: the DSP does the high-pass.
- Amp gain low: the Stetsom's RCA input is 200 mV sensitive, the DSP sends up to 3.5 V.
- Remote: BOSS Blue/White → DSP and amp turn-on.

**Tuning (Pixel phone + Mac)**

1. **Crossovers** (app on the Pixel): high-pass all four outputs at 80 Hz, Linkwitz-Riley 24 dB/oct.
2. **Gains:** BOSS at about 75% volume, a clean loud track, raise the amp gain until just below audible
   distortion; leave the DSP levels at 0 dB.
3. **Time alignment:** tape-measure from the driver's head (between the ears) to each speaker, in mm.
   Type the distances in; the app computes the delays (the farthest speaker gets 0).
4. **Levels:** match left and right; set the rears 3–6 dB below the fronts so they fill in without
   pulling the image back.
5. **EQ:** with a USB measurement mic (miniDSP UMIK-1) and **REW** (free, runs on the Mac) at the
   driver's head, measure each speaker, let REW's EQ tool suggest cuts, and type them into the
   DSP's parametric EQ. Mostly cuts, few boosts. Without the mic: tune by ear with familiar tracks.
6. Listen, adjust, save as a preset.

## Power and install

- **Alternator:** reported as **70 A** for 1987 and later (Bosch reman AL160X), about 25–30 A at
  idle, full output around 2000 rpm. Forum report, not verified: check the label
  ([PeachParts](https://www.peachparts.com/shopforum/3374870-post2.html) ([saved copy](references/pp-w123-alternator-post2/README.md)),
  [PeachParts](https://www.peachparts.com/shopforum/511545-post8.html) ([saved copy](references/pp-300e-battery-voltage-post8/README.md))). Fine for a system up to
  roughly 500 W RMS.
- **Power wire route:** the battery is on the passenger side in the engine bay. A rubber firewall
  grommet sits behind the glovebox, directly behind the battery. Run power down the passenger side,
  RCA and speaker wires down the driver side
  ([BenzWorld](https://www.benzworld.org/threads/running-4-gauge-thru-the-firewall.1307554/) ([partial archive](https://web.archive.org/web/20100317231135/http://www.benzworld.org/forums/w201-190-class/1307554-running-4-gauge-thru-firewall.html)),
  [PeachParts](https://www.peachparts.com/shopforum/car-audio-multimedia/120182-amplifier-power-where-run-power-thru-firewall.html) ([saved copy](references/pp-amp-power-thru-firewall/README.md))).
- Fuse within 30 cm of the battery. Many cheap 4 AWG kits are CCA (copper-clad aluminium): buy OFC.
- Ground: short run to bare body metal near the amp.
- Remote turn-on: from the head unit (wire colour in the head unit specs).
- Amp location: trunk side behind the trim, or a board in front of the fuel tank (as in the MBClub
  build).

## To measure on the car

- [ ] Rear seat cavity: depth, width, length, access plates, wiring
- [ ] Parcel shelf: first-aid-kit hole size; space below it in the trunk
- [ ] Front dash pod depth
- [ ] Alternator label (amp rating)

## Product sources

Retailer and maker pages used for the specs above.

| Product | Source |
|---------|--------|
| Infinity REF-4032cfx | [Crutchfield](https://www.crutchfield.ca/p_108R4032CX/Infinity-Reference-REF-4032cfx.html) ([archive](https://web.archive.org/web/20210401134322/https://www.crutchfield.ca/p_108R4032CX/Infinity-Reference-REF-4032cfx.html)) |
| Dayton DSP-408 | [Parts Express](https://parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500) ([archive](https://web.archive.org/web/20260623143611/https://www.parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500)) |
| Rockford R2-750X5 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-r2-750x5) ([archive](https://web.archive.org/web/20261026120542/https://www.soundoftristate.com/rockford-fosgate-r2-750x5)) |
| Rockford P3SD4-10 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-p3sd4-10) ([archive](https://web.archive.org/web/20261026120321/https://www.soundoftristate.com/rockford-fosgate-p3sd4-10)) |
| Rockford PS-8 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-ps-8) ([archive](https://web.archive.org/web/20261026115814/https://www.soundoftristate.com/rockford-fosgate-ps-8)) |
| JBL BassPro Nano | [JBL](https://support.jbl.com/gb/en/car-marine/car-speakers/car-speakers-subwoofers/SUBBPNANO-.html) ([saved copy](references/jbl-basspro-nano/README.md)) |
| Kicker KEY200.4 | [Worldwide Stereo](https://www.worldwidestereo.com/products/kicker-53key200-4-4-channel-full-range-smart-amplifier) ([archive](https://web.archive.org/web/20261026115802/https://www.worldwidestereo.com/products/kicker-53key200-4-4-channel-full-range-smart-amplifier)) |
| Kicker KEY500.1 | [Audio Intensity](https://audiointensity.com/products/kicker-key500-1-smart-mono-amplifier-500w-rms-class-d-car-audio-amplifier) ([archive](https://web.archive.org/web/20250715191549/https://audiointensity.com/products/kicker-key500-1-smart-mono-amplifier-500w-rms-class-d-car-audio-amplifier)) |
| Kicker L7T 10 | [Worldwide Stereo](https://www.worldwidestereo.com/products/kicker-46l7t104-10-solo-baric-l7t-shallow-mount-dual-4-ohm-voice-coil-subwoofer) ([archive](https://web.archive.org/web/20250613102414/https://www.worldwidestereo.com/products/kicker-46l7t104-10-solo-baric-l7t-shallow-mount-dual-4-ohm-voice-coil-subwoofer)) |
| JL Audio 10TW3-D4 | [Sound of Tri-State](https://www.soundoftristate.com/jl-audio-10tw3-d4) ([archive](https://web.archive.org/web/20261026115638/https://www.soundoftristate.com/jl-audio-10tw3-d4)) |
| Audison Prima AP4.9 bit | [Sound of Tri-State](https://www.soundoftristate.com/ap49bit) ([archive](https://web.archive.org/web/20261026120130/https://www.soundoftristate.com/ap49bit)) |
| AudioControl D-5.1300 | [AudioControl](https://audiocontrol.com/car-audio/power-amplifiers/d-51300/) ([archive](https://web.archive.org/web/20250513033220/https://www.audiocontrol.com/car-audio/power-amplifiers/d-51300/)) |
| Helix V EIGHT DSP MK2 | [Resonix](https://resonixsoundsolutions.com/products/helix-v-eight-dsp-mk2) ([archive](https://web.archive.org/web/20260208130542/https://resonixsoundsolutions.com/products/helix-v-eight-dsp-mk2)) |
| Alpine S2-S40C | [OnlineCarStereo](https://www.onlinecarstereo.com/CarAudio/p_91712_Alpine_S2-S40C.aspx) ([archive](https://web.archive.org/web/20260114103949/https://www.onlinecarstereo.com/CarAudio/p_91712_Alpine_S2-S40C.aspx)) |
| Focal ES 100 KE | [Sound of Tri-State](https://www.soundoftristate.com/focal-es100ke) ([archive](https://web.archive.org/web/20261026115615/https://www.soundoftristate.com/focal-es100ke)) |
| Resonix CLD Squares | [Resonix](https://resonixsoundsolutions.com/products/resonix-cld-squares-sound-deadening-material) ([archive](https://web.archive.org/web/20260524160457/https://resonixsoundsolutions.com/products/resonix-cld-squares-sound-deadening-material)) |
| Kilmat price | [Gilroy comparison](https://gilroyblackout.com/blog/sound-deadening-comparison-dynamat-kilmat-noico) (**not archived**) |
