"""Build and run the firmware test harness for both controller sketches.

Untested idea: checks the firmware logic of the power antenna controller ideas against a simulated
car and antenna, not real hardware. Needs Python 3 and a C++ compiler (clang++ or g++).
Run with: python3 run.py
"""
import os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKETCHES = [("Arduino Uno + PROFET", "arduino-uno-profet-shield.md", []),
            ("ESP32 relay board", "esp32-relay-board.md", ["-DTARGET_ESP32"])]

RESET = """
void fw_reset() {   // fresh RAM after a power-up
  move = STOP; pos = 0; posKnown = false; target = -1; afterHoming = -1;
  moveStart = lastTick = stallSince = lowSince = runMs = 0; fails = 0; downFlag = false;
  fromEnd = false; travelUp = travelDown = DEFAULT_TRAVEL_MS; prevR = false; lastTry = 0; lastLog = 0;
}
"""

def extract(md):
    s = open(os.path.join(HERE, "..", md)).read()
    code = re.search(r"```cpp\n(.*?)```", s, re.S).group(1)
    code = re.sub(r"#include <[^>]+>", "", code)
    # function-local statics become globals so a simulated power-up can reset them
    code = code.replace("  static uint32_t lastTry = 0;", "").replace("  static uint32_t lastLog = 0;", "")
    return "uint32_t lastTry = 0, lastLog = 0;\n" + code + RESET

def main():
    cxx = shutil.which("clang++") or shutil.which("g++")
    if not cxx:
        sys.exit("No C++ compiler found (install clang++ or g++).")
    build = os.path.join(HERE, "build")
    os.makedirs(build, exist_ok=True)
    ok = True
    for name, md, flags in SKETCHES:
        print(f"=== {name} ({md})", flush=True)
        open(os.path.join(build, "fw.inc"), "w").write(extract(md))
        exe = os.path.join(build, "harness")
        r = subprocess.run([cxx, "-std=c++17", "-O1", "-w", *flags, f"-I{build}", f"-I{HERE}",
                            os.path.join(HERE, "harness.cpp"), "-o", exe])
        if r.returncode:
            ok = False; continue
        r = subprocess.run([exe] + sys.argv[1:])
        ok &= r.returncode == 0
        print(flush=True)
    sys.exit(0 if ok else 1)

main()
