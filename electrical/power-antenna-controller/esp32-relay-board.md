# Power antenna controller idea: ESP32 relay board + INA260

**System:** electrical
**Status:** untested idea

> **Untested idea.** This is a design dump, not a finished or proven build. Nothing here has been
> built or run yet. The wiring comes from documentation and forum reports, and the firmware has not
> been compiled. Bench-test the antenna first (see the [README](README.md#bench-test-the-antenna-first))
> and check everything against your own parts.

An ESP32 board with 4 relays and a built-in 7–30 V supply, plus an INA260 current sensor breakout.
Cheaper than the [Arduino + PROFET idea](arduino-uno-profet-shield.md), with hobby-grade relays and a
separate current sensor instead of automotive-grade switches. How the controller behaves, the car
wiring and the bench tests are in the [README](README.md).

## Parts

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

## Wiring inside the box

Car-side colours and pins: see the [README](README.md#car-side-wiring-original-6-pin-antenna-plug).

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

 ground (pin 6) ── ground bus ── board GND, optocoupler input ground, antenna ground

 ESP32 3.3 V ── optocoupler output VCC, INA260 VIN
 ESP32 GND   ── optocoupler output GND, INA260 GND
 optocoupler OUT1 / OUT2 / OUT3 ── ESP32 GPIO 18 / 19 / 23
 INA260 SDA / SCL ── ESP32 GPIO 21 / 22
```

- The relay GPIOs differ between boards. Common ones are 32, 33, 25 and 26; check your board's
  listing and set them at the top of the firmware.
- Use the relays' **NO** (normally open) contacts, so everything is off when the board is off.
- The ESP32 board draws a few mA through its regulator and LEDs even when idle, which is why it
  also powers itself off completely instead of using deep sleep.
- The two diodes let the radio wire power the board, but stop the hold relay from pushing +12 V back
  into the radio wire.
- Keep the feed and ground wires to the antenna short and 1 mm² or thicker.

## Programming

1. Install the Arduino IDE, add the ESP32 boards package, and install the **Adafruit INA260**
   library.
2. Set the pins and the settings at the top of the sketch below.
3. Upload over USB. Open the serial monitor at 115200 baud, then follow the
   [bench test](README.md#test-the-controller-on-the-bench).

## Firmware

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
const uint32_t LOW_MS = 150;         // current must stay below RUN_MA this long to count as stopped
const int MAX_TRIES = 3;             // failed moves in a row before giving up
const uint32_t MIN_TRAVEL_MS = 2000, MAX_TRAVEL_MS = 15000;  // limits for the learned travel time
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
uint32_t moveStart = 0, lastTick = 0, stallSince = 0, lowSince = 0, runMs = 0;
int fails = 0;          // failed moves in a row (timeouts, faults)
bool downFlag = false;  // "clean shutdown, mast down" flag currently stored
bool fromEnd = false;   // this move started at an end stop (used to learn travel time)
uint32_t travelUp = DEFAULT_TRAVEL_MS, travelDown = DEFAULT_TRAVEL_MS;
bool prevR = false;

void relay(int pin, bool on) { digitalWrite(pin, on ? RELAY_ON : !RELAY_ON); }

bool readInput(int pin) {
  // simple debounce: majority of 3 reads, 5 ms apart
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
    if (downFlag) { prefs.putBool("down", false); downFlag = false; }  // the mast is moving: no longer a clean "down"
    fromEnd = posKnown && ((m == UP && pos <= 0) || (m == DOWN && pos >= 1));
  }
  move = m;
  moveStart = lastTick = millis();
  stallSince = 0;
  lowSince = 0;
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
  if (fromEnd && runMs > 1000 && inaOk) {   // learn travel time from a full end-to-end move
    uint32_t &t = up ? travelUp : travelDown;
    t = constrain((t * 3 + runMs) / 4, MIN_TRAVEL_MS, MAX_TRAVEL_MS);
    prefs.putUInt(up ? "tUp" : "tDown", t);
  }
  pos = up ? 1 : 0;
  posKnown = true;
  fails = 0;
  drive(STOP);
  target = -1;
  if (!up && afterHoming >= 0) { float h = afterHoming; afterHoming = -1; goTo(h); }
}

void giveUp(const char *why) {         // stop, don't trust the position, count the failure
  Serial.println(why);
  drive(STOP); posKnown = false; target = -1; afterHoming = -1;
  fails++;
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
    if (mA < RUN_MA) {                                              // antenna's own board cut the motor
      if (!lowSince) lowSince = now;
      if (now - lowSince > LOW_MS) { reachedEnd(); return; }
    } else lowSince = 0;
  }

  if (now - moveStart > MAX_MOVE_MS) {                              // safety
    giveUp("Timeout: stopping, position unknown");
    return;
  }

  if (target >= 0 && ((move == UP && pos >= target) || (move == DOWN && pos <= target))) {
    drive(STOP); target = -1;
  }
}

void powerOff(bool clean) {
  static uint32_t lastTry = 0;           // on USB power (bench) the board stays on: don't repeat
  if (lastTry && millis() - lastTry < 10000) return;
  lastTry = millis();
  if (clean && !downFlag) { prefs.putBool("down", true); downFlag = true; }  // shut down cleanly with the mast down
  Serial.println(clean ? "Mast down, powering off" : "Giving up after repeated failures, powering off");
  delay(50);
  relay(PIN_HOLD, false);                // the board loses power here...
  delay(1000);
  relay(PIN_HOLD, true);                 // ...unless the radio came back on (or USB on the bench): carry on
}

void setup() {
  pinMode(PIN_HOLD, OUTPUT);
  relay(PIN_HOLD, true);               // first thing: keep ourselves powered from +12 V permanent
  pinMode(PIN_FEED, OUTPUT); pinMode(PIN_TRIG, OUTPUT);
  Serial.begin(115200);
  WiFi.mode(WIFI_OFF);
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
  if (rRose) fails = 0;                              // turning the radio on retries after a give-up

  if (fails >= MAX_TRIES) {                          // keeps failing: outputs off, give up
    drive(STOP);
    if (!R) powerOff(false);                         // next start finds the bottom first
    delay(10);
    return;
  }

  if (!R) {                                          // radio off: all the way down, then off
    afterHoming = -1; target = -1;
    if (move == STOP && posKnown && pos <= 0) powerOff(true);
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

## Open questions (this idea)

- [ ] Relay GPIOs on the chosen board.
- [ ] Radio wire start-up current for the ESP32 board (more than the Uno; measure it).
