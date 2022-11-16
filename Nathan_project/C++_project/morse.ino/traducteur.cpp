#include "traducteur.h"

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
