#include <Servo.h>
Servo esc;   // Création de l'objet permettant le contrôle de l'ESC
int val = 80; //valeur iniale du moteur (change celon les test

void setup() {
  esc.attach(9); // On attache l'ESC au port numérique 9 (port PWM obligatoire)
  delay(15);
  Serial.begin(9600);
  // Initialisation de l'ESC
  esc.write(0);
  delay(1000);
  esc.write(180);
  delay(1000);
  esc.write(0);
  // Quelques informations pour que l'utilisateur choisisse une valeur
  //Serial.println("Saisir un nombre entre 0 et 179");
  //Serial.println("(0-89 : sensA - 91-179 : sensB");
  //Serial.println(" demarrage a partir de 24)");
}
void loop() {
  //if (Serial.available() > 0) {
    //val = Serial.parseInt();   // lecture de la valeur passée par le port série
    val++;                      //valeur incrémenter pour l'étude
    Serial.println(val);
    esc.write(val);
    delay(1000);
   // }
}
