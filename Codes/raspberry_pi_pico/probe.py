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
        ph = self.pHMeter.measure()
        temperature = self.thermometer.measure()
        turbidity = self.turboSensor.measure()
        print(f"""pH : {ph}
Temperature : {temperature}
Turbidity : {turbidity}
""")

    def test(self):
        self.pHMeter.test()
        self.thermometer.test()
        self.turboSensor.test()

    def send_data(self):
        pass