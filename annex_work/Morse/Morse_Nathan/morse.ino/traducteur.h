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
