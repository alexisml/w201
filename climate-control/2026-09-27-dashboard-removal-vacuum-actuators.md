# 2026-09-27 — Dashboard removal & broken HVAC vacuum actuators

**Mileage:** 
**Topic:** climate-control
**Status:** open

## Symptom

HVAC vacuum system problems. Dashboard removed to get at the heater box actuators.
_(Add details of the original symptoms here.)_

## Procedure followed

Removed the dashboard by following the Pelican Parts guide:

- [Mercedes-Benz 190E Dashboard Removal and Replacement](https://www.pelicanparts.com/techarticles/Mercedes-190E/43-BODY-Removing_the_Dashboard/43-BODY-Removing_the_Dashboard.htm)
  ([archived, text only](https://web.archive.org/web/20170810023426/http://www.pelicanparts.com/techarticles/Mercedes-190E/43-BODY-Removing_the_Dashboard/43-BODY-Removing_the_Dashboard.htm),
  [saved copy](references/pelican-190e-removing-the-dashboard/))

Prerequisites from the guide: remove the instrument cluster and center console first, then disconnect the battery.
Tip from BenzWorld (MSGGrunt): removing the **steering wheel** makes it much easier to reinstall the dash.

## Vacuum diagram

![W201 HVAC vacuum diagram](images/hvac-vacuum-diagram-w201.png)

Vacuum elements shown in the diagram (circled):

| Item | Element | Strokes (from switchover valve) |
|------|---------|---------------------------------|
| 37 | Blend air flaps ("cold") | single |
| 38 | Defroster outlet flaps ("closed") | **two**: 12.7 large / 12.6 short |
| 39 | Legroom flaps ("closed") | single (12.8) |
| 40 | Fresh air / recirculating air flap ("open"), on evaporator housing 34 | **two**: 12.10 large / 12.9 short |
| 41 | Heater valve ("closed"), with orifice 41a | single |

## Part list for this car

These four part numbers are what the EPC gives for a 1992 190E 2.3 8V. ECS Tuning ran that car's VIN in the
[chassis number thread](references/bw-chassis-number-defrost/), and it matches the parts removed from this car.
A fifth element sits in the center of the heater case. It has no part number and only comes with a new heater case.

| # | MB part number | Function | Type | Behr / Hella cross-ref | Rebuild option |
|---|----------------|----------|------|------------------------|----------------|
| a | **201 800 08 75** | TBD (see below) | Single diaphragm, round | Label on the removed part reads **9063100055** (Behr 90.631.00.055?), dated ?/05/88 | Single-stage diaphragm, **28 mm shallow cup** (Klimakit), probably the same as (c) |
| b | **000 800 87 75** | Defroster nozzle flap (item 38) | **Oval, dual-mode**: 2 stacked chambers, 2 vacuum ports, ½ open / full open | WOCO 40 0104 (molded on the housing, confirmed on the removed part). Hella 6NV 351 329-041 / 351329041 (per BenzWorld, which also gives the older MB number 201 800 05 75) | Use the seals from **2× 126 800 14 75** (same rubber, different color; Facebook 190E group) |
| c | **201 800 03 75** | Legroom flap (item 39) | Single diaphragm, round | Behr 351329721 | Single-stage diaphragm, 28 mm (Klimakit); 9zwo8 diaphragm lists A2018000375 as compatible |
| d | **201 800 00 75** | Main air flap = fresh/recirc (item 40, most likely) | **Double diaphragm** | Behr 90.622.00.375. Hella 6NV 351 329-301 / 351329301 | Dual-stage diaphragm cartridge, probably **clip style** (Klimakit) |

### Notes & open questions

- **Which item is (a)?** Items 38, 39 and 40 are accounted for by b, c and d. Item 38 is dual-stroke,
  matching (b)'s dual mode. Item 40 is dual-stroke, matching (d)'s double diaphragm and Klimakit's
  "defrost and fresh air flap" dual-stage cartridge. That leaves (a) as either **37 (blend air
  "cold")** or **41 (heater valve)**, and the other one is the unnumbered element in the heater case.
  **Where (a) was mounted when removed settles this.**
- MSGGrunt's 2014 parts list says "#37, #38, #39, #41 are replaceable, #40 only with the heater housing".
  That was based on a different, older diagram whose numbering probably doesn't match this one. Don't
  trust the item numbers across diagrams.
- Behr label number: this entry records what the photo shows (9063100055). An earlier note had
  906310055. Check it against the physical label.
- **000 800 87 75 is no longer made (NLA).** ECS and Norsider list their parts as unavailable. Rebuilding is the way forward.

![Actuator (a) 201 800 08 75, Behr, next to caliper set to ~28 mm](images/2026-09-27-actuator-a-201-800-08-75-behr.jpg)

![Actuator (b) 000 800 87 75, defroster, WOCO 40 0104](images/2026-09-27-actuator-b-000-800-87-75-woco-40-0104.jpg)

Actuator (b), as removed: a rectangular/oval housing with **two stacked diaphragm chambers** and **two vacuum
ports** (one per stage), molded **"40 0104"** (WOCO part number). This matches the dual-mode defroster element
(½ open / full open) and the rebuild route of 2× 126 800 14 75 diaphragms (one per chamber).

### Related parts (from the BenzWorld parts list, not yet verified for this car)

| Part                                   | Number          |
|----------------------------------------|-----------------|
| Switchover valve with vacuum lines     | 201 800 05 78   |
| Push-button climate control unit       | 201 830 09 85 / 88 (MSGGrunt's final fix: rebuilt 201 830 08 85) |
| Heater core                            | 002 835 54 01   |
| Heater control valve (by battery)      | 000 830 57 84   |
| Blower motor                           | 201 820 06 42   |
| Blower speed switch                    | 201 820 17 10   |
| In-car temp sensor blower              | 000 830 19 08   |
| Air mixing flap resistor ("flap rheostat"), a common failure | 201 821 02 60 |

While the dash is out, also replace all rubber vacuum elbows/connectors and leak-test the hard lines.
MSGGrunt replaced all 4 pods, but the system only worked after a **rebuilt push-button control unit**,
so test the control unit and switchover valve too.

## Fix

_Pending._

## To do

- [ ] Record where (a) 201 800 08 75 was mounted → settles 37 vs 41
- [ ] Double-check the Behr number on (a)'s label
- [ ] Measure the diaphragm cups of (a) and (c) to confirm the 28 mm shallow type
- [ ] Source 2× 126 800 14 75 for the (b) defroster rebuild
- [ ] Confirm the Klimakit dual-stage linkage type for (d) (clip vs eyelet)
- [ ] Vacuum-test each actuator and hard line before reassembly
- [ ] Test the push-button control unit + switchover valve
- [ ] Photos of each actuator in place → `images/`

## Sources

Every link has a saved copy: an Internet Archive link, or a full copy in the private archive (available on request). Each `references/` folder describes what's saved.

**Part identification / cross-reference**
- BenzWorld: [Chassis Number Help For HVAC Defrost Vacuum Actuator](https://www.benzworld.org/threads/chassis-number-help-for-hvac-defrost-vacuum-actuator.1948394/) ([saved](references/bw-chassis-number-defrost/)): source of the 4-part list and ECS's VIN lookup
- BenzWorld: [Climate Control, HVAC Restoration Parts List](https://www.benzworld.org/threads/climate-control-hvac-restoration-parts-list.1945626/) ([saved](references/bw-hvac-parts-list/))
- BenzWorld: [Vacuum Element - Defroster Nozzle Flap](https://www.benzworld.org/threads/vacuum-element-defroster-nozzle-flap.3004657/) ([saved](references/bw-defroster-nozzle-flap/)): includes a photo of all actuators with prices
- Pelican Parts: [201 800 00 75](https://www.pelicanparts.com/More_Info/2018000075.htm) ([archived 2023](https://web.archive.org/web/20230210040618/https://www.pelicanparts.com/More_Info/2018000075.htm)) · [201 800 03 75](https://www.pelicanparts.com/More_Info/2018000375.htm) ([saved](references/pelican-2018000375/)) · [201 800 08 75](https://www.pelicanparts.com/More_Info/2018000875.htm) ([saved, images only](references/pelican-2018000875/)) · [000 800 87 75](https://www.pelicanparts.com/More_Info/0008008775.htm) ([saved, images only](references/pelican-0008008775/))
- ECS Tuning: [000 800 87 75](https://www.ecstuning.com/b-genuine-mercedes-benz-parts/vacuum-element/0008008775/) ([saved](references/ecs-0008008775/))
- Norsider (used): [201 800 00 75 / Behr 90.622.00.375](https://autopecas.norsider.pt/en/en-heater-blower-flap-actuator-mercedes-190-201-from-1982-1983-1984-1985-1986-1987-1988-1989-1990-1991-1992-1993-2018000075-behr-90-622-00-375-199464) ([saved](references/norsider-2018000075/))
- NIParts: [201 800 00 75 → Hella 351329301](https://www.niparts.com/s_242A8B/2018000075.html) ([saved](references/niparts-2018000075/))
- DRIVE2: [A 201 800 00 75](https://www.drive2.ru/parts/mercedes/a2018000075/CUuWQEAAalk) ([saved](references/drive2-a2018000075/))
- Autoplicity: [Behr 201 800 03 75](https://autoplicity.com/3278849-behr-mercedes-201-800-03-75-vacuum-element): **not archived**. No Wayback snapshot, and the page could not be saved.

**Rebuild parts**
- Facebook, Mercedes 190E Owners Club: [How to repair the defroster flap vacuum element](https://www.facebook.com/groups/TheMercedes190Group/posts/10169573489405441/) ([saved, partial](references/fb-190group-defrost/)): use 2× 126 800 14 75 seals
- Klimakit: [Single-stage diaphragms](https://klimakit.com/product/universal-single-stage-vacuum-actuator-diaphragm/) ([saved](references/klimakit-single-stage/)) · [Dual-stage cartridge](https://klimakit.com/product/dual-stage-vacuum-actuator-diaphragm-cartridge-assembly/) ([saved](references/klimakit-dual-stage/))
- 9zwo8: [Replacement diaphragm vacuum can](https://9zwo8.com/en/products/replacement-diaphragm-vacuum-can-mercedes-benz) ([saved](references/9zwo8-diaphragm/))
