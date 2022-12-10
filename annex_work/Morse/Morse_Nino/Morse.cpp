//morse class definition

#include "Morse.h"
#include <Arduino.h>
/**
 * @brief Construct a new Morse:: Morse object
 * 
 * @param pin int: if you want to use a pin to make an action, otherwise use Morse::Morse()
 */
Morse::Morse(int pin) : len_list(LEN_LIST)
{
  pinMode(pin, OUTPUT);
  _pin = pin;
  *queue_time = (unsigned int*)malloc(len_list);
  last_time_queue = millis();
}

/**
 * @brief Construct a new Morse:: Morse object with the pin to default value (LED_BUILTIN)
 * 
 */
Morse::Morse() : len_list(LEN_LIST)
{
  Morse(LED_BUILTIN);
}

/**
 * @brief Destroy the Morse:: Morse object
 * 
 */
Morse::~Morse()
{
}

/**
 * @brief raw function for digitalWrite(pin, HIGH), it is used by the other functions.
 * 
 * @param pin 
 */
void up(short unsigned int pin)
{
  digitalWrite(pin, HIGH);
}

/**
 * @brief raw function for digitalWrite(pin, LOW), it is used by the other functions.
 * 
 * @param pin 
 */
void down(short unsigned int pin)
{
  digitalWrite(pin, LOW);
}

/**
 * @brief adds actions to the queue to make a dot (up at t=0, down at t=TIME_DOT, busy until t=2*TIME_DOT)
 * 
 */
void Morse::dot()
{
  addaction(up, &_pin, 0);              //up at t=0 
  addaction(down, &_pin, TIME_DOT);     //down at t=DOT_TIME
  addaction(down, &_pin, 2*TIME_DOT);   //busy until t=2*DOT_TIME
}

/**
 * @brief adds actions to the queue to make a dash (up at t=0, down at t=TIME_DOT*3, busy until t=4*TIME_DOT)
 * 
 */
void Morse::dash()
{
  addaction(up, &_pin, 0);
  addaction(down, &_pin, 3*TIME_DOT);
  addaction(down, &_pin, 4*TIME_DOT);
}

/**
 * @brief adds actions to the queue to make a little space (low at t=0, busy until t=TIME_DOT*3)
 * 
 */
void Morse::little_space()
{
  addaction(down, &_pin, 0);
  addaction(down, &_pin, 3*TIME_DOT);
}

/**
 * @brief adds actions to the queue to make a space (low at t=0,busy until t=TIME_DOT*7)
 * 
 */
void Morse::space()
{
  addaction(down, &_pin, 0);
  addaction(down, &_pin, 7*TIME_DOT);
}

/**
 * @brief callback function for the queue, must be called in the loop() function. Executes functions in the queue if nneded, with appropriate parameters.
 * 
 */
void Morse::makeaction()
{
  int i = 0;
  while (queue_function[i] != NULL)
  {
    if (*queue_time[i]<millis() && queue_time[i]!=0)
    {
      queue_function[i](*queue_pin[i]);
      queue_time[i] = 0;
      queue_function[i] = NULL;
    }
    i++;
  }
}

/**
 * @brief adds an action to the queue(adds teh function to the queue_function array, the time to the queue_time array, and the pin to the queue_pin array)
 * 
 * @param function void(*)(short unsigned int): function to execute
 * @param pin short unsigned int*: pointer to the pin to use
 * @param time unsigned int: time to execute the function
 */
void Morse::addaction(void (*function)(short unsigned int), short unsigned int *pin, int time)
{
  int i = 0;
  while (queue_function[i] != NULL)
  {
    i++;
  }
  queue_function[i] = function;
  queue_pin[i] = pin;
  *queue_time[i] = max(millis(),last_time_queue) + time;
}
