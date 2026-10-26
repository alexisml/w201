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
([product page](https://www.bossaudio.com/products/791489129558)); its manual link opens the
BVCP9700A manual ([PDF](https://images.salsify.com/image/upload/s--1dxs8W49--/b7z7dm3kmvaqlrfivqhu.pdf)).

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
([PDF, hosted by a Norwegian dealer](https://bilradiospes.no/media/multicase/documents/infinity/h%c3%b8yttalere/infinity%20reference%20spesifikasjoner.pdf)).

| Spec | Value |
|------|-------|
| Size | 4" (100 mm) coaxial |
| Power | 35 W RMS, 105 W peak |
| Sensitivity | 92 dB @ 2.83 V |
| Frequency response | 75 Hz – 21 kHz |
| Impedance | **3.0 Ω** nominal |
| Tweeter | Edge-driven textile (retailers say 1/2" or 1": conflict) |
| Mounting depth | 1-7/8" (retailers: [Sonic Electronix](https://www.sonicelectronix.com/viewitem.php?id=198893), [OnlineCarStereo](https://www.onlinecarstereo.com/CarAudio/p_51208_Infinity_Reference_REF-4032CFX.aspx)) |
| Cutout | 3-5/8" or 3-11/16" (retailers disagree) |

The 3 Ω rating matters: any amp driving them should be **2 Ω stable**. Amps rated 4 Ω minimum
(for example the Kicker KEY200.4) are a poor match. Their low end stops around 75 Hz, so a high-pass
near 80 Hz costs them nothing.

## What the car offers

Researched, **not verified on this car**. Forum reports unless noted.

### Speaker locations

- **Front dash corners:** 4" (10 cm) is about the maximum. Owners break off the mounting tabs and
  press-fit or silicone the speaker in; the factory grille refits. Only low-profile tweeters fit. No
  published mounting depth: **measure before buying front speakers.**
  ([PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/20531-190e-front-speaker-dash-installation.html),
  [Crutchfield fit guide](https://www.crutchfield.com/carsystems/Mercedesbenz-190E-Stereos-and-Speakers.html))
- **Rear parcel shelf:** stock size is reported differently (4–4.5", 5.25"). A 6.5" round fits
  without cutting metal if the deck-board holes are trimmed; 6×9 needs some metal trimming or a riser
  ([PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/12246-190e-speaker-sizes.html),
  [PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/28856-6-5-sony-xplods-fit-perfectly-190-a.html)).
  Ours hold 4" speakers.
- **Doors:** door speakers appear in threads about 1990–93 cars, not 1988 US cars. Probably absent on
  ours ([BenzWorld](https://www.benzworld.org/threads/190e-six-speaker-system-door-speakers-not-working.506164/)).

### Subwoofer locations

| Location | What's known | Verdict |
|----------|--------------|---------|
| **Under the rear seat cushion** | Cushion unclips at the front edge and lifts out. A factory hole under the passenger-side rear seat is reported, used to route wires under the carpet ([BenzWorld](https://www.benzworld.org/threads/running-wires-to-trunk.1282917/)). **No W201 build with a sub here was found**, and no measurements. One unconfirmed claim of a fuel sender access plate under the bench: check before cutting anything | Possible; **measure first** |
| **Rear parcel shelf, free air** | Best documented W201 build: with the first-aid-kit carrier removed, the hole in the metal shelf fits an oval (about 13×8") bass driver. MDF sub-shelf under the carpet, invisible and reversible. Done in a 190 E 2.6 ([MBClub](https://forums.mbclub.co.uk/threads/thinking-of-sub-amp-combos.74466/), [Wayback](https://web.archive.org/web/20250116020821/https://forums.mbclub.co.uk/threads/thinking-of-sub-amp-combos.74466/)) | **Strong option**, needs a free-air (IB) driver and sealed trunk-to-cabin gaps |
| **Trunk box** | The fuel tank stands upright behind the rear backrest, so the seat doesn't fold and there's no pass-through except the first-aid pocket and grommets. One owner found trunk bass "isn't very crisp" ([BenzWorld](https://www.benzworld.org/threads/where-to-put-a-sub-in-a-190e-help.1307263/), [PeachParts](http://www.peachparts.com/shopforum/car-audio-multimedia/122012-sub-190e.html)) | Works, loses output |
| **Spare wheel well** | No W201 build found | Possible, untested |

**Seat cavity to measure** (when the cushion is out): depth from floor to cushion frame, width,
length, any access plates, wiring (seat heat, harness), floor shape.

### Mockup sizes for a fit test

Cut cardboard boxes to these outside sizes and try them in the cavity with the cushion back on.

**Powered slim subs** (amp built in, low tier). W × D × H from the makers unless noted. Add about
**40–50 mm at the connector end** for plugs and the wire bend (estimate: no maker publishes it).

| Model | Driver | mm | inches | Price | Source |
|-------|--------|----|--------|-------|--------|
| Pioneer TS-WX140DA | 8" | 200 × 280 × 70 | 7.9 × 11.0 × 2.76 | ~$280 | [Pioneer USA](https://usa.pioneer/products/ts-wx140da) |
| Alpine PWE-S8 | 8", 120 W | 230 × 341 × 71 | 9-1/16 × 13-7/16 × 2-13/16 | $245–400 | [Alpine](https://www.alpine-usa.com/product/pwe-s8) |
| JBL BassPro SL2 | 8" | 250 × 344 × 71 | 9-7/8 × 13-9/16 × 2-13/16 | ~$380, often out of stock | [JBL](https://mm.jbl.com/car-subwoofers/SUBBPSL2.html) |
| JBL BassPro Nano | 6×8" | 195 × 260 × 75 | 7-11/16 × 10-1/4 × 2-15/16 | ~$230, often out of stock | [JBL](https://support.jbl.com/gb/en/car-marine/car-speakers/car-speakers-subwoofers/SUBBPNANO-.html) |
| Kicker Hideaway HS8 | 8", 150 W | 238 × 352 × 79 | 9-3/8 × 13-7/8 × 3-1/8 | ~$330 | [Kicker](https://www.kicker.com/hideaway) |
| Kicker Hideaway HS10 | 10", 180 W | 249 × 356 × 81 | 9-7/8 × 14 × 3-1/8 | $320–400 | [Kicker](https://www.kicker.com/hideaway-hs10) |
| Rockford PS-8 | 8", 150 W | 238 × 365 × 83 | 9.4 × 14.4 × 3.3 | $350–390 | [Rockford](https://rockfordfosgate.com/products/details/ps-8) |

**Found for sale in Uruguay** (Mercado Libre UY, seen by the owner 2026-10-23; UY prices not
recorded yet). Mercado Libre UY needs a login to browse, so specs come from makers and other
retailers.

| Model | Driver / amp | mm (W × D × H) | Notes | Source |
|-------|--------------|----------------|-------|--------|
| **Helix U 10A** | 10", 180 W RMS (class AB) | 245 × 345 × **78** | RCA in 0.3–4 V (matches the head unit's 4 V pre-outs) + high-level in; LPF 50–150 Hz 24 dB/oct; subsonic 16 Hz; phase 0–180°; wired level remote; 25 A fuse; diecast aluminium. The **U 8A** (8") is listed with the same box size | [Audiotec Fischer](https://www.audiotec-fischer.de/en/helix/subwoofers/u-10a) |
| **JBL SW68A-MS** | 6×8", 100 W RMS | 290 × 210 × **70** | LPF 50–150 Hz, bass boost +12 dB, subsonic 20 Hz, level remote, 15 A fuse. The older SW68A-S sheet says 80 W, 290 × 210 × 72 | [Magazine Luiza](https://www.magazineluiza.com.br/produto/p/db17ed5j21/te/smsa/) (retailer), [JBL SW68A-S sheet](https://support.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw2a6648bd/pdfs/58033016_Spec%20sheet%20JBLSW68A.pdf) |
| **JBL SW8A-MS** | 8" + 2 passive radiators; sub 200 W RMS at 2 Ω **plus 2 × 100 W at 2 Ω full-range channels** | 345 × 245.5 × **74.6** | The two extra channels could power the front Infinitys (2 Ω rated, so the 3 Ω load is fine). **Not confirmed:** whether those channels have a high-pass. 35 A fuse, RCA in. Specs from Brazilian retailers only; JBL's support page lists none. Made since 2022 | [JBL support](https://support.jbl.com/sg/en/car-marine/car-speakers/car-speakers-subwoofers/58033017.html), [Mercado Livre BR](https://www.mercadolivre.com.br/caixa-amplificada-jbl-sw8a-ms-slim-sub-8pol-200wrms-3-canais-cor-preto/p/MLB27447712) |
| AIWA AW-10US | 10", 120 W RMS | 261 × 345 × **69** | USD 149 at aiwa.com.uy, **out of stock** 2026-10-23; remote included | [AIWA Uruguay](https://aiwa.com.uy/catalogo/subwoofer-activo-para-auto-120w-rms-aiwa-bajo-asiento-caja-aluminio-slim-10-pulgadas-aw-10us_AW-10US_AW-10US) |
| Pioneer TS-WX010A | 17 × 8 cm, 50 W | 230 × 116 × **70** | Footwell size, very small; LPF 50–125 Hz, phase. Seen via Tiendamia (import) at USD 199 | [Pioneer Latin America](https://pioneer-latin.com/producto/ts-wx010a/) |

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
| Rockford P3SD2-8 | 67.5 mm | not published (~20) | Ø 181 mm | 7 L (5.7–20) | **325 × 325 × ~124 mm** at 7 L | [Rockford](https://rockfordfosgate.com/products/details/p3sd2-8) |
| Kicker L7T 8 (square) | 70 mm | 24 mm | 188 mm square | 5.7–21 L | **325 × 325 × 130 mm** at 7 L | Kicker drawing 46L7T8-CSD |
| JL Audio 10TW3-D4 | 83 mm | not published (~25) | Ø 244 mm | 14.2 L (14–21) | **425 × 425 × ~138 mm** at 14 L | [Audio Intensity](https://audiointensity.com/products/jl-audio-10tw3-d4) |
| Rockford P3SD4-10 | 89 mm | not published | Ø 230 mm | 14 L (11–28) | **440 × 440 × ~145 mm** at 14 L | [Rockford](https://rockfordfosgate.com/products/details/p3sd4-10) |
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
     road noise ([BenzWorld](https://www.benzworld.org/threads/dynamat-project.1238120/),
     [BenzWorld](https://www.benzworld.org/threads/soundproofing-with-dynamat.1712601/),
     [BenzWorld](https://www.benzworld.org/threads/stereo-in-190e-rattle.1187777/)).

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
| **Pioneer TS-WX140DA** | 280 × 200 × 70 | 50 W RMS (170 max) | $280 list | 8×5.25". Wired remote with gain, LPF, phase, bass mode. RCA + high-level in. Out of stock at one dealer | [Pioneer USA](https://usa.pioneer/products/ts-wx140da) |
| **Alpine PWE-S8** | 340 × 230 × 70–75 | 120 W RMS | $245 (Best Buy marketplace) – $400 | 8" quad-coil. Price conflict between sellers | [Best Buy](https://www.bestbuy.com/site/9597106.p) |
| JBL BassPro Nano | 260 × 195 × 75 | 100 W RMS | $230 | 6×8", bass remote. Often out of stock | [Sound of Tri-State](https://www.soundoftristate.com/jbl-subbpnanoam) |
| JBL BassPro SL2 | 344 × 250 × 71–73 | 125 W RMS | $308 new, $250 refurbished | 8", remote. Just over budget new | [Worldwide Stereo](https://www.worldwidestereo.com/products/jbl-basspro-sl2-self-powered-8-low-profile-underseat-vehicle-subwoofer-system) |
| Pioneer TS-WX010A | 230 × 116 × 70 | small | $130–200 | Footwell size, least bass | [Pioneer USA](https://usa.pioneer/products/ts-wx010a) |

Over budget or too big: Kicker HS8 ($330, ~80 mm tall), Rockford PS-8 ($350+, 83–86 mm). Helix U 10A
and the JBL SW8A-MS / SW68A-MS aren't sold in the US (the Helix is about €289 in the EU).

### Filters: high-pass for the 4" speakers

The head unit can't high-pass the main speakers. Three ways to do it, cheapest first:

1. **DIY series capacitors** (passive, 6 dB/oct). C = 1 / (2π · f · R): for 80 Hz at 3 Ω about
   **663 µF**, made from 3 × 220 µF 100 V non-polarized caps in parallel (Parts Express, about $4
   each; 12 caps for 4 speakers ≈ $50) ([Parts Express](https://parts-express.com/220uF-100V-Non-Polarized-Capacitor-027-368)).
   Approximate: the speaker's impedance rises near resonance, so the real cutoff moves.
   **Store-bought bass blockers don't work here:** they cut far too high (Metra BB99 is 400 Hz at
   4 Ω, about 535 Hz at 3 Ω; PAC BB-1PR 300 Hz) ([Metra](https://www.metraonline.com/part/BB99)).
2. **A 4-channel amp with a built-in high-pass** (12 dB/oct, adjustable). Also gives real power.
   The best value step.
3. **A DSP** (any slope, plus time alignment and EQ). The full fix.

### Compact 4-channel amps (2 Ω stable, adjustable high-pass)

| Model | RMS × 4 at 4 Ω / 2 Ω | HPF | Size (W × H × D mm) | Price | Source |
|-------|----------------------|-----|---------------------|-------|--------|
| **Pioneer GM-DX874** | 100 / 150 (1 Ω stable) | 40–500 Hz | 264 × 60 × 200 | $220 | [Car Toys](https://www.cartoys.com/products/pioneer-gm-dx874) |
| **JL Audio JD400/4** | 75 / 100 | variable | not found | $280–300 | [Sound of Tri-State](https://www.soundoftristate.com/jl-audio-jd400-4) |
| Rockford R2-300X4 | 50 / 75 | 50–250 Hz | 257 × 49 × 173 | $280–310 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-prime-r2-300x4) |
| Kicker CXA360.4 | 65 / 90 | 50–200 Hz | 171 × 60 × 317 (class A/B, big) | $173–230 | [Worldwide Stereo](https://worldwidestereo.com/products/kicker-cxa360-4-4-channel-90-watt-class-a-b-amplifier) |
| Sony XM-S400D | 45 / 45 | **fixed 120 Hz** (a bit high) | very small | $150 | [Car Toys](https://cartoys.com/products/sony-xm-s400d) |

Avoid: **Kicker KEY200.4** ($240, has DSP and auto-EQ but is **4 Ω minimum**), Rockford PBR300X4
(4 Ω only, discontinued). Discontinued: Kenwood X302-4, JBL Club A754.

### DSP

| Model | What | Price | Source |
|-------|------|-------|--------|
| **Dayton Audio DSP-408** | Processor only: 4 in / 8 out RCA, crossovers, 10-band PEQ per output, 0–8.1 ms delay, PC/app tuning | $165–180 | [Parts Express](https://www.parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500) |
| Rockford DSR1 | Processor only, 8 ch | $350–420 (over budget) | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-dsr1) |
| JBL MS-A1004 | 4 × 100 W DSP amp, 2 Ω | $550+ (over budget) | [JBL](https://support.jbl.com/product-registration/MS-A1004_.html) |

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
| **Sony XAV-AX6000** | **20 W**, rated 4 Ω | Yes, per speaker in 1 cm steps, seat presets | Yes, front + rear, adjustable slope / yes | 3 pairs, 5 V | Both | ~$600 | [Sony help guide](https://helpguide.sony.net/ev/xav-ax60/v1/en/contents/TP1000661292.html), [Sonic Electronix](https://www.sonicelectronix.com/viewitem.php?id=197726) |
| **Sony XAV-AX4000** | **20 W**, rated 4–8 Ω | Same as AX6000 | Same | 3 pairs (2 V or 5 V: sources conflict) | CarPlay wireless only; AA both | $400–600 | [Sony help guide specs](https://helpguide.sony.net/ev/xav-ax40/v1/en/contents/TP1000661344.html) |
| **Kenwood DMX5710S** | ~22 W (unverified) | Yes | Yes / yes | 2.5 V | Both | $380–460 | [Electronic Express](https://electronicexpress.com/catalog/567115/kenwood-dmx5710-6-8-in-digital-multimedia-bluetooth-receiver-with-apple-carplay-and-android-auto) |
| **Pioneer DMH-W3050NEX** | 14 W | Yes, presets + custom | 25–250 Hz, 6–24 dB/oct (forum, not manual) / yes; 3-way network mode | 3 pairs, 4 V | Both | $470–530 | [Team IU](https://teamiu.com/products/pioneer-dmh-w3050nex-digital-multimedia-receiver), [Pioneer network mode](https://usa.pioneer/blogs/tech-tips/better-sound-staging-with-time-alignment-network-mode) |
| Pioneer DMH-W4660NEX | 14 W | Yes | Same as W3050NEX | 3 pairs, 4 V | Both | $500–600 | [Car Toys](https://www.cartoys.com/pioneer-dmh-w4660nex) |
| Alpine iLX-507 | 18 W | 6-channel time correction | Yes / yes; 13-band parametric EQ per channel | 3 pairs, 4 V | Both | ~$650 | [Worldwide Stereo](https://www.worldwidestereo.com/products/alpine-ilx-507-7-hi-res-digital-multimedia-receiver) |
| Alpine iLX-W670 | 16 W | 6-channel time correction | Yes / yes | 3 pairs, 4 V | **Wired only** | $280–350 | [Alpine](https://alpine-usa.com/product/ilxw670s-alpine-7-inch-ultra-shallow-multimedia-receiver), [spec sheet](https://content.abt.com/documents/175113/alpine-car-video-ILX-W670-spec-sheet.pdf) |
| JVC KW-M785BW | ~22 W (unverified) | Yes | Yes / yes | 3 pairs | Both | $370–480, stock patchy | [Crutchfield](https://www.crutchfield.ca/p_105KWM785B/JVC-KW-M785BW.html) |

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

## Power and install

- **Alternator:** reported as **70 A** for 1987 and later (Bosch reman AL160X), about 25–30 A at
  idle, full output around 2000 rpm. Forum report, not verified: check the label
  ([PeachParts](https://www.peachparts.com/shopforum/3374870-post2.html),
  [PeachParts](https://www.peachparts.com/shopforum/511545-post8.html)). Fine for a system up to
  roughly 500 W RMS.
- **Power wire route:** the battery is on the passenger side in the engine bay. A rubber firewall
  grommet sits behind the glovebox, directly behind the battery. Run power down the passenger side,
  RCA and speaker wires down the driver side
  ([BenzWorld](https://www.benzworld.org/threads/running-4-gauge-thru-the-firewall.1307554/),
  [PeachParts](https://www.peachparts.com/shopforum/car-audio-multimedia/120182-amplifier-power-where-run-power-thru-firewall.html)).
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
| Infinity REF-4032cfx | [Crutchfield](https://www.crutchfield.ca/p_108R4032CX/Infinity-Reference-REF-4032cfx.html) |
| Dayton DSP-408 | [Parts Express](https://parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500) |
| Rockford R2-750X5 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-r2-750x5) |
| Rockford P3SD4-10 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-p3sd4-10) |
| Rockford PS-8 | [Sound of Tri-State](https://www.soundoftristate.com/rockford-fosgate-ps-8) |
| JBL BassPro Nano | [JBL](https://support.jbl.com/gb/en/car-marine/car-speakers/car-speakers-subwoofers/SUBBPNANO-.html) |
| Kicker KEY200.4 | [Worldwide Stereo](https://www.worldwidestereo.com/products/kicker-53key200-4-4-channel-full-range-smart-amplifier) |
| Kicker KEY500.1 | [Audio Intensity](https://audiointensity.com/products/kicker-key500-1-smart-mono-amplifier-500w-rms-class-d-car-audio-amplifier) |
| Kicker L7T 10 | [Worldwide Stereo](https://www.worldwidestereo.com/products/kicker-46l7t104-10-solo-baric-l7t-shallow-mount-dual-4-ohm-voice-coil-subwoofer) |
| JL Audio 10TW3-D4 | [Sound of Tri-State](https://www.soundoftristate.com/jl-audio-10tw3-d4) |
| Audison Prima AP4.9 bit | [Sound of Tri-State](https://www.soundoftristate.com/ap49bit) |
| AudioControl D-5.1300 | [AudioControl](https://audiocontrol.com/car-audio/power-amplifiers/d-51300/) |
| Helix V EIGHT DSP MK2 | [Resonix](https://resonixsoundsolutions.com/products/helix-v-eight-dsp-mk2) |
| Alpine S2-S40C | [OnlineCarStereo](https://www.onlinecarstereo.com/CarAudio/p_91712_Alpine_S2-S40C.aspx) |
| Focal ES 100 KE | [Sound of Tri-State](https://www.soundoftristate.com/focal-es100ke) |
| Resonix CLD Squares | [Resonix](https://resonixsoundsolutions.com/products/resonix-cld-squares-sound-deadening-material) |
| Kilmat price | [Gilroy comparison](https://gilroyblackout.com/blog/sound-deadening-comparison-dynamat-kilmat-noico) |
