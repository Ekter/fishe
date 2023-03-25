#include <Arduino.h>
#include <Servo.h>

Servo servo;
void setup()
{
  Serial.begin(119200);
}

void loop()
{
  if (Serial.available())
  {
    // Serial.println("Hello Jetson!");
    uint8_t a = Serial.read();
    Serial.print("Received: '");
    Serial.print(a);
    Serial.println("'");
    if (a>=181 && a<=200)
    {
      servo.attach(a-181);
      Serial.print("Servo attached to pin");
      Serial.println(a-181);
    }
    if (a == 201)
    {
      servo.detach();
      Serial.println("Servo detached");
    }
    if (a <= 180)
    {
      // uint16_t b = a-90;
      servo.write(a);
      Serial.print("Servo set to ");
      Serial.println(a);
    }
  }
}
