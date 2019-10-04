#if defined(ARDUINO) && ARDUINO >= 100
  #include "Arduino.h"
#else
  #include <WProgram.h>
#endif

#include <Servo.h>
#include <FastLED.h>
#include <ros.h>
#include <std_msgs/UInt32MultiArray.h>
#include <std_msgs/Char.h>

#define CLAW_PIN 45
#define LEVEL_PIN 44
#define LEVEL_DOWN 80
#define LEVEL_UP 20
#define CLAW_CLOSED 170
#define CLAW_OPEN 80
#define DIODE_PIN 30
#define NUM_LEDS 24

Servo claw;
Servo level;

class NewHardware : public ArduinoHardware
{
  public:
  NewHardware():ArduinoHardware(&Serial1, 115200){};
};

ros::NodeHandle_<NewHardware>  nh;

CRGB leds[NUM_LEDS];

int   state;

inline void raise_claw(void)
{
  if (! state & 0x1)
  {
    level.write(LEVEL_UP);
    state |= 0x1;
  }
}

inline void lower_claw(void)
{
  if (state & 0x1)
  {
    level.write(LEVEL_DOWN);
    state &= 0x2;
  }
}

inline void open_claw(void)
{
  if (! state & 0x2)
  {
    level.write(CLAW_OPEN);
    state |= 0x2;
  }
}

inline void close_claw(void)
{
  if (state & 0x2)
  {
    level.write(CLAW_CLOSED);
    state &= 0x1;
  }
}

void lidar_cb( const std_msgs::UInt32MultiArray& message){
  FastLED.clear();
  for (unsigned i = 0; i < message.data_length && i < NUM_LEDS; i++)
  {
    leds[i] = message.data[i];
  }
  FastLED.show();
}

void claw_cb( const std_msgs::Char& message){
  switch (message.data) {
    case 'u':
      raise_claw();
      break;
    case 'd':
      lower_claw();
      break;
    case 'o':
      open_claw();
      break;
    case 'c':
      close_claw();
      break;
  }
}

ros::Subscriber<std_msgs::UInt32MultiArray> sub_lidar("lidar", lidar_cb);
ros::Subscriber<std_msgs::Char> sub_claw("claw", claw_cb);

void setup(){
  claw.attach(CLAW_PIN);
  level.attach(LEVEL_PIN);
  nh.initNode();
  nh.subscribe(sub_lidar);
  nh.subscribe(sub_claw);
  FastLED.addLeds<WS2812, DIODE_PIN>(leds, NUM_LEDS);
  FastLED.clear();
  raise_claw();
  open_claw();
}

void loop(){
  nh.spinOnce();
  delay(1);
}
