//morse class definition


#include "Morse.h"
#include <Arduino.h>

Morse::Morse(int pin)
{
  pinMode(pin, OUTPUT);
  _pin = pin;
  queue_time = (int*)malloc(100);
}

Morse::Morse()
{
  Morse(LED_BUILTIN);
}

Morse::~Morse()
{
}

void Morse::dot()
{
  digitalWrite(_pin, HIGH);
  delay(TIME_DOT);
  digitalWrite(_pin, LOW);
  delay(TIME_DOT);
}

void Morse::dash()
{
  digitalWrite(_pin, HIGH);
  delay(TIME_DOT * 4);
  digitalWrite(_pin, LOW);
  delay(TIME_DOT);
}

void Morse::space()
{
  digitalWrite(_pin, LOW);
  delay(TIME_DOT * 8);
}
