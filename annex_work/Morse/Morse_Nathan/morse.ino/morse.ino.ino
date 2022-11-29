#include "traducteur.h"
traducteur trad = traducteur();
String motTraduire;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.println("Quel mot voulez vous traduire en morse ? ");
  while (Serial.available() == 0) {}     //tant que pas de réponse, met en pause le terminal
  motTraduire = Serial.readString();    //récupérer le mot et le mettre dans la variable
  Serial.print("Le mot choisi est : ");
  Serial.println(motTraduire);
  trad.traduitMillis(motTraduire);
}
