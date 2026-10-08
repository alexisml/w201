// Host test harness: runs a controller sketch against a simulated car and antenna.
// Untested idea: this checks the firmware logic of the power antenna controller ideas, not real hardware.
// Built and run by run.py (needs a C++ compiler: clang++ or g++). Define TARGET_ESP32 for the ESP32 sketch.
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdarg>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include "stubs.h"

// ---------------- simulated world ----------------
static int eeWrites = 0;            // EEPROM / NVS writes
static unsigned long NOW = 0;          // ms
static int PINS[64];
static std::map<int, unsigned char> EE;
static bool powered = false;
static bool usbPower = false;          // bench: HOLD low doesn't cut power
struct PowerLost {};

// car inputs (true = 12 V present)
static bool inR = false, inA = false, inU = false;
// antenna model
static double apos = 0.0;              // antenna mast: 0 down .. 1 up
static double TRAVEL_UP = 7.0, TRAVEL_DOWN = 6.0;   // s
static double RUN_UP_MA = 1500, RUN_DOWN_MA = 900, STALL_MA_REAL = 4000, IDLE_MA = 15;
static double stallTime = 0;           // s spent stalled at an end
static double BOARD_CUTOFF_S = 2.0;    // antenna's own board cuts the stalled motor after this
static bool boardCut = false;
static int lastTrig = -1;
static bool noisyDips = false;         // inject single low samples
static bool faultInject = false;       // force a saturated sense reading
static bool idleTooHigh = false;       // antenna idles above RUN_MA (end detection fails)
static double current_mA = 0;
static int dipCounter = 0;

#ifdef TARGET_ESP32
static const int P_FEED = 33, P_HOLD = 32, P_TRIG = 25, P_R = 18, P_A = 19, P_U = 23;
#else
static const int P_FEED = 9, P_HOLD = 10, P_TRIG = 11, P_R = 2, P_A = A4, P_U = A5;
#endif

static void stepAntenna(double dt) {
  bool feed = PINS[P_FEED] && powered;
  bool trig = PINS[P_TRIG] && powered;
  if (trig != lastTrig) { boardCut = false; stallTime = 0; lastTrig = trig; }
  if (!feed) { current_mA = 0; boardCut = false; stallTime = 0; return; }
  bool atEnd = trig ? apos >= 1.0 : apos <= 0.0;
  if (!atEnd) {
    apos += (trig ? 1 : -1) * dt / (trig ? TRAVEL_UP : TRAVEL_DOWN);
    if (apos > 1) apos = 1; if (apos < 0) apos = 0;
    current_mA = trig ? RUN_UP_MA : RUN_DOWN_MA;
    stallTime = 0; boardCut = false;
  } else if (!boardCut) {
    stallTime += dt;
    current_mA = STALL_MA_REAL;
    if (stallTime >= BOARD_CUTOFF_S) boardCut = true;
  } else {
    current_mA = idleTooHigh ? 600 : IDLE_MA;
  }
}

static void advance(unsigned long ms) {
  for (unsigned long i = 0; i < ms; i++) { NOW++; stepAntenna(0.001); }
}

// ---------------- Arduino API stubs ----------------
SerialT Serial; EEPROMT EEPROM; WireT Wire; WiFiT WiFi;
static bool VERBOSE = false;
template<class T> void SerialT::print(T) {}
template<class T> void SerialT::print(T, int) {}
template<class T> void SerialT::println(T v) {}
template<class T> void SerialT::println(T v, int) {}
template<> void SerialT::println<const char*>(const char* s) { if (VERBOSE) printf("    [fw %6.1fs] %s\n", NOW / 1000.0, s); }
void SerialT::begin(long) {}
void SerialT::printf(const char*, ...) {}
template<class T> void EEPROMT::put(int a, const T& v) { const unsigned char* p = (const unsigned char*)&v; for (size_t i = 0; i < sizeof(T); i++) EE[a + i] = p[i]; }
template<class T> void EEPROMT::get(int a, T& v) { unsigned char* p = (unsigned char*)&v; for (size_t i = 0; i < sizeof(T); i++) p[i] = EE.count(a + i) ? EE[a + i] : 0xFF; }
byte EEPROMT::read(int a) { return EE.count(a) ? EE[a] : 0xFF; }
void EEPROMT::update(int a, byte v) { if (read(a) != v) { EE[a] = v; eeWrites++; } }
void pinMode(int, int) {}
void digitalWrite(int p, int v) {
  PINS[p] = v;
  if (p == P_HOLD && v == 0 && !inR && !usbPower) { powered = false; throw PowerLost(); }
}
int digitalRead(int p) {
  bool on = (p == P_R) ? inR : (p == P_A) ? inA : (p == P_U) ? inU : false;
  return on ? 0 : 1;        // optocoupler pulls LOW when 12 V present
}
int analogRead(int p) {
  if (p != A2) return 0;
  double mA = current_mA;
  if (noisyDips && current_mA > 500 && (++dipCounter % 7 == 0)) mA = 50;   // occasional single low sample
  if (faultInject && current_mA > 500) return 1023;
  double volts = mA / 1000.0 / 14500.0 * 1000.0;          // I / kILIS * R_IS
  int adc = (int)(volts / 1.1 * 1023.0);
  return adc > 1023 ? 1023 : adc;
}
void analogReference(int) {}
static std::map<std::string, uint32_t> NVS;     // ESP32 Preferences
bool Adafruit_INA260::begin() { return true; }
float Adafruit_INA260::readCurrent() {
  double mA = current_mA;
  if (noisyDips && current_mA > 500 && (++dipCounter % 7 == 0)) mA = 50;
  return (float)mA;
}
void Preferences::begin(const char*, bool) {}
uint32_t Preferences::getUInt(const char* k, uint32_t d) { return NVS.count(k) ? NVS[k] : d; }
void Preferences::putUInt(const char* k, uint32_t v) { if (!NVS.count(k) || NVS[k] != v) eeWrites++; NVS[k] = v; }
bool Preferences::getBool(const char* k, bool d) { return NVS.count(k) ? NVS[k] != 0 : d; }
void Preferences::putBool(const char* k, bool v) { if (!NVS.count(k) || NVS[k] != (uint32_t)v) eeWrites++; NVS[k] = v; }
void WireT::begin(int, int) {}
void WiFiT::mode(int) {}
void delay(unsigned long ms) { advance(ms); }
unsigned long millis() { return NOW; }

// ---------------- the sketch ----------------
#include "fw.inc"

// ---------------- scenario runner ----------------
static void setCar(bool radio, const char* sw) {
  inR = radio;
  inA = radio && (!strcmp(sw, "AUTO") || !strcmp(sw, "UP") || !strcmp(sw, "MAX"));
  inU = radio && (!strcmp(sw, "UP") || !strcmp(sw, "MAX"));
}
static bool runFor(double seconds) {
  unsigned long end = NOW + (unsigned long)(seconds * 1000);
  while (NOW < end) {
    if (!powered) {
      if (inR) {                       // radio wire wakes the board
        powered = true;
        memset(PINS, 0, sizeof(PINS));
        // reset sketch globals by re-running setup (fresh RAM)
        fw_reset();
        try { setup(); } catch (PowerLost&) { continue; }
      } else { advance(10); continue; }
    }
    try { loop(); } catch (PowerLost&) {}
  }
  return powered;
}

int failures = 0;
static void check(const char* what, bool ok) {
  printf("  %-62s %s\n", what, ok ? "OK" : "FAIL");
  if (!ok) failures++;
}

int main(int argc, char** argv) {
  VERBOSE = argc > 1;
  printf("Scenario 1: normal use\n");
  setCar(true, "AUTO"); runFor(12);
  check("radio on in AUTO: mast near half height", fabs(apos - 0.5) < 0.12);
  setCar(true, "UP"); runFor(1); setCar(true, "AUTO"); runFor(2);
  double p1 = apos;
  check("rock UP 1 s: mast higher, then holds", p1 > 0.55 && p1 < 0.8);
  runFor(3); check("AUTO holds", fabs(apos - p1) < 0.01);
  setCar(true, "DOWN"); runFor(1.5); setCar(true, "AUTO"); runFor(2);
  check("rock DOWN 1.5 s: mast lower, holds", apos < p1 - 0.1 && apos > 0.05);
  setCar(true, "MAX"); runFor(12); check("MAX: fully up", apos > 0.99);
  setCar(true, "OFF"); runFor(12); check("OFF: fully down", apos < 0.01);
  setCar(true, "AUTO"); runFor(3); check("OFF -> AUTO: stays down", apos < 0.01);
  setCar(true, "MAX"); runFor(12);
  setCar(false, "MAX"); runFor(15);
  check("radio off from MAX: fully down", apos < 0.01);
  check("controller powered itself off", !powered);
  setCar(true, "AUTO"); runFor(12);
  check("next radio on: rises to about half again", fabs(apos - 0.5) < 0.12);
  setCar(false, "AUTO"); runFor(15);
  check("radio off again: down and off", apos < 0.01 && !powered);

  printf("Scenario 2: noisy current (single low samples)\n");
  noisyDips = true;
  setCar(true, "MAX"); runFor(12);
  check("MAX with noisy readings: still reaches the top", apos > 0.99);
  setCar(false, "MAX"); runFor(15);
  check("radio off with noisy readings: down and off", apos < 0.01 && !powered);
  noisyDips = false;

#ifndef TARGET_ESP32   // the PROFET shield reports faults; the INA260 build has no fault signal
  printf("Scenario 3: output fault during travel\n");
  setCar(true, "MAX"); runFor(12);
  faultInject = true;
  setCar(false, "MAX"); runFor(30);
  check("fault: controller gives up and powers off", !powered);
  check("fault: clean-shutdown flag NOT set", EEPROM.read(8) != 1);
  faultInject = false;
  setCar(true, "AUTO"); runFor(15);
  check("after fault, radio on: finds bottom then goes to ~half", fabs(apos - 0.5) < 0.15);
  setCar(false, "AUTO"); runFor(15);
  check("then radio off: down and off", apos < 0.01 && !powered);

#endif
  printf("Scenario 4: end detection fails (antenna idles above RUN_MA)\n");
  idleTooHigh = true; STALL_MA_REAL = 2000;      // stall below STALL_MA and idle above RUN_MA
  setCar(true, "MAX"); runFor(70);
  setCar(false, "MAX"); runFor(120);
  check("gives up after retries and powers off (no endless drain)", !powered);
  idleTooHigh = false; STALL_MA_REAL = 4000;
  setCar(true, "AUTO"); runFor(15); setCar(false, "AUTO"); runFor(15);

  printf("Scenario 5: power lost mid-travel (battery disconnect)\n");
  setCar(true, "MAX"); runFor(3);
  powered = false; inR = false;                // power cut, mast part way up
  double stuck = apos;
  setCar(true, "AUTO"); runFor(20);
  check("after power loss: homes down, then goes to ~half", stuck > 0.2 && fabs(apos - 0.5) < 0.15);
  setCar(false, "AUTO"); runFor(15);
  check("then radio off: down and off", apos < 0.01 && !powered);

  printf("Scenario 6: bench, radio off on USB power (board can't switch off)\n");
  usbPower = true;
  setCar(true, "AUTO"); runFor(15);
  setCar(false, "AUTO");
  int before = eeWrites;
  runFor(600);                                     // 10 minutes idling on the bench
  usbPower = false;
  check("bench: EEPROM writes stay small while idling", eeWrites - before <= 2);

  printf("\n%s (%d failure%s)\n", failures ? "SOME CHECKS FAILED" : "ALL CHECKS PASSED", failures, failures == 1 ? "" : "s");
  return failures ? 1 : 0;
}
