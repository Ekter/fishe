#include <Servo.h>
#define ir 9
Servo myservo;
int IR;


void setup() {
  Serial.begin(9600);
  myservo.attach(11);
  pinMode(ir, INPUT);                     // IR Sensor pin INPUT
}

void loop() {
  IR = digitalRead(ir); // Set the GPIO as Input
  if (IR == 1) // Check if the pin high or not
  {
    // if the pin is high turn off the onboard Led
    myservo.write(180);
    Serial.println("Motion Detected!"); // print Motion Detected! on the serial monitor window
    delay(15);
  }
  else  {
    //else turn on the onboard LED
    myservo.write(0);
    Serial.println("Motion Ended!"); // print Motion Ended! on the serial monitor window
    delay(15);
  }
}
