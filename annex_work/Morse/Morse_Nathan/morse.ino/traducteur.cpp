#include "traducteur.h"

traducteur::traducteur() {        //constructeur par defaut
}

void traducteur::traduitMillis(String mot) {
  previousTime=millis();                                    //initialise Millis pour ne pas avoir d'erreur
  mot.toLowerCase();                                        // transforme en lettre minuscule
  for (int lettre = 0; lettre < mot.length(); lettre++) {   // boucle prenant toute les lettres du mot
    for (int i = 0; i <= 37; i++) {                         // on vérifie pour toute les lettres
      charLettre = TabTraductlettres[i][0].charAt(0);       // transforme la lettre en char
      if (mot[lettre] == charLettre) {                      // on regarde si la lettre du mot correspond à une ocurance du tableau
        if (i == 26) {                                      // si espace
          Serial.println("Nouveau mot");
          while (!attendreMillis(2400));                    // entre chaques mots, attente plus longue
        }
        else {
          Serial.print("Lettre : ");
          Serial.println(TabTraductlettres[i][0]);
          for (int k = 0; k < TabTraductlettres[i][1].length(); k++) { //caractère morse (nombre court/long)
            if (TabTraductlettres[i][1][k] == court[0]) {     //  verifier si traduction de la lettre en morse est court/long
              Serial.print("court ");
              while (!allumerLedMillis(400, true));           // allumer led (true) et laisser 400ms allumée
              while (!allumerLedMillis(400, false));
            }
            else {
              Serial.print("long ");
              while (!allumerLedMillis(1200, true));          //allumer led (true) et laisser 1200ms allumée
              while (!allumerLedMillis(400, false));
            }
          }
          Serial.println();
          while (!attendreMillis(1200));                     // entre chaque lettres ,plus de delay
        }
        break;                                                //stop quand lettre trouvé
      }
      else if (i == 37) {                                     //cas ou ce n'est pas une lettre
        while (!attendreMillis(400));                        //juste attendre pour ignorer le caractère
      }
    }
  }
  while (!attendreMillis(1200)); //pause car fin du mot
}


bool traducteur::allumerLedMillis(int duree, bool ledState) {
  currentTime = millis();
  if ((currentTime - previousTime) > duree) { // si temps actuel - ancien temps > duree alors :
    previousTime = currentTime;
    return true;
  }
  digitalWrite(LED_BUILTIN, ledState);   // allume ou eteint led
  return false;
}

bool traducteur::attendreMillis(int duree) {
  currentTime = millis();
  if ((currentTime - previousTime) > duree) { // si le temps actuel - l'ancien temps est supérieur à duree alors :
    previousTime = currentTime;
    return true;
  }
  return false;
}
