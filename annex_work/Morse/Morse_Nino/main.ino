#include <Arduino.h>

#include "Translator.h"

Translator trad = Translator();
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial.available());
  Serial.println("bello la mondo");
  trad.translateword("bello0la0mondo");
}

void loop() {
  if (Serial.available()) {
    char letter = Serial.read();
    trad.translate(letter);
  }
}
