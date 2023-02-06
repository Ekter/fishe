float calibration_value = 21.34 + 9.75-0.36; //normal value to calibrate, add the value that allow you to reach the right Ph value (you obtain it after calibrate it for a 7 pH)
int phval = 0;
unsigned long int avgval = 0; 
int buffer_arr[10], temp; //capture values
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  for (int i = 0; i < 10; i++)
  {
    buffer_arr[i] = analogRead(A0);   //retrieve data
    delay(30);
  }
  for (int i = 0; i < 9; i++)
  {
    for (int j = i + 1; j < 10; j++)
    {
      if (buffer_arr[i] > buffer_arr[j])    //classes in ascending order
      {
        temp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = temp;
      }
    }
  }
  for (int i = 2; i < 8; i++)
    avgval += buffer_arr[i];        //summe of the midium value
  float volt = (float)avgval * 5.0 / 1024 / 6;    //convert in voltage (In:5V 2^10:1024 6 central values)
  float ph_act = -5.70 * volt + calibration_value;    //convert to pH
  Serial.print("rawValue : ");
  Serial.print(avgval);
  Serial.print("    Voltage : ");
  Serial.print(volt);
  Serial.print("    Ph : ");
  Serial.println(ph_act);
  delay(1000);                      //delay the different measures
}
