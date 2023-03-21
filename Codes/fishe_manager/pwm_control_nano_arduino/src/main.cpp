#include <Arduino.h>


void setup()
{
  Serial.begin(119200);
}

void loop()
{
  if (Serial.available())
  {
    Serial.println("Hello Jetson!");
  }
}
