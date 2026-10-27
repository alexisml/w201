# Audio: current setup and upgrade plan

**System:** interior / electrical
**Status:** planned

The factory radio and speakers are gone. This note has what's in the car now, the plan, and how to
wire and tune it. Everything researched along the way (budget tiers, US and Uruguay options, products
ruled out) is in [Audio: options researched](audio-options.md).

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


## Plan

Goal: a powered slim sub plus an amp and a DSP, so the 4" speakers get a high-pass at 80 Hz, real
power and time alignment.

- **Sub:** a powered slim unit on the BOSS sub pre-out (its own LPF at 80 Hz). Model picked after the
  seat-cavity fit test: see [Mockup sizes](#mockup-sizes-for-a-fit-test).
- **Amp + DSP:** budget about US$300–400; amp **stable at 2 Ω** (speakers are 3 Ω).
- **Ruled out** (details in [options](audio-options.md)): Genius GDSP-15404A (4 Ω, Windows only, 2 RCA
  inputs), Stetsom STX 2436 and Taramps PRO 2.4 BT (2 inputs), Kicker KEY200.4 (4 Ω minimum, would need
  resistors), Alpine OPTIM6 combos (~$700), a new head unit (the wireless Android Auto dongle already
  covers what it would add).

### Amp + DSP shortlist

**Top pick (owner, 2026-10-27): DS18 DSP4.8BTM**, with the **Helix DSP Mini MK2** as the alternative;
either one plus a local 2 Ω-stable 4-channel amp. The Stetsom DSPlayer stays as the budget fallback.

Requirement: **4 DSP inputs** (front and rear from the BOSS), so the head unit's
balance and fader keep working. 2-input processors (Taramps PRO 2.4 BT, Stetsom STX 2436 / STX 2448)
are out; most Brazilian processors are 2-input.

| Option | Boxes | Tuning | ≈ Cost (amp + DSP) |
|--------|-------|--------|--------------------|
| Helix DSP Mini MK2 (UY) + local 2 Ω amp: **alternative** | 2 | Windows laptop (PC-Tool) | ~$400 + amp (HL400.4 about US$135 on Mercado Libre UY) |
| **DS18 DSP4.8BTM** (imported) + local 2 Ω amp: **top pick** | 2 | Phone app (Pixel) | ~$320 + amp |
| Stetsom HL400.4 DSPlayer (amp + DSP in one, budget fallback; 4 inputs, use the speaker-wire inputs: its RCA takes 1 V max) | 1 | Phone app | ~$110 US (more after import) |

A Windows laptop is available, so the Helix's Windows-only tuning is workable. The wiring and tuning
steps below apply to all three (tool: PC-Tool, the DS18 app or the Stetsom app); REW and a UMIK-1
mic run on Windows or Mac.

### Choosing the amp

Any brand; what matters with the DSP and the 3 Ω Infinitys:
- 4 channels, **stable at 2 Ω** (the speakers are 3 Ω); avoid 4 Ω-minimum amps.
- About **50–100 W RMS per channel** (the speakers take 35 W RMS; more only adds headroom, set the
  gain accordingly).
- **RCA input that accepts the DSP's output level** (up to about 6 V on the Helix, 3.5 V on the DS18): an input sensitivity range
  reaching 4–8 V is ideal. A very sensitive input (like the Stetsom's 200 mV) still works with the
  gain near minimum, but leaves little adjustment.
- Crossover that can be set to **flat/off** (the DSP does the filtering).
- Class D and small, for under a seat or behind trim; a real RMS rating from a known brand.


### Wiring

- BOSS front and rear RCA pre-outs → DSP inputs 1–4. BOSS sub pre-out → powered sub directly
  (keep its 80 Hz LPF there). Switch the BOSS internal amp off.
- DSP outputs 1–4 → amp → the four Infinitys. Outputs 5–8 spare.
- Amp crossover switches to **flat**: the DSP does the high-pass.
- Amp gain low: the Stetsom's RCA input is 200 mV sensitive, the DSP sends up to 3.5 V.
- Remote: BOSS Blue/White → DSP and amp turn-on.


### Cables and parts (DS18 + amp + powered sub)

The DS18 has RCA jacks for its 4 inputs and 8 outputs (high-level inputs also possible), runs on
10–15 V at 300 mA max, and is set up over Bluetooth. Box contents (power harness?) not published: check
on arrival. Lengths assume the DSP and amp under the front passenger seat and the sub under the rear
seat: measure first.

| Item | Qty | Notes |
|------|-----|-------|
| RCA cable, stereo pair, ~2 m | 2 | BOSS front and rear pre-outs → DSP inputs 1–4 |
| RCA cable, stereo pair, ~0.5 m | 2 | DSP outputs 1–4 → amp inputs |
| RCA cable, ~4–5 m (mono, or a pair with one side used) | 1 | BOSS sub pre-out → powered sub |
| Amp power kit, 8 AWG OFC | 1 | Power and ground cable, fuse holder + fuse near the battery (size to the amp), ring terminals, grommet |
| Distribution block (fused) | 1 | Splits the 8 AWG feed to the amp, the sub and the DSP |
| 18 AWG wire + 1–2 A inline fuse | ~1 m | DSP power from the distribution block |
| Remote wire, 18 AWG | ~5 m | BOSS Blue/White → DSP, amp and sub turn-on |
| Speaker wire, 16 AWG | ~4 runs | Amp outputs → speakers. Easiest: back to the dash and into the car's speaker leads where the BOSS speaker outputs connect now (also where a bypass would go) |
| Short ground straps | 2–3 | DSP, amp and sub to bare body metal near them |

Run RCA and speaker cables down the driver side, power down the passenger side (see
[Power and install](#power-and-install)).

### Bypass

A way to run the speakers straight from the BOSS if the amp or
DSP fails, and to compare tuned vs untuned. Nothing ready-made for this exact use was found; it's a
simple DIY build (our design, not tested):

- **Relay switch-over:** 4 DPDT relays (or 8 SPDT), 12 V coil, contacts rated about 5 A or more. Each
  speaker's + and − go to the relay common; normally-closed contacts → BOSS speaker output (bypass);
  normally-open → amp output (normal). Coils fed from the remote turn-on line **through a toggle
  switch** under the dash: switch off (or amp/DSP not powered) = bypass, the BOSS drives the speakers.
  Fail-safe by design.
- **Switch both + and − of every channel.** The BOSS and most class-D amps have bridged outputs: never
  join speaker negatives together or to ground.
- **Keep the BOSS internal amp on** so bypass works (its outputs sit unloaded in normal mode, which is
  fine). Switching it off only matters for heat or noise.
- **Simpler manual version:** connectors at the amp end of the speaker wiring, plus a jumper plug that
  joins the BOSS speaker wires straight to the speaker lines. Swap plugs to bypass.
- Same relay approach as the [power antenna controller ideas](../electrical/power-antenna-controller/README.md).


### Tuning

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
