"""ph meter for the probe"""
from machine import Pin, ADC
from utime import sleep

class PHMeter:
    """PH meter class"""
    calibration_value = 25.74 #must be calibrated maybe

    def __init__(self, pin : int = 27):
        assert pin in range(26, 29), "Pin must be between 26 and 28 for ADC!"
        self.adc = ADC(Pin(pin, mode=Pin.IN))
        

    def measure(self, precision : int = 10, delay : float = 0.05):
        """makes a measure"""
        temp_values = []
        for _ in range(precision):
            temp_values.append(self.value())
            sleep(0.03)
        temp_values.sort()
        return sum(temp_values[2:precision-2])/(precision-4)

    def value(self):
        """returns the value of the sensor"""
        val_adc = self.adc.read_u16()
        voltage = val_adc * 3.3 / 65535
        voltage_sensor = voltage * 4 / 3
        ph_act = -5.70 * voltage_sensor + self.calibration_value
        return ph_act
    
    def test(self):
        """tests the probe and verifies values are correct"""
        a=self.measure()
        print(f"actual PH : {a}")
        if int(a) in range(0,14):
            print("Normal pH")
        else:
            raise AssertionError("PH not normal!")