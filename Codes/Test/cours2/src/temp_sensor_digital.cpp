#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2              // Data wire is plugged into digital pin 2 on the Arduino

OneWire oneWire(ONE_WIRE_BUS);        // Setup a oneWire instance to communicate with any OneWire device

DallasTemperature sensors(&oneWire);          // Pass oneWire reference to DallasTemperature library

void setup(void)
{
  sensors.begin();  // Start up the library
  Serial.begin(9600);
}

void loop(void)
{ 
  sensors.requestTemperatures();   // Send the command to get temperatures
  Serial.print("Temperature: ");      //print the temperature in Celsius
  Serial.print(sensors.getTempCByIndex(0));
  Serial.print((char)176);                    //shows degrees character
  Serial.println("C");
    
  delay(500);
}
