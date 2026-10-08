# Power antenna controller idea: Arduino Uno + Infineon PROFET+2 12V shield

**System:** electrical
**Status:** untested idea

> **Untested idea.** This is a design dump, not a finished or proven build. Nothing here has been
> built or run yet. The wiring comes from documentation and forum reports, and the firmware has not
> been compiled. Bench-test the antenna first (see the [README](README.md#bench-test-the-antenna-first))
> and check everything against your own parts.

An Arduino Uno with Infineon's PROFET+2 12V Arduino Shield. The shield's switches are
automotive-grade smart high-side switches: they protect themselves against short circuits, overload
and overheating, and they measure the load current, so no relays or separate current sensor are
needed. How the controller behaves, the car wiring and the bench tests are in the
[README](README.md).

Standby draw with the radio off: roughly 0.3 mA, from the shield's battery voltage divider and the
switches' standby current. The Arduino itself is fully off.

## Parts

Example parts are given; equivalents work.

| # | Part | What for | Example |
|---|---|---|---|
| 1 | **Arduino Uno R3** (or a clone) | The brain | Arduino Uno Rev3 |
| 2 | **Infineon PROFET+2 12V Arduino Shield**, BTS7008-1EPP version | 4 automotive-grade high-side switches (11 A each) with current measurement, overload and short-circuit protection, 33 V TVS on the supply | SHIELD_BTS7008-1EPP (the BTS7002/7004/7006 versions also work; set `K_ILIS` in the firmware) |
| 3 | **Optocoupler board, 4 channels, 12 V input** | Reads the 12 V car signals safely at 5 V | "PC817 4-channel optocoupler isolation board, 12 V" |
| 4 | **5 V step-down regulator, 36 V input** | Powers the Arduino from 12 V | Pololu D24V10F5 (5 V, 1 A) |
| 5 | 2 × rectifier diodes, 3 A or more | Lets either the radio wire or the hold output power the regulator | 1N5408 or SR560 (Schottky) |
| 6 | TVS diode, ~22 V | Absorbs spikes at the regulator input | 1.5KE22A (through-hole) |
| 7 | Inline blade fuse holder + 5 A fuse | Protects the +12 V permanent feed | Any automotive inline holder |
| 8 | Waterproof box with cable glands | Housing in the trunk | ABS box, IP65, about 150 × 100 × 70 mm |
| 9 | Lever connectors or screw terminals | Wiring inside the box | WAGO 221 |
| 10 | Wire: 1 mm² (red, brown) for power and ground; 0.5 mm² for signals | | Automotive (FLRY) wire |
| 11 | Optional: matching 6-pin plug from an old antenna | Plugs into the car harness without cutting it | Harness side is housing `A 011 545 51 28` (EPC 82.345) |

Tools: soldering iron, heat-shrink, multimeter, a USB cable for the Arduino, a 12 V bench supply
(2–3 A) or a car battery for testing.

## Shield facts used here

From Infineon's user manual and example code for the shield:

| Item | Value |
|---|---|
| Supply (BAT+) | 4.1–28 V working range; 33 V TVS (SMCJ33CA) on board |
| Control inputs | 3.3 V or 5 V logic: IN1 = D9, IN2 = D10, IN3 = D11, IN4 = D3 |
| Current sense | U1 or U2 on **A2**, U3 or U4 on **A3**; pick with DEN1+3 = **D6** or DEN2+4 = **D8**. Sense resistor 1 kΩ. Needs an Arduino whose analog inputs take 5 V (the Uno does) |
| Current ratio kILIS (typical) | BTS7002: 22700, BTS7004: 20000, BTS7006: 17700, BTS7008: 14500 |
| Battery voltage | A1, divider 47 kΩ / 10 kΩ |
| Other pins in use | LEDs on D4, D5, D12, D13; OLOFF on D7; optional push button on D2 / A0 (not fitted by default) |
| Jumper J1 | Fitted: the shield's BAT+ also powers the Arduino. **Leave it off here**, so the Arduino can switch itself off |

Load current = (voltage on A2) ÷ 1 kΩ × kILIS. With the Uno's internal 1.1 V reference and the
BTS7008, one ADC step is about 16 mA and full scale about 16 A. That's plenty for an antenna motor
(a few amps). The ratio is less accurate at low currents, which is fine because the firmware only
compares against thresholds you set from your own readings.

## Wiring inside the box

Car-side colours and pins: see the [README](README.md#car-side-wiring-original-6-pin-antenna-plug).

```
 +12 V permanent (pin 2) ── fuse 5 A ── shield BAT+          shield GND ── ground bus
                                         │
                                         ├─ OUT1 (U1, D9)  ───────────────► antenna +12 V (red)
                                         ├─ OUT3 (U3, D11) ───────────────► antenna trigger
                                         └─ OUT2 (U2, D10) ──►|── regulator IN (+)
                                                            diode 1
 radio on (pin 5) ──┬──►|── regulator IN (+)        TVS 22 V from regulator IN (+) to ground
                    │  diode 2                      regulator GND ── ground bus
                    └── optocoupler IN1+            regulator 5 V OUT ── Arduino 5V pin

 switch (pin 4) ───── optocoupler IN2+
 switch (pin 1) ───── optocoupler IN3+
 optocoupler IN- (all) ── ground bus

 ground (pin 6) ── ground bus ── Arduino GND, optocoupler input ground, antenna ground

 Arduino 5V  ── optocoupler output VCC
 Arduino GND ── optocoupler output GND
 optocoupler OUT1 / OUT2 / OUT3 ── Arduino D2 / A4 / A5
 shield jumper J1: OFF
```

Notes:

- The shield stacks on the Uno, so D2–D13 and A0–A5 are reached through the shield's headers.
  Solder the optocoupler wires to the shield's free header pins (D2, A4, A5).
- The two diodes let the radio wire power the regulator, but stop the hold output from pushing
  +12 V back into the radio wire.
- Don't plug in USB while the box runs from the car, since the regulator feeds the Uno's 5 V pin
  directly. For programming, unplug the car side (or the regulator) first.
- Keep the feed and ground wires to the antenna short and 1 mm² or thicker.

## Programming

1. Install the Arduino IDE. No extra libraries are needed.
2. Set the settings at the top of the sketch below, then follow the [bench test](README.md#test-the-controller-on-the-bench) (`K_ILIS` for your shield version).
3. Upload over USB. Open the serial monitor at 115200 baud.

## Firmware

```cpp
// Power antenna controller: drives a 3-wire aftermarket antenna like the original
// Mercedes semi-automatic antenna (switch MAX / UP / AUTO / DOWN / OFF).
// Arduino Uno + Infineon PROFET+2 12V Arduino Shield + PC817 optocoupler board.
// Not tested yet: bench-test first and adjust the settings below.

#include <EEPROM.h>

// ---------- shield pins (from Infineon's documentation) ----------
const int PIN_FEED  = 9;   // U1 / OUT1: +12 V to the antenna (current read on A2)
const int PIN_HOLD  = 10;  // U2 / OUT2: keeps the Arduino powered
const int PIN_TRIG  = 11;  // U3 / OUT3: trigger to the antenna
const int PIN_DEN13 = 6;   // diagnosis enable U1+U3: puts U1's current on A2
const int PIN_DEN24 = 8;   // diagnosis enable U2+U4: kept off
const int PIN_IS    = A2;  // current sense of U1
const int LED_UP = 4, LED_DOWN = 5;

// ---------- inputs from the optocoupler board ----------
const int PIN_R = 2;       // radio on (car pin 5)
const int PIN_A = A4;      // switch AUTO/UP/MAX (car pin 4)
const int PIN_U = A5;      // switch UP/MAX (car pin 1)
const int INPUT_ON = LOW;  // optocoupler output goes LOW when 12 V is present

// ---------- settings: adjust after the bench test ----------
const float K_ILIS = 14500;          // BTS7008: 14500, BTS7006: 17700, BTS7004: 20000, BTS7002: 22700
const float R_IS = 1000;             // sense resistor on the shield (ohms)
const float VREF = 1.1;              // internal ADC reference (volts)
const float AUTO_HEIGHT = 0.5;       // AUTO height, as a fraction of full travel
const float RUN_MA = 300;            // above this the motor is running
const float STALL_MA = 2500;         // above this the mast has hit an end stop
const uint32_t STALL_MS = 150;       // stall must last this long
const uint32_t BLANK_MS = 400;       // ignore the start-up current spike
const uint32_t MAX_MOVE_MS = 20000;  // safety: never drive longer than this
const uint32_t DEFAULT_TRAVEL_MS = 8000;

// EEPROM layout
const int EE_TUP = 0, EE_TDOWN = 4, EE_DOWN = 8, EE_MAGIC = 9;
const byte MAGIC = 0x5A;

enum Move { STOP, UP, DOWN };

Move move = STOP;
float pos = 0;          // 0 = fully down, 1 = fully up
bool posKnown = false;
float target = -1;      // height to stop at; -1 = none
float afterHoming = -1; // height to go to after finding the bottom
uint32_t moveStart = 0, lastTick = 0, stallSince = 0, runMs = 0;
bool fromEnd = false;   // this move started at an end stop (used to learn travel time)
uint32_t travelUp = DEFAULT_TRAVEL_MS, travelDown = DEFAULT_TRAVEL_MS;
bool prevR = false;

void out(int pin, bool on) { digitalWrite(pin, on ? HIGH : LOW); }

bool readInput(int pin) {
  // simple debounce: majority of 3 reads, 5 ms apart
  int a = digitalRead(pin); delay(5);
  int b = digitalRead(pin); delay(5);
  int c = digitalRead(pin);
  int v = (a == b || a == c) ? a : b;
  return v == INPUT_ON;
}

float readMilliamps() {
  int adc = analogRead(PIN_IS);
  if (adc >= 1020) return 1e6;       // sense output at its limit: fault or heavy overload
  float volts = adc * VREF / 1023.0;
  return volts / R_IS * K_ILIS * 1000.0;
}

void drive(Move m) {
  if (m == move) return;
  out(PIN_FEED, false);              // always stop first
  if (m != STOP) {
    delay(50);
    out(PIN_TRIG, m == UP);
    delay(20);
    out(PIN_FEED, true);             // switching IN off and on also clears a latched fault
    fromEnd = posKnown && ((m == UP && pos <= 0) || (m == DOWN && pos >= 1));
  }
  out(LED_UP, m == UP);
  out(LED_DOWN, m == DOWN);
  move = m;
  moveStart = lastTick = millis();
  stallSince = 0;
  runMs = 0;
}

void goTo(float h) {
  if (!posKnown) { afterHoming = h; target = -1; drive(DOWN); return; }
  target = h;
  if (h > pos + 0.02) drive(UP);
  else if (h < pos - 0.02) drive(DOWN);
  else { target = -1; drive(STOP); }
}

void reachedEnd() {
  bool up = (move == UP);
  if (fromEnd && runMs > 1000) {       // learn travel time from a full end-to-end move
    uint32_t &t = up ? travelUp : travelDown;
    t = (t * 3 + runMs) / 4;
    EEPROM.put(up ? EE_TUP : EE_TDOWN, t);
  }
  pos = up ? 1 : 0;
  posKnown = true;
  drive(STOP);
  target = -1;
  if (!up && afterHoming >= 0) { float h = afterHoming; afterHoming = -1; goTo(h); }
}

void track() {
  if (move == STOP) return;
  uint32_t now = millis();
  float mA = readMilliamps();
  uint32_t dt = now - lastTick;
  lastTick = now;
  bool blank = now - moveStart < BLANK_MS;

  if (mA > RUN_MA || blank) {          // count time only while the motor is running
    runMs += dt;
    float step = (float)dt / (move == UP ? travelUp : travelDown);
    // timing alone never reaches 0 or 1: only a detected end stop does
    pos = constrain(pos + (move == UP ? step : -step), 0.01, 0.99);
  }

  static uint32_t lastLog = 0;
  if (now - lastLog > 200) {
    lastLog = now;
    Serial.print(move == UP ? "UP " : "DOWN ");
    Serial.print(mA, 0); Serial.print(" mA  pos ");
    Serial.println(pos, 2);
  }

  if (!blank) {
    if (mA > STALL_MA) {
      if (!stallSince) stallSince = now;
      if (now - stallSince > STALL_MS) { reachedEnd(); return; }    // hit the end stop
    } else stallSince = 0;
    if (mA < RUN_MA) { reachedEnd(); return; }                      // antenna's own board cut the motor
  }

  if (now - moveStart > MAX_MOVE_MS) {                              // safety
    Serial.println("Timeout: stopping, position unknown");
    drive(STOP); posKnown = false; target = -1; afterHoming = -1;
    return;
  }

  if (target >= 0 && ((move == UP && pos >= target) || (move == DOWN && pos <= target))) {
    drive(STOP); target = -1;
  }
}

void powerOff() {
  static uint32_t lastTry = 0;           // on USB power (bench) the board stays on: don't repeat
  if (lastTry && millis() - lastTry < 10000) return;
  lastTry = millis();
  EEPROM.update(EE_DOWN, 1);             // shut down cleanly with the mast down
  Serial.println("Mast down, powering off");
  delay(50);
  out(PIN_HOLD, false);                  // the Arduino loses power here...
  delay(1000);
  out(PIN_HOLD, true);                   // ...unless the radio came back on: carry on
  EEPROM.update(EE_DOWN, 0);
}

void setup() {
  pinMode(PIN_HOLD, OUTPUT);
  out(PIN_HOLD, true);                   // keep ourselves powered from +12 V permanent
  pinMode(PIN_FEED, OUTPUT); pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_DEN13, OUTPUT); pinMode(PIN_DEN24, OUTPUT);
  pinMode(LED_UP, OUTPUT); pinMode(LED_DOWN, OUTPUT);
  out(PIN_FEED, false); out(PIN_TRIG, false);
  out(PIN_DEN13, true);                  // U1 current on A2
  out(PIN_DEN24, false);
  pinMode(PIN_R, INPUT_PULLUP); pinMode(PIN_A, INPUT_PULLUP); pinMode(PIN_U, INPUT_PULLUP);
  analogReference(INTERNAL);             // 1.1 V full scale for better current resolution
  Serial.begin(115200);

  if (EEPROM.read(EE_MAGIC) == MAGIC) {
    EEPROM.get(EE_TUP, travelUp);
    EEPROM.get(EE_TDOWN, travelDown);
    posKnown = EEPROM.read(EE_DOWN) == 1;  // last shutdown was clean, so the mast is down
  } else {
    EEPROM.put(EE_TUP, travelUp); EEPROM.put(EE_TDOWN, travelDown);
    EEPROM.update(EE_MAGIC, MAGIC);
  }
  pos = 0;
  EEPROM.update(EE_DOWN, 0);
}

void loop() {
  bool R = readInput(PIN_R), A = readInput(PIN_A), U = readInput(PIN_U);
  bool rRose = R && !prevR;
  prevR = R;

  if (!R) {                                          // radio off: all the way down, then off
    afterHoming = -1; target = -1;
    if (move == STOP && posKnown && pos <= 0) powerOff();
    else if (move != DOWN) drive(DOWN);
  } else if (A && U) {                               // UP held or MAX: go up
    target = -1; afterHoming = -1;
    if (move != UP && !(posKnown && pos >= 1)) drive(UP);
  } else if (!A) {                                   // DOWN held or OFF: go down
    target = -1; afterHoming = -1;
    if (move != DOWN && !(posKnown && pos <= 0)) drive(DOWN);
  } else {                                           // AUTO
    if (rRose) goTo(AUTO_HEIGHT);                    // radio just came on
    else if (target < 0 && afterHoming < 0 && move != STOP) drive(STOP);  // switch released: hold
  }

  track();
  delay(10);
}
```

What the firmware does that may need changing:

- After DOWN is released, or the switch goes from OFF back to AUTO, the mast **stays where it is**.
  The original board can't tell these two apart either. Turning the radio off and on sends it back
  to the auto height.
- If the controller loses power mid-travel (for example a battery disconnect), it doesn't know where
  the mast is. On the next start it first drives down to find the bottom, then goes to the auto
  height.
- If the shield reports a fault (short circuit or overload), the reading goes to its limit and the
  controller treats it like an end stop and cuts the output.

## Open questions (this idea)

- [ ] Check the shield's current reading against a multimeter, and adjust `K_ILIS` if needed.
- [ ] Radio wire start-up current for the Uno: roughly 50–100 mA at 12 V for half a second.

## References

- Infineon PROFET+2 12V Arduino Shield, user manual (2019) and example code (pin table, sense
  resistor, kILIS values): [repository](https://github.com/Infineon/PROFET-2-12V-Arduino-Shield)
  · [reference](../references/infineon-profet2-arduino-shield/README.md)
