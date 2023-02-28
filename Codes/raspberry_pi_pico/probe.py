"""main class of the probe, with attributes for each sensor"""
from thermometer import Thermometer
from pHMeter import PHMeter
from turbiditySensor import TurbiditySensor

class Probe:
    "probe class"

    def __init__(self, pHMeter : PHMeter, thermometer : Thermometer, turboSensor : TurbiditySensor):
        self.pHMeter = pHMeter
        self.thermometer = thermometer
        self.turboSensor = turboSensor

    def measure(self):
        print(f"""pH : {self.pHMeter.measure()}
Temperature : {self.thermometer.measure()}
Turbidity : {self.turboSensor.measure()}
""")

    def test(self):
        self.pHMeter.