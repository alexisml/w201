// Minimal stand-ins for the Arduino, ESP32, EEPROM, INA260 and Preferences APIs used by the sketches.
#include <stdint.h>
#include <math.h>
typedef unsigned char byte;
#define HIGH 1
#define LOW 0
#define OUTPUT 1
#define INPUT_PULLUP 2
#define INTERNAL 3
#define A0 14
#define A1 15
#define A2 16
#define A3 17
#define A4 18
#define A5 19
#define constrain(amt,low,high) ((amt)<(low)?(low):((amt)>(high)?(high):(amt)))
void pinMode(int,int); void digitalWrite(int,int); int digitalRead(int); int analogRead(int);
void analogReference(int); void delay(unsigned long); unsigned long millis();
struct SerialT { void begin(long); template<class T> void print(T); template<class T> void print(T,int); template<class T> void println(T); template<class T> void println(T,int); void printf(const char*,...);} ;
extern SerialT Serial;
struct EEPROMT { template<class T> void put(int,const T&); template<class T> void get(int,T&); byte read(int); void update(int,byte);} ;
extern EEPROMT EEPROM;
struct WireT { void begin(int,int);} ; extern WireT Wire;
struct WiFiT { void mode(int);} ; extern WiFiT WiFi;
#define WIFI_OFF 0
struct Preferences { void begin(const char*,bool); uint32_t getUInt(const char*,uint32_t); void putUInt(const char*,uint32_t); bool getBool(const char*,bool); void putBool(const char*,bool);} ;
struct Adafruit_INA260 { bool begin(); float readCurrent();} ;
