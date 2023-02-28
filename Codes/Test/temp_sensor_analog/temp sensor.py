import machine
from onewire import OneWire
from ds18x20 import DS18X20
import time

ds_pin = machine.Pin(26)
ds_sensor = DS18X20(OneWire(ds_pin))
value = []
roms = ds_sensor.scan()


while True:

    ds_sensor.convert_temp()
    for i in range(0, 10):
        for rom in roms:
            value.append(ds_sensor.read_temp(rom))
        time.sleep(0.05)
    value.sort()
    average = sum(value[2:8])/6

    print("Temp")
    print(average)

    time.sleep(0.5)
    value = []
