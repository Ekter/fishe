#include <Arduino.h>

#define tempSensor A0    // select the input pin for the potentiometer
#define ledPin  13      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  pinMode(ledPin, OUTPUT);  // declare the ledPin as an OUTPUT
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(tempSensor);    // read the value from the sensor:
  Serial.println(sensorValue);            //Write the value of the sensor
  digitalWrite(ledPin, HIGH);
  delay(200);                     // stop the program for 100 milliseconds:
  sensorValue = analogRead(tempSensor);    // read the value from the sensor:
  Serial.println(sensorValue);            //Write the value of the sensor
  digitalWrite(ledPin, LOW);
  delay(200);                     // stop the program for 100 milliseconds:
}
