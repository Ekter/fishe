"""Thermometer class for the probe"""

from utime import sleep

from ds18x20 import DS18X20
from machine import Pin
from onewire import OneWire


class Thermometer:
    """Thermometer class for the probe"""
    def __init__(self, pin : int = 18):
        self.pin = Pin(pin)
        self.one_wire_link = DS18X20(OneWire(self.pin))
        self.addresses = self.one_wire_link.scan()
        self.address()

    def measure(self, precision : int = 10, delay : float = 0.05) -> float:
        """makes a measure"""
        self.one_wire_link.convert_temp()
        temp_values = []
        for _ in range(precision):
            temp_values.append(self.one_wire_link.read_temp(self.address()))
            sleep(delay)
        temp_values.sort()
        return sum(temp_values[2:precision-2])/(precision-4)

    def address(self) -> bytes:
        """finds the thermometer's address"""
        try:
            addresses = self.one_wire_link.scan()
        except Exception as e:
            self.one_wire_link = DS18X20(OneWire(self.pin))
            addresses = self.one_wire_link.scan()
        if len(addresses)>=1:
            return addresses[0]
        raise Exception("No thermometer found!")

    def test(self) -> None:
        """tests the probe and verifies values are correct"""
        a=self.measure()
        print(f"actual temperature : {a}")
        if int(a) in range(0,25):
            print("Normal temperature")
        elif int(a) in range(-273,1000):
            print("Physically possible temperature, but not normal")
        else:
            raise AssertionError("Temperature not normal!")


if __name__ == "__main__":
    thermo = Thermometer(26)
    while True:
        print(f"actual temperature : {thermo.measure()}")
        sleep(0.5)
