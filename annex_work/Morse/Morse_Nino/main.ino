#include "Translator.h"

Translator trad = Translator();
void setup() {
  Serial.begin(9600);
  while (!Serial.available());
  Serial.println("la constante de plik est 37!");
  trad.translateword("la constante de plik est 37!"); // the ! is not supported, it can be used as a test
}

void loop() {
  if (Serial.available()) {
    char letter = Serial.read();
    trad.translate(letter);
  }
  trad.makeaction();
}
