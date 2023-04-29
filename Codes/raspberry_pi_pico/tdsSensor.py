"""TDS sensor class for the probe"""


from utime import sleep

from machine import Pin, ADC


class TDSSensor:
    "TDS sensor class for the probe"
    def __init__(self, pin : int = 27):
        assert pin in range(26, 29), "Pin must be between 26 and 28 for ADC!"
        self.adc = ADC(Pin(pin, mode=Pin.IN))
        self.temp = 25

    def measure(self, precision : int = 10, delay : float = 0.05) -> float:
        """makes a measure"""
        temp_values = []
        for _ in range(precision):
            temp_values.append(self.value())
            sleep(delay)
        temp_values.sort()
        return sum(temp_values[2:precision-2])/(precision-4)

    def value(self) -> float:
        """returns the value of the sensor"""
        val_adc = self.adc.read_u16()
        voltage = val_adc * 3.3 / 65535
        ec_value = 133.42 * voltage * voltage * voltage - 255.86 * voltage * voltage + 857.39 * voltage
        ec_t = ec_value / (1.0 + 0.02 * (self.temp - 25.0))
        return ec_t/2

    def set_temp(self,temp : float):
        """sets the temperature"""
        self.temp = temp

    def test(self) -> None:
        """tests the probe and verifies values are correct"""
        if int(self.measure()) in range(0,50000):
            print("Normal TDS")
        else:
            raise AssertionError("TDS not normal!")


if __name__ == "__main__":
    tds = TDSSensor(27)
    while True:
        print(f"actual TDS : {tds.measure()}")
        sleep(0.5)