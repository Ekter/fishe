//traducteur.ino
#include "traducteur.h"
traducteur Traducteur = traducteur();
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
    traducteur.traduitDelay(motTraduire);           //avec delay
  }
  else {
    traducteur.traduitMillis(motTraduire);          //sans delay
  }
}

//traducteur.h
#include <Arduino.h>

class traducteur {
  public :
    traducteur();
    //fonctions traduire :
    void traduitDelay(String mot);    // via delay
    void traduitMillis(String mot);   // via millis
  private :
    const char court[2] = "c";          //temps court
    unsigned long currentTime = 0;      //permet utilisation de millis
    unsigned long previousTime = 0;
    char charLettre;                    // transformer une lettre d'un tableau en char
    void allumerLedDelay(int duree);
    bool allumerLedMillis(int duree, bool ledState);
    String TabTraductlettres[28][2] = { //on met dans un tableau a double entre la lettre de l'alphabet (colonne 1) et sa traduction en morse (colonne 2)
      {"a", "cl"},
      {"b", "lccc"},
      {"c", "lclc"},
      {"d", "lcc"},
      {"e", "c"},
      {"f", "cclc"},
      {"g", "llc"},
      {"h", "cccc"},
      {"i", "cc"},
      {"j", "clll"},
      {"k", "lcl"},
      {"l", "clcc"},
      {"m", "ll"},
      {"n", "lc"},
      {"o", "lll"},
      {"p", "cllc"},
      {"q", "llcl"},
      {"r", "clc"},
      {"s", "ccc"},
      {"t", "l"},
      {"u", "ccl"},
      {"v", "cccl"},
      {"w", "cll"},
      {"x", "lccl"},
      {"y", "lcll"},
      {"z", "llcc"},
      {" ", ""},
      {"", ""},    //cas pour verifier si c'est une lettre
    };
};

//traducteur.cpp
traducteur::traducteur() {        //constructeur par defaut
}

void traducteur::traduitDelay(String mot) {
  mot.toLowerCase();                                        // transforme en lettre minuscule
  for (int lettre = 0; lettre < mot.length(); lettre++) {   // boucle prenant toute les lettres du mot
    for (int i = 0; i <= 27; i++) {                         // on vérifie pour toute les lettres
      charLettre = TabTraductlettres[i][0].charAt(0);       // transforme la lettre en char
      if (mot[lettre] == charLettre) {                      // on regarde si la lettre du mot correspond à une ocurance du tableau
        if (i == 26) {                                      // si espace
          Serial.println("Nouveau mot");
          delay(2400);                                      // entre chaques mots, attente plus longue
        }
        else {
          Serial.print("Lettre : ");
          Serial.println(TabTraductlettres[i][0]);
          for (int k = 0; k < TabTraductlettres[i][1].length(); k++) { // caractère morse (nombre court/long)
            if (TabTraductlettres[i][1][k] == court[0]) {     // verifier si traduction de la lettre en morse est court/long
              Serial.print("court ");
              allumerLedDelay(400);                           //court alors led allumée 400ms
            }
            else {
              Serial.print("long ");
              allumerLedDelay(1200);                          //long alors led allumé 1200ms
            }
          }
          Serial.println();
          delay(1200);                                        // delay plus long = separation lettre
        }
        break;                                                // stop quand lettre trouvé
      }
      else if (i == 27) {                                     //cas ou ce n'est pas une lettre
        Serial.print(mot[lettre]);
        Serial.println(" : ce n'est pas une lettre");
      }
    }
  }
  delay(1200);    //pause car fin du mot

  void traducteur::allumerLedDelay(int duree) {
    digitalWrite(LED_BUILTIN, HIGH);  // led allumé
    delay(duree);
    digitalWrite(LED_BUILTIN, LOW);   // led eteinte
    delay(400);
  }

  void traducteur::traduitMillis(String mot) {
    mot.toLowerCase();                                        // transforme en lettre minuscule
    for (int lettre = 0; lettre < mot.length(); lettre++) {   // boucle prenant toute les lettres du mot
      for (int i = 0; i <= 27; i++) {                         // on vérifie pour toute les lettres
        charLettre = TabTraductlettres[i][0].charAt(0);       // transforme la lettre en char
        if (mot[lettre] == charLettre) {                      // on regarde si la lettre du mot correspond à une ocurance du tableau
          if (i == 26) {                                      // si espace
            Serial.println("Nouveau mot");
            allumerLedMillis(2400, false);                    // entre chaques mots, attente plus longue
          }
          else {
            Serial.print("Lettre : ");
            Serial.println(TabTraductlettres[i][0]);
            for (int k = 0; k < TabTraductlettres[i][1].length(); k++) { //caractère morse (nombre court/long)
              if (TabTraductlettres[i][1][k] == court[0]) {     //  verifier si traduction de la lettre en morse est court/long
                Serial.print("court ");
                while (!allumerLedMillis(400, true));           // allumer led (true) et laisser 400ms allumée
              }
              else {
                Serial.print("long ");
                while (!allumerLedMillis(1200, true));          //allumer led (true) et laisser 1200ms allumée
              }
            }
            Serial.println();
            allumerLedMillis(1200, false);                      // entre chaque lettres ,plus de delay
          }
          break;                                                //stop quand lettre trouvé
        }
        else if (i == 27) {                                     //cas ou ce n'est pas une lettre
          Serial.print(mot[lettre]);
          Serial.println(" : ce n'est pas une lettre");
        }
      }
    }
    allumerLedMillis(1200, false); //pause car fin du mot
  }


  bool traducteur::allumerLedMillis(int duree, bool ledState) {
    currentTime = millis();
    if ((currentTime - previousTime) > duree) { // si temps actuel - ancien temps > duree alors :
      previousTime = currentTime;
      digitalWrite(LED_BUILTIN, ledState);   // allume ou eteint led
      return true;
    }
    return false;
  }
