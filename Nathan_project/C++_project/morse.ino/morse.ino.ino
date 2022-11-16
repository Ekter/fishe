#include "traducteur.h"
traducteur trad = traducteur();
String motTraduire;
String delayOuMillis;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.println("Quel mot voulez vous traduire en morse ? ");
  while (Serial.available() > 0) {}     //tant que pas de réponse, met en pause le terminal
  motTraduire = Serial.readString();    //récupérer le mot et le mettre dans la variable
  delayOuMillis = "";
  Serial.println("En utilisant delay (d) ou millis (m) ?");
  while (Serial.available() == 0) {}
  delayOuMillis = Serial.readString();
  while ((delayOuMillis != "d") && (delayOuMillis != "m")) {    // ne sort de la boucle que si la personne répond d ou m
    Serial.println("Veuillez écrire 'd' pour delay ou 'm' pour millis");
    while (Serial.available() == 0) {}
    delayOuMillis = Serial.readString();
  }
  Serial.print("Le mot choisi est : ");
  Serial.println(motTraduire);
  if (delayOuMillis == "d") {
    trad.traduitDelay(motTraduire);           //avec delay
  }
  else {
    trad.traduitMillis(motTraduire);          //sans delay
  }
}
