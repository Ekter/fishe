from time import sleep
from machine import Pin, ADC

calibration_value = 21.34 + 4.4 #normal value to calibrate, add the value that allow you to reach the right Ph value (you obtain it after trying it)
phval = 0
avgval = 0
buffer_arr =[]    #to capture different value
temp = 0
# Pin definitions

def loop():
    for i in range(0,10):   #capture 10 value
        adc = ADC(Pin(26, mode=Pin.IN)) #take value send by pin A26 (A0)
        buffer_arr.append(adc.read_u16())
        sleep(0.03);
    buffer_arr.sort() #sort values
    avgval = 0;
    for i in range(2,8): #take intermediate value
        avgval += buffer_arr[i] 
    #avgval = avgval/100
    volt = (avgval * 3.3) / (65536 * 6)   #convert in voltage (In:3.3V 2^16:65536 calibration:6)
    ph_act = -5.70 * volt + calibration_value #convert to pH
    print("rawValue : "+str(avgval)+"    Voltage : "+str(volt)+"    Ph : "+str(ph_act))
    sleep(1)

while True:
    loop()