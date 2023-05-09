#include <Arduino.h>
#include <Servo.h>

Servo servo;
Servo servo2;
void setup()
{
  Serial.begin(115200);
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
    if (a <= 30)
    {
      // uint16_t b = a-90;
      servo.write(a*6);
      Serial.print("Servo set to ");
      Serial.println(a*6);
    }
    else if (a <= 60)
    {
      servo2.write((a-30)*6);
      Serial.print("Servo2 set to ");
      Serial.println((a-30)*6);
    }
    else if (a<=120)
    {
      servo2.write(a);
      Serial.print("Servo2 set to ");
      Serial.println(a);
    }
    else if (a==121)
    {
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
    }
    else if (a==122)
    {
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
    }
    
    else if (a==209)
    {
      servo.attach(9);
    }
    else if (a==210)
    {
      servo2.attach(10);
    }
    else if (a==211)
    {
      pinMode(5,OUTPUT);
      pinMode(6,OUTPUT);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
    }
    else if (a==219)
    {
      servo.detach();
    }
    else if (a==220)
    {
      servo2.detach();
    }
    else if (a==221)
    {
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
    }
  }
}
