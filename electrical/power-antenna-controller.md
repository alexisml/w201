# Power antenna controller: make a 3-wire antenna work like the original

**System:** electrical
**Status:** design, not built yet

A small box that makes a cheap aftermarket 3-wire power antenna (ground, +12 V, trigger) behave
like the original Mercedes semi-automatic antenna with the dash switch (MAX / UP / AUTO / DOWN /
OFF). It's built from off-the-shelf modules: an ESP32 relay board, a current-sensor breakout and an
optocoupler board, wired with screw terminals and a few soldered parts. No custom PCB.

Background, original wiring and sources: [power-antenna.md](power-antenna.md). This is "option A"
there, the preferred option.

> **Not tested yet.** Everything here is a design from the documented wiring and from forum tests
> of other antennas. Do the [bench tests](#1-bench-test-the-antenna-before-building) first, and
> adjust the settings in the firmware to your antenna.

## How it works

The car still sends the original signals to the antenna plug: radio on (pin 5), and the two switch
lines (pins 4 and 1). The controller reads them and drives the aftermarket antenna with two relays:

| Motion | Relay "feed" (antenna +12 V) | Relay "trigger" |
|---|---|---|
| Up | on | on |
| Down | on | off |
| Stop / hold | off | (as it was) |

The aftermarket antenna needs its +12 V to move at all, so cutting it stops the mast where it is.
That's what makes the in-between heights possible.

**Position.** The antenna gives no position signal. The controller works it out:

- A current sensor on the antenna's +12 V shows when the motor is running.
- At the end of travel the motor stalls (the current jumps), or the antenna's own board cuts it
  (the current drops). Either way the controller knows the mast is fully up or fully down. It also
  cuts the power right away at a stall, which saves the gears.
- In between, it counts how long the motor has run, compared with the full travel time. It learns
  the travel time every time the mast goes from one end to the other.

**Behaviour** (with the radio on):

| Switch | Mast |
|---|---|
| Radio turns on, switch in AUTO | Goes to the "auto" height (default half) |
| UP (held) | Goes up while held, stops when released |
| MAX | Goes all the way up |
| DOWN (held) | Goes down while held, stops when released |
| OFF | Goes all the way down |
| Radio off / key off | Goes all the way down, then the controller switches itself off |

**Zero standby drain.** The controller is off when the radio is off. Turning the radio on powers it
up through the radio's antenna wire. It then switches on a "hold" relay that keeps it powered from
the permanent +12 V, so it can still lower the mast after the radio goes off. When the mast is down
it releases the hold relay and powers itself off.

## Parts

Example parts are given; any equivalent works.

| # | Part | What for | Example |
|---|---|---|---|
| 1 | **ESP32 board with 4 relays and a 7–30 V input** | Brain, power supply and relays in one | "ESP32 4-channel relay module, DC 7–30 V" (ESP32-WROOM-32E; often sold as ESP32_Relay_X4). Relays rated 10 A |
| 2 | **INA260 current/voltage sensor breakout** | Measures the antenna's current (up to 15 A, 36 V; shunt built in) | Adafruit INA260 (product 4226) |
| 3 | **Optocoupler board, 4 channels, 12 V input** | Reads the 12 V car signals safely at 3.3 V | "PC817 4-channel optocoupler isolation board, 12 V" |
| 4 | 2 × rectifier diodes, 3 A or more | Lets either the radio wire or the hold relay power the board | 1N5408 or SR560 (Schottky) |
| 5 | TVS diode, ~22 V | Absorbs voltage spikes from the car | 1.5KE22A (through-hole) |
| 6 | Inline blade fuse holder + 5 A fuse | Protects the +12 V permanent feed | Any automotive inline holder |
| 7 | Waterproof box with cable glands | Housing in the trunk | ABS box, IP65, about 150 × 100 × 70 mm |
| 8 | Lever connectors or screw terminals | Wiring inside the box | WAGO 221 |
| 9 | Wire: 1 mm² (red, brown) for power and ground; 0.5 mm² for signals | | Automotive (FLRY) wire |
| 10 | Optional: matching 6-pin plug from an old antenna | Plugs into the car harness without cutting it | Harness side is housing `A 011 545 51 28` (EPC 82.345) |

Tools: soldering iron, heat-shrink, multimeter, a USB cable for the ESP32, a 12 V bench supply
(2–3 A) or a car battery for testing.

## Wiring

### Car side (original 6-pin antenna plug)

Colours from the original W201/W124/W126 wiring. **Check them on your car with a multimeter.**

| Car pin | Colour | Signal | Goes to |
|---|---|---|---|
| 2 | red | +12 V permanent | Fuse → hold relay and feed relay |
| 5 | blue/white | Radio on | Optocoupler input 1 (R), and diode → board power |
| 4 | blue/green | Switch: AUTO, UP, MAX | Optocoupler input 2 (A) |
| 1 | blue/yellow | Switch: UP, MAX | Optocoupler input 3 (U) |
| 6 | brown | Ground | Ground bus |

Cars without the dash switch (or later 4-wire harnesses) only have pins R, +12 V and ground. Leave A
and U unconnected and the controller acts as "AUTO" all the time.

### Inside the box

```
 +12 V permanent (pin 2) ── fuse 5 A ──┬── relay HOLD (COM) ── NO ──►|── board power in (+)
                                       │                       diode 1
                                       ├── relay FEED (COM) ── NO ── INA260 Vin+ ; Vin- ──► antenna +12 V (red)
                                       └── relay TRIG (COM) ── NO ──────────────────────► antenna trigger

 radio on (pin 5) ──┬──►|── board power in (+)          TVS 22 V from board power in (+) to ground
                    │  diode 2
                    └── optocoupler IN1+

 switch (pin 4) ───── optocoupler IN2+
 switch (pin 1) ───── optocoupler IN3+
 optocoupler IN- (all) ── ground

 ground (pin 6) ── ground bus ── board GND, optocoupler input ground, antenna ground (brown/black)

 ESP32 3.3 V ── optocoupler output VCC, INA260 VIN
 ESP32 GND   ── optocoupler output GND, INA260 GND
 optocoupler OUT1 / OUT2 / OUT3 ── ESP32 GPIO 18 / 19 / 23
 INA260 SDA / SCL ── ESP32 GPIO 21 / 22
```

Notes:

- The relay GPIOs differ between boards. Common ones are 32, 33, 25 and 26; check your board's
  listing and set them at the top of the firmware.
- Use the relays' **NO** (normally open) contacts, so everything is off when the board is off.
- The two diodes make sure the radio wire can power the board, but the hold relay can't push
  +12 V back into the radio wire.
- Keep the feed and ground wires to the antenna short and 1 mm² or thicker.

### Bypass plug

Make a short adapter that connects car pin 2 → antenna +12 V, car pin 5 → antenna trigger, and
ground → ground. If the controller ever fails, plug this in and the antenna works the simple way
again (up with the radio, down without).

## Build steps

### 1. Bench-test the antenna before building

With the antenna on the bench and a 12 V supply, plus a multimeter in series with the +12 V wire:

1. +12 V and ground only: it should go down (or stay down). Note the idle current.
2. Add the trigger: it should go up. Time the full travel and note the **running current** and the
   **current when it hits the top**.
3. Remove the trigger: it should go down. Time it.
4. **Key test:** during travel, disconnect the +12 V. The mast must **stop where it is**. Reconnect
   it with the trigger on: it should carry on up; with the trigger off: it should go down. If the
   antenna doesn't behave like this, option A won't work with it.
5. Measure the current on the trigger wire too. It should be small (a signal, not motor current).

### 2. Program the ESP32 before wiring the car

1. Install the Arduino IDE (or PlatformIO), add the ESP32 boards package, and install the
   **Adafruit INA260** library.
2. Set the pins and the settings at the top of the sketch below.
3. Upload over USB. Open the serial monitor at 115200 baud.

### 3. Test on the bench

Power the box from the bench supply instead of the car: use a switch for "radio on", and two more
switches for the A and U lines (or a real antenna switch). Check every row of the behaviour table.
Watch the serial monitor for current readings, then set `RUN_MA` and `STALL_MA`:

- `RUN_MA`: about halfway between the idle current and the running current.
- `STALL_MA`: about halfway between the running current and the stall current.

### 4. Fit it in the car

Mount the box in the trunk near the antenna, away from water. Connect it to the car's antenna plug
(or splice into the harness with soldered, heat-shrunk joints), and the antenna to the box. Test
again with the real radio and switch.

## Firmware (ESP32, Arduino core)

```cpp
// Power antenna controller: drives a 3-wire aftermarket antenna like the original
// Mercedes semi-automatic antenna (switch MAX / UP / AUTO / DOWN / OFF).
// ESP32 + 4-relay board, INA260 current sensor, PC817 optocoupler board.
// Not tested yet: bench-test first and adjust the settings below.

#include <WiFi.h>
#include <Wire.h>
#include <Preferences.h>
#include <Adafruit_INA260.h>

// ---------- pins: check your board ----------
const int PIN_HOLD = 32;   // relay: keeps the controller powered from +12 V permanent
const int PIN_FEED = 33;   // relay: +12 V to the antenna
const int PIN_TRIG = 25;   // relay: trigger to the antenna
const int PIN_R = 18;      // optocoupler: radio on (car pin 5)
const int PIN_A = 19;      // optocoupler: switch AUTO/UP/MAX (car pin 4)
const int PIN_U = 23;      // optocoupler: switch UP/MAX (car pin 1)
const int RELAY_ON = HIGH; // most ESP32 relay boards switch on with HIGH
const int INPUT_ON = LOW;  // optocoupler output goes LOW when 12 V is present

// ---------- settings: adjust after the bench test ----------
const float AUTO_HEIGHT = 0.5;       // AUTO height, as a fraction of full travel
const float RUN_MA = 300;            // above this the motor is running
const float STALL_MA = 2500;         // above this the mast has hit an end stop
const uint32_t STALL_MS = 150;       // stall must last this long
const uint32_t BLANK_MS = 400;       // ignore the start-up current spike
const uint32_t MAX_MOVE_MS = 20000;  // safety: never drive longer than this
const uint32_t DEFAULT_TRAVEL_MS = 8000;

enum Move { STOP, UP, DOWN };

Adafruit_INA260 ina;
Preferences prefs;
bool inaOk = false;

Move move = STOP;
float pos = 0;          // 0 = fully down, 1 = fully up
bool posKnown = false;
float target = -1;      // height to stop at; -1 = none
float afterHoming = -1; // height to go to after finding the bottom
uint32_t moveStart = 0, lastTick = 0, stallSince = 0, runMs = 0;
bool fromEnd = false;   // this move started at an end stop (used to learn travel time)
uint32_t travelUp = DEFAULT_TRAVEL_MS, travelDown = DEFAULT_TRAVEL_MS;
bool prevR = false;

void relay(int pin, bool on) { digitalWrite(pin, on ? RELAY_ON : !RELAY_ON); }

bool readInput(int pin) {
  // simple debounce: same value on 3 reads, 5 ms apart
  int a = digitalRead(pin); delay(5);
  int b = digitalRead(pin); delay(5);
  int c = digitalRead(pin);
  int v = (a == b || a == c) ? a : b;
  return v == INPUT_ON;
}

float readMilliamps() {
  if (inaOk) return fabs(ina.readCurrent());
  // no sensor: pretend the motor runs for the expected travel time
  uint32_t t = (move == UP) ? travelUp : travelDown;
  return (millis() - moveStart < t * 1.1) ? RUN_MA + 1 : 0;
}

void drive(Move m) {
  if (m == move) return;
  relay(PIN_FEED, false);              // always stop first
  if (m != STOP) {
    delay(50);
    relay(PIN_TRIG, m == UP);
    delay(20);
    relay(PIN_FEED, true);
    fromEnd = posKnown && ((m == UP && pos <= 0) || (m == DOWN && pos >= 1));
  }
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
    prefs.putUInt(up ? "tUp" : "tDown", t);
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
    pos = constrain(pos + (move == UP ? step : -step), 0.01f, 0.99f);
  }

  static uint32_t lastLog = 0;
  if (now - lastLog > 200) { lastLog = now; Serial.printf("%s %.0f mA pos %.2f\n", move == UP ? "UP" : "DOWN", mA, pos); }

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
  prefs.putBool("down", true);         // shut down cleanly with the mast down
  Serial.println("Mast down, powering off");
  delay(50);
  relay(PIN_HOLD, false);              // the board loses power here...
  delay(1000);
  relay(PIN_HOLD, true);               // ...unless the radio came back on: carry on
  prefs.putBool("down", false);
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_OFF);
  pinMode(PIN_HOLD, OUTPUT); pinMode(PIN_FEED, OUTPUT); pinMode(PIN_TRIG, OUTPUT);
  relay(PIN_HOLD, true);               // keep ourselves powered from +12 V permanent
  relay(PIN_FEED, false); relay(PIN_TRIG, false);
  pinMode(PIN_R, INPUT_PULLUP); pinMode(PIN_A, INPUT_PULLUP); pinMode(PIN_U, INPUT_PULLUP);

  Wire.begin(21, 22);
  inaOk = ina.begin();
  Serial.println(inaOk ? "INA260 found" : "INA260 not found: timing only");

  prefs.begin("antenna", false);
  travelUp = prefs.getUInt("tUp", DEFAULT_TRAVEL_MS);
  travelDown = prefs.getUInt("tDown", DEFAULT_TRAVEL_MS);
  posKnown = prefs.getBool("down", false);   // last shutdown was clean, so the mast is down
  pos = 0;
  prefs.putBool("down", false);
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
- Wi-Fi is off. The ESP32's Wi-Fi or Bluetooth could later be used to set the auto height or read
  the logs from a phone.

## Open questions

- [ ] Does the aftermarket antenna stop when its +12 V is cut mid-travel? (Bench test 4.)
- [ ] Running and stall current of the antenna, to set `RUN_MA` and `STALL_MA`.
- [ ] How much current the radio's antenna output can supply. It has to power the ESP32 board for
      about half a second at start-up, until the hold relay closes (roughly 100–200 mA at 12 V).
      If it's too weak, add a small 12 V relay driven by the radio wire to switch on the board.
- [ ] Relay GPIOs on the chosen board.
